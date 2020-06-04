instructor = {
    "name": "saul",
    "owns_dog": True,
    "age": 26,
    "favorite_language": "JavaScript",
    "is great": True
}

# clear

instructor.clear()  # will empty the dictionary
dict_copy = instructor.copy()  # will copy the dictionary

{}.fromkeys("a", "b")  # from keys will normally be called on an empty dict
# the first argument is the key and the second is the value in the dict

# you can use this to set the default

# example

new_user = {}.fromkeys(["user", "age", "premium member"], "None")
print(new_user)

# get
# this will return the key if it exists, if it does not exist, will return none
instructor.get("name")
