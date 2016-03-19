#!/usr/bin/env python

import unittest

# tried putting tests in a "test" directory at same level as searcher
# relative import didn't work
# from ..searcher import arg_reader
# put tests above searcher directory
from searcher import searcher_arg_reader


class TestSearcherArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = searcher_arg_reader.SearcherArgReader()
        args = reader.args(None)
        self.assertEqual(None, args.keyword, '')
        self.assertEqual("../searcher_data/root_dir", args.root_dir, '')
        self.assertEqual("../searcher_data/results", args.out_directory, '')
        self.assertEqual("searcher_results.txt", args.out_file, '')

    def test_args_from_argument(self):
        reader = searcher_arg_reader.SearcherArgReader()

        keyword = "foo"
        root_dir = "some_root_dir"
        out_directory = "../some_directory"
        out_file = "some_results.txt"

        test_commandline = ["-keyword", keyword,
                            "-root_dir", root_dir,
                            "-out_directory", out_directory,
                            "-out_file", out_file
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(keyword, args.keyword, '')
        self.assertEqual(root_dir, args.root_dir, '')
        self.assertEqual(out_directory, args.out_directory, '')
        self.assertEqual(out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = searcher_arg_reader.SearcherArgReader()
        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./searcher_data/inputs/searcher_args.txt"])

        self.assertEqual("app*", args.keyword)
        self.assertEqual("./searcher_data/search_dir", args.root_dir)
        self.assertEqual("./searcher_data/results", args.out_directory)
        self.assertEqual("searcher_results.txt", args.out_file)

if __name__ == "__main__":
    unittest.main()
