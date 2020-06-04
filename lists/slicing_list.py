# slice

# some_list[start:end:step]
# uses index as arguments

first_list = [1, 2, 3, 4]
first_list[1]  # this willl return the item of that index
first_list[1:]  # this syntax is used if only taking in the start argument
# you can also use negative numbers for slicing backwards
# slices also create a copy of the list, does not change the acutal list
# this will count backwards two from the end and return those values
first_list[-2:]
print(first_list[-2:])  # this would return the 3 and 4 from the list

# second paramerter for Slice : end!
# this is EXCLUSIVE, will not include the item

first_list = [1, 2, 3, 4, 5]

# here the number that will be brought back is everthing before the index of 2
first_list[:2]
# same thing with negative numbers, it will count to the index, and will
first_list[:-1]
# not include that index in the slice

first_list[3:-2]  # will bring back everything in between of these indexs

# third parameter for slice: the is the step

second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(second_list[1:-1:3])
# this will bring back all the numbers between index of 1 and -1
# also will only bring back every 3 numbers between that slice.
# the third argument is the steps , will skip numbers between those steps

# if you start using negative step values, this will count backwards in the index

