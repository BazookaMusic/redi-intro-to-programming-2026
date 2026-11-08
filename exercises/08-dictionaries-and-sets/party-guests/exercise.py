# Party guests.
# Ana and Max are throwing a party together. Each of them has a set of
# friends to invite.
#
# 1. Write common_friends(friends1, friends2). It returns the set of friends
#    that are in both sets.
# 2. Write all_guests(friends1, friends2). It returns a set of everyone
#    invited, each person once. Print how many guests are invited.
# 3. (Advanced) Write everyone(groups). groups is a list of sets. It returns
#    one set with every guest from every group. Use a loop.
#
# Expected input and output:
# ana_friends = {"Ben", "Cleo", "Dan"}
# max_friends = {"Cleo", "Dan", "Eva"}
# common_friends(ana_friends, max_friends)       # returns {'Cleo', 'Dan'}
# len(all_guests(ana_friends, max_friends))      # 4
# everyone([{"Ben"}, {"Ben", "Cleo"}, {"Eva"}])  # returns {'Ben', 'Cleo', 'Eva'}
#
# Your program prints:
# 4
#
# Help:
# a = {1, 2, 3}
# b = {2, 3, 4}
# a.union(b)          # {1, 2, 3, 4}
# a.intersection(b)   # {2, 3}
#
# Write your solution below.
