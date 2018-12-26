#!/usr/bin/env python3

from searcher import file_helper
import re
import os


"""
Controller composed of several objects.
Reads input commands.
Searches files for expression.
"""


def search_file(expression, search_dir, file_name):
    """
    In directory search file for expression

    return file name if file contains expression
    """
    if file_name == ".DS_Store":
        # avoid read error
        return None

    else:
        file_path = file_helper.absolute_file_path(search_dir, file_name)

        if os.path.isdir(file_path):
            # avoid read error
            return None

        # throws UnicodeDecodeError: 'utf-8' codec can't decode byte
        # textfile = open(file_path, 'r', encoding='utf-8')
        textfile = open(file_path, 'r', encoding='ISO-8859-1')
        text = textfile.read()
        textfile.close()
        matches = re.findall(expression, text)
        # http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
        if len(matches) == 0:
            return None
        else:
            return file_name


def directories_number_of_files_containing_expression(root_dir, ignored_regex_objects, expression):
    """
    Searches root_dir and subdirectories for files containing expression

    param ignored_regex_objects contains regular expression objects compiled from patterns
    return dictionary with key directory name and value number of files that contain expression
    """

    directories = file_helper.directories_in_dir_recursive(root_dir, ignored_regex_objects)
    results = {}

    for directory in directories:

        # print to show user a simple progress indicator
        print("Searching " + directory)
        number_of_files_containing_expression = 0

        filenames = file_helper.files_in_dir(directory, ignored_regex_objects)

        for filename in filenames:

            if search_file(expression, directory, filename) is not None:
                number_of_files_containing_expression += 1

        results[directory] = number_of_files_containing_expression

        file_singular_or_plural = 'files'
        if number_of_files_containing_expression == 1:
            file_singular_or_plural = 'file'
        print("    found " + str(number_of_files_containing_expression) + " " + file_singular_or_plural)

    return results


def lines_in_file_containing_expression(expression, search_dir, file_name):
    """
    Search directory file for expression. Search is non recursive

    :param expression: regex string pattern to search for e.g. "^[a-zA-Z]+_TESTResult.*"
    :param search_dir: directory to search
    :param file_name:
    :return: list of strings that match. Each string starts with line number and ends with line
    e.g. ['line 1 a_TESTResult.txt']
    return None for files that don't contain expression
    """

    if file_name == ".DS_Store":
        # avoid read error
        return None

    else:
        file_path = file_helper.absolute_file_path(search_dir, file_name)

        if os.path.isdir(file_path):
            # avoid read error
            return None

        # throws UnicodeDecodeError: 'utf-8' codec can't decode byte
        # textfile = open(file_path, 'r', encoding='utf-8')
        textfile = open(file_path, 'r', encoding='ISO-8859-1')

        lines = []
        line_number = 1
        for line in textfile:
            matches = re.findall(expression, line)
            for match in matches:
                lines.append('line ' + str(line_number) + ' ' + line.rstrip())
            line_number += 1
        textfile.close()

        return lines


def lines_in_files_containing_expression(expression, root_dir, ignored_regex_objects):
    """
    Searches root_dir and subdirectories for files containing expression. Search is recursive

    :param expression: regex string pattern to search for e.g. "^[a-zA-Z]+_TESTResult.*"
    :param root_dir: directory to start search
    :param ignored_regex_objects: regular expression objects compiled from patterns
    :return: list of tuples. Each tuple contains file name and list of lines
    e.g. ('test_result01.txt', ['line 1 a_TESTResult.txt'])
    """

    directories = file_helper.directories_in_dir_recursive(root_dir, ignored_regex_objects)
    file_lines = []

    for directory in directories:

        # print to show user a simple progress indicator
        print("Searching " + directory)

        filenames = file_helper.files_in_dir(directory, ignored_regex_objects)

        for filename in filenames:
            lines_in_file = lines_in_file_containing_expression(expression, directory, filename)
            if lines_in_file is not None:
                file_lines.append((filename, lines_in_file))

    return file_lines

