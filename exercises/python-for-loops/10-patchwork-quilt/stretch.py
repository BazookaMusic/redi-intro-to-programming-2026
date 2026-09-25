# Exercise 10, stretch goal: Space invader zoom
#
# A picture is a list of text rows. Each character is one pixel.
#
# Finish the function zoom(picture, scale). Give back a bigger grid where
# every pixel becomes a tile of scale x scale cells. Every cell in the tile
# has the same character as the pixel.
#
# Expected output for zoom(INVADER, 2):
#
#     ....##..........##....
#     ....##..........##....
#     ......##......##......
#     ......##......##......
#     ....##############....
#     ....##############....
#     ..####..######..####..
#     ..####..######..####..
#     ######################
#     ######################
#     ##..##############..##
#     ##..##############..##
#     ##..##..........##..##
#     ##..##..........##..##
#     ......####..####......
#     ......####..####......
#
# When the tests pass, draw your own picture and zoom in on it!

INVADER = [
    "..#.....#..",
    "...#...#...",
    "..#######..",
    ".##.###.##.",
    "###########",
    "#.#######.#",
    "#.#.....#.#",
    "...##.##...",
]


def zoom(picture, scale):
    # Build the grid: scale times as many rows and columns as the picture.
    # len() gives the number of items in a list or characters in a string.
    height = len(picture) * scale
    width = len(picture[0]) * scale
    grid = []
    for row in range(height):
        grid.append(["."] * width)

    # Write your code here.

    return grid


# Print the invader twice as big, one row per line.
big_invader = zoom(INVADER, 2)
for big_row in big_invader:
    for cell in big_row:
        print(cell, end="")
    print()
