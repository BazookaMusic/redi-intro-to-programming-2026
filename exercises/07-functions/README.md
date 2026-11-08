# Functions

First follow [How to clone this repository](../../README.md#clone-repository),
then [How to do exercises and check my answers](../../README.md#do-exercises).

Open one task folder with **File → Open Folder...** in VS Code.
Write your code in `exercise.py`, save it, then choose **Terminal → New Terminal**.

On Windows, run:

```powershell
py check.py
```

On macOS, run:

```sh
python3 check.py
```

Each checker works with just `exercise.py` and `check.py`. The Hangman checker
uses sample words and needs neither internet access nor installed packages.

## Homework

### Homework 1: Ticket prices

[Open the task folder](homework-01-ticket-prices/)

Write `ticket_price(age)`.
Return `5` if the age is below `12`. Otherwise return `10`.
Print the returned prices for ages `8` and `16`.
Add those two returned prices and print the total.

Example output:

```text
5
10
15
```

### Homework 2: High scores

[Open the task folder](homework-02-high-scores/)

Write `count_high_scores(scores, minimum)`.
Use a loop to count scores greater than or equal to `minimum`.
Return the count.
Use `[12, 45, 7, 30]` and a minimum of `20`. Print the result.

Example output:

```text
2
```

### Homework 3: Average score

[Open the task folder](homework-03-average-score/)

Write `average(scores)`. Assume the list is non-empty.
Use a loop to find the total, then return `total / len(scores)`.
Call it with `[12, 18, 24]`. Print the result.
If it is at least `15`, also print `Pass`.

Example output:

```text
18.0
Pass
```

### Homework 4: Roll a die

[Open the task folder](homework-04-roll-a-die/)

Import `random`. Write `roll_die(sides=6)` with a docstring.
Return a random integer from `1` through `sides`, including both ends.
Print one roll using the default and one using `sides=20`.

One possible output:

```text
4
17
```

## Classroom exercises

### Draw a face

[Open the task folder](draw-a-face/)

Write `draw_face(eyes, mouth)`.
Print the eyes twice, with a space between them.
Print the mouth on the next line, with one space before it.
Call the function twice with different characters. Choose your own!

Example output for `draw_face("o", "-")` and `draw_face("^", "v")`:

```text
o o
 -
^ ^
 v
```

### Shopping budget

[Open the task folder](shopping-budget/)

You are building the code for a wallet. The wallet starts with **20 euros**.
You will buy different items with it and check whether you can afford them.

1. Write a function `total_price(unit_price, quantity)`. It **returns** a
   number: the total cost of buying **quantity** items, each costing
   **unit_price**.
2. A notebook costs 3 euros. Print the total for 4 notebooks and for
   8 notebooks.
3. **(Advanced)** Define a shopping basket: a list of tuples, each with a
   price and a quantity. Write `can_afford(shopping_basket, wallet_amount)`.
   It **returns** `True` if the wallet can pay for the whole basket,
   otherwise `False`.

Expected input and output:

```python
total_price(3, 4)       # returns 12
total_price(3, 8)       # returns 24
basket = [(3, 4), (2, 3)]
can_afford(basket, 20)  # returns True
can_afford(basket, 10)  # returns False
```

Helpful code: loop over a list of tuples.

```python
for unit_price, quantity in basket:
    print(unit_price, quantity)
```

### Trace execution and scope

This is a reading task, so it has no task folder.

What three lines are printed? Could we use `result` outside the function?

```python
value = 10

def add_two(value):
    result = value + 2
    print(result)
    return result

answer = add_two(1)
print(answer)
print(value)
```

### Lunch picker

[Open the task folder](lunch-picker/)

You and your friends can never decide what to eat for lunch.
You will write a program that picks a lunch for you at random.

1. Import `random`. Write a function `pick_lunch(options)`. It takes a list
   of foods and **returns** one of them, chosen at random.
2. Make a list called `foods` with at least three foods. Print the lunch that
   `pick_lunch` chooses from it.
3. **(Advanced)** Write `plan_week(options, days)`. It **returns** a list with
   one random lunch for each day, so the list has `days` items. Use
   `pick_lunch` inside it.

Expected input and output (your results are random):

```python
foods = ["pizza", "sushi", "falafel"]
pick_lunch(foods)     # returns "sushi" (or another food from the list)
plan_week(foods, 3)   # returns ["pizza", "pizza", "falafel"]
```

Your program prints one food from your list, for example:

```text
sushi
```

Helpful code:

```python
import random
print(random.choice(["heads", "tails"]))  # heads or tails
```

### Words for Hangman

[Open the task folder](hangman-words/)

Our Hangman game needs words that are not too long or too short.
For this task, use a small list of words before connecting the library.

1. Write `game_words(words)`. It **returns** a list containing only words
   with 4 to 8 letters, including both ends.
2. Print the result for `["cat", "apple", "banana", "watermelon"]`.
3. **(Advanced)** Write `pick_word(words)`. It **returns** a random word from
   `game_words(words)`. Assume at least one word fits.

**Expected input and output**

```python
game_words(["cat", "apple", "banana", "watermelon"])
# returns ["apple", "banana"]
pick_word(["cat", "apple", "banana"])
# returns "apple" or "banana"
```

Your program prints:

```text
['apple', 'banana']
```

**Help**

```python
result = []
for word in words:
    if 4 <= len(word) <= 8:
        result.append(word)
```

### Mini project: Hangman

Copy the code from the starter: [mini-project-hangman/exercise.py](mini-project-hangman/exercise.py).
[Open the task folder](mini-project-hangman/).

Guess a secret eight-letter English word, one letter at a time.
Correct guesses reveal letters. You can make six mistakes before losing.
A skeleton moves towards the player after each mistake.
Install `english-words` using the setup below.

1. Write `victory(word)`. It **returns** `True` if the displayed word has no `_`,
   otherwise `False`.
2. Write `display_hidden_word(secret_word, guessed_letters)`. It **returns** the word
   with `_` for each letter not yet guessed.
3. Write `get_user_guess(guessed_letters)`. It asks for one letter from `a` to `z`
   and **returns** it in lowercase. Ask again for invalid or repeated guesses.

**Expected input and output**

```python
display_hidden_word("linguist", ["i"])  # returns "_i___i__"
victory("_i___i__")             # returns False
victory("linguist")             # returns True
get_user_guess(["i"])           # input " A " returns "a"; "i" asks again
lives_bar(6, 6)                 # returns "💀______😊"
lives_bar(6, 5)                 # returns "_💀_____😊"
lives_bar(6, 0)                 # returns "______💀😊"
```

**Help**

```python
words = list(get_english_words_set(["web2"], lower=True))
print(random.choice(words))
for letter in secret_word:
    if letter in guessed_letters:
        print(letter)
guess = input("Guess a letter: ").strip().lower()
```

The starter supplies the game loop, lives bar and word picker.
The supplied helpers are below `hangman()`.
Invalid or repeated guesses do not use a chance.

## Running Hangman with the English word collection

Only **Hangman** needs this setup. Open its task folder and choose
**Terminal → New Terminal**.

Install `english-words` once, then run the program.

On Windows (PowerShell):

```powershell
py -m pip install english-words==2.0.2
py exercise.py
```

On macOS:

```sh
python3 -m pip install english-words==2.0.2
python3 exercise.py
```

Installation needs internet access. The library includes the word collection,
so the game runs offline afterwards. It provides words, not their definitions.
The game selects alphabetic English words with eight letters.
Some dictionary words are uncommon; their length does not guarantee difficulty.

`-m pip` installs the package for the same Python that runs your code.

[See the solutions after trying the tasks](../../solutions/07-functions/README.md).
