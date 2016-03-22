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
    def walk_files_in_dir_recursive(search_dir, ignored_regex_objects, expression):
        """ walks search_dir, for each file check if it contains expression

            return dictionary with key directory name and value number of files that contain expression
        """

        # TODO: Fix method to reuse dictionary
        search_dir_abspath = os.path.abspath(search_dir)
        results = {}
        number_of_files_containing_expression = 0

        for file in [file for file in os.listdir(search_dir_abspath)]:

            if expression_helper.ExpressionHelper.is_string_matched_in_regular_expression_objects(file, ignored_regex_objects):
                continue

            full_name = os.path.join(search_dir_abspath,file)

            if (expression_searcher.ExpressionSearcher.search_file(expression, search_dir_abspath, file) is not None):
                number_of_files_containing_expression += 1

            # recursively walk subdirectories
            if os.path.isdir(full_name):
                DirWalker.walk_files_in_dir_recursive(full_name, ignored_regex_objects, expression)

        results[search_dir_abspath] = number_of_files_containing_expression
        print results
        return results

