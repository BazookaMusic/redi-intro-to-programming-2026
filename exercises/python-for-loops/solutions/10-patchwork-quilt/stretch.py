# Solution for Exercise 10, stretch goal: Space invader zoom
#
# The two inner loops are the same as in the main exercise. Only the
# tile's top-left cell and the character are new.

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
    height = len(picture) * scale
    width = len(picture[0]) * scale
    grid = []
    for row in range(height):
        grid.append(["."] * width)

    for pixel_row in range(len(picture)):
        for pixel_col in range(len(picture[0])):
            pixel = picture[pixel_row][pixel_col]
            tile_top = pixel_row * scale
            tile_left = pixel_col * scale
            for row in range(tile_top, tile_top + scale):
                for col in range(tile_left, tile_left + scale):
                    grid[row][col] = pixel

    return grid


big_invader = zoom(INVADER, 2)
for big_row in big_invader:
    for cell in big_row:
        print(cell, end="")
    print()
