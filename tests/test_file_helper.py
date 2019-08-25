#!/usr/bin/env python3

import unittest
from searcher import file_helper
from searcher import expression_helper
import os
import pathlib


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_directories_in_dir_recursive_dont_ignore(self):

        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        # use os.path.join so macos and linux will use separator '/' and Windows will use separator '\'
        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        # search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.directories_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {os.path.join('.', 'searcher_data', 'search_dir'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4')
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore1(self):

        ignored_dirname_patterns = ['level_1']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        actual = file_helper.directories_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {os.path.join('.', 'searcher_data', 'search_dir')}
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore_git(self):

        # Note: git version control normally ignores its own database .git
        # So for testing, committed a file search_dir/level_1/.git_fake/objects_fake/object_fake

        ignored_dirname_patterns = [r'\.git']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        actual = file_helper.directories_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {os.path.join('.', 'searcher_data', 'search_dir'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4')
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore2(self):

        ignored_dirname_patterns = ['level_2']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        actual = file_helper.directories_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {os.path.join('.', 'searcher_data', 'search_dir'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake')
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore3(self):

        ignored_dirname_patterns = ['level_3']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        actual = file_helper.directories_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {os.path.join('.', 'searcher_data', 'search_dir'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2')
                    }
        self.assertEqual(expected, set(actual))

    def test_files_in_dir(self):

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'httppython.org',
                    'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                    'httpswww.google.com#q=python',
                    'httpwww.beepscore.comhubcape',
                    }

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_ignore_ython(self):

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$', r'ython']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'httpwww.beepscore.comhubcape'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_1(self):

        ignored_regex_objects = expression_helper.regex_objects_from_patterns(expression_helper.ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'a.txt', 'c.txt alias'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_2(self):

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'b.txt', 'c.txt', 'd.txt'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_level_3(self):

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'d.txt alias'}

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_set_from_reordered_list(self):
        """ test we are using set correctly. """

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.files_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected_from_reordered_list = {'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                                        'httpswww.google.com#q=python',
                                        'httpwww.beepscore.comhubcape',
                                        'httppython.org'
                                        }

        self.assertEqual(expected_from_reordered_list, set(actual))

    # test files_in_dir_recursive

    def test_files_in_dir_recursive(self):
        ignored_directory_patterns = [r'\A\.$', r'\A\.\.$']
        ignored_directory_regex_objects = expression_helper.regex_objects_from_patterns(ignored_directory_patterns)

        ignored_filename_patterns = [r'\A\.DS_Store$']
        ignored_file_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        # TODO: fix recursive to work withpathlib.Path
        # search_dir_full_path =pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.files_in_dir_recursive(search_dir_full_path,
                                                    ignored_directory_regex_objects,
                                                    ignored_file_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
                    os.path.join('.', 'searcher_data', 'search_dir', 'httpwww.beepscore.comhubcape'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4', 'test_result01.txt'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake', 'object_fake'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'c.txt alias'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'httpswww.google.com#q=python'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'something.exe'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'a.txt'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'c.txt'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'httpsen.wikipedia.orgwikiPython_%28programming_language%29'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'httppython.org'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'b.txt'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'd.txt'),
                    os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'd.txt alias')
                    }

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_recursive_ignore_ython(self):
        ignored_directory_patterns = [r'\A\.$', r'\A\.\.$']
        ignored_directory_regex_objects = expression_helper.regex_objects_from_patterns(ignored_directory_patterns)

        ignored_filename_patterns = [r'\A\.DS_Store$', r'ython']
        ignored_file_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir')
        actual = file_helper.files_in_dir_recursive(search_dir_full_path,
                                                    ignored_directory_regex_objects,
                                                    ignored_file_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            os.path.join('.', 'searcher_data', 'search_dir', 'httpwww.beepscore.comhubcape'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4', 'test_result01.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake', 'object_fake'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'c.txt alias'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'something.exe'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'a.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'c.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'b.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'd.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'd.txt alias')
        }

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_recursive_level_2(self):
        ignored_directory_patterns = [r'\A\.$', r'\A\.\.$']
        ignored_directory_regex_objects = expression_helper.regex_objects_from_patterns(ignored_directory_patterns)

        ignored_filename_patterns = [r'\A\.DS_Store$']
        ignored_file_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path = os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2')
        actual = file_helper.files_in_dir_recursive(search_dir_full_path,
                                                    ignored_directory_regex_objects,
                                                    ignored_file_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4', 'test_result01.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'c.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'b.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'd.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'd.txt alias')
        }

        self.assertEqual(expected, set(actual))

    def test_files_in_dir_recursive_level_3(self):
        ignored_directory_patterns = [r'\A\.$', r'\A\.\.$']
        ignored_directory_regex_objects = expression_helper.regex_objects_from_patterns(ignored_directory_patterns)

        ignored_filename_patterns = [r'\A\.DS_Store$']
        ignored_file_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_path = os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3')
        actual = file_helper.files_in_dir_recursive(search_dir_path,
                                                    ignored_directory_regex_objects,
                                                    ignored_file_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4', 'test_result01.txt'),
            os.path.join('.', 'searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'd.txt alias')
        }

        self.assertEqual(expected, set(actual))

# test pathlib functions

    def test_pathlib_path(self):
        """
        test shows how to use pathlib.Path() and joinpath()
        """
        search_dir_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')
        search_dir_posix = search_dir_path.as_posix()

        self.assertEqual(search_dir_posix, 'searcher_data/search_dir')

    def test_directory_paths_in_dir_recursive_dont_ignore(self):
        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_full_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.directory_paths_in_dir_recursive(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            pathlib.Path('.').joinpath('searcher_data', 'search_dir'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', '.git_fake'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4')
        }
        self.assertEqual(expected, set(actual))

    def test_directory_paths_in_dir_recursive_ignore1(self):
        ignored_dirname_patterns = ['level_1']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.directory_paths_in_dir_recursive(search_dir_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            pathlib.Path('.').joinpath('searcher_data', 'search_dir'),
        }
        self.assertEqual(expected, set(actual))

    def test_directory_paths_in_dir_recursive_ignore_git(self):
        # Note: git version control normally ignores its own database .git
        # So for testing, committed a file search_dir/level_1/.git_fake/objects_fake/object_fake

        ignored_dirname_patterns = [r'\.git']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.directory_paths_in_dir_recursive(search_dir_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            pathlib.Path('.').joinpath('searcher_data', 'search_dir'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', 'level_2', 'level_3', 'level_4')
        }
        self.assertEqual(expected, set(actual))

    def test_directory_paths_in_dir_recursive_ignore2(self):
        ignored_dirname_patterns = ['level_2']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        search_dir_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.directory_paths_in_dir_recursive(search_dir_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            pathlib.Path('.').joinpath('searcher_data', 'search_dir'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', '.git_fake'),
            pathlib.Path('.').joinpath('searcher_data', 'search_dir', 'level_1', '.git_fake', 'objects_fake'),
        }
        self.assertEqual(expected, set(actual))

    def test_paths_in_dir(self):

        ignored_filename_patterns = [r'\A\.$', r'\A\.\.$', r'\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        search_dir_full_path = pathlib.Path('.').joinpath('searcher_data', 'search_dir')

        actual = file_helper.paths_in_dir(search_dir_full_path, ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {
            search_dir_full_path.joinpath('httppython.org'),
            search_dir_full_path.joinpath('httpsen.wikipedia.orgwikiPython_%28programming_language%29'),
            search_dir_full_path.joinpath('httpswww.google.com#q=python'),
            search_dir_full_path.joinpath('httpwww.beepscore.comhubcape'),
        }
        self.assertEqual(expected, set(actual))


if __name__ == "__main__":
    unittest.main()
