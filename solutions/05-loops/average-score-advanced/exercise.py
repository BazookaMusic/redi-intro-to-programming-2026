# Average of passing scores (advanced)
# Add up and count only the scores of 5 or more, then print their average.

scores = [8, 2, 10, 4, 6]

total = 0
count = 0
for score in scores:
    if score >= 5:
        total = total + score
        count = count + 1

print(f"Passing scores: {count}")
print(f"Average of passing scores: {total / count}")
