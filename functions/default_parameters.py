def exponent(num, power=2):  # adding the = , will set the power to the default value
    return num ** power


print(exponent(2, 9))
print(exponent(2, 9))


# example

def add(a=10, b=20):
    return a + b


print(add(2, 3))
print(add())


# default params can be any data structure and even other functions!

def math(a, b, fn=add):  # defaults should be at the end or all parameters should have defaults
    # for reassignments

    # print(math(2, 3))

    # Define speak below:


def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"


print(speak())
