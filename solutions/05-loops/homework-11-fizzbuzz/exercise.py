# Homework 11: FizzBuzz
# Print Fizz, Buzz, FizzBuzz, or the number for 1 to 20.
# Check "both" first, or 15 would stop at Fizz.

for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
