# 04 · Strings and Conditionals exercises

These exercises come from the [Strings and Conditionals slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/04-strings-and-conditionals.html). When you finish, compare your work with the [solutions](../../solutions/04-strings-and-conditionals/).

New to this? Follow [How to clone this repository to get access to exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026#clone-repository) and [How to do exercises and check my answers](https://github.com/BazookaMusic/redi-intro-to-programming-2026#do-exercises) first.

## Homework

Do these at home after the lesson.

### Homework 1: Five-question weather quiz

**Folder:** [`homework-01-five-question-quiz`](homework-01-five-question-quiz/)

Extend the weather quiz from class to five questions. Start `score` at `0`. Ask each question with `input()` and add 1 to `score` for every correct answer. At the end, print the score out of 5.

Questions and correct answers:

1. At what °C does water freeze? → `0`
2. What falls from clouds as frozen flakes? → `snow`
3. What appears when the sun shines during rain? → `rainbow`
4. At what °C does water boil? → `100`
5. What do you call air that moves outside? → `wind`

Example input: 0, snow, rain, 100, wind

Example output:

```text
You scored 4 out of 5.
```

### Homework 2: Weather game show

**Folder:** [`homework-02-weather-game-show`](homework-02-weather-game-show/)

Turn the three-question weather quiz into a game show. Clean every text answer with `.strip().lower()` before you check it.

For each question:

- Correct on the first try: print `+2 points` and add 2 to `score`.
- Wrong: print the hint, then ask again with `input("Try again: ")`.
  - Correct now: print `+1 point` and add 1 to `score`.
  - Still wrong: print `No points. The answer was [answer].`

Questions, answers, and hints:

1. At what °C does water freeze? → `0` · Hint: it's between -1 and 1.
2. What falls from clouds as frozen flakes? → `snow` · Hint: it's white and cold.
3. What appears when the sun shines during rain? → `rainbow` · Hint: it has seven colours.

After the three questions, print `You scored [score] out of 6.` If the score is 6, print `Bonus question unlocked!` and ask: How many colours does a rainbow have? → `7`

- Correct: print `Bonus point! Final score: 7`
- Wrong: print `No bonus this time.`

Example input: 0, rain, snow, rainbow

Example output:

```text
+2 points
Hint: it's white and cold.
+1 point
+2 points
You scored 5 out of 6.
```

## Classroom exercises

We do these together during the lesson.

### Exercise 1: Profile card

**Folder:** [`profile-card`](profile-card/)

Ask for a name, a city, and a hobby with `input()`. Clean the name with `.strip().capitalize()`. Print three lines with f-strings, then print how many letters are in the name with `len()`.

Example input: `"  maria "`, Berlin, hiking

Example output:

```text
Hi, my name is Maria.
I live in Berlin.
I love hiking.
My name has 5 letters.
```

### Exercise 1 (advanced): Full profile card

**Folder:** [`profile-card-advanced`](profile-card-advanced/)

Ask for a first name, last name, birth year, city, hobby, and short bio. Clean every answer with `.strip()`. Also use `.capitalize()` on the first name, last name, city, and hobby.

Print a card with:

- the full name in capitals
- a line of `=` signs exactly as long as the full name
- a username: the full name in lowercase, with `_` instead of spaces
- the age, worked out from the birth year (use 2026 as this year)
- the city, hobby, and bio, each with the emoji shown below

Copy emojis from [getemoji.com](https://getemoji.com/).

Example input: maria, jensen, 1996, berlin, hiking, I love maps and coffee.

Example output:

```text
MARIA JENSEN
============
👤 @maria_jensen
🎂 30 years old
📍 Berlin
❤️ Hiking
📝 I love maps and coffee.
```

### Exercise 2: Player sign-up checks

**Folder:** [`player-sign-up-checks`](player-sign-up-checks/)

A game stores a new player's details in the variables in `exercise.py`. Print `True` or `False` for each check, in this order:

1. `age` is at least 18
2. `password` is `"secret"`
3. `city` is `"Copenhagen"`
4. `points` is not 0

Use comparison operators, so your answers stay right if the values change.

Example output (for the values in `exercise.py`):

```text
True
True
True
True
```

### Exercise 2 (advanced): Password checker

**Folder:** [`password-checker`](password-checker/)

Players must have strong passwords for their account. Ask for a username and a password with `input()`. Print `True` if the password is strong, or `False` if it is not. A strong password:

- has at least 8 characters
- does not start with `123`
- is not `password`, in any case (so `PassWord` is not allowed either)
- does not contain the username, in any case

Example input: maria, Sunny2026

Example output:

```text
True
```

Example input: maria, Maria2026

Example output:

```text
False
```

### Predict the output

This one needs no code and no folder. Read the program, then write down what it prints.

```python
weather = "snow"
temperature = 2
wind = "yes"

if weather == "rain" or weather == "snow":
    if temperature < 0 and wind == "yes":
        print("🥶 Stay inside!")
    elif wind == "yes":
        print("🧥 Wear a hood, it's windy!")
    else:
        print("🌂 Take an umbrella!")
elif temperature < 0:
    print("🧤 Wear gloves!")
else:
    print("😎 Enjoy your day!")
```

What does it print with `weather = "sun"` and `temperature = -5`?

### Exercise 3: Weather advisor

**Folder:** [`weather-advisor`](weather-advisor/)

Ask for the temperature and whether it's raining (`yes` / `no`). Print what to wear:

- 20° or more → `Wear a T-shirt.`
- 10° to 19° → `Wear a jacket.`
- below 10° → `Wear a warm coat.`

If it's raining, also print `Take an umbrella.`

Example input: 14, yes

Example output:

```text
Wear a jacket.
Take an umbrella.
```

### Exercise 3 (advanced): Daily weather report

**Folder:** [`weather-advisor-advanced`](weather-advisor-advanced/)

Ask for the weather (like rain, snow, or sun), the temperature, and the wind speed in km/h. Clean the weather with `.strip().lower()`.

First, print a summary line like `Rain, -1°C, wind 40 km/h`. Then:

- wind 75 or more: print `Storm warning! Stay inside.` and nothing else
- wind 30 or more: it feels 5° colder. Print `Feels like [number]°C` and choose clothes for that temperature
- clothes: 20° or more → `Wear a T-shirt.` · 10° to 19° → `Wear a jacket.` · below 10° → `Wear a warm coat.`
- rain or snow: print `Take an umbrella.`, or `Wear a raincoat.` instead if the wind is 30 or more
- rain or snow below 0° (the real temperature): also print `Icy roads!`

Example input: `" RAIN "`, -1, 40

Example output:

```text
Rain, -1°C, wind 40 km/h
Feels like -6°C
Wear a warm coat.
Wear a raincoat.
Icy roads!
```

### Closing exercise: Weather quiz

**Folder:** [`weather-quiz`](weather-quiz/)

Build a weather quiz. Start `score` at `0`. Ask each question with `input()` and add 1 to `score` for every correct answer. At the end, print the score out of 3.

Questions and correct answers:

1. At what °C does water freeze? → `0`
2. What falls from clouds as frozen flakes? → `snow`
3. What appears when the sun shines during rain? → `rainbow`

Example input: 0, snow, rain

Example output:

```text
You scored 2 out of 3.
```

### Closing exercise (advanced): A fairer quiz

**Folder:** [`weather-quiz-advanced`](weather-quiz-advanced/)

Players complain the quiz marks right answers as wrong. Make it fairer:

- `" Snow "` and `"SNOW"` count as correct
- answers that contain the right word, like `"a rainbow"` or `"snowflakes"`, count too
- add a fourth question: At what °C does water boil? → `100`

Print the score out of 4, then a message:

- 4 points: `Perfect forecast! ☀️`
- 3 points: `Mostly sunny! 🌤️`
- fewer: `Cloudy with a chance of revision. 🌧️`

Example input: 0, snowflakes, A RAINBOW, 100

Example output:

```text
You scored 4 out of 4.
Perfect forecast! ☀️
```
