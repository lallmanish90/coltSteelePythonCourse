"""
map 

map is a standard function that accepets at LEAST  two arguments, 
a function and an "iterable"


iterable - somthing that can be iterated over (lists , stings, dicts, sets, tuples)

runs the lambda for each value in the iterable and returns a map object which can 
be converted into another data structure

map objects can only be iterated once 
"""

nums = [2, 4, 6, 8, 10]

doubles = list(map(lambda x: x * 2, nums))
print(doubles)
