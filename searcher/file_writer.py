#!/usr/bin/env python

import os


class FileWriter:
    """
    Writes file to path.
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    """

    @staticmethod
    def absolute_dir_path(dirname):
        # Note Python does not expand ~ in path as on OS X
        # http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        # current_dir is absolute path
        # current_dir = os.path.dirname(__file__)
        absolute_path = os.path.abspath(dirname)
        return absolute_path

    @staticmethod
    def absolute_file_path(dirname, filename):
        absolute_dir_path = FileWriter.absolute_dir_path(dirname)
        absolute_file_path = os.path.join(absolute_dir_path, filename)
        return absolute_file_path

    def __init__(self, dirname, filename, content):
        self.filename = filename
        self.dirname = dirname
        self.content = content

