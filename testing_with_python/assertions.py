"""
**Assertions

-we can make simple assertions with the assert keyword
-assert accepts an expression
-returns NON if the expression is truthy
-Raises an AssertionError if the expression if falsy
-Accepts an optional error message as a second argument 

** Assertions warning
-if a python file is run with the -O flag, assertions will not be evaluated!
"""
# **Assertions example


# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y


# print(add_positive_numbers(1, 1))
# if not some_expression : raise AssertionError()
#     Truthy        Falsey


def eat_junk(food):
    assert food in ['pizza', 'ice cream', 'candy',
                    'fried butter'], "Food must be a junk food"
    return f"NOM NOM NOM I am eating {food}"


print(eat_junk(input("What would you like to eat?")))
