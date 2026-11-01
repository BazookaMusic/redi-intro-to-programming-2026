def total_price(unit_price, quantity):
    return unit_price * quantity


print(total_price(3, 4))
print(total_price(3, 8))


def can_afford(shopping_basket, wallet_amount):
    total = 0
    for unit_price, quantity in shopping_basket:
        total += total_price(unit_price, quantity)
    return total <= wallet_amount


basket = [(3, 4), (2, 3)]
print(can_afford(basket, 20))
print(can_afford(basket, 10))