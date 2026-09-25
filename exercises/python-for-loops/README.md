# Python for Loops: Practice Exercises

These 10 exercises help you practise **for loops** in Python. They start easy and get harder.

## How to use these exercises

Before you start, read [How to use the exercises](../../README.md#how-to-use-the-exercises) in the main README. It shows how to set up pytest, run your code and read the test results.

Each exercise has its own folder. Open the folder in VS Code and read its `README.md`. It has the task, the expected output, a hint and a link to the solution.

## Exercises

| # | Exercise | What you practise |
| --- | --- | --- |
| 🟢 1 | [Counting sheep 🐑](01-counting-sheep/README.md) | `range()` |
| 🟢 2 | [Fruit salad 🍎](02-fruit-salad/README.md) | Looping over a list |
| 🟢 3 | [Shopping basket 🛒](03-shopping-basket/README.md) | Adding up numbers |
| 🟢 4 | [Bunny hops 🐰 and rocket launch 🚀](04-bunny-hops-and-rocket-launch/README.md) | Counting in steps and counting down |
| 🟡 5 | [The biggest fish 🐟](05-biggest-fish/README.md) | Finding the largest number |
| 🟡 6 | [Vowel hunt 🔍](06-vowel-hunt/README.md) | Looping over text |
| 🟡 7 | [Times-table tower 🏰](07-times-table-tower/README.md) | Loops inside loops |
| 🔴 8 | [Star staircase ✨](08-star-staircase/README.md) | Drawing a shape |
| 🔴 9 | [Chess night ♟️](09-chess-night/README.md) | Filling a grid |
| 🔴 10 | [Patchwork quilt 🧵](10-patchwork-quilt/README.md) | Filling a grid tile by tile, with a stretch goal |

🟢 Beginner · 🟡 Intermediate · 🔴 Advanced

## Key words

Read these first. Each exercise explains new words when they appear.

- A **loop** runs the same code many times.
- A **for loop** runs the code once for each item, for example once for each number or each word.
- The **loop variable** holds the current item. It gets a new value each time the loop runs.
- The **loop body** is the code that repeats. It is the indented code under the `for` line.
- **Indented** means the line starts with spaces. Use 4 spaces. Python uses them to know which lines are inside the loop.
- One run of the loop body is called an **iteration**.

```python
for number in range(3):
    print("Hello")    # indented: part of the loop body
print("Done")         # not indented: runs once, after the loop
```

```text
Hello
Hello
Hello
Done
```

In this example, `number` is the loop variable. The loop body runs 3 times, so there are 3 iterations.

**Start here:** [Exercise 1: Counting sheep 🐑](01-counting-sheep/README.md)
