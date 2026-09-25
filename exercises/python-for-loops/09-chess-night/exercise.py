# Exercise 9: Chess night
#
# Finish the function make_checkerboard(size). It must give back a board
# with size rows and size columns.
# Use "#" for dark squares and "." for light squares.
# The top-left square is "#".
#
# The tests run your function with different sizes.
#
# Expected output for make_checkerboard(10):
#
#     #.#.#.#.#.
#     .#.#.#.#.#
#     #.#.#.#.#.
#     .#.#.#.#.#
#     #.#.#.#.#.
#     .#.#.#.#.#
#     #.#.#.#.#.
#     .#.#.#.#.#
#     #.#.#.#.#.
#     .#.#.#.#.#


def make_checkerboard(size):
    # Build the grid: size rows, each with size "." cells.
    # ["."] * size makes a list with size copies of ".".
    # .append() adds an item to the end of a list.
    grid = []
    for row in range(size):
        grid.append(["."] * size)

    # Write your code here.

    return grid


# Print a 10 x 10 board, one row per line.
board = make_checkerboard(10)
for board_row in board:
    for cell in board_row:
        print(cell, end="")
    print()
