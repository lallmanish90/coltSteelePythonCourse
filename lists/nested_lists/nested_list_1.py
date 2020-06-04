nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# to access nested lists you just trail the index call with anther one
print(nested_list[-1][1])

print("____________________________________")
# nested loops

for lists in nested_list:
    for list in lists:
        print(list)
