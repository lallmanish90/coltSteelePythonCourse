"""
Inheritance and objectives

*inheritance
- a key feature of OOP is the ability to define a class which inherits from
another class(a "base" or "parent" class)




"""
# EXAMPLE:


class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    pass


blue = Cat()
# blue.make_sound("meow")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)
print(isinstance(blue, Animal))
