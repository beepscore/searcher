#!/usr/bin/env python

import os
import os.path
from searcher import expression_helper
from searcher import expression_searcher


class DirWalker:
    """
    Walks directory

    http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
    https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
    """

    @staticmethod
    def directories_in_dir_recursive(search_dir, ignored_regex_objects):
        """
        Searches search_dir and subdirectories for directories

        Ignores symlinks. Doesn't ignore alias.
        http://apple.stackexchange.com/questions/2991/whats-the-difference-between-alias-and-link

        param search_dir is the directory to search
        param ignored_regex_objects contains regular expression objects compiled from patterns
        return list of un-ignored directories in search_dir and subdirectories
        """

        dir_paths = [search_dir]

        for dirpath, dirnames, filenames in os.walk(search_dir):

                for dirname in dirnames:

                    if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(dirpath,
                                                                                                          ignored_regex_objects):
                        # ignore subdirectories of ignored directory
                        continue

                    if os.path.islink(dirname):
                        # ignore symlink
                        # http://stackoverflow.com/questions/15718006/check-if-directory-is-symlink
                        continue

                    if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(dirname,
                                                                                                          ignored_regex_objects):
                        # ignore this directory
                        continue

                    full_name = os.path.join(dirpath, dirname)
                    dir_paths.append(full_name)

        return dir_paths

    @staticmethod
    def files_in_dir(search_dir, ignored_regex_objects):
        """
        Searches search_dir for files

        Ignores symlinks. Doesn't ignore alias.
        http://apple.stackexchange.com/questions/2991/whats-the-difference-between-alias-and-link

        param ignored_regex_objects contains regular expression objects compiled from patterns
        return list of un-ignored files in search_dir, relative to search_dir
        """

        file_paths = []
        dir_list = os.listdir(search_dir)
        for filename in dir_list:

            search_dir_abspath = os.path.abspath(search_dir)
            full_name = os.path.join(search_dir_abspath, filename)
            if os.path.isdir(full_name):
                # ignore directory
                continue

            if os.path.islink(full_name):
                # ignore symlink
                # http://stackoverflow.com/questions/15718006/check-if-directory-is-symlink
                continue

            if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(filename,
                                                                                                  ignored_regex_objects):
                # ignore this file
                continue

            file_paths.append(filename)

        return file_paths

    @staticmethod
    def directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword):
        """
        Searches root_dir and subdirectories for files containing keyword

        param ignored_regex_objects contains regular expression objects compiled from patterns
        return dictionary with key directory name and value number of files that contain expression
        """

        directories = DirWalker.directories_in_dir_recursive(root_dir, ignored_regex_objects)
        results = {}

        for directory in directories:

            number_of_files_containing_expression = 0

            filenames = DirWalker.files_in_dir(directory, ignored_regex_objects)

            for filename in filenames:

                if (expression_searcher.ExpressionSearcher.search_file(keyword, directory, filename) is not None):
                    number_of_files_containing_expression += 1

            results[directory] = number_of_files_containing_expression

        return results
