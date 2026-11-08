# Unique visitors.
# A small museum writes down the name of every visitor at the door.
# Some people come more than once.
#
# 1. Write unique_visitors(names). It returns how many different people
#    visited. Use a set.
# 2. Print the result for ["Ana", "Ben", "Ana", "Cleo", "Ben"].
# 3. (Advanced) Write first_visits(names). It returns a list of names in the
#    order they first came, without duplicates. Use a set to remember who you
#    have already seen.
#
# Expected input and output:
# visits = ["Ana", "Ben", "Ana", "Cleo", "Ben"]
# unique_visitors(visits)   # returns 3
# first_visits(visits)      # returns ['Ana', 'Ben', 'Cleo']
#
# Your program prints:
# 3
#
# Help:
# seen = set()
# seen.add("Ana")
# print("Ana" in seen)      # True
#
# Write your solution below.
