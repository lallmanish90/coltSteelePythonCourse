"""
range(7): gives you integers from 0 thru 6
range(1,8): gives you integers from 1 through 8 but excludes 8
range(1,10,2): will give you odds from 1 to 10
range(7,0,-1): will give you integers from 7 to 1

"""

r = range(10)

print(list(r))  # this will make it a list in the termial

# this will make the list odd numbers. The way it is read is
nums = range(1, 10, 2)
# 1-10 and then exlude every second number
print(list(nums))
nums = range(20, 100, 2)
# 20-100 and then exlude every second number
print(list(nums))
