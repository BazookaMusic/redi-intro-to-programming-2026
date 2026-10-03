---
theme: default
title: Introduction to Programming - Fall 2026
info: |
  ReDISchool Week 4 — Strings & Conditionals
highlighter: shiki
transition: slide-left
mdc: true
# Fira Mono has no ligatures, so ==, !=, <=, >= show as two characters
fonts:
  mono: Fira Mono
---

<div class="absolute inset-0 bg-[#E8522A]" />

<!-- Top bar -->
<div class="absolute top-6 left-8 flex items-center gap-3 text-white">
  <div class="w-10 h-10 bg-white rounded flex items-center justify-center">
    <svg viewBox="0 0 40 40" class="w-8 h-8" fill="#E8522A" xmlns="http://www.w3.org/2000/svg">
      <rect x="4" y="4" width="14" height="14" rx="1"/>
      <rect x="22" y="4" width="14" height="14" rx="1"/>
      <rect x="4" y="22" width="14" height="14" rx="1"/>
      <rect x="22" y="22" width="14" height="14" rx="1"/>
    </svg>
  </div>
  <span class="text-lg font-semibold tracking-wide">ReDISchool</span>
</div>
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 4</div>

<!-- Main content -->
<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6">Introduction to Programming - Fall 2026</h1>
  <p class="text-2xl font-light opacity-90">Working with text, then teaching your program to decide 🧠</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Agenda

|  |  |
|---|---|
| 01 | String operations, methods & f-strings |
| 02 | Exercise — Profile card |
| 03 | Comparison & logical operators |
| 04 | Exercise — Checks |
| — | Break (15 min) |
| 05 | If, elif, else, nesting & conditional expressions |
| 06 | Exercise — Weather advisor |
| 07 | Closing exercise — Weather quiz |

Each exercise has a 🟢 basic and a 🔵 advanced version. Pick one.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Recap from last week
<br>

Last week we covered:

- 🐍 **Python basics** — `print()`, comments, running a script
- 📦 **Variables & data types** — `str`, `int`, `float`, `bool`
- ➕ **Arithmetic** — all the operators and how to use them
- ⌨️ **Input & output** — `input()`, `print()`, type conversion with `int()` and `float()`

Today we go deeper on **text**, then teach our programs to **make decisions**.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## 01 - String Operations
<br>

A **string** is text. In Python it lives between quotes: `"hello"` or `'hello'`.

Strings have their own operations — they are not the same as maths:

```python
first = "Hello"
second = "World"

print(first + " " + second)    # Hello World   — concatenation
print("ha" * 3)                # hahaha         — repetition
print(len("Python"))           # 6              — length
```

<br>

`+` joins strings. `*` repeats a string. `len()` counts characters, including spaces.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## String Operations in Practice
<br>

```python
city = "Copenhagen"
country = "Denmark"

print(city + ", " + country)     # Copenhagen, Denmark
print(len(city))                 # 10
print("-" * 12)                  # ------------

# You cannot add a string and a number
age = 30
# print("Age: " + age)           # TypeError!
print("Age: " + str(age))        # Age: 30
```

<br>

`str()` turns a number into text, so it can be joined with `+`.

⚠️ `"10" + "3"` is `"103"`, not `13`. If you want maths, convert with `int()` or `float()` first.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## String Methods
<br>

Strings come with built-in **methods** — actions you call with a dot `.`:

```python
name = "  alice  "

print(name.upper())                 #   ALICE     (spaces kept)
print(name.lower())                 #   alice     (spaces kept)
print(name.strip())                 # alice
print(name.strip().capitalize())    # Alice

greeting = "Hello, World!"
print(greeting.replace("World", "Python"))  # Hello, Python!
```

<br>

💡 Methods do **not** change the original variable. They return a **new** string.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Methods Don't Change the Original
<br>

```python
name = "  alice  "
clean = name.strip().capitalize()

print(name)     #   alice     — still the same, spaces and all
print(clean)    # Alice       — the new string
```

<br>

If you want to keep the result, store it:

```python
answer = input("yes or no? ")
answer = answer.strip().lower()
```

<br>

`.strip()` removes spaces the user typed by accident. `.lower()` makes `"Yes"`, `"YES"`, and `"yes"` all become `"yes"`.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Useful Methods for User Input
<br>

