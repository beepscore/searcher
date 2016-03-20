#!/usr/bin/env python

import os
import os.path


class DirWalker:
    """
    Walks directory

    http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
    https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
    """

    @staticmethod
    def files_in_dir_recursive(dir):
        """ return list of files in dir and subdirectories """
        ignored_filenames = ['.DS_Store']
        file_paths = []
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if filename in ignored_filenames:
                    continue
                full_name = os.path.join(dirpath, filename)
                file_paths.append(full_name)
        return file_paths


#    def walk_files_in_dir(dir, method):
#        """ walks a directory, and executes a method on each file """
#        dir = os.path.abspath(dir)
#        for file in [file for file in os.listdir(dir) if not file in [".",".."]]:
#            nfile = os.path.join(dir,file)
#                method(nfile)
#                if os.path.isdir(nfile):
#                    self.walk(nfile,method)
