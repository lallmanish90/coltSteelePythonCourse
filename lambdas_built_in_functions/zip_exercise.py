def interleave(arg1, arg2):
    return "".join("".join(x) for x in (zip(arg1, arg2)))


print(interleave("hi", "no"))


def triple_and_filter(nums):
    return [(n * 3) for n in (tuple(filter(lambda n: n % 4 == 0, nums)))]


print(triple_and_filter([2, 4, 16, 32, 35]))
