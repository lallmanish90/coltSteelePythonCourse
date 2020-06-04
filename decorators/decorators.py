"""
whats a decorator ??

- decorators are functions
-decorators wrap other functions and enhance their behavior 
-decorators are example of higher order functions
-decorators have their own syntax, using "@" (syntactic sugar)
"""

"""
def be_polite(fn):
    def wrapper():
        print("what a pleasure to meet you!")
        fn()
        print("have a nice day")
    return wrapper()


def greet():
    print("my name is colt")


def rage():
    print("I hate you!")


wrapped_greet = be_polite(greet)


polite_rage = be_polite(rage)
"""

# the @ wraps the functions below it with the function after the @


def be_polite(fn):
    def wrapper():
        print("what a pleasure to meet you!")
        fn()
        print("have a nice day")
    return wrapper()


@be_polite
def greet():
    print("my name is colt")


@be_polite
def rage():
    print("I hate you!")


rage
