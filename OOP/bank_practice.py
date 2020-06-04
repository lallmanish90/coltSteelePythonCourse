class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def welcome(self):
        return f"welcome to python bank {self.owner}!"

    def getBalance(self):
        return {self.balance}

    def deposit(self, d):
        self.balance += d
        return f"you deposited ${d} new balance is ${self.balance}, thank you {self.owner}"

    def withdraw(self, w):
        self.balance -= w
        return f"you withdrew ${w}, your new balance is ${self.balance}, thank you {self.owner}"


acct = BankAccount("Darcy")

print(acct.owner())
