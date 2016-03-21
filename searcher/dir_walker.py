#!/usr/bin/env python

import os
import os.path
import re


class DirWalker:
    """
    Walks directory

    http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
    https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
    """

    @staticmethod
    def regex_objects_from_patterns(patterns):
        """ returns regex_objects compiled from regular expression patterns"""

        regex_objects = []

        for pattern in patterns:
            regex_object = re.compile(pattern)
            regex_objects.append(regex_object)

        return regex_objects

    @staticmethod
    def is_string_matched_in_regular_expression_objects(string, regex_objects):
        """ param regex_objects contains regular expression objects compiled from patterns
        searches string for any occurence of each regex_object
        """

        for regex_object in regex_objects:
            if regex_object.search(string):
                return True
        return False

    @staticmethod
    def files_in_dir_recursive(dir, ignored_regex_objects):
        """ param ignored_regex_objects contains regular expression objects compiled from patterns
        return list of files in dir and subdirectories
        """

        file_paths = []
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if DirWalker.is_string_matched_in_regular_expression_objects(filename,
                        ignored_regex_objects):
                    continue

                full_name = os.path.join(dirpath, filename)
                file_paths.append(full_name)
        return file_paths

    def walk_files_in_dir_recursive(dir, ignored_regex_objects, map_method):
        """ walks a directory, and executes a method on each file """

        dir = os.path.abspath(dir)
        for file in [file for file in os.listdir(dir)]:

            if DirWalker.is_string_matched_in_regular_expression_objects(file, ignored_regex_objects):
                continue

            full_name = os.path.join(dir,file)

            # call map_method on file
            map_method(full_name)

            # recursively walk subdirectories
            if os.path.isdir(full_name):
                self.walk_files_in_dir_recursive(full_name, ignored_regex_objects, map_method)

