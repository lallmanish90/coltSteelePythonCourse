list1 = [1, 2, 3, 4, 5]
print(list1)
# append adds to the end of the list, append adds ONE ITEM to the end
list1.append(6)
# the one item can be any of the data types including another list
print(list1)

print("extend method")
# extend addeds to the end of the list and only uses one argument
list1.extend([8, 0])
# you have to wrap the desired input inside brackets to be added into the list
# doing this will add each input as an individual part of the list,
# not add as a whole list
print(list1)

print("insert method")

list2 = [1, 2, 3, 4]
# with this method, first argument is what index you want to
list2.insert(2, "insert")
# insert at , then the item you want to insert
print(list2)
