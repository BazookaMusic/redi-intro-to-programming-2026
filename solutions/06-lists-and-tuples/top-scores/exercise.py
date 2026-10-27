# Top scores
# Write a program that:
# 1. Sorts the scores from highest to lowest.
# 2. Prints the top 3 scores (use slicing).
# 3. Prints the lowest score.
# 4. Prints how many scores are above 50.
#
# Example output:
# Top 3: [91, 89, 76]
# Lowest: 11
# Scores above 50: 5
#
# Write your solution below.
scores = [42, 17, 89, 55, 23, 76, 34, 91, 60, 11]
scores.sort(reverse=True)
print("Top 3:", scores[:3])     # Top 3: [91, 89, 76]
print("Lowest:", scores[-1])    # Lowest: 11
count = 0
for score in scores:
    if score > 50:
        count = count + 1
print(f"Scores above 50: {count}")
