#!/usr/bin/env python3

# References:
# https://docs.python.org/2/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


class SearcherArgReader:
    """
    Read arguments from command line or from a file.
    """

    def __init__(self):
        pass

    def args(self, commandline=None):
        """
        Read arguments from method argument commandline, command line or a file.
        Reference http://stackoverflow.com/questions/18325211/argparse-fails-when-called-from-unittest-test
        """

        parser = argparse.ArgumentParser(description="""    For help, use argument -h
                                         To specify an argument, prefix with -
                                         $ ./searcher/search_expression.py -expression a_regular_expression -root_dir directory_name
                                         To read arguments from a file, prefix file name with @
                                         $ ./searcher/search_expression.py @./searcher_data/inputs/searcher_args_test_result.txt
                                         To specify arguments from command line and from a file
                                         $ ./searcher/search_expression.py @./searcher_data/inputs/searcher_args_this.txt -expression foo""",
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-expression', action="store", dest="expression", default="foo",
                            help='expression regular expression to search for. Default "foo"'
                            )
        parser.add_argument('-root_dir', action="store", dest="root_dir", default="./searcher_data/search_dir",
                            help='directory to search. Default "./searcher_data/search_dir"'
                            )

        if commandline is not None:
            args = parser.parse_args(commandline)
        else:
            args = parser.parse_args()

        return args
