# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums):
#             i = 0
#         result.append(nums[i])
#         i += 1
#     return result


# def current_beat():
#     nums = (1, 2, 3, 4)
#     i = 0
#     while True:
#         if i >= len(nums):
#             i = 0
#         yield nums[i]
#         i += 1


# print(current_beat())


def make_song(verses=99, beverage="soda"):
    for i in range(verses, -1, -1):
        if i > 1:
            yield "{} bottles of {} on the wall.".format(i, beverage)
        elif i == 1:
            yield "only 1 bottle of {} left!".format(beverage)
        else:
            yield "no more {}!".format(beverage)


def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)


kombucha_song = make_song(5, "kombucha")
print(kombucha_song)
