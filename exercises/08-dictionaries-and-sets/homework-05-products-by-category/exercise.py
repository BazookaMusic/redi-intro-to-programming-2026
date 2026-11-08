# Homework 5: Products by category (advanced).
# A shop has a list of products. Each has a name and a category.
# Make a list of product names for each category.
#
# 1. Write products_by_category(products). It returns a dictionary where each
#    category is a key and its value is a list of product names. Keep the names
#    in the order they appear in products.
# 2. Print the result for PRODUCTS.
# 3. (Advanced) Write categories_with_multiple(products). It returns a set of
#    categories with more than one product. Reuse products_by_category.
#
# Expected input and output:
# products_by_category(PRODUCTS) returns:
# {'fruit': ['apple', 'banana'], 'bakery': ['bread', 'cake'], 'dairy': ['milk']}
# categories_with_multiple(PRODUCTS) returns {'fruit', 'bakery'}.
# The order of a set may be different.
#
# Your program prints:
# {'fruit': ['apple', 'banana'], 'bakery': ['bread', 'cake'], 'dairy': ['milk']}
#
# Help:
# product = {"name": "apple", "category": "fruit"}
# product["category"]   # 'fruit'
# names = []
# names.append(product["name"])   # names is ['apple']
#
# Write your solution below.

PRODUCTS = [
    {"name": "apple", "category": "fruit"},
    {"name": "bread", "category": "bakery"},
    {"name": "banana", "category": "fruit"},
    {"name": "cake", "category": "bakery"},
    {"name": "milk", "category": "dairy"},
]
