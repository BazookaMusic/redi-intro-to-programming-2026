# Café menu.
# You are building the till for a small café. A dictionary stores the price
# of each item.
#
# 1. Make a dictionary menu: tea costs 2, coffee costs 3 and cake costs 4.
# 2. Write price_of(menu, item). It returns the item's price, or 0 if the item
#    is not on the menu. Print the price of "coffee" and of "pizza".
# 3. (Advanced) Write order_total(menu, items). items is a list of item names.
#    It returns the total price. Reuse price_of.
#
# Expected input and output:
# price_of(menu, "coffee")                    # returns 3
# price_of(menu, "pizza")                     # returns 0
# order_total(menu, ["tea", "cake", "tea"])   # returns 8
#
# Your program prints:
# 3
# 0
#
# Help:
# "tea" in menu            # True
# menu.get("water", 0)     # 0
#
# Write your solution below.
