# Solution for Exercise 9: Chess night
#
# Moving one square right or one square down changes row + col by 1.
# So it switches between even and odd, and the colours take turns.
# Every cell starts as ".", so you only need to change the "#" squares.


def make_checkerboard(size):
    grid = []
    for row in range(size):
        grid.append(["."] * size)

    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                grid[row][col] = "#"

    return grid


board = make_checkerboard(10)
for board_row in board:
    for cell in board_row:
        print(cell, end="")
    print()
