#!/usr/bin/env python3

import unittest

from searcher import expression_helper
from searcher import expression_searcher
from os import linesep


class TestExpressionSearcher(unittest.TestCase):

    def setUp(self):
        pass

    # test_search_file

    def test_search_file_returns_none(self):
        actual = expression_searcher.search_file("not there",
                                                 "./searcher_data/search_dir",
                                                 "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        actual = expression_searcher.search_file("Apps",
                                                 "./searcher_data/search_dir",
                                                 "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

    def test_search_file_is_case_sensitive(self):
        actual = expression_searcher.search_file("Apps",
                                                 "./searcher_data/search_dir",
                                                 "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

        actual = expression_searcher.search_file("apps",
                                                 "./searcher_data/search_dir",
                                                 "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    # test_directories_number_of_files_containing_expression

    def test_directories_number_of_files_containing_expression_ython(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        expression = "ython"

        actual = expression_searcher.directories_number_of_files_containing_expression(root_dir, ignored_regex_objects, expression)

        expected = {'./searcher_data/search_dir': 2,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 1,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_expression_this(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        # \A == start of a line
        expression = "\AThis"

        actual = expression_searcher.directories_number_of_files_containing_expression(root_dir, ignored_regex_objects, expression)

        # searcher searches the alias text, not the text of the file it links to
        expected = {'./searcher_data/search_dir': 0,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_expression_foo(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        expression = "foo"

        actual = expression_searcher.directories_number_of_files_containing_expression(root_dir, ignored_regex_objects, expression)

        # foo matches 'footer' in several html files
        expected = {'./searcher_data/search_dir': 4,
                    './searcher_data/search_dir/level_1': 0,
                    './searcher_data/search_dir/level_1/level_2': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_expression_test_result(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        expression = "^[a-zA-Z]+_TESTResult.*"

        actual = expression_searcher.directories_number_of_files_containing_expression(root_dir, ignored_regex_objects, expression)

        expected = {'./searcher_data/search_dir': 0,
                    './searcher_data/search_dir/level_1': 0,
                    './searcher_data/search_dir/level_1/level_2': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 1}

        self.assertEqual(expected, actual)

    def test_lines_in_file_containing_expression(self):
        expected = ["line 34     <li><a href=\"#\">Apps</a>"]
        actual = expression_searcher.lines_in_file_containing_expression("Apps",
                                                                         "./searcher_data/search_dir", "httpwww.beepscore.comhubcape")
        self.assertEqual(expected, actual)

    def test_lines_in_files_containing_expression_this(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        # \A == start of a line
        expression = "\AThis"

        actual = expression_searcher.lines_in_files_containing_expression(expression, root_dir, ignored_regex_objects)

        expected = [('httpwww.beepscore.comhubcape', []),
                    ('httpsen.wikipedia.orgwikiPython_%28programming_language%29', []),
                    ('httppython.org', []),
                    ('httpswww.google.com#q=python', []),
                    ('a.txt', ['line 1 This file has at least one "a".']),
                    ('c.txt alias', []),
                    ('c.txt', ['line 1 This file has Python Jython pythonic.']),
                    ('b.txt', ['line 1 This file has at least one big "b".']),
                    ('d.txt', []),
                    ('d.txt alias', []),
                    ('test_result01.txt', [])
                    ]

        self.assertEqual(expected, actual)

    def test_lines_in_files_containing_expression_test_result(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        expression = "^[a-zA-Z]+_TESTResult.*"

        actual = expression_searcher.lines_in_files_containing_expression(expression, root_dir, ignored_regex_objects)

        expected = [('httpwww.beepscore.comhubcape', []),
                    ('httpsen.wikipedia.orgwikiPython_%28programming_language%29', []),
                    ('httppython.org', []), ('httpswww.google.com#q=python', []),
                    ('a.txt', []),
                    ('c.txt alias', []),
                    ('c.txt', []),
                    ('b.txt', []),
                    ('d.txt', []),
                    ('d.txt alias', []),
                    ('test_result01.txt', ['line 1 a_TESTResult.txt'])
                    ]

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
