# Solution for Exercise 10: Patchwork quilt
#
# The two outer loops find the top-left cell of each tile. The two inner
# loops visit every cell in that tile. str() turns the number into text.
#
# Want to see the order of the cells? Add print(row, col) inside the
# innermost loop.


def fill_tiles(height, width, tile_size):
    grid = []
    for row in range(height):
        grid.append(["."] * width)

    tile_number = 1

    for tile_top in range(0, height, tile_size):
        for tile_left in range(0, width, tile_size):
            for row in range(tile_top, tile_top + tile_size):
                for col in range(tile_left, tile_left + tile_size):
                    grid[row][col] = str(tile_number)
            tile_number = tile_number + 1

    return grid


tiles = fill_tiles(9, 9, 3)
for tiles_row in tiles:
    for cell in tiles_row:
        print(cell, end="")
    print()
