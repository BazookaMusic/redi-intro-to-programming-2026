# Shop stock.
# You run a small corner shop. A dictionary stores how many of each item
# you have.
#
# 1. Write restock(stock, item, amount). It adds amount to the item's count.
#    A new item starts at amount. It returns nothing.
# 2. Write sell(stock, item). If the item's count is above 0, take 1 away and
#    return True. Otherwise return False.
# 3. (Advanced) Write out_of_stock(stock). It returns a list of the items with
#    a count of 0.
#
# Expected input and output:
# stock = {"apples": 5, "bread": 1, "milk": 0}
# sell(stock, "bread")      # returns True
# sell(stock, "bread")      # returns False
# restock(stock, "eggs", 6)
# print(stock)              # {'apples': 5, 'bread': 0, 'milk': 0, 'eggs': 6}
# out_of_stock(stock)       # returns ['bread', 'milk']
#
# Help:
# stock.get("eggs", 0)      # 0
# for item, count in stock.items():
#     print(item, count)
#
# Write your solution below.
