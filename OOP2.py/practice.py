class Human:
    def __init__(self, name, age):
        self._name = name
        if age > 0:
            self._age = age
        else:
            self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name_change(self, name):
        self._name = name


angie = Human("angie", 34)

print(angie.age)
angie.name_change("saul")
print(angie.name)
