# Shopping list.
# Your shopping list is saved in a file, one item per line. Write code that
# reads it.
#
# 1. Create a file called "shopping_list.txt" in VS Code, in the same folder
#    as this exercise.py. Add a few lines with stuff you want to buy next
#    week, one item per line. For example:
#    cheese
#    bread
#    toothbrush
# 2. Write print_list(filename). It reads the file and prints every item in
#    the file, without empty lines between them.
# 3. (Advanced) Write has_item(filename, item). It reads the file and returns
#    True if item is on the list, otherwise False.
#
# Expected input and output:
# If shopping_list.txt contains:
# bread
# milk
# eggs
#
# print_list("shopping_list.txt")           # prints:
#                                           # bread
#                                           # milk
#                                           # eggs
# has_item("shopping_list.txt", "milk")     # returns True
# has_item("shopping_list.txt", "cheese")   # returns False
#
# Help:
# with open(filename, "r") as file:
#     for line in file:
#         print(line.strip())
#
# .strip() removes the "\n" at the end of a line.
# For has_item, check line.strip() == item.
#
# Write your solution below.
