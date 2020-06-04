
class User:
    def __init__(self, first, last, age):
        #print("A new user has been made!")
        self.first = first
        self.last = last
        self.age = age

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


user1 = User("Joe", "Flaco", 32)
user2 = User("Blanca", "Lopez", 69)


print(user1.full_name())
print(user1.likes("chips"))
print(user2.initials())
print(user2.is_senior())
print(user2.birthday())
