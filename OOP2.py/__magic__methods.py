"""
Magic Methods
what is happing in our example?
8 + 2
'8' + '2'

the + operator is shorthand for a special method called __add__()
that gets called on the first operand.

if the first(left) operand is an instance of int, __add__() does
mathematical addition. if it's a string, it does string
concatenation.
"""
from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Human named {self.first} {self.last} aged {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="newborn", last=self.last, age=0)
        return "you cant add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "can't multiply"


j = Human("jenny", "larsen", 47)
k = Human("Kevin", "jones", 49)
# print(j)
# print(len(j))

# print(j + k)
triplets = j * 3
triplets[1].first = "Jessica"
# print(triplets)

triplets = (k + j) * 3
print(triplets)
