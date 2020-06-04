# set methods

# add
s = set({1, 2, 3, 4, 5})

s.add(7)  # takes a value and adds it to the end of the set
print(s)

# remove

s.remove(3)  # this will remove the value if it exists , if not , will throw an error
print(s)

# discard
# same as remove , will not return errors

s.discard(3)
print(s)

# copy

a = s.copy()  # this will copy a set and add it to a variable, they are equal but are not the same in memory
print(a)

# clear

s.clear()  # emptys the set
print(s)


# ********************* Set MATH ************************
math_students = {'matthew', 'helen', 'prashant', 'james', 'aparna', 'oliver'}
biology_students = {'jane', 'mathew', 'oliver', 'james', 'mesut', 'charlotte'}
# INTERSECTION
# will return the values that are the same in two or more sets in a single set
print(math_students & biology_students)

# SYMMETRIC_DIFFERENCE


# UNION

#                 pipe represents union
# in a union, will return the values in two or more sets and will not repeat them
print(math_students | biology_students)
