#!/usr/bin/env python

from searcher import expression_helper
from searcher import expression_searcher

argsfile = '@./searcher_data/inputs/searcher_args.txt'
mysearcher = expression_searcher.ExpressionSearcher(argsfile)

ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
ignored_regex_objects = expression_helper.ExpressionHelper.regex_objects_from_patterns(ignored_filename_patterns)

results = expression_searcher.ExpressionSearcher.directories_number_of_files_containing_keyword(mysearcher.search_dir,
        ignored_regex_objects, mysearcher.expression)

print results

