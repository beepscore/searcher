#!/usr/bin/env python3

import unittest
from searcher import expression_helper


class TestExpressionHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_ignored_filename_patterns(self):
        expected = ['\A\.$', '\A\.\.$', '\A\.DS_Store$', '\.git', '\.svn', '\.exe$']
        self.assertEqual(expected, expression_helper.ignored_filename_patterns)

    def test_is_string_matched_in_regular_expression_objects_dot(self):
        """ match '.' representing current directory
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects('.', ignored_regex_objects))

        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('..', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('a.', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('.c', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('a.c', ignored_regex_objects))

    def test_is_string_matched_in_regular_expression_objects_dotdot(self):
        """ match '..' representing directory above current directory
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.\.$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects('..', ignored_regex_objects))

        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('a..', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('..c', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('a..c', ignored_regex_objects))

    def test_is_string_matched_in_regular_expression_objects_dotDS_Store(self):
        """ match '.DS_Store' OSX file system file
        \A matches only at start of string
        $ matches at end of string
        https://docs.python.org/2/library/re.html
        """

        ignored_filename_patterns = ['\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects('.DS_Store', ignored_regex_objects))

        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('a.DS_Store', ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects('.DS_Storeb', ignored_regex_objects))

    def test_is_string_matched_in_regular_expression_objects_inner(self):
        """ match 'ython' within string. Case sensitive """

        ignored_filename_patterns = ['ython']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects("A big python is here.", ignored_regex_objects))

        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects("A big pythoxyz", ignored_regex_objects))

    def test_is_string_matched_in_regular_expression_objects_dot_git(self):
        ignored_filename_patterns = ['\.git']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects(".git", ignored_regex_objects))
        self.assertTrue(expression_helper.is_string_matched_in_regular_expression_objects("a/.git/objects", ignored_regex_objects))

        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects("git", ignored_regex_objects))
        self.assertFalse(expression_helper.is_string_matched_in_regular_expression_objects("a/git/objects", ignored_regex_objects))


if __name__ == "__main__":
    unittest.main()
