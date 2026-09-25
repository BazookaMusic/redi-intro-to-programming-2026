# Exercise 9: Chess night ♟️

🔴 Advanced · Exercise 9 of 10 · [All exercises](../README.md)

A checkerboard has dark and light squares that take turns. We use `#` for dark squares and `.` for light squares.

This exercise has three new ideas. Read them one at a time.

**1. Grids.** A **grid** has rows and columns, like a spreadsheet. In Python, we store a grid as a list of rows. Each row is a list of cells:

```python
grid = [
    [".", ".", "."],
    [".", ".", "."],
]
```

`grid[row][col]` is one cell. `row` is the row number and `col` is the column number. Both start at `0`. This changes the cell in row 0, column 2:

```python
grid[0][2] = "X"
```

Now the grid looks like this:

```text
..X
...
```

**2. Functions.** A **function** is a piece of code with a name. You can run it many times with different values. The function for this exercise is already in `exercise.py`:

- `def make_checkerboard(size):` starts the function.
- `size` holds the value you give it. `make_checkerboard(10)` runs the function with `size` equal to 10.
- `return grid` gives the finished grid back.

Write your code inside the function, between the grid code and `return grid`. Every line inside the function starts with 4 spaces.

The tests run your function with different sizes. They check the grid that it gives back.

**3. Even and odd numbers.**

- `%` gives the **remainder** after you divide. For example, `7 % 2` is `1` and `6 % 2` is `0`.
- `==` checks if two values are the same. Do not mix it up with `=`, which puts a value in a variable.
- A number is even when `number % 2 == 0`.

**Task:** Finish the function `make_checkerboard(size)`. It must give back a board with `size` rows and `size` columns. The top-left square is `#`.

For `make_checkerboard(10)`, the starting code prints this board.

**Expected output:**

```text
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
```

This starting code is already in `exercise.py`. Write your code where the comment says so.

```python
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
```

<details>
<summary>Hint</summary>

Write down the row and column numbers of a few `#` squares. Then do the same for a few `.` squares.

Add the row number and the column number together. What do you notice about the result for `#` squares? And for `.` squares?

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/09-chess-night/exercise.py).

**Next:** [Exercise 10: Patchwork quilt 🧵](../10-patchwork-quilt/README.md)
