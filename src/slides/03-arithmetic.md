---
theme: ../../themes/clio
title: Arithmetic and User Input
info: |
  Intro to Programming
  ReDI School 2026
drawings:
  persist: false
transition: slide-left
preloadImages: false
mdc: true
class: foundation-slide lesson-overview-slide
---

<div class="eyebrow">Python · Lesson 3</div>

# What will we cover?

<p class="lesson-overview-intro">Numbers, maths, reading from the keyboard — and how Python handles the types when you combine them.</p>

<div class="lesson-overview-path">
  <section><b>1</b><span><strong>Arithmetic operators</strong>+, -, *, /, //, %, ** and order of operations</span></section>
  <section><b>2</b><span><strong>abs() and round()</strong>Two built-ins you will use in almost every calculator</span></section>
  <section><b>3</b><span><strong>input()</strong>Read text from the keyboard — and why it is always a string</span></section>
  <section><b>4</b><span><strong>Type conversion</strong>int(), float(), str(), bool() — and common type errors</span></section>
</div>

<p class="lesson-overview-goal"><strong>Goal:</strong> build a personal calculator that reads two numbers from the keyboard and prints all the arithmetic results.</p>

---
class: foundation-slide
---

<div class="eyebrow">Arithmetic</div>

# Arithmetic operators

<p class="foundation-intro">Python can do maths. Use these seven operators on any numbers or numeric variables.</p>

<div class="op-grid">
  <div class="op-row op-header">
    <span>Operator</span><span>Name</span><span>Example</span><span>Result</span>
  </div>
  <div class="op-row"><code>+</code><span>Addition</span><code>10 + 3</code><span>13</span></div>
  <div class="op-row"><code>-</code><span>Subtraction</span><code>10 - 3</code><span>7</span></div>
  <div class="op-row"><code>*</code><span>Multiplication</span><code>10 * 3</code><span>30</span></div>
  <div class="op-row"><code>/</code><span>Division</span><code>10 / 3</code><span>3.333… (always float)</span></div>
  <div class="op-row op-highlight"><code>//</code><span>Integer division</span><code>10 // 3</code><span>3 (whole part only)</span></div>
  <div class="op-row op-highlight"><code>%</code><span>Remainder (modulo)</span><code>10 % 3</code><span>1 (10 = 3×3 + 1)</span></div>
  <div class="op-row"><code>**</code><span>Power</span><code>2 ** 8</code><span>256</span></div>
</div>

<p class="foundation-note"><code>//</code> gives the <strong>whole number</strong> part of a division — useful for splitting things evenly. <code>%</code> gives the <strong>remainder</strong> — useful for checking odd/even.</p>

---
class: python-code-slide
---

<div class="eyebrow">Arithmetic</div>

# Arithmetic in action

<div class="code-and-output">
  <section class="code-panel">

```python
# Shopping total
price    = 2.99
quantity = 4
total    = price * quantity
print(total)          # 11.96

# Age in days
age_years = 25
age_days  = age_years * 365
print(age_days)       # 9125

# Is a number even? remainder is 0 if yes
number = 8
print(number % 2)     # 0 — even!
number = 7
print(number % 2)     # 1 — odd!

# Update a variable with itself
score = 10
score = score + 5     # add 5
print(score)          # 15
score += 3            # shortcut for score = score + 3
print(score)          # 18
```

  </section>
  <section class="output-panel">
    <span class="object-label">Shortcuts</span>
    <h2>+=  -=  *=  /=</h2>
    <p>Instead of <code>score = score + 3</code> you can write <code>score += 3</code>. Works with all four main operators.</p>

```python
x = 10
x += 5    # x is now 15
x -= 2    # x is now 13
x *= 2    # x is now 26
x /= 4    # x is now 6.5
```

    <p class="output-note">These are just shortcuts — they do not change what the operation does.</p>
  </section>
</div>

---
class: foundation-slide
---

<div class="eyebrow">Arithmetic</div>

# Order of operations

<p class="foundation-intro">Python follows the same maths rules you learned in school. <strong>Brackets run first, then powers, then multiply and divide, then add and subtract.</strong></p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">Without brackets</span>
    <h2>Default order</h2>

