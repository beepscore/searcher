#!/usr/bin/env python

import os
import os.path
from searcher import expression_helper


class DirWalker:
    """
    Walks directory

    http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
    https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
    """

    @staticmethod
    def files_in_dir_recursive(search_dir, ignored_regex_objects):
        """ param ignored_regex_objects contains regular expression objects compiled from patterns
        return list of files in search_dir and subdirectories
        """

        file_paths = []
        for dirpath, dirnames, filenames in os.walk(search_dir):
            for filename in filenames:
                if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(filename,
                        ignored_regex_objects):
                    continue

                full_name = os.path.join(dirpath, filename)
                file_paths.append(full_name)
        return file_paths

    @staticmethod
    def some_method(string):
        return len(string)

    @staticmethod
    def walk_files_in_dir_recursive(search_dir, ignored_regex_objects, map_method):
        """ walks a directory, and executes a method on each file """

        search_dir = os.path.abspath(search_dir)
        for file in [file for file in os.listdir(search_dir)]:

            if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(file, ignored_regex_objects):
                continue

            full_name = os.path.join(search_dir,file)

            # call map_method on file
            result = map_method(full_name)
            print(full_name, result)

            # recursively walk subdirectories
            if os.path.isdir(full_name):
                DirWalker.walk_files_in_dir_recursive(full_name, ignored_regex_objects, map_method)

