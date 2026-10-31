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
You do not need to understand the checker code.

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

### Pizza slices

[Open the task folder](pizza-slices/)

Write `slices_left(slices, eaten)` that returns the slices remaining.
Start with `8` slices and eat `3`.
Save the returned value in `remaining` and print it.
Use `remaining` in another call: eat `2` more slices.
Save and print the new result.
Assume no one eats more slices than are available.

Example output:

```text
5
3
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

### Circle area

[Open the task folder](circle-area/)

Import `math`. Write `circle_area(radius)` that returns
`math.pi * radius * radius`.
Call it with radius `2` and print its result rounded to two decimal places.
Keep the unrounded value inside the function.

Example output:

```text
12.57
```

### Pokemon stats

[Open the task folder](pokemon-stats/)

Install `pokebase` as explained below.
Import `pokebase` and fetch Pikachu with `pokebase.pokemon("pikachu")`.
Loop over `pokemon.stats`; each number is in `stat.base_stat`.
Add the six numbers together. Do not use `sum()`.
Print the total.
The real program needs internet access; `check.py` uses sample data offline.

Example output:

```text
320
```

### Mini project: Pokemon battle

[Open the task folder](mini-project-pokemon-battle/)

Install `pokebase` as explained below.
Implement `get_hp(name)`: fetch the Pokemon with `pokebase.pokemon(name)`
and return `pokemon.stats[0].base_stat`, its starting health.
Implement `attack(hp, damage)`: return `hp` minus `damage`, never below zero.
Add a docstring to each function. Replace both `pass` placeholders.
Fill the two missing `attack()` calls in the supplied loop.
Enter any supported Pokemon name. Press Enter to attack.
Damage is a random integer from `5` to `15`. A defeated opponent cannot attack.
The input and error-handling code is supplied; leave it unchanged.

**HP** means health points.

Sample input: `pikachu`, then Enter for each attack.

One possible start of the output:

```text
Your Pokemon: pikachu
You: pikachu (35 HP)
Opponent: bulbasaur (45 HP)
Press Enter to attack:
bulbasaur has 33 HP.
pikachu has 28 HP.
```

## Running the Pokemon programs with real data

Only **Pokemon stats** and **Pokemon battle** need this setup.
Open that task folder and choose **Terminal → New Terminal**.

A **virtual environment** is a folder containing a separate Python environment
and its packages. Create a `.venv` folder in each Pokemon task folder.
No activation command is needed: the commands below use its Python directly.

On Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pokebase==1.4.1
.\.venv\Scripts\python.exe exercise.py
```

On macOS:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install pokebase==1.4.1
.venv/bin/python exercise.py
```

Installation and live lookups need an internet connection. The library may keep
downloaded data in its own cache. If a name is not found, check its spelling;
for example, use `pikachu` or `mewtwo`, not a nickname.
The battle starter asks again for unknown names and reports connection failures.

If you use VS Code's Run button, choose **Python: Select Interpreter** from the
Command Palette and select the Python in this task's `.venv`.
Do not commit `.venv`.

[See the solutions after trying the tasks](../../solutions/07-functions/README.md).