```python
print(2 + 3 * 4)      # 14
# multiply first: 3*4=12, then 2+12=14

print(10 - 2 ** 3)    # 2
# power first: 2**3=8, then 10-8=2

print(10 / 2 + 3)     # 8.0
# divide first: 10/2=5, then 5+3=8
```

  </section>
  <section class="definition-panel">
    <span class="object-label">With brackets</span>
    <h2>Brackets change everything</h2>

```python
print((2 + 3) * 4)    # 20
# brackets first: 2+3=5, then 5*4=20

# Average of three scores — MUST use brackets!
score1 = 80
score2 = 90
score3 = 70

wrong   = score1 + score2 + score3 / 3  # 193.3!
correct = (score1 + score2 + score3) / 3 # 80.0
print(correct)
```

  </section>
</div>

<p class="foundation-note">Forgetting brackets around an average is one of the most common bugs in beginner code. When in doubt — add brackets to make your intention clear.</p>

---
class: python-code-slide
---

<div class="eyebrow">Arithmetic · Built-ins</div>

# abs() and round()

<div class="code-and-output">
  <section class="code-panel">

```python
# abs() — absolute value, always positive
print(abs(-15))           # 15
print(abs(7))             # 7

temperature = -8
print(abs(temperature))   # 8  ("8 degrees below zero")

# round() — round to nearest whole number
print(round(3.7))         # 4
print(round(3.2))         # 3

# round(number, digits) — keep decimal places
print(round(9.999, 2))    # 10.0
print(round(2.675, 2))    # 2.68

# Practical: price after discount
price    = 49.99
discount = 0.15
final    = round(price * (1 - discount), 2)
print(final)              # 42.49
```

  </section>
  <section class="output-panel">
    <span class="object-label">abs()</span>
    <h2>Remove the minus sign</h2>
    <p>Use when you care about the <em>size</em> of a difference, not its direction. Temperature changes, balance differences, distances.</p>
    <span class="object-label" style="margin-top:0.7rem;display:block">round()</span>
    <h2>Control decimal places</h2>
    <p>The second argument is optional. Without it, rounds to the nearest whole number. With it, keeps that many decimal places.</p>
    <p class="output-note">Always <code>round()</code> money calculations before displaying them — floating point arithmetic can give results like <code>2.9999999999</code>.</p>
  </section>
</div>

---
class: foundation-slide
---

<div class="eyebrow">Real world · Arithmetic</div>

# Arithmetic powers every app

<p class="foundation-intro">Every time you pay online, Python-style arithmetic is running behind the scenes.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">E-commerce checkout</span>
    <h2>Price × quantity − discount + shipping</h2>

```python
item_price   = 29.99
quantity     = 3
discount_pct = 10       # 10%
shipping     = 4.90

subtotal = item_price * quantity
discount = subtotal * (discount_pct / 100)
total    = round(subtotal - discount + shipping, 2)
print(f"Total: €{total}")   # Total: €85.87
```

  </section>
  <section class="definition-panel">
    <span class="object-label">Ride-sharing fare</span>
    <h2>Base + distance × rate × surge</h2>

```python
base_fare   = 2.50
distance_km = 8.3
rate_per_km = 1.20
surge       = 1.5

price = (base_fare + distance_km * rate_per_km) * surge
price = round(price, 2)
print(f"Fare: €{price}")    # Fare: €18.69
```

  </section>
</div>

---
class: exercise-slide
---

<div class="eyebrow">Exercise · Arithmetic</div>

# Maths with Python

<div class="py-exercise-layout">
  <div class="py-exercise-steps">
    <div class="py-exercise-step"><b>1</b><span>You buy <strong>3 coffees at €2.50 each</strong>. What is the total? Use <code>round()</code>.</span></div>
    <div class="py-exercise-step"><b>2</b><span>You have <strong>€20</strong>. How much <strong>change</strong> do you get?</span></div>
    <div class="py-exercise-step"><b>3</b><span><strong>7 students, 30 biscuits</strong>. How many does each get? How many are left over? Use <code>//</code> and <code>%</code>.</span></div>
    <div class="py-exercise-step"><b>4</b><span>What is <strong>2 to the power of 8</strong>?</span></div>
    <div class="py-exercise-step"><b>5</b><span>Temperature is <strong>−12°C</strong>. Use <code>abs()</code> to print "12 degrees below zero".</span></div>
    <div class="py-exercise-done"><strong>Done when:</strong> all five values print correctly.</div>
  </div>
  <div class="py-exercise-starter">

