instructor = {
    "name": "saul",
    "owns_dog": True,
    "age": 26,
    "favorite_language": "JavaScript",
    "is great": True
}

for v in instructor.values():  # iterates for  value
    print(v)
for k in instructor.keys():  # iterates for key
    print(k)

for i in instructor.items():  # iterates for key and value
    print(i)

for k, v in instructor.items():
    print(f"key: {k} , value: {v}")
