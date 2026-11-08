menu = {"tea": 2, "coffee": 3, "cake": 4}


def price_of(menu, item):
    return menu.get(item, 0)


print(price_of(menu, "coffee"))
print(price_of(menu, "pizza"))


def order_total(menu, items):
    total = 0
    for item in items:
        total += price_of(menu, item)
    return total


print(order_total(menu, ["tea", "cake", "tea"]))
