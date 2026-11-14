# Wallet methods.
# Our wallet is not useful yet. Let's allow it to receive money and pay for
# things. The Wallet class from the previous exercise is already below. Add
# the new methods to it.
#
# 1. Add a method receive(amount) that adds amount to money.
# 2. Add a method has_enough_money(price) that returns True if money is at
#    least price, otherwise False.
# 3. Add a method pay(price). If money is at least price, it subtracts price
#    from money and returns True. Otherwise it returns False and does not
#    change money.
# 4. (Advanced) Add a method pay_all(prices) that calls pay for each price in
#    the list and returns how many prices were paid.
#
# Expected input and output:
# wallet = Wallet("Ana", 200)
# wallet.receive(50)             # money 250
# wallet.has_enough_money(300)   # False
# wallet.pay(100)                # True, money 150
# wallet.pay(400)                # False, money 150
# wallet.pay_all([50, 200, 30])  # 2, money 70
#
# Help:
# class Dog:
#     def eat(self):          # changes an attribute
#         self.hungry = False
#
#     def is_hungry(self):    # returns a value
#         return self.hungry
#
# Write your solution below.
class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money
