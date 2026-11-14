import json
import os

name = "hyarel"
age = 25
balance = 1000.50
is_active = True

friends = ["priya", "rahul", "amit"]
account = {"name": "hyarel", balance: 1000, "city": "pune"}
branches = ("pune", "mumbai", "delhi")
cities = {"pune", "mumbai", "pune"}

total = 1000 + 500
left = 1000 - 500

hello_list = [f"Hello {friend}" for friend in friends]  #list compresion 
account_copy = {key: value for key, value in account.items()} #directory  compresion

#iterartor
friends_iterator = iter(friends)
first_friend = next(friends_iterator)
second_friend = next(friends_iterator)

#generator

def count_generator():
    yield 1
    yield 2
    yield 3

gen = count_generator()
g1 = next(gen)
g2 = next(gen)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        return f"{self.name} has {self.balance} rupees"

class SavingAccount(BankAccount):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest
    
    def add_interest(self):
        self.balance = self.balance + self.interest
        return f"{self.name} new balance with interest is {self.balance}"

    def show_interest(self):
        return f"{self.name} interest is {self.interest}"

a1 = BankAccount("Hyarel", 1000)
s1 = SavingAccount("Priya", 1000, 100)

print(a1.show())
print(s1.show())
print(s1.add_interest())
print(s1.show_interest())

if age >= 10:
    print("hyarel is adult, can open account")
else:
    print("hyarel is child, cannot open account")

for friend in friends:
    print(f"Hello {friend}")

for key in account:
    print(f"{key} = {account[key]}")

count = 1
while count <=3 :
    print(f"COUNT IS {count}")
    count = count + 1


try:
    #file handing
    with open("account.json", "w") as f:
        json.dump(account, f)
    print("file saved")
    #file open 
    with open("account.json", "r") as f:
        data = json.load(f)
    print(data)
except Exception as e:
    print(f"Error came: {e}")
