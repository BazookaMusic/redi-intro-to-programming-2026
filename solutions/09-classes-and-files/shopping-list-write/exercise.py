# Add to the shopping list.
# Now you want to change your shopping list from Python. Write code that saves
# a new list and adds items to it.
#
# 1. Write the function save_list(filename, items): filename is the name of
#    the file, such as "shopping.txt". items is a list of strings. It writes
#    each item into the file, one per line. Anything already in the file is
#    replaced.
# 2. Write the function add_item(filename, item): item is one string. It adds
#    item to the end of the file. The old items stay.
# 3. (Advanced) Write the function add_items(filename, items): items is a list
#    of strings. It adds each item to the end of the file. Use add_item.
#
# Expected input and output:
# save_list("shopping.txt", ["bread", "milk"])
# add_item("shopping.txt", "eggs")
# add_items("shopping.txt", ["cheese", "apples"])
#
# shopping.txt afterwards:
# bread
# milk
# eggs
# cheese
# apples
#
# Help:
# with open(filename, "w") as file:
#     file.write(item + "\n")
#
# "w" replaces the file. "a" adds to the end.
# Use a for loop to write every item in a list.
#
# Write your solution below.
def save_list(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")


def add_item(filename, item):
    with open(filename, "a") as file:
        file.write(item + "\n")


def add_items(filename, items):
    for item in items:
        add_item(filename, item)


save_list("shopping.txt", ["bread", "milk"])
add_item("shopping.txt", "eggs")
add_items("shopping.txt", ["cheese", "apples"])
with open("shopping.txt", "r") as file:
    print(file.read())
