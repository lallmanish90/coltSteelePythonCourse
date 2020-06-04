instructor = {
    "name": "saul",
    "owns_dog": True,
    "age": 26,
    "favorite_language": "JavaScript",
    "is great": True
}

print(instructor["name"])
"""
unlike lists where you have to pass an index to find the key, you can pass in
the value you are looking for and value will be returned

If you don't know what is in the the dictionary you are looking for and pass
in an key that does not exist, you will get a typeError
"""

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)
