# Lunch picker.
# You and your friends can never decide what to eat for lunch.
# You will write a program that picks a lunch for you at random.
#
# 1. Import random. Write a function pick_lunch(options). It takes a list of
#    foods and returns one of them, chosen at random.
# 2. Make a list called foods with at least three foods. Print the lunch that
#    pick_lunch chooses from it.
# 3. (Advanced) Write plan_week(options, days). It returns a list with one
#    random lunch for each day, so the list has days items. Use pick_lunch
#    inside it.
#
# Expected input and output (your results are random):
# foods = ["pizza", "sushi", "falafel"]
# pick_lunch(foods)
# # returns "sushi" (or another food from the list)
# plan_week(foods, 3)
# # returns ["pizza", "pizza", "falafel"]
#
# Your program prints one food from your list, for example:
# sushi
#
# Helpful code:
# import random
# print(random.choice(["heads", "tails"]))  # heads or tails
#
# Write your solution below.
