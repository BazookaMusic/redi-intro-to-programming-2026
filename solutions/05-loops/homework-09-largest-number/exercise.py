# Homework 9: The largest number
# Find the largest number in the list.
# Starting at 0 works here because every number in the list is positive.

numbers = [4, 19, 2, 8, 11]

largest = 0
for number in numbers:
    if number > largest:
        largest = number
print(largest)
