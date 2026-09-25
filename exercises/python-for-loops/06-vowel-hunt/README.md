# Exercise 6: Vowel hunt 🔍

🟡 Intermediate · Exercise 6 of 10 · [All exercises](../README.md)

A for loop can also go through a **string** (a piece of text), one character at a time. A **character** is one letter, digit, space or symbol.

You need two new tools:

- `.lower()` makes text lowercase. For example, `"A".lower()` gives `"a"`.
- `in` checks if some text is inside other text. For example, `"a" in "cat"` is `True`.

**Task:** Count the vowels (`a`, `e`, `i`, `o`, `u`) in this text and print how many there are. Uppercase vowels count too. The text is already in `exercise.py`:

```python
text = "Hello ReDI School"
```

**Rule:** Use a for loop.

**Expected output:**

```text
Number of vowels: 6
```

<details>
<summary>Hint</summary>

This is like the running total in Exercise 3, but you add 1 only for some characters. Which ones?

The text has an uppercase `I`. How can the two new tools help you count it too?

</details>

**Solution:** Try the hint first. Still stuck? Compare your code with the [solution](../solutions/06-vowel-hunt/exercise.py).

**Next:** [Exercise 7: Times-table tower 🏰](../07-times-table-tower/README.md)
