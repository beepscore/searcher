#!/usr/bin/env python3

import unittest

from searcher import expression_helper
from searcher import expression_searcher
from os import linesep


class TestExpressionSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = expression_searcher.ExpressionSearcher()
        self.assertIsNotNone(searcher)

    # test_search_file

    def test_search_file_returns_none(self):
        actual = expression_searcher.ExpressionSearcher.search_file("not there",
                "./searcher_data/search_dir",
                "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        actual = expression_searcher.ExpressionSearcher.search_file("Apps",
                "./searcher_data/search_dir",
                "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

    def test_search_file_is_case_sensitive(self):
        actual = expression_searcher.ExpressionSearcher.search_file("Apps",
                "./searcher_data/search_dir",
                "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

        actual = expression_searcher.ExpressionSearcher.search_file("apps",
                "./searcher_data/search_dir",
                "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    # test_directories_number_of_files_containing_keyword

    def test_directories_number_of_files_containing_keyword_ython(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        keyword = "ython"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        expected = {'./searcher_data/search_dir': 2,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 1,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_keyword_this(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        # \A == start of a line
        keyword = "\AThis"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        # searcher searches the alias text, not the text of the file it links to
        expected = {'./searcher_data/search_dir': 0,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 0,
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_keyword_foo(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        keyword = "foo"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        # foo matches 'footer' in several html files
        expected = {'./searcher_data/search_dir': 4,
                './searcher_data/search_dir/level_1': 0,
                './searcher_data/search_dir/level_1/level_2': 0,
                './searcher_data/search_dir/level_1/level_2/level_3': 0,
                './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_keyword_test_result(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        keyword = "^[a-zA-Z]+_TESTResult.*"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        expected = {'./searcher_data/search_dir': 0,
                './searcher_data/search_dir/level_1': 0,
                './searcher_data/search_dir/level_1/level_2': 0,
                './searcher_data/search_dir/level_1/level_2/level_3': 0,
                './searcher_data/search_dir/level_1/level_2/level_3/level_4': 1}

        self.assertEqual(expected, actual)

    def test_lines_in_file_containing_expression(self):
        expected = "httpwww.beepscore.comhubcape 1 match" + linesep + "httpwww.beepscore.comhubcape 34     <li><a href=\"#\">Apps</a>" + linesep
        actual = expression_searcher.ExpressionSearcher.lines_in_file_containing_expression("Apps",
                                                                                            "./searcher_data/search_dir", "httpwww.beepscore.comhubcape")
        print("test_lines_in_file_containing_expression")
        print(actual)
        self.assertEqual(expected, actual)

    def test_lines_in_files_containing_expression_this(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        # \A == start of a line
        expression = "\AThis"

        actual = expression_searcher.ExpressionSearcher.lines_in_files_containing_expression(expression, root_dir, ignored_regex_objects)
        print('test_lines_in_files_containing_expression_this')
        print(actual)

        expected = ('httppython.org 0 matches' + linesep
                    + 'httpsen.wikipedia.orgwikiPython_%28programming_language%29 0 matches'
                    + linesep
                    + 'httpswww.google.com#q=python 0 matches'
                    + linesep
                    + 'httpwww.beepscore.comhubcape 0 matches'
                    + linesep
                    + 'a.txt 1 match'
                    + linesep
                    + 'a.txt 1 This file has at least one "a".'
                    + linesep
                    + 'c.txt alias 0 matches'
                    + linesep
                    + 'b.txt 1 match'
                    + linesep
                    + 'b.txt 1 This file has at least one big "b".'
                    + linesep
                    + 'c.txt 1 match'
                    + linesep
                    + 'c.txt 1 This file has Python Jython pythonic.'
                    + linesep
                    + 'd.txt 0 matches'
                    + linesep
                    + 'd.txt alias 0 matches'
                    + linesep
                    + 'test_result01.txt 0 matches'
                    + linesep
                    )

        self.assertEqual(expected, actual)

    def test_lines_in_files_containing_expression_test_result(self):
        root_dir = './searcher_data/search_dir'

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        expression = "^[a-zA-Z]+_TESTResult.*"

        actual = expression_searcher.ExpressionSearcher.lines_in_files_containing_expression(expression, root_dir, ignored_regex_objects)

        expected = ('httppython.org 0 matches' + linesep
                    + 'httpsen.wikipedia.orgwikiPython_%28programming_language%29 0 matches'
                    + linesep
                    + 'httpswww.google.com#q=python 0 matches'
                    + linesep
                    + 'httpwww.beepscore.comhubcape 0 matches'
                    + linesep
                    + 'a.txt 0 matches'
                    + linesep
                    + 'c.txt alias 0 matches'
                    + linesep
                    + 'b.txt 0 matches'
                    + linesep
                    + 'c.txt 0 matches'
                    + linesep
                    + 'd.txt 0 matches'
                    + linesep
                    + 'd.txt alias 0 matches'
                    + linesep
                    + 'test_result01.txt 1 match'
                    + linesep
                    + 'test_result01.txt 1 a_TESTResult.txt'
                    + linesep
                    )

        self.assertEqual(expected, actual)
if __name__ == "__main__":
    unittest.main()
