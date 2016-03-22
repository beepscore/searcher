#!/usr/bin/env python

import unittest
from sets import Set
from searcher import dir_walker
from searcher import expression_helper


class TestDirWalker(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        walker = dir_walker.DirWalker()
        self.assertIsNotNone(walker)

    def test_directories_in_dir_recursive_dont_ignore(self):

        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = dir_walker.DirWalker.directories_in_dir_recursive("./searcher_data/search_dir",
                                                             ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1',
            './searcher_data/search_dir/level_1/level_2',
        ])
        self.assertEqual(expected, Set(actual))

    def test_directories_in_dir_recursive_ignore1(self):

        ignored_dirname_patterns = ['level_1']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = dir_walker.DirWalker.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        # TODO: Consider change method to ignore subdirectories of ignored directory level_1
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1/level_2',
        ])
        self.assertEqual(expected, Set(actual))

    def test_directories_in_dir_recursive_ignore2(self):

        ignored_dirname_patterns = ['level_2']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = dir_walker.DirWalker.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1',
        ])
        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_recursive(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir",
                ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
                './searcher_data/search_dir/httppython.org',
                './searcher_data/search_dir/httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                './searcher_data/search_dir/httpswww.google.com#q=python',
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                './searcher_data/search_dir/level_1/a.txt',
                './searcher_data/search_dir/level_1/level_2/b.txt',
                './searcher_data/search_dir/level_1/level_2/c.txt',
                ])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_recursive_ignore_ython(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$', 'ython']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir",
                ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                './searcher_data/search_dir/level_1/a.txt',
                './searcher_data/search_dir/level_1/level_2/b.txt',
                './searcher_data/search_dir/level_1/level_2/c.txt',
                ])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_recursive_set_from_reordered_list(self):
        """ test we are using Set correctly. """

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir",
                ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected_from_reordered_list = Set([
                './searcher_data/search_dir/httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                './searcher_data/search_dir/httpswww.google.com#q=python',
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                './searcher_data/search_dir/httppython.org',
                './searcher_data/search_dir/level_1/a.txt',
                './searcher_data/search_dir/level_1/level_2/c.txt',
                './searcher_data/search_dir/level_1/level_2/b.txt',
                ])

        self.assertEqual(expected_from_reordered_list, Set(actual))

    def test_walk_files_in_dir_recursive(self):
        search_dir = './searcher_data/search_dir'

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        expression = "ython"

        dir_walker.DirWalker.walk_files_in_dir_recursive(search_dir,
                ignored_regex_objects, expression)

if __name__ == "__main__":
    unittest.main()
