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

    def test_files_in_dir_recursive(self):
        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir")

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

    def test_files_in_dir_recursive_set_from_reordered_list(self):
        """ test we are using Set correctly. """
        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir")

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
