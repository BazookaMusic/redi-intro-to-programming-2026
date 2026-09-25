# Exercise 8: Star staircase ✨

🔴 Advanced · Exercise 8 of 10 · [All exercises](../README.md)

Exercises 8 to 10 draw shapes. You need one new tool for them.

Normally, `print()` starts a new line after it prints. With `end=""`, it stays on the **same line**. So `print("*", end="")` prints a star, and the next `print()` continues right after it. An empty `print()` starts a new line.

```python
print("a", end="")
print("b", end="")
print()
print("c")
```

```text
ab
c
```

**Task:** In `exercise.py`, print a triangle of stars with 5 rows. Row 1 has 1 star, row 2 has 2 stars, and so on.

**Rule:** Use for loops.

**Expected output:**

```text
*
**
***
****
*****
```

<details>
<summary>Hint</summary>

- Think of one loop for the rows and one loop for the stars in each row.
- How many stars does row 3 have? How is that number linked to the row number?
- When should the program start a new line?

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/08-star-staircase/exercise.py).

**Next:** [Exercise 9: Chess night ♟️](../09-chess-night/README.md)
