# Homework 4: Tuple unpacking
# Loop through the list of (name, age) tuples and print a sentence for each person.
#
# Example output:
# Alice is 28 years old.
# Bruno is 34 years old.
# Carla is 22 years old.
#
# Write your solution below.
people = [("Alice", 28), ("Bruno", 34), ("Carla", 22)]

for name, age in people:
    print(f"{name} is {age} years old.")
