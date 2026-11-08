# Homework 1: Vote counter.
# Your class votes on where to go for a trip. Each vote is a place name in
# a list.
#
# 1. Write count_votes(votes). It returns a dictionary: each place and its
#    number of votes.
# 2. Print the result for ["zoo", "museum", "zoo", "park", "zoo", "park"].
# 3. (Advanced) Write winner(counts). It returns the place with the most
#    votes. Loop over counts.items().
#
# Expected input and output:
# votes = ["zoo", "museum", "zoo", "park", "zoo", "park"]
# count_votes(votes)    # returns {'zoo': 3, 'museum': 1, 'park': 2}
# winner({'zoo': 3, 'museum': 1, 'park': 2})   # returns 'zoo'
#
# Your program prints:
# {'zoo': 3, 'museum': 1, 'park': 2}
#
# Help:
# counts = {}
# counts["zoo"] = counts.get("zoo", 0) + 1
#
# Write your solution below.
