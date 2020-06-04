"""
Class Attributes 

-we can also define attributes directly on a class that are shared by all instances of a class and
the class itself. 

- class attributes are used way less than instance attributes and instance methods 


"""


class User:
    # class attributes dont use self in it
    active_users = 0

    def __init__(self, first, last, age):
        #print("A new user has been made!")
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday {self.first}!"


print(User.active_users)
user1 = User("Joe", "Flaco", 32)
user2 = User("Blanca", "Lopez", 69)


# print(user1.full_name())
# print(user1.likes("chips"))
# print(user2.initials())
# print(user2.is_senior())
# print(user2.birthday())
print(User.active_users)
print(user2.logout())
print(User.active_users)
