PRICES = {"apple": 1, "bread": 2, "cheese": 5, "milk": 1}


def add_to_cart(cart, item, quantity):
    """Adds quantity of item to the cart. Returns False for unknown items."""
    if item not in PRICES:
        return False
    cart[item] = cart.get(item, 0) + quantity
    return True


def cart_total(cart):
    """Returns the total price of everything in the cart."""
    total = 0
    for item, quantity in cart.items():
        total += PRICES[item] * quantity
    return total


def sale_total(cart, sale_items):
    """Returns the total price. Items in sale_items cost half price."""
    total = 0
    for item, quantity in cart.items():
        price = PRICES[item]
        if item in sale_items:
            price = price / 2
        total += price * quantity
    return total


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
