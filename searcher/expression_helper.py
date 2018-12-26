#!/usr/bin/env python3

import re


""" methods for using regular expressions """

ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$', r'\.git', r'\.svn', r'\.exe$']


def regex_objects_from_patterns(patterns):
    """ returns regex_objects compiled from regular expression patterns"""

    regex_objects = []

    for pattern in patterns:
        regex_object = re.compile(pattern)
        regex_objects.append(regex_object)

    return regex_objects


def is_string_matched_in_regular_expression_objects(string, regex_objects):
    """ param regex_objects contains regular expression objects compiled from patterns
    searches string for any occurence of each regex_object
    """

    for regex_object in regex_objects:
        if regex_object.search(string):
            return True
    return False
