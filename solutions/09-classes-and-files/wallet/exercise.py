# Wallet.
# You are building a wallet. Every wallet has an owner and an amount of money
# in Danish Kroner.
#
# 1. Write a class Wallet. It should be initialized with an owner (string)
#    and money (a number) and save them as attributes.
# 2. Create a wallet for "Ana" with 200 DKK and a wallet for "Ben" with
#    125 DKK. Store them in the variables ana and ben.
# 3. Print each wallet's owner and money: first Ana's owner and money,
#    then Ben's.
# 4. (Advanced) Put both wallets in a list and use a loop to print every owner
#    and their money, like "Ana has 200 DKK".
#
# Expected input and output:
# ana = Wallet("Ana", 200)
# print(ana.owner)          # Ana
# print(ana.money)          # 200
# ben = Wallet("Ben", 125)
# print(ben.money)          # 125
#
# Printed by steps 3 and 4:
# Ana
# 200
# Ben
# 125
# Ana has 200 DKK
# Ben has 125 DKK
#
# Help:
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# rex = Dog("Rex", 3)
# print(rex.name)
#
# Write your solution below.
class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money


ana = Wallet("Ana", 200)
ben = Wallet("Ben", 125)

print(ana.owner)
print(ana.money)
print(ben.owner)
print(ben.money)

wallets = [ana, ben]
for wallet in wallets:
    print(f"{wallet.owner} has {wallet.money} DKK")
