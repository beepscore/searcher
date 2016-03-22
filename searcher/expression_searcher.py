#!/usr/bin/env python

from searcher import searcher_arg_reader
from searcher import file_helper
import re
import os


class ExpressionSearcher:
    """
    Controller composed of several objects.
    Reads input commands.
    Searches files for expression.
    """

    @staticmethod
    def search_file(expression, search_dir, file_name):
        """
        In directory search file for expression

        return file name if file contains expression
        """
        if file_name == ".DS_Store":
            # avoid read error
            return None

        else:
            file_path = file_helper.FileHelper.absolute_file_path(search_dir, file_name)

            if os.path.isdir(file_path):
                # avoid read error
                return None

            textfile = open(file_path, 'r')
            text = textfile.read()
            textfile.close()
            matches = re.findall(expression, text)
            if matches == []:
                return None
            else:
                return file_name

    def __init__(self, argfile):
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = searcher_arg_reader.SearcherArgReader()
        self.args = self.arg_reader.args([argfile])
        self.expression = self.args.keyword
