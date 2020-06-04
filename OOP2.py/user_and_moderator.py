class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_strings(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
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


class Moderator(User):
    total_mods = 0
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active moderators"

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name} removed a post from {self.community} community"


print(User.display_active_users())
u1 = User("tom", "garcia", 35)
u2 = User("tom", "garcia", 35)
u3 = User("tom", "garcia", 35)
print(User.display_active_users())
jasmine = Moderator("jasmine", "o'conner", 61, 'piano')
jasmine2 = Moderator("jasmine", "o'conner", 61, 'piano')
print(User.display_active_users())
print(Moderator.display_active_mods())
