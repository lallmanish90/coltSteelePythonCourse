total = 0


def increment():
    total += 1
    return total  # this will not work


def increment():
    global total
    total += 1
    return total  # this will not work

# accessing , not trying to change it


name = "rusty"


def greet():
    print(name)  # this way it can be accessed, just not changed in any way
    # cannot change the global variable state


# nonlocal can access the parent variable and change it

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


outer()
