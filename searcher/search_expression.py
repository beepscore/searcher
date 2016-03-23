#!/usr/bin/env python

# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'searcher')))

# References:
# https://docs.python.org/2/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text
import argparse
from argparse import RawTextHelpFormatter

from searcher import expression_helper
from searcher import expression_searcher


if __name__ == '__main__':

        """
        Search for expression without instantiating an instance. Use command line arguments.
        """

        parser = argparse.ArgumentParser(description="""    For help, use argument -h
                                         $ ./search_expression.py -h
                                         To specify an argument, prefix with -
                                         $ ./search_expression.py -keyword a_regular_expression -path a_path
                                         To read arguments from a file, prefix file name with @
                                         $ ./search_expression.py @args.txt
                                         To specify arguments from command line and from a file
                                         $ ./search_expression.py @args.txt -keyword foo""",
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-keyword', action="store", dest="keyword", default='ython',
                            help='keyword to search for, as a regular expression.'
                            )
        parser.add_argument('-root_dir', action="store", dest="root_dir", default="./searcher_data/search_dir",
                            help='directory to search. Default "../searcher_data/root_dir"'
                            )

        args = parser.parse_args()
        expression = args.keyword
        search_dir = args.root_dir

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

        results = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(search_dir,
                                                                                                        ignored_regex_objects, expression)
        print results
