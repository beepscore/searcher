#!/usr/bin/env python

import unittest
from sets import Set
from searcher import dir_walker


class TestDirWalker(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        walker = dir_walker.DirWalker()
        self.assertIsNotNone(walker)

    def test_is_string_matched_in_regular_expression_objects_dot(self):
        """ match '.' representing current directory
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.$']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('.', ignored_regex_objects))

        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('..', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('a.', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('.c', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('a.c', ignored_regex_objects))

    def test_is_filename_matched_in_patterns_dotdot(self):
        """ match '..' representing directory above current directory
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.\.$']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('..', ignored_regex_objects))

        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('a..', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('..c', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('a..c', ignored_regex_objects))

    def test_is_filename_matched_in_patterns_dotDS_Store(self):
        """ match '.DS_Store' OSX file system file
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.DS_Store$']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('.DS_Store', ignored_regex_objects))

        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('a.DS_Store', ignored_regex_objects))
        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects('.DS_Storeb', ignored_regex_objects))

    def test_is_filename_matched_in_patterns_inner(self):
        """ match 'ython' within string. Case sensitive """

        ignored_filename_patterns = ['ython']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects("A big python is here.", ignored_regex_objects))

        self.assertFalse(dir_walker.DirWalker.is_string_matched_in_regular_expression_objects("A big pythoxyz", ignored_regex_objects))

    def test_files_in_dir_recursive(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

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
                ])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_recursive_ignore_ython(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$', 'ython']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir",
                ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = Set([
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                './searcher_data/search_dir/level_1/a.txt',
                './searcher_data/search_dir/level_1/level_2/b.txt',
                ])

        self.assertEqual(expected, Set(actual))

    def test_files_in_dir_recursive_set_from_reordered_list(self):
        """ test we are using Set correctly. """

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = dir_walker.DirWalker.regex_objects_from_patterns(ignored_filename_patterns)

        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir",
                ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected_from_reordered_list = Set([
                './searcher_data/search_dir/httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                './searcher_data/search_dir/httpswww.google.com#q=python',
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                './searcher_data/search_dir/httppython.org',
                './searcher_data/search_dir/level_1/a.txt',
                './searcher_data/search_dir/level_1/level_2/b.txt',
                ])

        self.assertEqual(expected_from_reordered_list, Set(actual))

if __name__ == "__main__":
    unittest.main()
