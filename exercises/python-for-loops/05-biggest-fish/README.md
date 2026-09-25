# Exercise 5: The biggest fish 🐟

🟡 Intermediate · Exercise 5 of 10 · [All exercises](../README.md)

Python has a `max()` function that finds the largest number. In this exercise, you find it yourself, without `max()`.

You need two new tools:

- **Index:** the position of an item in a list. Counting starts at `0`, so `numbers[0]` is the first item.
- **if:** an `if` runs its indented code only when something is `True`. For example, `if price > 5:` runs its code only when `price` is bigger than 5.

**Task:** Print the largest number in this list. The list is already in `exercise.py`:

```python
numbers = [12, 45, 7, 89, 23, 56]
```

**Rules:**

- Use a for loop.
- Do not use `max()`, `sorted()` or `.sort()`.

**Expected output:**

```text
The largest number is 89
```

<details>
<summary>Hint</summary>

Imagine you read the numbers one by one. You only remember the biggest number so far.

- Before you read any numbers, what could you remember?
- When you read a new number, when do you change what you remember?

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/05-biggest-fish/exercise.py).

**Next:** [Exercise 6: Vowel hunt 🔍](../06-vowel-hunt/README.md)