```python
# Exercise — Maths with Python

coffee_price = 2.50
quantity     = 3

# 1. Total


# 2. Change from €20


# 3. Biscuits — each student gets? leftover?
students = 7
biscuits = 30


# 4. 2 to the power of 8


# 5. Temperature
temp = -12
```

  </div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

<div class="eyebrow">Solution · Maths with Python</div>

# Maths with Python — solution

```python
# 1. Total cost of coffees
coffee_price = 2.50
quantity     = 3
total        = round(coffee_price * quantity, 2)
print(total)                             # 7.5

# 2. Change from €20
change = 20 - total
print(change)                            # 12.5

# 3. Biscuits per student and leftovers
students = 7
biscuits = 30
each     = biscuits // students
leftover = biscuits % students
print(each, leftover)                    # 4, 2

# 4. Power of 2
print(2 ** 8)                            # 256

# 5. abs() for temperature
temp = -12
print(abs(temp), "degrees below zero")  # 12 degrees below zero
```
<!-- solution:end -->

---
class: python-code-slide
---

<div class="eyebrow">User input</div>

# input()

<div class="code-and-output">
  <section class="code-panel">

```python
# Ask for the user's name
name = input("What is your name? ")
print("Hello, " + name + "!")

# Ask for their city
city = input("Where are you from? ")
print("Nice! " + city + " is a great city.")

# Use f-strings for cleaner output
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1}.")
```

  </section>
  <section class="output-panel">
    <span class="object-label">What happens when you run it</span>

```text
What is your name? Sara
Hello, Sara!
Where are you from? Berlin
Nice! Berlin is a great city.
How old are you? 25
Next year you will be 26.
```

    <p class="output-note"><code>input()</code> pauses the program and waits for the user to press Enter. Whatever they typed is returned as a string. Always add a space at the end of the prompt text so the cursor is not right against it.</p>
  </section>
</div>

---
class: foundation-slide
---

<div class="eyebrow">User input</div>

# input() always returns a string

<p class="foundation-intro">Even if the user types a number, <code>input()</code> gives you a <strong>string</strong>. You must convert it before doing any maths.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">The crash</span>
    <h2>TypeError</h2>

```python
# ✗ This crashes!
age = input("How old are you? ")
print(age + 1)
# TypeError: can only concatenate
# str (not "int") to str
```

    <p>Python cannot add a string and a number. <code>input()</code> gave you the string <code>"25"</code>, not the number <code>25</code>.</p>
  </section>
  <section class="definition-panel">
    <span class="object-label">The fix</span>
    <h2>Wrap with int() or float()</h2>

```python
# ✓ Convert while reading
age = int(input("How old are you? "))
print(age + 1)          # 26 ✓

# ✓ Or convert after
age_text = input("How old are you? ")
age      = int(age_text)
print(age + 1)          # 26 ✓

# For decimal numbers
height = float(input("Height in metres? "))
print(height * 100, "cm")
```

  </section>
</div>

<p class="foundation-note">Always ask yourself: <strong>"What type does input() give me, and what type do I need?"</strong> If you need to do maths — convert it.</p>

---
class: foundation-slide
---

<div class="eyebrow">User input · Examples</div>

# input() in practice

<p class="foundation-intro">Here are two small programs that use <code>input()</code> — one with text, one with numbers.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">Text — no conversion needed</span>
    <h2>Greeting program</h2>

```python
name = input("What is your name? ")
city = input("Where are you from? ")

print("Hello, " + name + "!")
print(city + " sounds like a great place.")
```

  </section>
  <section class="definition-panel">
    <span class="object-label">Numbers — must convert</span>
    <h2>Coffee calculator</h2>

```python
price    = float(input("Price per coffee (€): "))
quantity = int(input("How many coffees? "))

total = round(price * quantity, 2)
print(f"Total: €{total}")
```

  </section>
</div>

<p class="foundation-note">The rule is simple: if you are going to do maths with the value, wrap <code>input()</code> with <code>int()</code> or <code>float()</code>. If you only need text, leave it as is.</p>

---
class: python-code-slide
---

<div class="eyebrow">Type conversion</div>

# Converting between types

<div class="code-and-output">
  <section class="code-panel">

