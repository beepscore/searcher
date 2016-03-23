#!/usr/bin/env python

import unittest

from searcher import expression_helper
from searcher import expression_searcher


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

    def test_directories_number_of_files_containing_keyword(self):
        root_dir = './searcher_data/search_dir'

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        keyword = "ython"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        expected = {'./searcher_data/search_dir': 2,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 1}

        self.assertEqual(expected, actual)

    def test_directories_number_of_files_containing_keyword_this(self):
        root_dir = './searcher_data/search_dir'

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        # \A == start of a line
        keyword = "\AThis"

        actual = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        # searcher searches the alias text, not the text of the file it links to
        expected = {'./searcher_data/search_dir': 0,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 0}

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
