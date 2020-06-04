# ************************** Set Comprehension ******************************
print({x**2 for x in range(10)})
# this looks just like comprehension for dictionaries
# the difference is you don't create a key value pair like in dictionaries

# this would be a dictionary
print({x: x**2 for x in range(10)})
