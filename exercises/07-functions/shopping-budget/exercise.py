# Shopping budget.
# You are building the code for a wallet. The wallet starts with 20 euros.
# You will buy different items with it and check whether you can afford them.
#
# 1. Write a function total_price(unit_price, quantity). It returns a number:
#    the total cost of buying quantity items, each costing unit_price.
# 2. A notebook costs 3 euros. Print the total for 4 notebooks and for
#    8 notebooks.
# 3. (Advanced) Define a shopping basket: a list of tuples, each with a price
#    and a quantity. Write can_afford(shopping_basket, wallet_amount). It
#    returns True if the wallet can pay for the whole basket, otherwise False.
#
# Expected input and output:
# total_price(3, 4)       # returns 12
# total_price(3, 8)       # returns 24
# basket = [(3, 4), (2, 3)]
# can_afford(basket, 20)  # returns True
# can_afford(basket, 10)  # returns False
#
# Helpful code: loop over a list of tuples.
# for unit_price, quantity in basket:
#     print(unit_price, quantity)
#
# Write your solution below.
