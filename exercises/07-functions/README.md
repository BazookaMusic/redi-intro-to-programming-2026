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

Each checker works with just `exercise.py` and `check.py`. The Pokemon checkers
use sample data and need neither internet access nor installed packages.

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

### Pokemon stats

[Open the task folder](pokemon-stats/)

You are building a Pokedex app. Players want to know how strong each Pokemon
is. A Pokemon's strength is the total of its six base stats.
Install `pokebase` as explained below.

1. Import `pokebase`. Write a function `total_stats(name)`. It fetches the
   Pokemon and **returns** the total of its six base stats.
2. Print the totals for Pikachu and Bulbasaur.
3. **(Advanced)** Write `strongest(names)`. It takes a list of names and
   **returns** the name with the highest total. Use `total_stats` inside it.

Expected input and output:

```python
total_stats("pikachu")               # returns 320
strongest(["bulbasaur", "pikachu"])  # returns "pikachu"
```

Your program prints:

```text
320
318
```

Helpful code: each stat has a `base_stat` number.

```python
pokemon = pokebase.pokemon("pikachu")
for stat in pokemon.stats:
    print(stat.base_stat)  # 35, 55, 40, 50, 50, 90
```

The real program needs internet access; `check.py` uses sample data offline.

### Mini project: Pokemon battle

[Open the task folder](mini-project-pokemon-battle/)

You are building a battle game. You and the computer each pick a Pokemon and
the program simulates the battle: they take turns hitting each other for random
damage until one has 0 **HP** (health points). The
starter already runs the game. Install `pokebase` as explained below.

1. Write `get_hp(name)`. It fetches the Pokemon and **returns** its starting HP.
2. Write `attack(hp, damage)`. It **returns** the HP left after the hit,
   never below 0.
3. In the game loop, use `attack` to update `opponent_hp` and `player_hp`.
4. **(Advanced)** Write `health_bar(hp)`. It **returns** one `#` for every
   full 10 HP. Print it after each hit.

Expected input and output:

```python
get_hp("pikachu")   # returns 35
attack(35, 10)      # returns 25
attack(5, 10)       # returns 0
health_bar(35)      # returns "###"
```

Helpful code: the first stat is HP.

```python
pokemon = pokebase.pokemon(name)
print(pokemon.stats[0].base_stat)
```

## Running the Pokemon programs with real data

Only **Pokemon stats** and **Pokemon battle** need this setup.
Open that task folder and choose **Terminal → New Terminal**.

Install `pokebase` once, then run the program.

On Windows (PowerShell):

```powershell
py -m pip install pokebase==1.4.1
py exercise.py
```

On macOS:

```sh
python3 -m pip install pokebase==1.4.1
python3 exercise.py
```

Installation and live lookups need an internet connection. The library may keep
downloaded data in its own cache. If a name is not found, check its spelling;
for example, use `pikachu` or `mewtwo`, not a nickname.
The battle starter asks again for unknown names and reports connection failures.

`-m pip` installs the package for the same Python that runs your code.

[See the solutions after trying the tasks](../../solutions/07-functions/README.md).
