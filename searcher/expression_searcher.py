#!/usr/bin/env python

from searcher import file_helper
import re
import os


class ExpressionSearcher:
    """
    Controller composed of several objects.
    Reads input commands.
    Searches files for expression.
    """

    @staticmethod
    def search_file(expression, search_dir, file_name):
        """
        In directory search file for expression

        return file name if file contains expression
        """
        if file_name == ".DS_Store":
            # avoid read error
            return None

        else:
            file_path = file_helper.FileHelper.absolute_file_path(search_dir, file_name)

            if os.path.isdir(file_path):
                # avoid read error
                return None

            textfile = open(file_path, 'r')
            text = textfile.read()
            textfile.close()
            matches = re.findall(expression, text)
            if matches == []:
                return None
            else:
                return file_name

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

            # print to show useer a simple progress indicator
            print "Searching " + directory
            number_of_files_containing_expression = 0

            filenames = file_helper.FileHelper.files_in_dir(directory, ignored_regex_objects)

            for filename in filenames:

                if (ExpressionSearcher.search_file(keyword, directory, filename) is not None):
                    number_of_files_containing_expression += 1

            results[directory] = number_of_files_containing_expression

            file_singular_or_plural = 'files'
            if number_of_files_containing_expression == 1:
                file_singular_or_plural = 'file'
            print "    found " + str(number_of_files_containing_expression) + " " + file_singular_or_plural

        return results

