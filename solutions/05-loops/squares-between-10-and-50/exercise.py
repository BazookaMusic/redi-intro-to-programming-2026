# Squares between 10 and 50
# Print the squares from 10 to 50: skip the small ones, stop at the big ones.

for n in range(1, 100):
    square = n * n
    if square < 10:
        continue
    if square > 50:
        break
    print(f"{n} * {n} = {square}")
