#!/usr/bin/env python3

# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'searcher')))

import pprint

from searcher import searcher_arg_reader

from searcher import expression_helper
from searcher import expression_searcher


if __name__ == '__main__':

    """
    Search for expression without instantiating an instance. Use command line arguments.
    """

    # instantiate arg_reader
    arg_reader = searcher_arg_reader.SearcherArgReader()

    # Call arg_reader.args() without an argument list so it reads from command line.
    args = arg_reader.args()

    expression = args.keyword
    search_dir = args.root_dir
    print("Searching root_dir " + search_dir + " for keyword " + expression)

    ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(expression_helper.ExpressionHelper.ignored_filename_patterns)

    results = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_expression(search_dir,
                                                                                                       ignored_regex_objects, expression)
    print("Results")
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(results)
