# Homework 4: Shopping cart project.
# You are building a small online shop. PRICES stores each item's price.
# The cart is a dictionary: item -> quantity.
#
# 1. Write add_to_cart(cart, item, quantity). If the item is not in PRICES,
#    return False. Otherwise add quantity to the item in the cart and
#    return True.
# 2. Write cart_total(cart). It returns the total price of everything in the
#    cart.
# 3. (Advanced) Write sale_total(cart, sale_items). sale_items is a set.
#    Those items cost half price. It returns the total.
#
# Expected input and output:
# cart = {}
# add_to_cart(cart, "apple", 3)   # returns True
# add_to_cart(cart, "apple", 2)   # cart is now {'apple': 5}
# add_to_cart(cart, "pizza", 1)   # returns False
# add_to_cart(cart, "cheese", 1)  # returns True
# cart_total(cart)                # returns 10
# sale_total(cart, {"cheese"})    # returns 7.5
#
# Help:
# PRICES["cheese"]          # 5
# cart.get("apple", 0)      # 0 if not in the cart
# for item, quantity in cart.items():
#     print(item, quantity)
#
# The shop loop and the receipt are supplied below your functions.
#
# Write your solution below.

PRICES = {"apple": 1, "bread": 2, "cheese": 5, "milk": 1}


def add_to_cart(cart, item, quantity):
    """Adds quantity of item to the cart. Returns False for unknown items."""
    # ==================================================
    # >>> STEP 1: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


def cart_total(cart):
    """Returns the total price of everything in the cart."""
    # ==================================================
    # >>> STEP 2: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


# STEP 3 (Advanced): write sale_total(cart, sale_items) here.


# Supplied code.
def print_receipt(cart):
    """Prints one line for each item in the cart."""
    print("Receipt:")
    for item, quantity in cart.items():
        print(f"{item} x{quantity} = {PRICES[item] * quantity} euros")


def shop():
    cart = {}
    print("We sell:")
    for item, price in PRICES.items():
        print(f"- {item}: {price} euros")

    while True:
        item = input("Item to buy (or done): ").strip().lower()
        if item == "done":
            break
        quantity = int(input("How many? "))
        if add_to_cart(cart, item, quantity):
            print("Added to the cart.")
        else:
            print("Sorry, we do not sell", item)

    print_receipt(cart)
    print("Total:", cart_total(cart), "euros")


shop()
