"""
Generators 

- Generators are iterators 
-generators can be created with generator functions 
-generator functions use the yield keyword
-generators can be created with generator expressions

Generator functions:
-generator functions are similar to normal functions but use the yield keyword instead of return
- can also yield multiple times instead of return once  
"""
# what yield does is it returns the iterable and passes until next is called on the iterable again.


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
