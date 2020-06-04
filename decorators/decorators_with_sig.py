def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, i'm {name}."


@shout
def order(main, side):
    return f"hi, id like the {main}, with a side of {side}, please!"


print(greet("todd"))
print(order("burger", "fries"))
