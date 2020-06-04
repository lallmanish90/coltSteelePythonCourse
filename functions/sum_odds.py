def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total  # if return is inside the loop , will end the execution of the loop


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
