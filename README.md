# searcher

# Purpose
Search directory for files that contain a search term regular expression "keyword".  

# References

## websearcher Python 3
https://github.com/beepscore/websearcher

## search_terms ruby
https://github.com/beepscore/search_terms

## walk directories

### os.walk
Note Be aware that setting followlinks to True can lead to infinite recursion if a link points to a parent directory of itself.  
walk() does not keep track of the directories it visited already.  
https://docs.python.org/2/library/os.html#os.walk

## Mark Smith - Writing Awesome Command-Line Programs in Python
https://www.youtube.com/watch?v=CJ7-SroGtZ8

# Results

## To use from command line
cd to project root directory "searcher"

    cd searcher

### supply arguments on command line
Result prints to terminal.

    python ./searcher/search_expression.py -keyword 'ython' -root_dir './searcher_data/search_dir'

### supply arguments in a file
Create args file with desired values, e.g. searcher_args_test_result.txt.  
On command line specify one argument @ prefix + args file name

    python ./searcher/search_expression.py @./searcher_data/inputs/searcher_args_test_result.txt

    Searching root_dir ./searcher_data/search_dir/ for keyword ^[a-zA-Z]+_TESTResult.*
    Results
    {   './searcher_data/search_dir/': 0,
        './searcher_data/search_dir/level_1': 0,
        './searcher_data/search_dir/level_1/level_2': 0,
        './searcher_data/search_dir/level_1/level_2/level_3': 0,
        './searcher_data/search_dir/level_1/level_2/level_3/level_4': 1}

### use default arguments

    python ./searcher/search_expression.py

    Searching root_dir ./searcher_data/search_dir for keyword foo
    Results
    {   './searcher_data/search_dir': 4,
        './searcher_data/search_dir/level_1': 0,
        './searcher_data/search_dir/level_1/level_2': 0,
        './searcher_data/search_dir/level_1/level_2/level_3': 0,
        './searcher_data/search_dir/level_1/level_2/level_3/level_4': 0}

## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.

### python command
This command lists and tests all modules except searcher_arg_reader.

    python -m unittest tests.test_expression_searcher tests.test_expression_helper tests.test_file_helper

#### searcher_arg_reader_tests
Attempting to run searcher_arg_reader_tests has problem with arguments for unittest and for argparse.  
e.g. python -m unittest discover says "unrecognized arguments: discover" and wants the argparse arguments.  
TODO: Consider alternative solutions.  
http://stackoverflow.com/questions/35270177/passing-arguments-for-argparse-with-unittest-discover

### Bash script
Runs all test modules.  
Works on OS X. On Windows may work with Cygwin, I don't know.

    $ ./bin/run_tests

# Appendix- Requirements
Use Python language v2.7.x

Implement a stand-alone script that does the following:

## Input:
taking an argument “root_dir” as a root directory to start traversing  
taking an argument “keyword” as a regular expression for example ( “^[a-zA-Z]+_TESTResult.*” )  
to detect that a file contains a string

## Functionality:
The script should recursively walk the “root_dir”  
and detect all the files under that dir contains “keywords” and count the number of files for that sub dir.  
All results should be saved in a key:value array  
with key being subdir string, and value being counts of file contains the key line  

## Output:
A output array of all the data, for example {’a/b’: 6, ’a/b/c’: 7, ‘/a/b/c/d’:0}  
Stretch goal:- An output graph with a plot with X as subdir name string, Y as count values.  

## Tests:
Please design a set of tests for the above routine you just wrote,  
how many ways can break the routine above and how many ways can you test the routine.  
Send these tests in a text file.  

The code will be evaluated based on the following criteria:
- Coding style - module name, class name, functions, clarity, data structure, algorithms etc.
- Argument handling - what module do you use for argument that’s easy to expend, exception checking etc.
- Portability - think about how your program would behavior for various OS systems
- Scalability - how do you make your routine scalable, multithreading, parallel computing etc.
- Reliability - how robust can you make the routine that under any environment it won’t crash - either exit gracefully with error message or complete what you can
