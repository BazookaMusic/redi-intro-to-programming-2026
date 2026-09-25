# Solution for Exercise 8: Star staircase
#
# range(row) is short for range(0, row). It runs row times, so row 3
# prints 3 stars.

for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
