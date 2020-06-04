"""
**raise your own exception!**
-can be used by using the raise keyword
example:

raise ValueError("invalid error")
"""


def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError("text must be instance of string")
    if color not in colors:
        raise ValueError('value is invalid color')
    print(f"printed {text} in {color}")


print(colorize("hello", "blue"))
print(colorize(34, "red"))  # this will raise error


def divide(num1, num2):
    try:
        total = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
