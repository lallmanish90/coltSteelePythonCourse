# index
print("index methods")

list_1 = [1, 2, 4, 5, 6, 7, 8, 9, 9, 12, 11]

print(list_1)

list_1.index(12)  # this will return the index of the value
print(list_1.index(12))

# this will return the value of 12 after the index of 3
print(list_1.index(12, 3))
# this will return the value of 12 after the index of 3
print(list_1.index(12, 3, 10))
# and before the index of 10. index is also INCLUSIVE

# Count
print("count methods")

list_1 = [1, 2, 4, 5, 6, 7, 8, 9, 9, 12, 11]

# count will bring back how many times the value occures in the list
print(list_1.count(9))


# reverse
print("reverse method")
print(list_1)
list_1.reverse()  # this will bring back the list in reverse
print(list_1)


# Sort

print("sort method")
list_1 = [1, 2, 4, 5, 6, 7, 8, 9, 9, 12, 11]

list_1.sort()  # this will sort in acending order will do this with numbers as well as letters
# Capital letters are first when sorting with this method
print(list_1)


# join

print("join method")
name = ["mr", "vega"]
".".join(name)  # mr. vega
print(".".join(name))
# this will take the value at the front of the method and then takes the list as the argument
