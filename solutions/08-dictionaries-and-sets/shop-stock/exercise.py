def restock(stock, item, amount):
    stock[item] = stock.get(item, 0) + amount


def sell(stock, item):
    if stock.get(item, 0) > 0:
        stock[item] -= 1
        return True
    return False


def out_of_stock(stock):
    empty = []
    for item, count in stock.items():
        if count == 0:
            empty.append(item)
    return empty


stock = {"apples": 5, "bread": 1, "milk": 0}
print(sell(stock, "bread"))
print(sell(stock, "bread"))
restock(stock, "eggs", 6)
print(stock)
print(out_of_stock(stock))