| Method | What it does | Example |
|---|---|---|
| `.lower()` | all lowercase | `"Yes".lower()` → `"yes"` |
| `.upper()` | all uppercase | `"ok".upper()` → `"OK"` |
| `.strip()` | remove spaces at the ends | `"  hi  ".strip()` → `"hi"` |
| `.capitalize()` | first letter uppercase | `"alice".capitalize()` → `"Alice"` |
| `.replace(a, b)` | swap one piece of text | `"hi-there".replace("-", " ")` → `"hi there"` |
| `.startswith()` | does it begin with this? | `"Python".startswith("Py")` → `True` |
| `.endswith()` | does it end with this? | `"notes.txt".endswith(".txt")` → `True` |

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## String Formatting
<br>

Building sentences with `+` gets messy fast. **f-strings** are the clean way.

Put an `f` before the quote, and drop expressions inside `{}`:

```python
name = "Alice"
age = 30
city = "Copenhagen"

print(f"My name is {name}, I am {age} years old.")
print(f"I live in {city}.")
print(f"Next year I will be {age + 1}.")
```

Output:
```
My name is Alice, I am 30 years old.
I live in Copenhagen.
Next year I will be 31.
```

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## f-Strings in Practice
<br>

You can put **any expression** (code that produces a value) inside `{}`.
For example, variables, maths, and method calls:

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

```python
name = "maria"
city = "berlin"
age = 30

print(f"Hi, {name}!")                               # variable
print(f"Next year you will be {age + 1}.")          # maths
print(f"You live in {city.capitalize()}.")          # method call
print(f"{name.upper()} is {age * 12} months old.")  # combined
```

</div>

<div>

```
Hi, maria!
Next year you will be 31.
You live in Berlin.
MARIA is 360 months old.
```

</div>

</div>

f-strings are the **modern, recommended** way to format text in Python.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Multiline f-Strings
<br>

Use three quotes `"""` to write one f-string over several lines.
The line breaks show up in the output too:

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

```python
name = "Maria"
city = "Berlin"
hobby = "hiking"

print(f"""👤 {name}
📍 {city}
❤️ {hobby}""")
```

</div>

<div>

```
👤 Maria
📍 Berlin
❤️ hiking
```

</div>

</div>

💡 Close the `"""` at the end of the last line, or you get an extra empty line.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 1 — Profile Card · 20 min

Ask for a name, a city, and a hobby. Print a short profile.

<div class="flex flex-col gap-3 profile-exercise">

<div class="level-box level-basic">

🟢 **Basic**

- Clean the name with `.strip().capitalize()`
- Print three lines with f-strings
- Print how many letters are in the name (`len`)

</div>

<div class="level-box level-advanced grid grid-cols-[3fr_2fr] gap-4">

<div>

🔵 **Advanced** — a full profile card

Also ask for a last name, birth year, and bio. Print a card with:

- the full name in capitals, underlined with `=`
- a username: lowercase, `_` instead of spaces
- the age, worked out from the birth year
- the city, hobby, and bio, each with an emoji

</div>

<div>

```
MARIA JENSEN
============
👤 @maria_jensen
🎂 30 years old
📍 Berlin
❤️ Hiking
📝 I love maps and coffee.
```

