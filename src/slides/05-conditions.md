---
theme: default
title: "Lesson 05 – Conditions & Logic | ReDI School"
info: |
  ## Introduction to Programming in Python
  Lesson 05: Conditions & Logic
  ReDI School of Digital Integration
class: text-center
transition: slide-left
colorSchema: light
fonts:
  sans: 'Inter'
  mono: 'Fira Code'
---

<style>
.concept-box { background: #F0F4FF; border-left: 4px solid #4A6CF7; padding: 12px 16px; border-radius: 4px; margin: 8px 0; }
.exercise-box { background: #F0FFF4; border-left: 4px solid #38A169; padding: 12px 16px; border-radius: 4px; margin: 8px 0; }
.warning-box { background: #FFFBEB; border-left: 4px solid #D69E2E; padding: 12px 16px; border-radius: 4px; margin: 8px 0; }
.mistake-box { background: #FFF5F5; border-left: 4px solid #E53E3E; padding: 12px 16px; border-radius: 4px; margin: 8px 0; }
.real-box { background: #EBF8FF; border-left: 4px solid #3182CE; padding: 12px 16px; border-radius: 4px; margin: 8px 0; }
.break-box { background: #F7FAFC; border: 2px dashed #CBD5E0; padding: 20px; border-radius: 8px; margin: 8px 0; text-align: center; font-size: 1.2em; }
.part-badge { background: #2D3748; color: white; padding: 3px 12px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
</style>

# 🐍 Conditions & Logic

<div class="text-2xl mt-4 text-gray-600">Introduction to Programming in Python</div>
<div class="mt-2 text-gray-500">Lesson 05 · ReDI School of Digital Integration</div>
<div class="mt-8 text-gray-400 text-sm">Arun</div>

---
layout: center
---

# What did we learn last week?

<div class="grid grid-cols-3 gap-4 mt-8">
<div class="concept-box text-center">
  <div class="text-3xl mb-2">✂️</div>
  <div class="font-bold">Indexing & Slicing</div>
  <div class="text-sm text-gray-600"><code>name[0]</code> <code>name[1:4]</code></div>
</div>
<div class="concept-box text-center">
  <div class="text-3xl mb-2">🔧</div>
  <div class="font-bold">String Methods</div>
  <div class="text-sm text-gray-600"><code>.upper()</code> <code>.strip()</code> <code>.replace()</code></div>
</div>
<div class="concept-box text-center">
  <div class="text-3xl mb-2">✨</div>
  <div class="font-bold">f-strings</div>
  <div class="text-sm text-gray-600"><code>f"Hello, {name}!"</code></div>
</div>
</div>

<div class="mt-6 text-xl">
Today our programs learn to <strong>make decisions</strong>!
</div>

---
layout: center
---

# Today's Plan

<div class="grid grid-cols-2 gap-4 mt-6 text-left">
<div>

**Part 1 — if / else**
- Comparing values
- Running code only when a condition is true
- 🟢 Exercise

**Part 2 — elif**
- Checking multiple options in order
- 🟢 Exercise

**☕ Break**

</div>
<div>

**Part 3 — and, or, not**
- Combining conditions
- 🟢 Exercise

**Part 4 — Nested conditions**
- Conditions inside conditions
- 🟢 Exercise

**Common Mistakes · Mini Project · Homework**

</div>
</div>

---
layout: center
---

# <span class="part-badge">PART 1</span> &nbsp; if / else

---

# Making Decisions

Every day you make decisions based on conditions:

- **If** it is raining → take an umbrella
- **If** you are hungry → eat something
- **If** the light is red → stop

Python uses the same idea:

```python
temperature = 32

if temperature > 30:
    print("It is hot today!")
```

<div class="concept-box mt-4">
The code inside the <code>if</code> block only runs when the condition is <code>True</code>.<br>
If the condition is <code>False</code>, Python skips that block completely.
</div>

---

# The if / else Structure

```python
temperature = 32

if temperature > 30:
    print("It is hot today — wear light clothes!")
else:
    print("The weather is fine.")
```

<div class="warning-box mt-4">
⚠️ <strong>Indentation matters!</strong> The code inside <code>if</code> and <code>else</code> must be indented with 4 spaces (or one Tab). Python uses indentation to know what belongs inside the block.
</div>

```python
# This is WRONG — Python cannot tell what belongs to the if
if temperature > 30:
print("hot")      # IndentationError!

# This is RIGHT
if temperature > 30:
    print("hot")  # 4 spaces inside
```

---

# Comparison Operators

These operators compare two values and return `True` or `False`:

```python
age = 20

print(age == 20)   # True   — equal to
print(age != 20)   # False  — not equal to
print(age > 18)    # True   — greater than
print(age < 18)    # False  — less than
print(age >= 20)   # True   — greater than or equal to
print(age <= 20)   # True   — less than or equal to
```

<div class="mistake-box mt-4">
🚫 <strong>Common confusion:</strong><br>
<code>=</code> stores a value in a variable: <code>age = 20</code><br>
<code>==</code> checks if two values are equal: <code>age == 20</code><br>
Writing <code>if age = 20:</code> gives a <strong>SyntaxError</strong>.
</div>

---

# Comparing Strings

You can compare strings too:

```python
city = "Copenhagen"

if city == "Copenhagen":
    print("Welcome to Denmark!")

answer = input("Continue? yes or no: ")

if answer == "yes":
    print("Let's go!")
else:
    print("OK, stopping.")
```

<div class="warning-box mt-4">
⚠️ String comparison is <strong>case sensitive</strong>.<br>
<code>"yes"</code>, <code>"Yes"</code>, and <code>"YES"</code> are all different.<br>
Use <code>answer.lower() == "yes"</code> to accept any case.
</div>

---

# if / else — Full Example

```python
score = int(input("What did you score? "))

if score >= 50:
    print("You passed — well done!")
else:
    print("You did not pass — try again next time.")
```

**What happens step by step:**

1. Python reads the score from the user
2. It checks: is `score >= 50` True or False?
3. If True → run the first block
4. If False → skip to `else` and run that block
5. Only one block ever runs

---
layout: center
---

# 🟢 Exercise 1 — Weather Advice

<div class="exercise-box text-left mt-4">

Ask the user for today's temperature (as a number). Then print advice:

- If the temperature is above 25 → `"Great weather for a walk!"`
- Otherwise → `"Maybe stay indoors today."`

**Bonus:** also handle if it is below 0 — print `"It is freezing — wrap up!"`

```python
temperature = int(input("What is the temperature today? "))

# your code here
```

</div>

<div class="mt-4 text-gray-500 text-sm">⏱️ 8 minutes — try it yourself first!</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Exercise 1 — Solution

```python
temperature = int(input("What is the temperature today? "))

if temperature < 0:
    print("It is freezing — wrap up!")
elif temperature > 25:
    print("Great weather for a walk!")
else:
    print("Maybe stay indoors today.")
```

**Test it:**
```
What is the temperature today? 30   → Great weather for a walk!
What is the temperature today? 15   → Maybe stay indoors today.
What is the temperature today? -3   → It is freezing — wrap up!
```
<!-- solution:end -->

---
layout: center
---

# <span class="part-badge">PART 2</span> &nbsp; elif — Multiple Options

---

# Choosing Between Many Options

`elif` means "else if". It lets you check several conditions in order. Python stops at the **first one that is True**:

```python
score = 75

if score >= 90:
    print("Grade: A — Excellent!")
elif score >= 70:
    print("Grade: B — Good!")
elif score >= 50:
    print("Grade: C — Pass")
else:
    print("Grade: F — Not passed")

# Output: Grade: B — Good!
```

<div class="concept-box mt-4">
Think of <code>if / elif / else</code> like a series of gates.<br>
Python checks them from top to bottom and goes through the <strong>first gate that opens</strong>. All the rest are skipped.
</div>

---

# Order Matters!

Put the **most specific** condition first:

```python
age = 70

# WRONG — age 70 matches the first condition, never reaches senior
if age > 18:
    print("Adult")
elif age > 65:
    print("Senior")   # this never runs!

# RIGHT — check the more specific case first
if age > 65:
    print("Senior")
elif age > 18:
    print("Adult")
```

<div class="warning-box mt-4">
⚠️ When conditions overlap, always check the <strong>smaller/more specific</strong> range first.
</div>

---

# elif — Another Example

```python
hour = int(input("What hour is it? (0-23) "))

if hour < 12:
    print("Good morning!")
elif hour < 17:
    print("Good afternoon!")
elif hour < 21:
    print("Good evening!")
else:
    print("Good night!")
```

<div class="concept-box mt-4">
You can have as many <code>elif</code> blocks as you need.<br>
The <code>else</code> at the end is optional — it catches everything that did not match.
</div>

---
layout: center
---

# 🟢 Exercise 2 — Ticket Price

<div class="exercise-box text-left mt-4">

Write a program that asks for a person's age and prints the correct ticket price:

- Under 5 years old → **Free**
- 5 to 15 → **€5**
- 16 to 64 → **€12**
- 65 and over → **€7**

```python
age = int(input("How old are you? "))

# your code here
```

</div>

<div class="mt-4 text-gray-500 text-sm">⏱️ 8 minutes</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Exercise 2 — Solution

```python
age = int(input("How old are you? "))

if age < 5:
    print("Your ticket is free!")
elif age <= 15:
    print("Your ticket costs €5")
elif age <= 64:
    print("Your ticket costs €12")
else:
    print("Your ticket costs €7")
```

**Test it:**
```
How old are you? 3   → Your ticket is free!
How old are you? 12  → Your ticket costs €5
How old are you? 30  → Your ticket costs €12
How old are you? 70  → Your ticket costs €7
```
<!-- solution:end -->

---
layout: center
---

# ☕ Break — 10 minutes

<div class="break-box">
Back in 10 minutes
</div>

---
layout: center
---

# <span class="part-badge">PART 3</span> &nbsp; and, or, not

---

# Combining Conditions

Sometimes one condition is not enough. You can combine them:

```python
age        = 25
has_ticket = True

# AND — both must be True
if age >= 18 and has_ticket:
    print("You can enter!")

# OR — at least one must be True
if age >= 18 or has_ticket:
    print("Access allowed.")

# NOT — flips True to False, and False to True
is_closed = False

if not is_closed:
    print("The shop is open.")
```

---

# and, or, not — How They Work

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="concept-box">

**`and`** — both must be True

| A | B | Result |
|---|---|---|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

</div>
<div class="concept-box">

**`or`** — at least one True

| A | B | Result |
|---|---|---|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

</div>
<div class="concept-box">

**`not`** — flips it

| A | Result |
|---|---|
| True | **False** |
| False | **True** |

</div>
</div>

<div class="warning-box mt-4">
⚠️ When mixing <code>and</code> and <code>or</code>, use brackets to be clear:<br>
<code>if age >= 18 and (has_ticket or is_vip):</code>
</div>

---

# Everyday Examples

```python
day     = "Saturday"
weather = "sunny"

# Planning a picnic
if day == "Saturday" or day == "Sunday":
    if weather == "sunny":
        print("Perfect day for a picnic!")
    else:
        print("Weekend but not sunny — maybe next week.")
else:
    print("It is a weekday.")
```

```python
# Checking a username input
name = input("Your name: ")

if name != "" and len(name) >= 2:
    print(f"Hello, {name}!")
else:
    print("Please enter a valid name (at least 2 characters).")
```

---

# not — Practical Use

```python
items = []   # empty shopping list

if not items:
    print("Your shopping list is empty.")
else:
    print(f"You have {len(items)} items.")
```

```python
username = input("Username: ")
password = input("Password: ")

correct_user = "redi"
correct_pass = "python2026"

if username == correct_user and password == correct_pass:
    print("Welcome!")
else:
    print("Incorrect username or password.")
```

<div class="concept-box mt-4">
<code>not items</code> is True when the list is empty — this is a very common Python pattern.
</div>

---
layout: center
---

# 🟢 Exercise 3 — Weekend Planner

<div class="exercise-box text-left mt-4">

Ask the user two questions:
1. What day is it? (`"Saturday"` or `"Sunday"` or a weekday name)
2. Is the weather good? (`"yes"` or `"no"`)

Then print:
- Weekend **and** good weather → `"Great day for outdoor plans!"`
- Weekend **but** bad weather → `"Staying in this weekend."`
- Not a weekend → `"It is a weekday — back to work!"`

```python
day     = input("What day is it? ")
weather = input("Is the weather good? (yes/no) ").lower()

# your code here
```

</div>

<div class="mt-4 text-gray-500 text-sm">⏱️ 8 minutes</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Exercise 3 — Solution

```python
day     = input("What day is it? ").strip().title()
weather = input("Is the weather good? (yes/no) ").lower()

is_weekend = day == "Saturday" or day == "Sunday"

if is_weekend and weather == "yes":
    print("Great day for outdoor plans!")
elif is_weekend and weather != "yes":
    print("Staying in this weekend.")
else:
    print("It is a weekday — back to work!")
```

Storing the weekend check in a variable (`is_weekend`) makes the code easier to read.
<!-- solution:end -->

---
layout: center
---

# <span class="part-badge">PART 4</span> &nbsp; Nested Conditions

---

# Conditions Inside Conditions

You can put an `if` inside another `if`. This is called **nesting**:

```python
has_ticket = True
age        = 15

if has_ticket:
    print("You have a ticket — checking age...")
    if age >= 18:
        print("Access to all areas!")
    else:
        print("Access to family areas only.")
else:
    print("Sorry — no ticket, no entry.")
```

**Output:**
```
You have a ticket — checking age...
Access to family areas only.
```

---

# When to Use Nesting

Use nested conditions when the second check only makes sense if the first one passed:

```python
username = input("Username: ").strip()
password = input("Password: ").strip()

if username == "redi":
    if password == "python2026":
        print("Welcome!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")
```

<div class="warning-box mt-4">
⚠️ Each level of nesting adds 4 more spaces. Try not to nest more than 2 or 3 levels deep — it gets hard to read. Sometimes you can replace nesting with <code>and</code>:

```python
if username == "redi" and password == "python2026":
    print("Welcome!")
```
</div>

---

# Nesting vs and

Both approaches can work — choose the one that is clearer:

```python
# Using nesting — good when the second check depends on the first
if has_ticket:
    if age >= 18:
        print("Full access")
    else:
        print("Limited access")
else:
    print("Buy a ticket first")

# Using and — good when you just need both to be True
if has_ticket and age >= 18:
    print("Full access")
elif has_ticket and age < 18:
    print("Limited access")
else:
    print("Buy a ticket first")
```

---
layout: center
---

# 🟢 Exercise 4 — Coffee Order

<div class="exercise-box text-left mt-4">

Ask the user:
1. Do they want coffee? (`"yes"` or `"no"`)
2. If yes — do they want milk? (`"yes"` or `"no"`)

Print:
- Coffee with milk → `"Here is your flat white!"`
- Coffee without milk → `"Here is your black coffee!"`
- No coffee → `"No coffee for you — enjoy your water!"`

```python
wants_coffee = input("Would you like coffee? (yes/no) ").lower()

# your code here
```

</div>

<div class="mt-4 text-gray-500 text-sm">⏱️ 8 minutes</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Exercise 4 — Solution

```python
wants_coffee = input("Would you like coffee? (yes/no) ").lower()

if wants_coffee == "yes":
    wants_milk = input("Would you like milk? (yes/no) ").lower()
    if wants_milk == "yes":
        print("Here is your flat white!")
    else:
        print("Here is your black coffee!")
else:
    print("No coffee for you — enjoy your water!")
```
<!-- solution:end -->

---
layout: center
---

# ⚠️ Common Mistakes

---

# Common Mistakes — Part 1

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="mistake-box">

**1. `=` instead of `==`**
```python
# WRONG — SyntaxError
if name = "Sara":

# RIGHT
if name == "Sara":
```

</div>
<div class="mistake-box">

**2. Forgetting `int()` with input**
```python
# WRONG — compares string to number!
age = input("Age: ")
if age >= 18:      # TypeError

# RIGHT
age = int(input("Age: "))
if age >= 18:
```

</div>
<div class="mistake-box">

**3. Wrong elif order**
```python
# WRONG — age 70 never reaches senior
if age > 18:    print("adult")
elif age > 65:  print("senior")  # never runs

# RIGHT
if age > 65:    print("senior")
elif age > 18:  print("adult")
```

</div>
<div class="mistake-box">

**4. Case sensitivity with strings**
```python
# WRONG — misses "Yes", "YES"
if answer == "yes":

# RIGHT
if answer.lower() == "yes":
```

</div>
</div>

---

# Common Mistakes — Part 2

<div class="mistake-box mt-4">

**5. Forgetting the colon `:`**
```python
# WRONG — SyntaxError
if score > 50
    print("Passed!")

# RIGHT
if score > 50:
    print("Passed!")
```

</div>

<div class="mistake-box mt-4">

**6. Wrong indentation breaks the logic**
```python
temperature = 35

if temperature > 30:
    print("It is hot.")
print("Drink water.")   # This always runs — it is NOT inside the if!
else:
    print("Nice weather!")   # SyntaxError — else has no if!
```

```python
# RIGHT
if temperature > 30:
    print("It is hot.")
    print("Drink water.")   # Now this is inside the if
else:
    print("Nice weather!")
```

</div>

---
layout: center
---

# 🛠️ Mini Project — Smart Quiz

<div class="exercise-box text-left mt-4">

Build a 3-question quiz. Ask each question, check the answer, and keep a score. At the end, print the score and a message based on how they did.

```python
score = 0

answer1 = input("What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong — the answer is Paris.")

answer2 = input("How many days are in a week? ").strip()
if answer2 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong — the answer is 7.")

answer3 = input("What colour do you get mixing red and blue? ").strip().lower()
if answer3 == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong — the answer is purple.")

print(f"\nYou scored {score} out of 3.")
if score == 3:
    print("Perfect score — amazing!")
elif score >= 2:
    print("Well done!")
else:
    print("Keep practising!")
```

</div>

---
layout: center
---

# 📋 What We Learned Today

<div class="grid grid-cols-2 gap-4 mt-6">
<div class="concept-box">

**if / elif / else**
- Run code only when a condition is True
- Use `elif` for multiple options
- `else` catches anything that did not match

</div>
<div class="concept-box">

**Comparison operators**
- `==` `!=` `>` `<` `>=` `<=`
- Always `==` for comparing, never `=`
- Works on numbers and strings

</div>
<div class="concept-box">

**and, or, not**
- `and` — both must be True
- `or` — at least one must be True
- `not` — flips True to False

</div>
<div class="concept-box">

**Nested conditions**
- if inside an if
- Use when the second check depends on the first
- Don't nest too deep — use `and` instead when possible

</div>
</div>

---
layout: center
---

# 📚 Homework

---

# Homework — Beginner (1–5)

<div class="exercise-box mt-4">

**1. Grade Calculator**
Ask for a score (0–100). Print:
- 90 and above → `"Grade A"`
- 75 to 89 → `"Grade B"`
- 60 to 74 → `"Grade C"`
- 50 to 59 → `"Grade D"`
- Below 50 → `"Grade F"`

**2. Even or Odd**
Ask for a number. Print whether it is even or odd. Hint: use `%` — if `number % 2 == 0` it is even.

**3. Bigger Number**
Ask for two numbers. Print which one is bigger, or say they are equal.

**4. Time of Day Greeting**
Ask for the current hour (0–23). Print `"Good morning!"` (before 12), `"Good afternoon!"` (12–17), or `"Good evening!"` (after 17).

**5. Favourite Season**
Ask for a month number (1–12). Print the season:
- December, January, February → Winter
- March, April, May → Spring
- June, July, August → Summer
- September, October, November → Autumn

</div>

---

# Homework — Intermediate (6–10)

<div class="exercise-box mt-4">

**6. Number Classifier**
Ask for a number. Print all that apply:
- Positive, negative, or zero
- Even or odd
- Divisible by 3 (yes or no)

**7. BMI Calculator**
Ask for weight in kg and height in metres. Calculate BMI (`weight / height ** 2`).
Print: `"Underweight"` (below 18.5), `"Normal"` (18.5–24.9), `"Overweight"` (25 or above).

**8. Simple Calculator**
Ask for two numbers and an operation (`+`, `-`, `*`, `/`). Print the result. Handle division by zero — print an error message instead of crashing.

**9. Vending Machine**
Ask for a product name and the amount of money inserted.
- Cola → €1.50, Water → €1.00, Juice → €2.00
- If money is enough → print the change
- If not enough → print how much more is needed
- If product not found → print an error message

**10. Login Checker**
Ask for a username and password. Store the correct ones as variables. If both match → `"Welcome!"`. If the username matches but the password is wrong → `"Wrong password."`. Otherwise → `"User not found."`.

</div>

---

# 📅 Next Week — Loops

<div class="concept-box mt-6 text-center">
Right now your program runs each line once.<br>
Next week you will make it <strong>repeat things automatically</strong>.
</div>

<div class="grid grid-cols-3 gap-4 mt-6">
<div class="exercise-box text-center">
  <div class="text-3xl mb-2">🔁</div>
  <div class="font-bold">for loop</div>
  <div class="text-sm text-gray-600 mt-1">Do something for every item in a list</div>
</div>
<div class="exercise-box text-center">
  <div class="text-3xl mb-2">⏳</div>
  <div class="font-bold">while loop</div>
  <div class="text-sm text-gray-600 mt-1">Keep going until a condition is met</div>
</div>
<div class="exercise-box text-center">
  <div class="text-3xl mb-2">🎯</div>
  <div class="font-bold">range()</div>
  <div class="text-sm text-gray-600 mt-1">Count from any number to any number</div>
</div>
</div>

<div class="warning-box mt-6 text-center">
💡 How would you print "Hello" 100 times right now? Next week — one line of code.
</div>

---
layout: center
---

# Great work today! 🎉

<div class="text-xl text-gray-600 mt-4">Your programs can now think and make decisions</div>

<div class="grid grid-cols-3 gap-4 mt-8">
<div class="concept-box text-center">
  <div class="text-3xl">🚦</div>
  <div class="font-bold mt-2">if / elif / else</div>
  <div class="text-sm text-gray-500 mt-1">Control the flow</div>
</div>
<div class="concept-box text-center">
  <div class="text-3xl">🔗</div>
  <div class="font-bold mt-2">and / or / not</div>
  <div class="text-sm text-gray-500 mt-1">Combine conditions</div>
</div>
<div class="concept-box text-center">
  <div class="text-3xl">🪆</div>
  <div class="font-bold mt-2">Nesting</div>
  <div class="text-sm text-gray-500 mt-1">Conditions inside conditions</div>
</div>
</div>

<div class="mt-10 text-gray-500">
  See you next week! 👋
</div>
