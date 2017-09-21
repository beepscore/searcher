#!/usr/bin/env python3

import unittest

from searcher import searcher_arg_reader


class TestSearcherArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = searcher_arg_reader.SearcherArgReader()
        args = reader.args(None)
        self.assertEqual('foo', args.expression, '')
        self.assertEqual("./searcher_data/search_dir", args.root_dir, '')

    def test_args_from_argument(self):
        reader = searcher_arg_reader.SearcherArgReader()

        expression = "bar"
        root_dir = "some_root_dir"

        test_commandline = ["-expression", expression,
                            "-root_dir", root_dir
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(expression, args.expression, '')
        self.assertEqual(root_dir, args.root_dir, '')

    def test_args_from_argument_file(self):
        reader = searcher_arg_reader.SearcherArgReader()
        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./searcher_data/inputs/searcher_args.txt"])

        self.assertEqual("app*", args.expression)
        self.assertEqual("./searcher_data/search_dir", args.root_dir)


if __name__ == "__main__":
    unittest.main()
