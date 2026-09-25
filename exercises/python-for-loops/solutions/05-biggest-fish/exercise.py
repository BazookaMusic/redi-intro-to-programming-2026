# Solution for Exercise 5: The biggest fish
#
# We start with the first number instead of 0. Then the code also works
# if all the numbers are negative.

numbers = [12, 45, 7, 89, 23, 56]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is", largest)