Copy emojis from [getemoji.com](https://getemoji.com/)

</div>

</div>

</div>

<style>
.profile-exercise li { margin-top: 0; margin-bottom: 0; line-height: 1.6; }
.profile-exercise p { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.profile-exercise ul { margin-top: 0.25rem; margin-bottom: 0; }
.level-box { border: 2px solid; border-left-width: 6px; border-radius: 8px; padding: 0.5rem 1rem; }
.level-basic { border-color: #2e9e5b; }
.level-advanced { border-color: #2f6fdc; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 1 — Hints

🟢 **Basic**

1. One `input()` per question. Store each answer.
2. `name = name.strip().capitalize()`
3. `print(f"Hi, my name is {name}.")`
4. `print(f"My name has {len(name)} letters.")`

🔵 **Advanced**

1. `"ha" * 3` gives `hahaha`. The `=` line has to fit **any** name, not just `MARIA JENSEN`.
2. `"2026-10-03".replace("-", "/")` gives `2026/10/03`, which is handy for the username.
3. Build the username and the line first, then print everything with one `"""` f-string.
4. Test with messy input like `"  anna maria  "`. Does everything still line up?

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 1 — Solution

<div class="grid grid-cols-2 gap-4 text-[13px] leading-snug">

<div>

🟢 **Basic**

```python
name = input("Name: ").strip().capitalize()
city = input("City: ").strip()
hobby = input("Hobby: ").strip()

print(f"Hi, my name is {name}.")
print(f"I live in {city}.")
print(f"I love {hobby}.")
print(f"My name has {len(name)} letters.")
```

</div>

<div>

🔵 **Advanced**

```python
first = input("First name: ").strip().capitalize()
last = input("Last name: ").strip().capitalize()
year = int(input("Birth year: "))
city = input("City: ").strip().capitalize()
hobby = input("Hobby: ").strip().capitalize()
bio = input("Short bio: ").strip()

title = f"{first} {last}"
line = "=" * len(title)
username = title.lower().replace(" ", "_")

print(f"""{title.upper()}
{line}
👤 @{username}
🎂 {2026 - year} years old
📍 {city}
❤️ {hobby}
📝 {bio}""")
```

</div>

</div>
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## From Text to Decisions
<br>

So far every line runs, top to bottom, every time.

Next we teach the program to **choose**:

- Is this password correct?
- Is the user old enough?
- Did they type `"yes"`, or something else?

<br>

To choose, Python needs to **compare** values — numbers and strings — and get back `True` or `False`.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## 03 - Comparison Operators
<br>

Comparison operators **compare two values** and always return `True` or `False`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<` | Less than | `2 < 1` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 2` | `False` |

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Comparing Numbers and Text
<br>

```python
age = 20
print(age >= 18)              # True

password = "abc123"
print(password == "abc123")   # True
print(password == "ABC123")   # False — case sensitive!

city = "Copenhagen"
print(city.lower() == "copenhagen")   # True
print(len(city) > 5)                  # True
```

<br>

⚠️ Don't confuse `=` (store a value) with `==` (compare two values).

Strings compare **character by character**. `"Yes"` and `"yes"` are not equal.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Is It Inside? The `in` Operator
<br>

`in` checks whether a piece of text appears **anywhere** inside a string:

```python
email = "maria.jensen@example.com"

print("@" in email)                  # True
print("jensen" in email)             # True
print("gmail" in email)              # False
print("JENSEN" in email)             # False — case sensitive!
print("JENSEN".lower() in email)     # True
```

<br>

`not in` checks the opposite:

```python
password = "sunny2026"
print("123" not in password)         # True
```

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Logical Operators
<br>

Logical operators let you **combine multiple conditions**:

| Operator | Meaning | Result is `True` when... |
|---|---|---|
| `and` | Both must be true | **Both** conditions are `True` |
| `or` | At least one must be true | **Either** condition is `True` |
| `not` | Reverses the result | The condition is `False` |

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Logical Operators in Practice
<br>

```python
age = 25
has_ticket = True
city = "aarhus"

print(age >= 18 and has_ticket)          # True
print(age < 18 or has_ticket)            # True
print(not has_ticket)                    # False

print(city == "copenhagen" or city == "aarhus")   # True
```

<br>

Clean user input first, then combine the checks:

```python
answer = input("Do you have a ticket? ").strip().lower()
print(answer == "yes" or answer == "y")
```

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 2 — Checks · 20 min

<div class="grid grid-cols-2 gap-6 mt-6 checks-exercise">

<div class="level-box level-basic">

🟢 **Basic** — player sign-up

Store a player's `age`, `password`, `city`, and `points` in variables. Print `True` or `False` for each:

- `age` is at least 18
- `password` is `"secret"`
- `city` is `"Copenhagen"`
- `points` is not 0

**Example:** `age = 20` → `True`

</div>

<div class="level-box level-advanced">

🔵 **Advanced** — password checker

Players must have strong passwords for their account. Write a program that reads a username and a password with `input()` and prints `True` if the password is strong, or `False` otherwise. A password is strong if it:

- has at least 8 characters
- does not start with `123`
- is not `password`, in any case
- does not contain the username, in any case

**Example:** `Sunny2026` → `True` · `Maria2026` for user `maria` → `False`

</div>

</div>

<style>
.checks-exercise li { margin-top: 0; margin-bottom: 0; line-height: 1.6; }
.checks-exercise p { margin-top: 0.25rem; margin-bottom: 0.5rem; }
.level-box { border: 2px solid; border-left-width: 6px; border-radius: 8px; padding: 0.5rem 1rem; }
.level-basic { border-color: #2e9e5b; }
.level-advanced { border-color: #2f6fdc; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 2 — Hints
<br>

🟢 **Basic**

```python
age = 20
password = "secret"
city = "Copenhagen"
points = 10
```

Then `print(age >= 18)`, `print(password == "secret")`, and so on.

🔵 **Advanced**

1. `"Python".startswith("Py")` gives `True`. Which operator flips it?
2. Lowercase both before comparing, so `Password` and `MARIA2026` are caught too.
3. Store each rule in a variable, like `long_enough = len(password) >= 8`, then combine them with `and`.

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 2 — Solution

<div class="grid grid-cols-2 gap-4 text-[13px] leading-snug">

<div>

🟢 **Basic**

```python
age = 20
password = "secret"
city = "Copenhagen"
points = 10

print(age >= 18)             # True
print(password == "secret")  # True
print(city == "Copenhagen")  # True
print(points != 0)           # True
```

</div>

<div>

🔵 **Advanced**

```python
username = input("Username: ")
password = input("Password: ")

long_enough = len(password) >= 8
no_123 = not password.startswith("123")
not_obvious = password.lower() != "password"
no_username = username.lower() not in password.lower()

strong = long_enough and no_123
strong = strong and not_obvious and no_username
print(strong)
```

</div>

</div>
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

<br>
<br>
<br>
<br>
<br>
<br>
<div class="font-bold text-[#000000] uppercase tracking-widest mb-18 text-center" style="font-size: 40px;">Questions before the break?</div>

---

<div class="absolute inset-0 bg-[#E8522A]" />

<!-- Top bar -->
<div class="absolute top-6 left-8 flex items-center gap-3 text-white">
  <div class="w-10 h-10 bg-white rounded flex items-center justify-center">
    <svg viewBox="0 0 40 40" class="w-8 h-8" fill="#E8522A" xmlns="http://www.w3.org/2000/svg">
      <rect x="4" y="4" width="14" height="14" rx="1"/>
      <rect x="22" y="4" width="14" height="14" rx="1"/>
      <rect x="4" y="22" width="14" height="14" rx="1"/>
      <rect x="22" y="22" width="14" height="14" rx="1"/>
    </svg>
  </div>
  <span class="text-lg font-semibold tracking-wide">ReDISchool</span>
</div>
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 4</div>

<!-- Main content -->
<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">Break (15 min)</h1>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## 05 - If Statements
<br>

An `if` runs code **only when a condition is `True`**:

```python
temperature = 30

if temperature >= 25:
    print("T-shirt weather ☀️")

print("Have a nice day!")
```

<br>

- The condition ends with a colon `:`
- The indented line runs only if the condition is `True`
- `"Have a nice day!"` is not indented, so it **always** runs

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Indentation Decides What's Inside
<br>

The lines indented under the `if` are its **block**. Moving one line changes the program:

<div class="grid grid-cols-2 gap-6">
<div>

```python
temperature = 10

if temperature >= 25:
    print("T-shirt weather ☀️")
    print("Bring sunscreen 🧴")
print("Have a nice day!")
```

```text
Have a nice day!
```

</div>
<div>

```python
temperature = 10

if temperature >= 25:
    print("T-shirt weather ☀️")
print("Bring sunscreen 🧴")
print("Have a nice day!")
```

```text
Bring sunscreen 🧴
Have a nice day!
```

</div>
</div>

- **Tab** indents, **Shift + Tab** removes the indent. VS Code uses **4 spaces**
- VS Code also indents for you when you press Enter after a `:`
- No indentation after `:` gives `IndentationError: expected an indented block`

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Adding Else
<br>

`else` runs when the condition is `False`:

```python
weather = input("What's the weather like? ").strip().lower()

if weather == "rain":
    print("🌂 Take an umbrella!")
else:
    print("😎 Leave the umbrella at home.")
```

<br>

Only **one** of these two lines will ever print — never both.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Adding Elif
<br>

`elif` ("else if") adds more choices in between:

```python
weather = input("What's the weather like? ").strip().lower()

if weather == "rain":
    print("🌂 Take an umbrella!")
elif weather == "snow":
    print("🧤 Wear gloves and boots!")
elif weather == "sun":
    print("🧴 Don't forget sunscreen!")
else:
    print("🤔 Hmm, I don't know that weather.")
```

Python checks the conditions **from top to bottom** and runs only the first one that is `True`.
If none of them match, the `else` block runs.

You can add as many `elif` as you need, and `else` is optional.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Combining Conditions
<br>

Logical operators and string methods belong **inside** `if` statements:

```python
weather = input("What's the weather like? ").strip().lower()
wind = input("Is it windy? (yes/no) ").strip().lower()

if weather == "rain" and wind == "yes":
    print("🧥 Wear a raincoat, an umbrella will flip!")
elif weather == "rain" or weather == "snow":
    print("🌂 Take an umbrella!")
else:
    print("😎 No umbrella needed.")
```

<br>

Order matters: windy rain is checked **before** plain rain, otherwise the umbrella would always win.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Nested Conditionals
<br>

You can put an `if` **inside** another `if` — this is called nesting:

```python
weather = input("What's the weather like? ").strip().lower()

if weather == "snow":
    driving = input("Do you have to drive? (yes/no) ").strip().lower()
    if driving == "yes":
        print("🚗 Leave early, the roads are slippery!")
    else:
        print("🛷 Go sledding!")
else:
    print("🙂 No snow plans needed today.")
```

<br>

The inner `if` only runs when the outer one is `True`, so we only ask about driving when it snows.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Truthy & Falsy Values
<br>

In Python, **every value has a boolean meaning** — not just `True` and `False`.

These values are treated as `False`:

```python
False    # the boolean False
0        # zero
0.0      # zero as a float
""       # empty string
```

**Everything else is treated as `True`** — any non-zero number, any non-empty string, etc.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Truthy & Falsy in Practice
<br>

An empty string is falsy, so this checks "did they type anything?":

```python
city = input("Which city are you in? ").strip()

if city:
    print(f"Checking the weather in {city.capitalize()}...")
else:
    print("You didn't enter a city.")
```

```python
rain_mm = int(input("How many mm of rain today? "))

if rain_mm:
    print(f"{rain_mm} mm of rain today. 💧")
else:
    print("No rain today! ☀️")
```

<br>

💡 This is a very **Pythonic** pattern — you'll see it everywhere in real code.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Conditional Expressions
<br>

An `if` statement chooses which **code** runs. A conditional expression chooses which **value** to use:

```python
temperature = 30
clothes = "a T-shirt" if temperature >= 25 else "a jacket"
print(f"Wear {clothes}.")    # Wear a T-shirt.
```

The pattern is: `value_if_true if condition else value_if_false`

<br>

It gives the same result as this longer `if`/`else`:

```python
if temperature >= 25:
    clothes = "a T-shirt"
else:
    clothes = "a jacket"
```

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Conditional Expressions in Practice
<br>

```python
temperature = int(input("How many degrees is it? "))
feel = "warm" if temperature >= 20 else "cold"
print(f"It's {feel} outside.")

city = input("Your city: ").strip()
place = city.capitalize() if city else "your area"
print(f"Here's the forecast for {place}.")
```

<br>

⚠️ Use it to **pick between two values**. To run different code, use a normal `if`/`else`.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Predict the Output 🤔

What does this program print? Discuss with your neighbour for a minute.

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

And with `weather = "sun"` and `temperature = -5`?

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Predict the Output — Answers
<br>

**Snow, 2°, windy** prints `🧥 Wear a hood, it's windy!`

- `"snow"` matches the outer `if`, so Python goes inside.
- `2 < 0` is `False`, so the first inner check fails.
- `wind == "yes"` is `True`, so the `elif` runs.

<br>

**Sun, -5°** prints `🧤 Wear gloves!`

- `"sun"` is not rain or snow, so Python skips the whole inner block.
- `-5 < 0` is `True`, so the outer `elif` runs.
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 3 — Weather Advisor · 20 min

<div class="grid grid-cols-2 gap-6 mt-4 weather-exercise">

<div class="level-box level-basic">

🟢 **Basic** — what to wear

Ask for the temperature and whether it's raining (`yes` / `no`). Print what to wear:

- 20° or more → `Wear a T-shirt.`
- 10° to 19° → `Wear a jacket.`
- below 10° → `Wear a warm coat.`
- raining → also `Take an umbrella.`

**Example:** `14`, `yes`

```
Wear a jacket.
Take an umbrella.
```

</div>

<div class="level-box level-advanced">

🔵 **Advanced** — daily report

Read the weather, temperature, and wind (km/h). Print a report like the example:

- wind 75+: a storm warning instead of advice
- wind 30+: feels 5° colder, dress for that
- rain or snow: umbrella, or raincoat if windy
- rain or snow below 0°: `Icy roads!`

**Example:** `" RAIN "`, `-1`, `40`

```
Rain, -1°C, wind 40 km/h
Feels like -6°C
Wear a warm coat.
Wear a raincoat.
Icy roads!
```

</div>

</div>

<style>
.weather-exercise li { margin-top: 0; margin-bottom: 0; line-height: 1.6; }
.weather-exercise p { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.weather-exercise ul { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.weather-exercise pre { font-size: 12px; line-height: 1.4; }
.level-box { border: 2px solid; border-left-width: 6px; border-radius: 8px; padding: 0.5rem 1rem; }
.level-basic { border-color: #2e9e5b; }
.level-advanced { border-color: #2f6fdc; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 3 — Hints
<br>

🟢 **Basic**

1. The temperature is a number, so convert it with `int()`.
2. Check from the warmest down: `>= 20` first, then `>= 10`, then `else`.
3. The umbrella is a separate `if` **after** the outfit, so both lines can print.

🔵 **Advanced**

1. Which rule stops all the others? Make it the outer `if`, and put the rest in its `else`.
2. Work out the feels-like temperature **once**, before you choose clothes.
3. Rain gear and icy roads can both print. Do they belong in the same `if` / `elif` chain?

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Exercise 3 — Basic Solution

```python
temperature = int(input("Temperature: "))
rain = input("Is it raining? (yes/no) ").strip().lower()

if temperature >= 20:
    print("Wear a T-shirt.")
elif temperature >= 10:
    print("Wear a jacket.")
else:
    print("Wear a warm coat.")

if rain == "yes":
    print("Take an umbrella.")
```
<!-- solution:end -->

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-2">Week 4 — Strings & Conditionals</div>

## Exercise 3 — Advanced Solution

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-2 adv-solution">

<div>

```python
weather = input("Weather: ").strip().lower()
temperature = int(input("Temperature: "))
wind = int(input("Wind (km/h): "))

print(f"{weather.capitalize()}, {temperature}°C, wind {wind} km/h")
if wind >= 75:
    print("Storm warning! Stay inside.")
else:
    windy = wind >= 30
    wet = weather == "rain" or weather == "snow"
    feels = temperature - 5 if windy else temperature
    if windy:
        print(f"Feels like {feels}°C")
    if feels >= 20:
        print("Wear a T-shirt.")
    elif feels >= 10:
        print("Wear a jacket.")
    else:
        print("Wear a warm coat.")
    if wet and windy:
        print("Wear a raincoat.")
    elif wet:
        print("Take an umbrella.")
    if wet and temperature < 0:
        print("Icy roads!")
```

</div>

<div>

**Why it works**

- The storm is the outer `if`. All other advice lives in its `else`, so a storm skips it.
- `feels` is worked out once and reused for the clothes.
- Clothes, rain gear, and icy roads are **separate** `if`s, so several lines can print.

</div>

</div>

<style>
.adv-solution pre, .adv-solution pre code { font-size: 11px !important; line-height: 1.35 !important; }
</style>
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Closing Exercise — Weather Quiz · 20 min

<div class="grid grid-cols-2 gap-6 mt-6 quiz-exercise">

<div class="level-box level-basic">

🟢 **Basic** — three questions

Build a weather quiz. Start `score` at `0`, add `1` for each correct answer, and print the total at the end.

- At what °C does water freeze? → `0`
- What falls from clouds as frozen flakes? → `snow`
- What appears when the sun shines during rain? → `rainbow`

**Example:** `You scored 2 out of 3.`

</div>

<div class="level-box level-advanced">

🔵 **Advanced** — a fairer quiz

Players complain the quiz marks right answers as wrong. Make it fairer:

- `" Snow "` and `"SNOW"` count as correct
- answers like `"a rainbow"` or `"snowflakes"` count too
- add a fourth weather question of your own
- after the score, print a different message for 4/4, 3/4, and below

**Example:** `You scored 4 out of 4.` then `Perfect forecast! ☀️`

</div>

</div>

<style>
.quiz-exercise li { margin-top: 0; margin-bottom: 0; line-height: 1.6; }
.quiz-exercise p { margin-top: 0.25rem; margin-bottom: 0.5rem; }
.level-box { border: 2px solid; border-left-width: 6px; border-radius: 8px; padding: 0.5rem 1rem; }
.level-basic { border-color: #2e9e5b; }
.level-advanced { border-color: #2f6fdc; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Closing Exercise — Hints
<br>

🟢 **Basic**

1. `score = 0` before the questions.
2. After each answer, an `if` checks it. Inside, indented: `score = score + 1`
3. The freezing question needs `int(input(...))`.
4. One f-string at the end for the score.

🔵 **Advanced**

1. Clean every text answer before you check it.
2. Look back at the `in` operator slide.
3. Use `if` / `elif` / `else` on the score for the final message.

<!-- solution:start -->
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-2">Week 4 — Strings & Conditionals</div>

## Closing Exercise — Solution

<div class="grid grid-cols-2 gap-4 text-[12px] leading-tight">

<div>

🟢 **Basic**

```python
score = 0

freeze = int(input("Water freezes at? (°C) "))
if freeze == 0:
    score = score + 1

flakes = input("Frozen flakes? ")
if flakes == "snow":
    score = score + 1

colours = input("Sun + rain makes a? ")
if colours == "rainbow":
    score = score + 1

print(f"You scored {score} out of 3.")
```

</div>

<div>

🔵 **Advanced**

```python
score = 0
if int(input("Water freezes at? (°C) ")) == 0:
    score = score + 1
flakes = input("Frozen flakes? ").strip().lower()
if "snow" in flakes:
    score = score + 1
colours = input("Sun + rain makes a? ").strip().lower()
if "rainbow" in colours:
    score = score + 1
if int(input("Water boils at? (°C) ")) == 100:
    score = score + 1
print(f"You scored {score} out of 4.")
if score == 4:
    print("Perfect forecast! ☀️")
elif score == 3:
    print("Mostly sunny! 🌤️")
else:
    print("Cloudy with a chance of revision. 🌧️")
```

</div>

</div>
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## What We Learned Today
<br>

✅ **String operations** — concatenation with `+`, repetition with `*`, `len()`

✅ **String methods** — `.lower()`, `.strip()`, `.capitalize()`, `.replace()`

✅ **f-strings** — `f"Hello, {name}!"` to build clean output

✅ **Comparison operators** — `==`, `!=`, `<`, `>`, `<=`, `>=`, and `in` to look inside text

✅ **Logical operators** — `and`, `or`, `not`

✅ **if / elif / else** — and nested conditionals

✅ **Truthy & falsy** — an empty string is `False`

✅ **Conditional expressions** — `value if condition else other` to pick a value

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 4 — Strings & Conditionals</div>

## Homework
<br>

🏠 Finish the weather quiz if you didn't, then extend it:

🟢 **Basic** — add 2 more questions and keep the score correct (`out of 5`).

<div class="grid grid-cols-[3fr_2fr] gap-6 items-start homework-adv">

<div>

🔵 **Advanced** — turn it into a game show:

- Wrong answer? Print a hint and give **one** more try.
- 2 points on the first try, 1 on the second.
- All answers right on the first try? Unlock a **bonus question**.

</div>

<div>

**Example:**

```
Frozen flakes? rain
Hint: it's white and cold.
Try again: snow
+1 point
```

</div>

</div>

📌 **Remember:** Commit your work to GitHub when you're done!

<style>
.homework-adv li { margin-top: 0; margin-bottom: 0; line-height: 1.6; }
.homework-adv pre { font-size: 12px; line-height: 1.4; }
</style>

---

<div class="absolute inset-0 bg-[#E8522A]" />

<!-- Top bar -->
<div class="absolute top-6 left-8 flex items-center gap-3 text-white">
  <div class="w-10 h-10 bg-white rounded flex items-center justify-center">
    <svg viewBox="0 0 40 40" class="w-8 h-8" fill="#E8522A" xmlns="http://www.w3.org/2000/svg">
      <rect x="4" y="4" width="14" height="14" rx="1"/>
      <rect x="22" y="4" width="14" height="14" rx="1"/>
      <rect x="4" y="22" width="14" height="14" rx="1"/>
      <rect x="22" y="22" width="14" height="14" rx="1"/>
    </svg>
  </div>
  <span class="text-lg font-semibold tracking-wide">ReDISchool</span>
</div>
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 4</div>

<!-- Main content -->
<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">🎉 See you next week!</h1>
</div>
