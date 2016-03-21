#!/usr/bin/env python

import os
import os.path
import re


class ExpressionHelper:
    """ Has methods for using regular expressions """

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

