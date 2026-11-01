import random


def pick_lunch(options):
    return random.choice(options)


foods = ["pizza", "sushi", "falafel"]
print(pick_lunch(foods))


def plan_week(options, days):
    lunches = []
    for day in range(days):
        lunches.append(pick_lunch(options))
    return lunches
