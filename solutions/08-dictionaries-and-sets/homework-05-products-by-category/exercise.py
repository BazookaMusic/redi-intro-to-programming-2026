PRODUCTS = [
    {"name": "apple", "category": "fruit"},
    {"name": "bread", "category": "bakery"},
    {"name": "banana", "category": "fruit"},
    {"name": "cake", "category": "bakery"},
    {"name": "milk", "category": "dairy"},
]


def products_by_category(products):
    result = {}
    for product in products:
        category = product["category"]
        if category not in result:
            result[category] = []
        result[category].append(product["name"])
    return result


print(products_by_category(PRODUCTS))


def categories_with_multiple(products):
    result = set()
    for category, names in products_by_category(products).items():
        if len(names) > 1:
            result.add(category)
    return result
