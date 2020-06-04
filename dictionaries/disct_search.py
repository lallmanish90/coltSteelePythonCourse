instructor = {
    "name": "saul",
    "owns_dog": True,
    "age": 26,
    "favorite_language": "JavaScript",
    "is great": True
}


# looking for a key
# key in dictionary
"name" in instructor  # True
"movie" in instructor  # False

if "name" in instructor:
    print("there is a name")

# looking for a value

if "saul" in instructor.values():
    print("there is a saul")
