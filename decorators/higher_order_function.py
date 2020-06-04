"""
higher order functions

- return a function from inside it 
-or accepts another function


"""
"""

def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x * x*x


print(sum(3, cube))
"""

"""
# this is a different type of HOC , it uses a function within a function 

def greet(person):
    def get_mood():
        msg = choice(('hello there ', 'go away ', 'i love you '))
        return msg

    result = get_mood() + person
    return result


print(greet("toby"))
"""
"""
# we can return funcs from other funcs

from random import choice
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('hahahaha', 'lol', 'tehehe'))
        return f"{laugh} {person}"
    return get_laugh


laugh = make_laugh_at_func("linda")

print(laugh())
"""
