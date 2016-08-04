#!/usr/bin/env python3

import os
from searcher import expression_helper


""" Utility methods for working with files and directories

http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
"""


def absolute_dir_path(dirname):
    # Note Python does not expand ~ in path as on OS X
    # http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    # current_dir is absolute path
    # current_dir = os.path.dirname(__file__)
    absolute_path = os.path.abspath(dirname)
    return absolute_path


def absolute_file_path(dirname, filename):
    dir_path = absolute_dir_path(dirname)
    file_path = os.path.join(dir_path, filename)
    return file_path


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

            if expression_helper.is_string_matched_in_regular_expression_objects(dirpath,
                                                                                                  ignored_regex_objects):
                # ignore subdirectories of ignored directory
                continue

            if os.path.islink(dirname):
                # ignore symlink
                # http://stackoverflow.com/questions/15718006/check-if-directory-is-symlink
                continue

            if expression_helper.is_string_matched_in_regular_expression_objects(dirname,
                                                                                                  ignored_regex_objects):
                # ignore this directory
                continue

            full_name = os.path.join(dirpath, dirname)
            dir_paths.append(full_name)

    return dir_paths


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

        if expression_helper.is_string_matched_in_regular_expression_objects(filename,
                                                                                              ignored_regex_objects):
            # ignore this file
            continue

        file_paths.append(filename)

    return file_paths

