instructor = {
    "name": "saul",
    "owns_dog": True,
    "age": 26,
    "favorite_language": "JavaScript",
    "is great": True
}

"""
Takes a single argument corresponding to a key and removes 
that key-value pair from the dictionary. Returns the value correspoding 
to the key that was removed 
"""

# requires at least one argument


instructor.pop("is great")
# will return a boolean value
instructor.popitem()  # this will remove a random key and value then return the key/value
instructors = {}
# this will add the value to a dictionary from another
instructors.update(instructor)
# and will not delete existing data but will update data if they match
