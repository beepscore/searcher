#!/usr/bin/env python

import unittest

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

if __name__ == "__main__":
    unittest.main()
