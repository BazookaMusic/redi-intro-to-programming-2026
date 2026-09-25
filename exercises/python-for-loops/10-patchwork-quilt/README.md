# Exercise 10: Patchwork quilt 🧵

🔴 Advanced · Exercise 10 of 10 · [All exercises](../README.md)

This folder also has the files for the stretch goal at the end of this page: `stretch.py` and `test_stretch.py`. To test only the main exercise, run:

```sh
python3 -m pytest test_exercise.py
```

On Windows, use `python` instead of `python3`.

A **tile** is a small square of cells. A patchwork quilt is sewn from square patches. In this exercise, you cut a grid into tiles like the patches of a quilt, and give each tile a number.

Like in Exercise 9, you fill a grid inside a function. This function gets three values:

- `height`: the number of rows
- `width`: the number of columns
- `tile_size`: how many cells wide and tall each tile is

The tiles are numbered like you read a page: left to right, then top to bottom. For example, `fill_tiles(9, 9, 3)` makes a grid with 9 rows and 9 columns. It has 9 tiles, and each tile is 3 × 3 cells.

**Task:** Finish the function `fill_tiles(height, width, tile_size)`. Write each tile's number into every cell of that tile. Finish one tile before you start the next one. Then give back the grid.

In this exercise, the tiles always fit the grid exactly.

For `fill_tiles(9, 9, 3)`, the starting code prints this grid.

**Expected output:**

```text
111222333
111222333
111222333
444555666
444555666
444555666
777888999
777888999
777888999
```

This starting code is already in `exercise.py`. Write your code where the comment says so.

```python
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
```

<details>
<summary>Hint</summary>

Split the problem into two jobs:

1. **Find each tile.** Every tile has a top-left cell. Write down the row and column of the top-left cell of all 9 tiles. What pattern do you see? Which `range()` step gives that pattern?
2. **Fill one tile.** You know a tile's top-left cell. Which rows and columns are part of that tile?

You also need the tile number. When should it go up?

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/10-patchwork-quilt/exercise.py).

## ⭐ Stretch goal: Space invader zoom 👾

Old video games drew their pictures with **pixels**: tiny squares of color. To make a picture bigger, you turn every pixel into a tile of the same color.

In `stretch.py`, a picture is a list of text rows. Each character is one pixel. This is a space invader:

```python
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
```

You can read one pixel like a cell in a grid. For example, `INVADER[2][3]` is `"#"`: row 2, column 3.

**Task:** Open `stretch.py`. Finish the function `zoom(picture, scale)`. Give back a bigger grid where every pixel becomes a tile of `scale` × `scale` cells. Every cell in the tile has the same character as the pixel.

For `zoom(INVADER, 2)`, the starting code prints this grid.

**Expected output:**

```text
....##..........##....
....##..........##....
......##......##......
......##......##......
....##############....
....##############....
..####..######..####..
..####..######..####..
######################
######################
##..##############..##
##..##############..##
##..##..........##..##
##..##..........##..##
......####..####......
......####..####......
```

Check your answer with the stretch test:

```sh
python3 -m pytest test_stretch.py
```

On Windows, use `python` instead of `python3`.

When the tests pass, draw your own picture in `stretch.py` and zoom in on it! Every row of your picture must have the same number of characters.

<details>
<summary>Hint</summary>

This is the main exercise again. Each pixel is one tile, and `scale` is the tile size.

1. **Visit each pixel.** Which loops visit every row and column of the small picture?
2. **Find its tile.** The pixel in row 0, column 0 gets the tile that starts at the top-left of the big grid. Where does the tile for row 1, column 3 start when `scale` is 2?
3. **Fill the tile.** You did this part in the main exercise.

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/10-patchwork-quilt/stretch.py).

🎉 You finished all the for-loop exercises! Go back to [all exercises](../README.md).
