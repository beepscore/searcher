#!/usr/bin/env python3

import pprint

from searcher import expression_helper
from searcher import expression_searcher
from searcher import searcher_arg_reader


if __name__ == '__main__':

    """
    Search for expression without instantiating an instance. Use command line arguments.
    """

    # instantiate arg_reader
    arg_reader = searcher_arg_reader.SearcherArgReader()

    # Call arg_reader.args() without an argument list so it reads from command line.
    args = arg_reader.args()

    expression = args.expression
    search_dir = args.root_dir
    print("Searching root_dir " + search_dir + " for expression " + expression)

    ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

    results = expression_searcher.directories_number_of_files_containing_expression(search_dir,
                                                                                    ignored_regex_objects, expression)
    print("Results")
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(results)
