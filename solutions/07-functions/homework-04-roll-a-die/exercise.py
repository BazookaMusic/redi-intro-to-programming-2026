import random


def roll_die(sides=6):
    """Return a random integer from 1 through sides."""
    return random.randint(1, sides)


print(roll_die())
print(roll_die(sides=20))
