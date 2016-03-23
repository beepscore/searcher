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
Note Be aware that setting followlinks to True can lead to infinite recursion  
if a link points to a parent directory of itself.  
walk() does not keep track of the directories it visited already.  
https://docs.python.org/2/library/os.html#os.walk

# Results

## To use from command line
cd to project root directory "searcher"

    cd searcher

### supply arguments on command line

    python ./searcher/search_expression.py -keyword 'ython' -root_dir './searcher_data/search_dir'

### supply arguments in a file
Create args file with desired values, e.g. searcher_args_this.txt.
On command line specify one argument @ prefix + args file name

    python ./searcher/search_expression.py '@./searcher_data/inputs/searcher_args_this.txt'

### use default arguments

    python ./searcher/search_expression.py

Result prints to terminal e.g.  

    Searching root_dir ./searcher_data/search_dir for keyword foo
    Results
    {   './searcher_data/search_dir': 4,
        './searcher_data/search_dir/level_1': 0,
        './searcher_data/search_dir/level_1/level_2': 0,
        './searcher_data/search_dir/level_1/level_2/level_3': 0}

## Unit tests
To run tests, open terminal shell.  
cd to project directory and run tests using command below. For more info see script.

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
