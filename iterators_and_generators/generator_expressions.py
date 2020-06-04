"""
Generator Expressions

-you can also create generators from generator expressions
-generators expressions look a lot like list comprehensions
-generator expressions use() instead of []

"""


# def nums():
#     for num in range(91, 10):
#         yield num
# # or


# g = (num for num in range(1, 10))
import time

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
