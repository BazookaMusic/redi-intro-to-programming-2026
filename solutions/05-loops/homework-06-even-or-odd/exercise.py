# Homework 6: Even or odd?
# Print whether each number in the list is even or odd.

numbers = [3, 8, 15, 22, 7]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
