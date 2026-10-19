# Average score
# Add up the scores, then divide by how many there are.

scores = [8, 6, 10, 4, 7]

total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print(f"Average: {average}")
