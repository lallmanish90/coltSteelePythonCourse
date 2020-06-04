from functools import wraps


# def ensure_fewer_than_three_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if len(args) < 3:
#             return fn(*args, **kwargs)
#         return "Too many arguments!"
#     return wrapper


# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)


# print(add_all(1, 2, 4))


# from functools import wraps


# def ensure_authorized(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs.get("role") == "admin":
#             return fn(*args, **kwargs)
#         return "Unauthorized"
#     return wrapper


# @ensure_authorized
# def show_secrets(*args, **kwargs):
#     return "Shh! Don't tell anybody!"


# print(show_secrets(role="admin"))
from functools import wraps
from time import sleep


def delay(time):
    def inner(fn):
        @wraps(time)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(time, fn.__name__))
            sleep(time)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return 'hi'
