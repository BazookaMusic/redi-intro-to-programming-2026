# Homework 8: Multiplication table
# Print the multiplication table for 1 to 5, with an empty line after each group.

for a in range(1, 6):
    for b in range(1, 6):
        print(f"{a} * {b} = {a * b}")
    print()
