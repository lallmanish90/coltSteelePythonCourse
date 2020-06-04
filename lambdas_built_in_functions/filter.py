"""
Filter 
- there is a lambda for each value in the iterable.
-returns filter object which can be converted into other iterables 
-the object contains only the values that return true to the lambda 
"""

l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

names = ["austin", "amy", "arnold", "maria", "saul"]

a_names = filter(lambda n: n[0] == 'a', names)
print(list(a_names))
