"""
Defining the simplest possible class

whenever creating a class , python

"""
# classes are singular with camel case
# self referse to the that current instance
# init will auto run when a class is called


class User:
    def __init__(self, first, last, age):
        #print("A new user has been made!")
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Flaco", 32)
user2 = User("Blanca", "Smith", 17)

print(user1.first)
print(user1.last)
print(user1.age)
print(user2.first)
print(user2.last)
print(user2.age)
