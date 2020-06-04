# *************ALL*****************
# returns True if all elements of the iterable are truthy(or if the iterable is empty)

all([0, 1, 2, 3])  # all returns False

# example
people = ['Cody', "Chealse", "Cody"]
name = [name[0] == "C" for name in people]
print(all(name))

# *************Any*****************
# return true if ANY element of the iterable is truthy:

# example:

peoples = ['Cody', "Chealse", "Cody"]
names = [name[1] == "o" for name in peoples]
# only two of the 3 items inside the list are true, any will return true because
# there is at least one True value in the list
print(any(names))

# *************sorted *****************
# returns a new sorted list copy from the items in the iterable
# will sort lists,tuples, dicts unlike .sort
# the return value is a COPY of the iterable, sorted does not change the iterable
nums = [2, 33, 55, 24, 78]
print(sorted(nums))
print(sorted(nums, reverse=True))


# *************Max *****************
# returns the largest item in the iterable or the largest of two or more arguments

max(3, 67, 99)
max("a", "D", "e")
# *************Min *****************
# returns the smallest item in the iterable or the smallest of two or more arguments

max(3, 67, 99)
max("a", "D", "e")

# to bring back the actual value of the iterable

max(names, key=lambda n: len(n))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "servicer", "playcount": 12},
    {"title": "YMCA", "playcount": 1000},
    {"title": "Toxic", "playcount": 50},
]

min(songs, key=lambda s: s["playcount"])["title"]
