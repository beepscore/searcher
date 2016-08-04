#!/usr/bin/env python3

import unittest
from searcher import file_helper
from searcher import expression_helper


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_directories_in_dir_recursive_dont_ignore(self):

        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'./searcher_data/search_dir',
                    './searcher_data/search_dir/level_1',
                    './searcher_data/search_dir/level_1/.git_fake',
                    './searcher_data/search_dir/level_1/.git_fake/objects_fake',
                    './searcher_data/search_dir/level_1/level_2',
                    './searcher_data/search_dir/level_1/level_2/level_3',
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4'
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore1(self):

        ignored_dirname_patterns = ['level_1']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'./searcher_data/search_dir'}
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore_git(self):

        # Note: git version control normally ignores its own database .git
        # So for testing, committed a file search_dir/level_1/.git_fake/objects_fake/object_fake

        ignored_dirname_patterns = ['\.git']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                     ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'./searcher_data/search_dir',
                    './searcher_data/search_dir/level_1',
                    './searcher_data/search_dir/level_1/level_2',
                    './searcher_data/search_dir/level_1/level_2/level_3',
                    './searcher_data/search_dir/level_1/level_2/level_3/level_4'
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore2(self):

        ignored_dirname_patterns = ['level_2']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'./searcher_data/search_dir',
                    './searcher_data/search_dir/level_1',
                    './searcher_data/search_dir/level_1/.git_fake',
                    './searcher_data/search_dir/level_1/.git_fake/objects_fake',
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore3(self):

        ignored_dirname_patterns = ['level_3']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive("./searcher_data/search_dir",
                                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'./searcher_data/search_dir',
                    './searcher_data/search_dir/level_1',
                    './searcher_data/search_dir/level_1/.git_fake',
                    './searcher_data/search_dir/level_1/.git_fake/objects_fake',
                    './searcher_data/search_dir/level_1/level_2',
                    }
        self.assertEqual(expected, set(actual))

    def test_files_in_dir(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'httppython.org',
                    'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                    'httpswww.google.com#q=python',
                    'httpwww.beepscore.comhubcape',
                    }

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_ignore_ython(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$', 'ython']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'httpwww.beepscore.comhubcape'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_1(self):

        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir/level_1",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'a.txt', 'c.txt alias'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_2(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir/level_1/level_2",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'b.txt', 'c.txt', 'd.txt'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_3(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir/level_1/level_2/level_3",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = set(['d.txt alias'])

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_set_from_reordered_list(self):
        """ test we are using set correctly. """

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir("./searcher_data/search_dir",
                                                   ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected_from_reordered_list = {'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                                        'httpswww.google.com#q=python',
                                        'httpwww.beepscore.comhubcape',
                                        'httppython.org'
                                        }

        self.assertEqual(expected_from_reordered_list, set(actual))

if __name__ == "__main__":
    unittest.main()
