#!/usr/bin/env python

from searcher import file_helper
from searcher import expression_searcher


class DirWalker:
    """
    Walks directory

    """

    @staticmethod
    def directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword):
        """
        Searches root_dir and subdirectories for files containing keyword

        param ignored_regex_objects contains regular expression objects compiled from patterns
        return dictionary with key directory name and value number of files that contain expression
        """

        directories = file_helper.FileHelper.directories_in_dir_recursive(root_dir, ignored_regex_objects)
        results = {}

        for directory in directories:

            number_of_files_containing_expression = 0

            filenames = file_helper.FileHelper.files_in_dir(directory, ignored_regex_objects)

            for filename in filenames:

                if (expression_searcher.ExpressionSearcher.search_file(keyword, directory, filename) is not None):
                    number_of_files_containing_expression += 1

            results[directory] = number_of_files_containing_expression

        return results
