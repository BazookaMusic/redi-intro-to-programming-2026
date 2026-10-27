# Homework 2: Sum of a list
# Use a loop to calculate the sum of all numbers in this list. Do not use the built-in sum() function.
#
# Example output:
# 108
#
# Write your solution below.
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for number in numbers:
    total = total + number
print(total)
