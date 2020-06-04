"""
What is a Tuple?

An ordered collection or grouping of items!

but it is immutable! cant be changed 
numbers = (1,2,3,4)

why use tuples?
 -tuples are faster than lists 
 -makes your code safer, safer from bugs
 - tuples are valid keys in a dictionary
"""

alphabet = ("a", "b", 'c', 'd')

# creating tuples
"""
    -can be created with parens
    -can be created with the tuple method
    - you can access tuple items by using [] : example tuple[2] uses index 

    - lists may not be used as a key in dictionary 
"""
# in a dictionary

locations = {
    (3.5, 4.5): "walmart",
    (8.5, 4.6): "target",
    (5.5, 4.7): "bestbuy",
    (2.5, 4.9): "some other store"
}

# searching a for a tuple in a dictionary
print(locations[(8.5, 4.6)])
