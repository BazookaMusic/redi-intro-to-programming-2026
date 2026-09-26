# 02 · Variables and Data Types exercises

These exercises come from the [Variables and Data Types slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/02-variables.html). When you finish, compare your work with the [solutions](../../solutions/02-variables-and-data-types/).

Each exercise has its own folder with two files:

- `exercise.py` has the instructions at the top. Write your code below them.
- `check.py` runs your code and tells you if your answer is correct.

## How to check your answer

1. In VS Code, open the exercise folder with **File → Open Folder...**.
2. Write your code in `exercise.py` and save it.
3. Choose **Terminal → New Terminal**, then run the checker.

On macOS:

```sh
python3 check.py
```

On Windows:

```powershell
py check.py
```

New to this? Follow [How to clone this repository to get access to exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026#clone-repository) and [How to do exercises and check my answers](https://github.com/BazookaMusic/redi-intro-to-programming-2026#do-exercises) first.

## Build an About Me program

**Folder:** [`about-me`](about-me/)

Choose your own name, age, city, language, and whether you are a student. Create variables named `name` (text), `age` (whole number), `city` (text), `language` (text), and `is_student` (True or False). Print the five values, one per line, in that order. Then print the type of each variable in the same order. Add 1 to `age` and print it again. Finally, print the number of characters in `name`.

Example values: `name = "Sara"`, `age = 25`, `city = "Berlin"`, `language = "Arabic"`, `is_student = True`

Example output:

```text
Sara
25
Berlin
Arabic
True
<class 'str'>
<class 'int'>
<class 'str'>
<class 'str'>
<class 'bool'>
26
4
```

## Type detective

**Folder:** [`type-detective`](type-detective/)

First guess the answers to these six questions before running any code. Then write code to print each answer, one per line, in this order:

1. What is `type("42")`?
2. What is `int(3.9)`?
3. What is `len("ReDI")`?
4. Does `"I am " + 25` work? Print `"TypeError"` if it does not. Add a comment explaining why text and a number cannot be joined by `+`.
5. What is `str(True)`?
6. What is `type(3.0)`?

Example output:

```text
<class 'str'>
3
4
TypeError
True
<class 'float'>
```

## Bonus: Swap two values

**Folder:** [`bonus-swap-variables`](bonus-swap-variables/)

First, put `5` in a variable named `first` and `9` in a variable named `second`. Now swap them: `first` should hold `9`, and `second` should hold `5`. Imagine moving the values between two boxes. You can use a third box (another variable) to hold one value while you move the other. Print both values after the swap, with the labels shown below.

Example output:

```text
First: 9
Second: 5
```

## Homework 1: All About Me

**Folder:** [`homework-01-all-about-me`](homework-01-all-about-me/)

Choose your own name, age, city, favourite food, favourite colour, and whether you are working. Create variables named `name`, `age`, `city`, `favourite_food`, `favourite_colour`, and `is_working`. Use a whole number for `age` and True or False for `is_working`. Print each value on its own line, in that order, with no extra labels.

Example values: `"Sara"`, `25`, `"Berlin"`, `"Pizza"`, `"Blue"`, `False`

Example output:

```text
Sara
25
Berlin
Pizza
Blue
False
```

## Homework 2: Type inspector

**Folder:** [`homework-02-type-inspector`](homework-02-type-inspector/)

Create the same six variables as in All About Me: `name`, `age`, `city`, `favourite_food`, `favourite_colour`, and `is_working`. You can choose your own values again. Use a whole number for `age` and True or False for `is_working`. Print the type of each variable, one per line, in order.

Example output:

```text
<class 'str'>
<class 'int'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'bool'>
```

## Homework 3: Receipt

**Folder:** [`homework-03-receipt`](homework-03-receipt/)

Create `item` (text), `price` (a decimal number), and `quantity` (a whole number). Choose your own values. Print one line in this format:
`[item] — quantity: [quantity] — price: [price]`

Example values: `item = "Bread"`, `price = 1.5`, `quantity = 2`

Example output:

```text
Bread — quantity: 2 — price: 1.5
```

## Homework 4: len() explorer

**Folder:** [`homework-04-length-explorer`](homework-04-length-explorer/)

Create three text variables named `name`, `city`, and `food`. Choose words so that one of them is clearly the longest (no equal longest lengths). Print the length of each, then print the longest word. Use the labels shown below. You can decide which is longest by looking at the lengths.

Example values: `name = "Sara"`, `city = "Berlin"`, `food = "Pizza"`

Example output:

```text
Name length: 4
City length: 6
Food length: 5
Longest: Berlin
```

## Homework 5: Mad libs

**Folder:** [`homework-05-mad-libs`](homework-05-mad-libs/)

Choose your own adjective, animal, place, and whole number. Create variables named `adjective`, `animal`, `place`, and `number`. Print this sentence with your values:
`The [adjective] [animal] visited [number] places in [place].`

Example values: `"happy"`, `"cat"`, `"Berlin"`, `3`

Example output:

```text
The happy cat visited 3 places in Berlin.
```

## Homework 6: Converter chain

**Folder:** [`homework-06-converter-chain`](homework-06-converter-chain/)

Start with `age_text = "28"`. Change it to an int, then to a float, then back to a str. After each change, print its type on a new line. You can reuse `age_text` or create new variables as you go.

Example output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
```

## Homework 7: Interactive profile

**Folder:** [`homework-07-interactive-profile`](homework-07-interactive-profile/)

Ask for a name and an age using `input()`. Print one sentence with both, in the format shown below. Bonus: print the name's length on a second line. The bonus line is optional, but the checker checks it if you add it.

Example input: Sara, then 25

Example output:

```text
Hello, Sara! You are 25 years old.
Name length: 4
```
