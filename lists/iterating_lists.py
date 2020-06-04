colors = ["purple", "teal", "magenta", 1.2, True]

for color in colors:  # singular in plural variable
    print(color)

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * number)


# while loops

numbers = [1, 2, 3, 4, 5]

i = 0  # here we set up an index to use to iterate over the list

while i < len(numbers):
    # you have to add the index variable so that it iterates each item in the loop
    print(numbers[i])
    i += 1

colors = ["purple", "red", "blue"]

index = 0

while index < len(colors):
    print(colors[index])
    print(f"{index}: {colors[index]}")
    index += 1
