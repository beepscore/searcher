#!/usr/bin/env python

import unittest
from searcher import file_helper
from searcher import expression_helper
from sets import Set


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        walker = file_helper.FileHelper()
        self.assertIsNotNone(walker)

    def test_directories_in_dir_recursive_dont_ignore(self):

        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.FileHelper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1',
            './searcher_data/search_dir/level_1/level_2',
            './searcher_data/search_dir/level_1/level_2/level_3',
        ])
        self.assertEqual(expected, Set(actual))

    def test_directories_in_dir_recursive_ignore1(self):

        ignored_dirname_patterns = ['level_1']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.FileHelper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
        ])
        self.assertEqual(expected, Set(actual))

    def test_directories_in_dir_recursive_ignore2(self):

        ignored_dirname_patterns = ['level_2']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.FileHelper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1',
        ])
        self.assertEqual(expected, Set(actual))

    def test_directories_in_dir_recursive_ignore3(self):

        ignored_dirname_patterns = ['level_3']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.FileHelper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            './searcher_data/search_dir',
            './searcher_data/search_dir/level_1',
            './searcher_data/search_dir/level_1/level_2',
        ])
        self.assertEqual(expected, Set(actual))

    def test_files_in_dir(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
            'httppython.org',
            'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
            'httpswww.google.com#q=python',
            'httpwww.beepscore.comhubcape',
        ])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_ignore_ython(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$', 'ython']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set(['httpwww.beepscore.comhubcape'])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_level_1(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir/level_1",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set(['a.txt', 'c.txt alias'])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_level_2(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir/level_1/level_2",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set(['b.txt', 'c.txt', 'd.txt'])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_level_3(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir/level_1/level_2/level_3",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set(['d.txt alias'])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_set_from_reordered_list(self):
        """ test we are using Set correctly. """

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.FileHelper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected_from_reordered_list = Set([
            'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
            'httpswww.google.com#q=python',
            'httpwww.beepscore.comhubcape',
            'httppython.org',
        ])

        self.assertEqual(expected_from_reordered_list, Set(actual))

if __name__ == "__main__":
    unittest.main()