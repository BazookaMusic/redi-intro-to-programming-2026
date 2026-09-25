# Exercise 10: Patchwork quilt
#
# Finish the function fill_tiles(height, width, tile_size).
#
# - height is the number of rows.
# - width is the number of columns.
# - tile_size is how many cells wide and tall each tile is.
#
# Number the tiles left to right, then top to bottom. Write each tile's
# number into every cell of that tile. Finish one tile before you start
# the next one. Then give back the grid.
#
# The tests run your function with different sizes. The tiles always fit
# the grid exactly.
#
# Expected output for fill_tiles(9, 9, 3):
#
#     111222333
#     111222333
#     111222333
#     444555666
#     444555666
#     444555666
#     777888999
#     777888999
#     777888999


def fill_tiles(height, width, tile_size):
    # Build the grid: height rows, each with width "." cells.
    # ["."] * width makes a list with width copies of ".".
    # .append() adds an item to the end of a list.
    grid = []
    for row in range(height):
        grid.append(["."] * width)

    # Write your code here.

    return grid


# Print a 9 x 9 grid with 3 x 3 tiles, one row per line.
tiles = fill_tiles(9, 9, 3)
for tiles_row in tiles:
    for cell in tiles_row:
        print(cell, end="")
    print()
