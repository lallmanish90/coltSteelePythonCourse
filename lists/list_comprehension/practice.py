nums = [1, 2, 3, 4, 5, 6, 7]

odd_nums = [num for num in nums if num % 2 != 0]
print(odd_nums)

students = ["austin", "racheal", "maria", "saul", "ayden"]
teachers = ["blerk", "matt", "saul", "maria"]

names = [name.upper() for name in students if name in teachers]
print(names)
