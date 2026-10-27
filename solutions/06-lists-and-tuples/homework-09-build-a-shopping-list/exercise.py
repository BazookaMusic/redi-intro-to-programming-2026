# Homework 9: Build a shopping list
# Keep asking the user to type an item. Add each item to a list. When they
# type "done", stop and print the full list.
#
# Example input:
# milk
# bread
# done
#
# Example output:
# Your list: ['milk', 'bread']
#
# Write your solution below.
shopping_list = []

while True:
    item = input("Add item (or 'done' to finish): ")
    if item == "done":
        break
    shopping_list.append(item)
print(f"Your list: {shopping_list}")
