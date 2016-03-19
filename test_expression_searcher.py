#!/usr/bin/env python

import unittest

# tried putting tests in a "test" directory at same level as searcher
# relative import didn't work, might need __init.py__ file
from searcher import expression_searcher


class TestExpressionSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = expression_searcher.ExpressionSearcher("@./searcher_data/inputs/searcher_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)
        self.assertEqual("app*", searcher.expression, '')

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

    def test_search_directory_Apps(self):
        actual = expression_searcher.ExpressionSearcher.search_directory("Apps",
                "./searcher_data/search_dir")
        self.assertEqual(["httpwww.beepscore.comhubcape"], actual)

    def test_search_directory_Python(self):
        actual = expression_searcher.ExpressionSearcher.search_directory("Python",
                "./searcher_data/search_dir")
        self.assertEqual(['httppython.org',
            'httpsen.wikipedia.orgwikiPython_%28programming_language%29'], actual)

    def test_search_directory_data(self):
        actual = expression_searcher.ExpressionSearcher.search_directory("dat*",
                "./searcher_data/search_dir")
        self.assertEqual(['httppython.org',
            'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
            'httpswww.google.com#q=python',
            'httpwww.beepscore.comhubcape'], actual)

    def test_search_directory_write_results_data(self):
        expression_searcher.ExpressionSearcher.search_directory_write_results("dat*",
                "./searcher_data/search_dir",
                "./searcher_data/results",
                "searcher_results.txt")

if __name__ == "__main__":
    unittest.main()
