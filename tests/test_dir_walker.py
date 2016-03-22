#!/usr/bin/env python

import unittest
from searcher import dir_walker
from searcher import expression_helper


class TestDirWalker(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        walker = dir_walker.DirWalker()
        self.assertIsNotNone(walker)

    def test_directories_number_of_files_containing_keyword(self):
        root_dir = './searcher_data/search_dir'

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        keyword = "ython"

        actual = dir_walker.DirWalker.directories_number_of_files_containing_keyword(root_dir, ignored_regex_objects, keyword)

        expected = {'./searcher_data/search_dir': 2,
                    './searcher_data/search_dir/level_1': 1,
                    './searcher_data/search_dir/level_1/level_2': 2,
                    './searcher_data/search_dir/level_1/level_2/level_3': 1}

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
