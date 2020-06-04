"""
Sets
-sets are like formal mathematical sets.
- sets do not have duplicate values
-elements in sets aren't ordered.
-cannot access items in a set by index
"""
# sets cannot have duplicates
s = set({1, 2, 3, 4, 5, 5, 5})  # will return :{1, 2, 3, 4, 5}

# creating a new set
a = set({1, 4, 5})

# creates a set with the same values as above
b = {1, 4, 5}

4 in s  # True

5 in s  # True


# accessing values in a set

# can use loops

for thing in s:
    print(thing)
