#!/usr/bin/env python

import unittest

from searcher import dir_walker


class TestDirWalker(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        walker = dir_walker.DirWalker()
        self.assertIsNotNone(walker)

    def test_files_in_dir_recursive(self):
        actual = dir_walker.DirWalker.files_in_dir_recursive("./searcher_data/search_dir")

        expected = [
                './searcher_data/search_dir/httppython.org',
                './searcher_data/search_dir/httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                './searcher_data/search_dir/httpswww.google.com#q=python',
                './searcher_data/search_dir/httpwww.beepscore.comhubcape',
                ]

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