```python
# str → int
age = int("25")
print(age + 1)            # 26

# str → float
price = float("9.99")
print(price * 2)          # 19.98

# int/float → str  (needed before joining with +)
age = 25
print("I am " + str(age) + " years old")

# int → float and back
x = float(5)              # 5.0
y = int(3.9)              # 3  ← cut off, NOT rounded!

# Anything → bool
print(bool(1))            # True
print(bool(0))            # False
print(bool("hello"))      # True
print(bool(""))           # False  ← empty string is False
```

  </section>
  <section class="output-panel">
    <span class="object-label">The four converters</span>
    <div class="converter-list">
      <div class="converter"><code>int()</code><span>To a whole number. Cuts the decimal — does not round. Fails on non-numeric strings.</span></div>
      <div class="converter"><code>float()</code><span>To a decimal number.</span></div>
      <div class="converter"><code>str()</code><span>To text. Always works — every value has a string representation.</span></div>
      <div class="converter"><code>bool()</code><span>To True/False. Zero, empty string, and <code>None</code> are False. Everything else is True.</span></div>
    </div>
  </section>
</div>

---
class: foundation-slide
---

<div class="eyebrow">Type conversion</div>

# Common type errors and fixes

<div class="error-grid">
  <section class="error-panel">
    <span class="object-label error-label">TypeError — mixing str and int</span>
    <h2>Cannot add string and number</h2>

```python
# ✗ Crashes
name = "Sara"
age  = 25
print(name + age)

# ✓ Fix — convert age to string
print(name + " is " + str(age))    # Sara is 25
# ✓ Or use a comma (no conversion needed)
print(name, "is", age)             # Sara is 25
```

  </section>
  <section class="error-panel">
    <span class="object-label error-label">ValueError — invalid conversion</span>
    <h2>Cannot convert letters to a number</h2>

```python
# ✗ Crashes
score = "90"
print(score + 10)          # TypeError!

# ✓ Fix — convert score to int
print(int(score) + 10)     # 100

# ✗ Also crashes
age = int("twenty five")   # ValueError!

# ✓ Only numeric strings work
age = int("25")            # 25 ✓
```

  </section>
</div>

<p class="foundation-note"><strong>TypeError</strong> — you mixed incompatible types; check and add a conversion. <strong>ValueError</strong> — the string you tried to convert is not a valid number.</p>

---
class: foundation-slide
---

<div class="eyebrow">Type conversion · Why it matters</div>

# The wrong type causes crashes

<p class="foundation-intro">Python cannot guess what you mean. If you try to add a string and a number it stops immediately. The fix is always the same — convert first.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">The problem</span>
    <h2>input() gives you text</h2>

```python
age    = input("How old are you? ")
# age is the string "25", not the number 25

print(age + 1)       # TypeError — crashes!
print(age * 2)       # prints "2525" — wrong!
```

    <p>When you multiply a string by a number, Python repeats the text. That is not what you want.</p>
  </section>
  <section class="definition-panel">
    <span class="object-label">The fix</span>
    <h2>Convert to the right type</h2>

```python
age    = int(input("How old are you? "))
# now age is the number 25

print(age + 1)       # 26 ✓
print(age * 2)       # 50 ✓

height = float(input("Height in metres? "))
print(height * 100)  # converts to cm ✓
```

  </section>
</div>

---
class: exercise-slide
---

<div class="eyebrow">Exercise · User input</div>

# User input and conversion

<div class="py-exercise-layout">
  <div class="py-exercise-steps">
    <div class="py-exercise-step"><b>1</b><span>Ask for the user's <strong>name</strong> with <code>input()</code>. Print "Hello, [name]!"</span></div>
    <div class="py-exercise-step"><b>2</b><span>Ask for their <strong>age</strong> (as int). Print how old they will be in 10 years.</span></div>
    <div class="py-exercise-step"><b>3</b><span>Ask for a <strong>price</strong> (as float). Print the price with <strong>21% VAT</strong> added, rounded to 2 decimal places.</span></div>
    <div class="py-exercise-step"><b>4</b><span>Ask for two numbers. Print their <strong>sum, difference, product, and quotient</strong>.</span></div>
    <div class="py-exercise-done"><strong>Done when:</strong> your program runs, accepts input, and prints all results without crashing.</div>
  </div>
  <div class="py-exercise-starter">

