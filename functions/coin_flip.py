from random import random


def flip_coin():
    # generate random number  0-1
    r = random()
    if r > 0.5:
        return "heads"
    else:
        return "tails"

# or , sidenote: this will overwrite the previous function


def flip_coin():
    # generate random number  0-1
    if random() > 0.5:
        return "heads"
    else:
        return "tails"


print(flip_coin())
