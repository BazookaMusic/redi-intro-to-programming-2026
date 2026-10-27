# Homework 10: Two-list comparison
# Print only the names that appear in both lists.
#
# Example output:
# Bruno
# Dina
#
# Write your solution below.
list_a = ["Alice", "Bruno", "Carla", "Dina"]
list_b = ["Bruno", "Erik", "Dina", "Fatima"]

for name in list_a:
    if name in list_b:
        print(name)
