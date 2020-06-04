"""
**Doctests
-we can write tests for functions inside of the docstring 
-write code that looks like we are writing in a REPL >>>

python3 -m doctest -v test_file.py


** issues with doctests
-syntax is a little strange
-clusters up our function code
-lacks many features of larger testing tools
"""


def add(a, b):
    """
    >>> add(2,3)
    6

    >>> add(100,200)
    300


    """
    return a * b

# def double(values):
#     """ double the values in a list

#     >>> double([1,2,3,4])
#     [2,4,6,8]
#     >>> double([])
