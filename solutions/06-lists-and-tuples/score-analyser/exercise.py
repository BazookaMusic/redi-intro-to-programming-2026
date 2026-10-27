# Score analyser
# Write a program that:
# 1. Prints every score above 10.
# 2. Calculates and prints the total of all scores.
# 3. Finds and prints the highest score.
#
# Example output:
# 15
# 21
# Total: 67
# Highest: 21
#
# Write your solution below.
scores = [8, 3, 15, 7, 21, 4, 9]
for score in scores:
    if score > 10:
        print(score)
total = 0
for score in scores:
    total = total + score
print(f"Total: {total}")
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(f"Highest: {highest}")