```python
# Exercise — User Input & Conversion

# 1. Name greeting
name =
print()

# 2. Age in 10 years
age =
print()

# 3. Price with VAT
price =
vat_rate = 0.21
print()

# 4. Two numbers
a =
b =
print("Sum:", )
print("Difference:", )
print("Product:", )
print("Quotient:", )
```

  </div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

<div class="eyebrow">Solution · User input</div>

# User input and conversion — solution

```python
# 1. Name greeting
name = input("What is your name? ")
print("Hello, " + name + "!")

# 2. Age in 10 years
age = int(input("How old are you? "))
print("In 10 years you will be", age + 10)

# 3. Price with VAT
price    = float(input("Enter a price (€): "))
vat_rate = 0.21
total    = round(price * (1 + vat_rate), 2)
print(f"Price with VAT: €{total}")

# 4. Two numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print("Sum:",        round(a + b, 2))
print("Difference:", round(a - b, 2))
print("Product:",    round(a * b, 2))
print("Quotient:",   round(a / b, 2))
```
<!-- solution:end -->

---
class: knowledge-check-slide
---

<div class="eyebrow">Common mistakes</div>

# Watch out for these

<ol class="knowledge-questions">
  <li><b>1</b><span><strong>Using input() result as a number without converting</strong><br><code>age = input("Age: ")</code> → <code>age + 1</code> crashes. Always wrap with <code>int()</code> or <code>float()</code>.</span></li>
  <li><b>2</b><span><strong>Forgetting brackets in averages</strong><br><code>score1 + score2 + score3 / 3</code> only divides the last number. Write <code>(score1 + score2 + score3) / 3</code>.</span></li>
  <li><b>3</b><span><strong>Expecting int() to round</strong><br><code>int(3.9)</code> gives <code>3</code>, not <code>4</code>. Use <code>round()</code> when you want rounding, <code>int()</code> only cuts the decimal.</span></li>
  <li><b>4</b><span><strong>Capitalised built-ins</strong><br><code>Round()</code>, <code>Abs()</code>, <code>Int()</code> all crash with NameError. Python built-ins are always lowercase.</span></li>
</ol>

---
class: knowledge-check-slide homework-slide
---

<div class="eyebrow">Homework · Lesson 3</div>

# For next class

<ol class="knowledge-questions">
  <li><b>1</b><span><strong>All operators</strong> — create two variables <code>a = 17</code>, <code>b = 5</code>. Print the result of all seven operators (+, -, *, /, //, %, **) with a label for each.</span></li>
  <li><b>2</b><span><strong>Average calculator</strong> — create three test scores and calculate the average using brackets. Round to 1 decimal place.</span></li>
  <li><b>3</b><span><strong>abs() practice</strong> — create two temperature variables (e.g. yesterday = -3, today = 7). Print the difference using abs() so it is always positive.</span></li>
  <li><b>4</b><span><strong>Discount calculator</strong> — ask the user for a price and a discount percentage. Print the original price, the discount amount, and the final price. Round everything to 2 decimal places.</span></li>
  <li><b>5</b><span><strong>BMI calculator</strong> — ask the user for weight (kg) and height (m). Calculate BMI as <code>weight / height ** 2</code>. Print the result rounded to 1 decimal place.</span></li>
  <li><b>6</b><span><strong>Seconds converter</strong> — ask for a number of seconds. Print how many full hours, minutes, and leftover seconds that is. Use <code>//</code> and <code>%</code>.</span></li>
  <li><b>7</b><span><strong>Personal calculator</strong> — ask the user for two numbers. Print their sum, difference, product, quotient (rounded to 2 dp), integer division, remainder, and the first number to the power of the second.</span></li>
</ol>

---
layout: center
class: finish-slide
---

<div class="eyebrow">Lesson complete</div>

# You can do maths with Python

<div class="recap">
  <span><b>1</b> +  -  *  /  //  %  **</span>
  <span><b>2</b> Order of operations</span>
  <span><b>3</b> abs() · round()</span>
  <span><b>4</b> input() always returns str</span>
  <span><b>5</b> int() · float() · str() · bool()</span>
</div>

<p class="lead">Next lesson: strings, string methods, and f-strings.</p>

<style>
.python-code-slide {
  padding: 0.8rem 2.4rem;
}

.python-code-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 2rem;
  letter-spacing: 0;
  margin: 0.15rem 0 0.55rem;
}

