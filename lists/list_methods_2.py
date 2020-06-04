# Clear
print("Clear method")

list_1 = ["socks", "mug", "tea pot", "cat food"]
print(list_1.clear())


# pop
print("pop method")
# pop method will remove the last item by default, or if you pass in index, it will
# remove that item located at that index
# it will return the removed item
list_2 = ["socks", "mug", "tea pot", "cat food"]

print(list_2.pop(0))
print(list_2)

# remove
print("remove method")
# using the remove method will remove the first item in the list that matches
# the argmuent passed into the remove method
# this argument will take in a value, not an index to remove the item

list_3 = ["socks", "mug", "tea pot", "cat food"]
print(list_3)
list_3.remove("socks")
print(list_3)
