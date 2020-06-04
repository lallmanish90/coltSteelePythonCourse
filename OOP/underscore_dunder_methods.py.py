# _name  - single underscore in front means , this is a private
# __name - when trying to print, this will do name mangleing , looks like _class__firstDoubleUnderscore
# __name__ - dunder methods convention to respect, should not define your own ,reserved for python


class Person:
    def __init__(self):
        self._secret = "hi!"
        self.name = "Tony"
        self.__message = "i like turtles"


p = Person()

print(p.name)
print(p._secret)
print(p._Person__message)