.code-and-output {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: 1.15fr 0.85fr;
}

.code-panel .slidev-code-wrapper {
  margin: 0;
}

.output-panel {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  padding: 0.85rem 1rem;
}

.output-panel h2 {
  font-size: 0.95rem;
  margin: 0.7rem 0 0.2rem;
}

.output-panel h2:first-of-type {
  margin-top: 0;
}

.output-panel p {
  color: var(--lesson-muted);
  font-size: 0.82rem;
  line-height: 1.4;
  margin: 0.2rem 0 0.5rem;
}

.output-panel .slidev-code-wrapper {
  margin: 0.3rem 0;
}

.output-note {
  background: rgb(192 132 252 / 16%);
  border-left: 3px solid var(--lesson-blue);
  color: var(--lesson-ink) !important;
  font-size: 0.78rem !important;
  line-height: 1.35 !important;
  margin-top: 0.6rem !important;
  padding: 0.3rem 0.5rem;
}

.op-grid {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  overflow: hidden;
}

.op-row {
  align-items: center;
  border-bottom: 1px solid var(--lesson-border);
  display: grid;
  font-size: 0.82rem;
  gap: 0;
  grid-template-columns: 3rem 8rem 10rem 1fr;
  padding: 0.3rem 0.8rem;
}

.op-row:last-child {
  border-bottom: none;
}

.op-header {
  background: rgb(192 132 252 / 14%);
  color: var(--lesson-muted);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.op-highlight {
  background: rgb(192 132 252 / 8%);
}

.op-row code {
  color: var(--lesson-blue);
  font-size: 0.9rem;
  font-weight: 700;
}

.op-row span {
  color: var(--lesson-muted);
}

.converter-list {
  display: grid;
  gap: 0.4rem;
  margin-top: 0.3rem;
}

.converter {
  background: rgb(192 132 252 / 12%);
  border-left: 3px solid var(--lesson-blue);
  display: grid;
  gap: 0.25rem;
  padding: 0.35rem 0.6rem;
}

.converter code {
  color: var(--lesson-blue);
  font-size: 0.9rem;
  font-weight: 700;
}

.converter span {
  color: var(--lesson-muted);
  font-size: 0.76rem;
  line-height: 1.3;
}

.error-grid {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: 1fr 1fr;
}

.error-panel {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  padding: 0.9rem 1rem;
}

.error-panel .slidev-code-wrapper {
  margin: 0.3rem 0;
}

.error-panel h2 {
  font-size: 0.95rem;
  margin: 0.3rem 0 0.4rem;
}

.error-panel p {
  color: var(--lesson-muted);
  font-size: 0.78rem;
  line-height: 1.35;
  margin: 0.25rem 0;
}

.error-label {
  color: #ff9a9a !important;
}

.py-exercise-layout {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr);
}

.py-exercise-steps {
  display: grid;
  gap: 0.35rem;
}

.py-exercise-step {
  align-items: start;
  border-bottom: 1px solid var(--lesson-border);
  display: grid;
  font-size: 0.72rem;
  gap: 0.5rem;
  grid-template-columns: 1.5rem 1fr;
  padding: 0.2rem 0.15rem 0.35rem;
}

.py-exercise-step b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: inline-flex;
  height: 1.5rem;
  justify-content: center;
  width: 1.5rem;
}

.py-exercise-done {
  background: rgb(192 132 252 / 16%);
  border-left: 4px solid var(--lesson-blue);
  font-size: 0.72rem;
  margin-top: 0.2rem;
  padding: 0.4rem 0.6rem;
}

.py-exercise-starter .slidev-code-wrapper {
  margin: 0;
}

.py-exercise-starter pre {
  font-size: 0.6rem;
  line-height: 1.3;
}

.homework-slide {
  padding: 0.9rem 2.4rem;
}

.homework-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 1.85rem;
  letter-spacing: 0;
  margin: 0.1rem 0 0.45rem;
}

.knowledge-questions-wide li {
  padding: 0.4rem 0.3rem !important;
}

.knowledge-questions-wide .slidev-code-wrapper {
  margin: 0.3rem 0 0;
}

.bug-label {
  color: #ff9a9a !important;
}

.recap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  margin-top: 2.5rem;
}
</style>
