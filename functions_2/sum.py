#        *args
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(4, 6, 9, 4, 10))
print(sum_all_nums(4, 6))


def ensure_correct_info(*args):
    if "saul" in args and "vega" in args:
        return "welcome back Saul"
    return "who are you ??"


print(ensure_correct_info("saul", "vega"))
print(ensure_correct_info("maria", "vega"))
