# searcher

# Purpose
Search directory for files that contain a search term regular expression "expression".

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

    python ./searcher/search_expression.py -expression 'ython' -root_dir './searcher_data/search_dir'

### supply arguments in a file
Create args file with desired values, e.g. searcher_args_test_result.txt.  
On command line specify one argument @ prefix + args file name

    python ./searcher/search_expression.py @./searcher_data/inputs/searcher_args_test_result.txt

    Searching root_dir ./searcher_data/search_dir/ for expression ^[a-zA-Z]+_TESTResult.*
    Results
    {   './searcher_data/search_dir/': 0,
        './searcher_data/search_dir/level_1': 0,
        './searcher_data/search_dir/level_1/level_2': 0,
        './searcher_data/search_dir/level_1/level_2/level_3': 0,
        './searcher_data/search_dir/level_1/level_2/level_3/level_4': 1}

### use default arguments

    python ./searcher/search_expression.py

    Searching root_dir ./searcher_data/search_dir for expression foo
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
Attempting to run test_searcher_arg_reader has problem with arguments for unittest and for argparse.  
e.g. python -m unittest discover says "unrecognized arguments: discover" and wants the argparse arguments.  
TODO: Consider alternative solutions.  
http://stackoverflow.com/questions/35270177/passing-arguments-for-argparse-with-unittest-discover

### Bash script
Runs all test modules.  
Works on OS X. On Windows may work with Cygwin, I don't know.

    $ ./bin/run_tests

## Appendix virtual environment venv

The project uses a virtual environment.

https://docs.python.org/3/library/venv.html

This can hold a python version and pip installed packages such as "requests".

https://github.com/kennethreitz/requests

### Install virtual environment in directory named "venv"

    $ cd <project root directory>
    $ pyvenv venv

### Before activating virtual environment

On my machine, active python is 2.7.11

    ➜  searcher git:(master) ✗ which python
    /usr/local/bin/python
    ➜  searcher git:(master) python --version
    Python 2.7.11

On my machine, to use python3 must specify python3

    ➜  searcher git:(master) which python3
    /usr/local/bin/python3

### Use virtualenv to activate the desired virtual environment
#### on macOS
    ➜  searcher git:(master) source venv/bin/activate

#### on Windows
    venv\Scripts\activate

### Now active python is in venv and is version 3.5.1

Notice command prompt shows venv is active

    (venv) ➜  searcher git:(master) which python
    /Users/stevebaker/Documents/projects/pythonProjects/searcher/venv/bin/python
    (venv) ➜  searcher git:(master) python --version
    Python 3.5.1

### Deactivate virtual environment
In shell run deactivate
    (venv) ➜  searcher git:(master) ✗ deactivate
