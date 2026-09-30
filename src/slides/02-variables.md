---
theme: ../../themes/clio
title: Variables and Data Types
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

<div class="eyebrow">Python · Lesson 2</div>

# What will we cover?

<p class="lesson-overview-intro">We start with your first Python commands, then build up to storing, checking, and converting values.</p>

<div class="lesson-overview-path">
  <section><b>1</b><span><strong>print() and comments</strong>Display output and annotate your code</span></section>
  <section><b>2</b><span><strong>Variables</strong>Store values and name them</span></section>
  <section><b>3</b><span><strong>Data types</strong>str, int, float, bool — and how to check them</span></section>
  <section><b>4</b><span><strong>Type conversion and input</strong>Convert between types and read from the keyboard</span></section>
</div>

<p class="lesson-overview-goal"><strong>Goal:</strong> write a program that stores personal information in variables and prints a formatted profile.</p>

---
class: foundation-slide
---

<div class="eyebrow">Python basics</div>

# print()

<p class="foundation-intro"><code>print()</code> displays something on the screen. You will use it in almost every program.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">What it does</span>
    <h2>Displays output</h2>
    <p>Whatever you put inside the parentheses appears on the screen when the program runs. Python processes each <code>print()</code> line in order, top to bottom.</p>
    <p>You can print text, numbers, variables, or a mix of all three.</p>
  </section>
  <section class="definition-panel">
    <span class="object-label">Syntax</span>
    <h2>Text needs quotes</h2>

```python
print("Hello, World!")
print("My name is Sara")
print(42)
print(3.14)
print("I am", 25, "years old")
```

  </section>
</div>

<p class="foundation-note">Use <strong>double</strong> quotes <code>"..."</code> or <strong>single</strong> quotes <code>'...'</code> around text — both work. Numbers go in without quotes.</p>

---
class: python-code-slide
---

<div class="eyebrow">Python basics</div>

# print() in action

<div class="code-and-output">
  <section class="code-panel">

```python
print("Hello, World!")
print("My name is Sara")
print("I am", 25, "years old")

# Print a blank line
print()

# Numbers — no quotes needed
print(42)
print(3.14)
```

  </section>
  <section class="output-panel">
    <span class="object-label">Output</span>

```text
Hello, World!
My name is Sara
I am 25 years old

42
3.14
```

<p>Each <code>print()</code> starts on a new line. A <code>print()</code> with nothing inside prints a blank line.</p>
<p>Commas inside <code>print()</code> add a space between the values automatically.</p>
  </section>
</div>

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

.output-panel p {
  color: var(--lesson-muted);
  font-size: 0.82rem;
  line-height: 1.4;
  margin: 0.2rem 0 0.5rem;
}
</style>

---
class: foundation-slide
---

<div class="eyebrow">Python basics</div>

# Comments

<p class="foundation-intro">A comment is a note written for the programmer. Python ignores everything after a <code>#</code> symbol on that line.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">Why use them</span>
    <h2>Explain your thinking</h2>
    <p>Comments do not affect what the program does. They help you and others understand <em>why</em> the code is written the way it is.</p>
    <p>Professional code has comments. Get in the habit early.</p>
  </section>
  <section class="definition-panel">
    <span class="object-label">Syntax</span>
    <h2>Start with #</h2>

```python
# This whole line is a comment
print("Hello!")   # comment at end of line

# Describe what the next line does
print("My name is Sara")

# You can comment out code to disable it
# print("This line will not run")
```

  </section>
</div>

---
class: foundation-slide
---

<div class="eyebrow">Variables</div>

# What is a variable?

<p class="foundation-intro">A <strong>variable</strong> is a named box that stores a value. You give it a name, and Python remembers the value for you.</p>

<div class="var-compare">
  <section class="var-compare-panel">
    <span class="object-label">Without a variable</span>

```python
print("Sara")
print("Sara")
print("Sara")
```

<p class="var-compare-note">You repeat the value every time. If it changes, you must update every single occurrence.</p>
  </section>
  <section class="var-compare-panel var-compare-better">
    <span class="object-label">With a variable</span>

```python
name = "Sara"

print(name)
print(name)
print(name)
```

<p class="var-compare-note">Change the value in one place — it updates everywhere automatically.</p>
  </section>
</div>

<p class="foundation-note">Think of a variable as a sticky note: you write a label on it and stick a value underneath. Any time you need the value, just use the label.</p>

<style>
.var-compare {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr 1fr;
  margin-top: 0.5rem;
}

.var-compare-panel {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  padding: 0.9rem 1rem;
}

.var-compare-better {
  border-color: var(--lesson-blue);
}

.var-compare-panel .slidev-code-wrapper {
  margin: 0.4rem 0;
}

.var-compare-note {
  color: var(--lesson-muted);
  font-size: 0.8rem;
  line-height: 1.35;
  margin: 0;
}
</style>

---
class: foundation-slide
---

<div class="eyebrow">Variables</div>

# Creating variables

<p class="foundation-intro">Write the name, then <code>=</code>, then the value. Python creates the variable and remembers the value.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">Examples</span>
    <h2>All four types</h2>

```python
name       = "Sara"    # text
age        = 25        # whole number
height     = 1.68      # decimal number
is_student = True      # True or False

print(age)             # 25

# Update a value any time
age = 26
print(age)             # 26
```

  </section>
  <section class="definition-panel">
    <span class="object-label">Naming rules</span>
    <h2>Valid names</h2>
    <div class="name-rules">
      <p class="rule-ok">✓ Use letters, digits, underscores</p>
      <p class="rule-ok">✓ Start with a letter or underscore</p>
      <p class="rule-ok">✓ Use <code>snake_case</code> for readability</p>
      <p class="rule-bad">✗ Cannot start with a digit — <code>1name</code></p>
      <p class="rule-bad">✗ No spaces — use <code>my_name</code> not <code>my name</code></p>
      <p class="rule-bad">✗ Case matters — <code>name</code> ≠ <code>Name</code></p>
    </div>
  </section>
</div>

<style>
.name-rules p {
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0.25rem 0;
}

.rule-ok {
  color: var(--lesson-green) !important;
}

.rule-bad {
  color: #ff9a9a !important;
}
</style>

---
class: foundation-slide
---

<div class="eyebrow">Data types</div>

# The four basic types

<p class="foundation-intro">Every value in Python has a <strong>type</strong>. The type tells Python what the value is and what you can do with it.</p>

<div class="type-grid">
  <section class="type-panel">
    <span class="object-label">str</span>
    <h2>String</h2>
    <p>Text — always inside quotes.</p>

```python
name  = "Sara"
city  = 'Berlin'
email = "sara@redi.de"
```

  </section>
  <section class="type-panel">
    <span class="object-label">int</span>
    <h2>Integer</h2>
    <p>Whole numbers — no quotes, no decimal point.</p>

```python
age      = 25
students = 12
year     = 2026
```

  </section>
  <section class="type-panel">
    <span class="object-label">float</span>
    <h2>Float</h2>
    <p>Decimal numbers — no quotes.</p>

```python
height  = 1.68
price   = 2.99
average = 8.5
```

  </section>
  <section class="type-panel">
    <span class="object-label">bool</span>
    <h2>Boolean</h2>
    <p>Only two values — must be capitalised.</p>

```python
is_student  = True
has_ticket  = False
is_raining  = True
```

  </section>
</div>

<style>
.type-grid {
  display: grid;
  gap: 0.75rem;
  grid-template-columns: repeat(4, 1fr);
}

.type-panel {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  padding: 0.9rem;
}

.type-panel h2 {
  font-size: 1.05rem;
  margin: 0.3rem 0 0.35rem;
}

.type-panel p {
  color: var(--lesson-muted);
  font-size: 0.78rem;
  line-height: 1.35;
  margin: 0 0 0.5rem;
}

.type-panel .slidev-code-wrapper {
  margin: 0;
}
</style>

---
class: python-code-slide
---

<div class="eyebrow">Data types</div>

# type() and len()

<div class="code-and-output">
  <section class="code-panel">

```python
name   = "Sara"
age    = 25
height = 1.68
flag   = True

# type() tells you the type of a value
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
print(type(flag))    # <class 'bool'>

# len() counts characters in a string
print(len(name))     # 4
print(len("Berlin")) # 6
print(len(""))       # 0  — empty string
```

  </section>
  <section class="output-panel">
    <span class="object-label">Why use them</span>
    <h2>type()</h2>
    <p>Use it when you are unsure what type a variable holds — especially useful when debugging.</p>
    <h2>len()</h2>
    <p>Counts how many characters are in a string. Works on lists too (you will see that later).</p>
    <p class="output-note">Both are <strong>built-in functions</strong> — they come with Python and are always available.</p>
  </section>
</div>

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

.output-note {
  background: rgb(192 132 252 / 16%);
  border-left: 3px solid var(--lesson-blue);
  color: var(--lesson-ink) !important;
  font-size: 0.78rem !important;
  line-height: 1.35 !important;
  margin-top: 0.6rem !important;
  padding: 0.3rem 0.5rem;
}
</style>

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
print(age + 1)          # 26

# str → float
price = float("9.99")
print(price * 2)        # 19.98

# int/float → str  (needed when joining text)
age  = 25
print("I am " + str(age) + " years old")

# int → float and back
x = float(5)    # 5.0
y = int(3.9)    # 3  ← decimal is cut, not rounded!
```

  </section>
  <section class="output-panel">
    <span class="object-label">The three converters</span>
    <div class="converter-list">
      <div class="converter">
        <code>int()</code>
        <span>Converts to a whole number. Cuts off any decimal — does not round.</span>
      </div>
      <div class="converter">
        <code>float()</code>
        <span>Converts to a decimal number.</span>
      </div>
      <div class="converter">
        <code>str()</code>
        <span>Converts anything to text. Required before joining a number into a string with <code>+</code>.</span>
      </div>
    </div>
  </section>
</div>

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

.converter-list {
  display: grid;
  gap: 0.5rem;
  margin-top: 0.25rem;
}

.converter {
  background: rgb(192 132 252 / 12%);
  border-left: 3px solid var(--lesson-blue);
  display: grid;
  gap: 0.35rem;
  padding: 0.4rem 0.6rem;
}

.converter code {
  color: var(--lesson-blue);
  font-size: 0.95rem;
  font-weight: 700;
}

.converter span {
  color: var(--lesson-muted);
  font-size: 0.78rem;
  line-height: 1.35;
}
</style>

---
class: foundation-slide
---

<div class="eyebrow">Type conversion</div>

# Common type errors

<div class="error-grid">
  <section class="error-panel">
    <span class="object-label error-label">TypeError</span>
    <h2>Cannot mix str and int</h2>

```python
# ✗ This crashes
age = 25
print("I am " + age)
```

<p class="error-fix">Fix: convert with <code>str(age)</code> or use a comma instead of <code>+</code>:</p>

```python
print("I am " + str(age))  # ✓
print("I am", age)          # ✓ comma works too
```

  </section>
  <section class="error-panel">
    <span class="object-label error-label">ValueError</span>
    <h2>Cannot convert non-numbers</h2>

```python
# ✗ This crashes
age = int("twenty five")
```

<p class="error-fix">Fix: <code>int()</code> and <code>float()</code> only work on numeric strings:</p>

```python
age = int("25")     # ✓  "25" is a valid number
```

  </section>
</div>

<p class="foundation-note"><strong>TypeError</strong> — check your types and add a conversion. <strong>ValueError</strong> — check what you are trying to convert.</p>

<style>
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
  margin: 0.4rem 0;
}

.error-panel h2 {
  font-size: 1rem;
  margin: 0.3rem 0 0.4rem;
}

.error-label {
  color: #ff9a9a !important;
}

.error-fix {
  color: var(--lesson-muted);
  font-size: 0.8rem;
  line-height: 1.35;
  margin: 0.3rem 0 0.15rem;
}
</style>

---
class: python-code-slide
---

<div class="eyebrow">User input</div>

# input()

<div class="code-and-output">
  <section class="code-panel">

```python
# Ask for text — always returns a string
name = input("What is your name? ")
print("Hello, " + name + "!")

# Ask for a number — must convert!
age = int(input("How old are you? "))
print("Next year you will be", age + 1)

# Ask for a decimal number
price = float(input("Enter a price: "))
print("Double:", price * 2)
```

  </section>
  <section class="output-panel">
    <span class="object-label">What happens</span>

```text
What is your name? Sara
Hello, Sara!
How old are you? 25
Next year you will be 26
Enter a price: 4.99
Double: 9.98
```

<p class="output-note"><code>input()</code> <strong>always</strong> returns a string — even when the user types a number. Wrap it with <code>int()</code> or <code>float()</code> if you need to do maths.</p>
  </section>
</div>

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

.output-note {
  background: rgb(192 132 252 / 16%);
  border-left: 3px solid var(--lesson-blue);
  color: var(--lesson-ink) !important;
  font-size: 0.78rem !important;
  line-height: 1.35 !important;
  margin-top: 0.6rem !important;
  padding: 0.3rem 0.5rem;
}
</style>

---
class: exercise-slide
---

<div class="eyebrow">Exercise</div>

# Build an About Me program

<div class="py-exercise-layout">
  <div class="py-exercise-steps">
    <div class="py-exercise-step"><b>1</b><span><strong>Create variables</strong>Name five variables about yourself: <code>name</code>, <code>age</code>, <code>city</code>, <code>language</code>, <code>is_student</code>.</span></div>
    <div class="py-exercise-step"><b>2</b><span><strong>Print each one</strong>Use <code>print()</code> to display every variable on its own line.</span></div>
    <div class="py-exercise-step"><b>3</b><span><strong>Check the types</strong>Use <code>type()</code> to print the type of each variable.</span></div>
    <div class="py-exercise-step"><b>4</b><span><strong>Update your age</strong>Change <code>age</code> to next year's value and print it again.</span></div>
    <div class="py-exercise-step"><b>5</b><span><strong>Measure your name</strong>Use <code>len(name)</code> to print how many letters your name has.</span></div>
    <div class="py-exercise-done"><strong>Done when:</strong> your output shows all five values, five types, the updated age, and the name length.</div>
  </div>

  <div class="py-exercise-starter">

```python
# Lesson 2 — About Me

# 1. Create your variables
name       =
age        =
city       =
language   =
is_student =

# 2. Print each variable


# 3. Check types with type()


# 4. Update age and print again


# 5. Print the length of your name
```

  </div>
</div>

<style>
.py-exercise-layout {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr);
}

.py-exercise-steps {
  display: grid;
  gap: 0.4rem;
}

.py-exercise-step {
  align-items: start;
  border-bottom: 1px solid var(--lesson-border);
  display: grid;
  font-size: 0.72rem;
  gap: 0.5rem;
  grid-template-columns: 1.5rem 1fr;
  padding: 0.25rem 0.15rem 0.4rem;
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

.py-exercise-step strong,
.py-exercise-step span {
  display: block;
}

.py-exercise-done {
  background: rgb(192 132 252 / 16%);
  border-left: 4px solid var(--lesson-blue);
  font-size: 0.72rem;
  padding: 0.45rem 0.6rem;
}

.py-exercise-starter .slidev-code-wrapper {
  margin: 0;
}

.py-exercise-starter pre {
  font-size: 0.6rem;
  line-height: 1.3;
}
</style>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

<div class="eyebrow">Solution · About Me</div>

# About Me — solution

<div class="solution-code-columns">
  <section>

```python
# 1. Variables
name       = "Sara"
age        = 25
city       = "Berlin"
language   = "Arabic"
is_student = True

# 2. Print each one
print(name)           # Sara
print(age)            # 25
print(city)           # Berlin
print(language)       # Arabic
print(is_student)     # True
```

  </section>
  <section>

```python
# 3. Types
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(is_student)) # <class 'bool'>

# 4. Update age
age = 26
print(age)            # 26

# 5. Name length
print(len(name))      # 4
```

  </section>
</div>

<style>
.solution-code-columns {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: 1fr 1fr;
}

.solution-code-columns .slidev-code-wrapper {
  margin: 0;
}
</style>
<!-- solution:end -->

---
class: knowledge-check-slide
---

<div class="eyebrow">Take-home exercise · Variables</div>

# Type detective

<p class="knowledge-check-intro">For each code snippet, predict the output before you run it. Then run the code to check.</p>

<ol class="knowledge-questions knowledge-questions-wide">
  <li><b>1</b><span>What does <code>type("42")</code> return?</span></li>
  <li><b>2</b><span>What does <code>int(3.9)</code> return?</span></li>
  <li><b>3</b><span>What does <code>len("ReDI")</code> return?</span></li>
  <li><b>4</b><span>Does <code>"I am " + 25</code> work? Why or why not?</span></li>
  <li><b>5</b><span>What does <code>str(True)</code> return?</span></li>
  <li><b>6</b><span>What does <code>type(3.0)</code> return?</span></li>
</ol>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

<div class="eyebrow">Solution · Type detective</div>

# Type detective — solution

<div class="knowledge-solutions">
  <section><b>1</b><span><strong>type("42")</strong><code>&lt;class 'str'&gt;</code> — quotes make it a string, not a number.</span></section>
  <section><b>2</b><span><strong>int(3.9)</strong><code>3</code> — int() cuts the decimal off; it does not round up.</span></section>
  <section><b>3</b><span><strong>len("ReDI")</strong><code>4</code> — four characters.</span></section>
  <section><b>4</b><span><strong>"I am " + 25</strong>No — TypeError. Use <code>str(25)</code> first, or a comma.</span></section>
  <section><b>5</b><span><strong>str(True)</strong><code>"True"</code> — the boolean becomes the string "True".</span></section>
  <section><b>6</b><span><strong>type(3.0)</strong><code>&lt;class 'float'&gt;</code> — the decimal point makes it a float.</span></section>
</div>
<!-- solution:end -->

---
class: knowledge-check-slide homework-slide
---

<div class="eyebrow">Homework · Lesson 2</div>

# For next class

<ol class="knowledge-questions">
  <li><b>1</b><span><strong>All About Me</strong> — create variables for <code>name</code>, <code>age</code>, <code>city</code>, <code>favourite_food</code>, <code>favourite_colour</code>, <code>is_working</code>. Print each on its own line.</span></li>
  <li><b>2</b><span><strong>Type inspector</strong> — for every variable above, print its type with <code>type()</code>.</span></li>
  <li><b>3</b><span><strong>Receipt</strong> — create <code>item</code>, <code>price</code> (float), <code>quantity</code> (int). Print: <code>Bread — quantity: 2 — price: 1.5</code></span></li>
  <li><b>4</b><span><strong>len() explorer</strong> — create three string variables (name, city, food). Print the length of each. Which is longest?</span></li>
  <li><b>5</b><span><strong>Mad libs</strong> — create <code>adjective</code>, <code>animal</code>, <code>place</code>, <code>number</code>. Print: <em>The [adjective] [animal] visited [number] places in [place].</em></span></li>
  <li><b>6</b><span><strong>Converter chain</strong> — start with <code>age_text = "28"</code>. Convert it to <code>int</code>, then to <code>float</code>, then back to <code>str</code>. Print the type after each step.</span></li>
  <li><b>7</b><span><strong>Interactive profile</strong> — use <code>input()</code> to ask for a name and age. Print a sentence using both. Bonus: print how many letters the name has.</span></li>
</ol>

<style>
.homework-slide {
  padding: 0.9rem 2.4rem;
}

.homework-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 1.85rem;
  letter-spacing: 0;
  margin: 0.1rem 0 0.45rem;
}

.homework-slide .knowledge-questions li {
  font-size: 0.78rem;
  padding: 0.5rem 0.3rem;
}
</style>

---
layout: center
class: finish-slide
---

<div class="eyebrow">Lesson complete</div>

# You have variables

<div class="recap">
  <span><b>1</b> print() and comments</span>
  <span><b>2</b> Variables</span>
  <span><b>3</b> str · int · float · bool</span>
  <span><b>4</b> type() · len() · input()</span>
</div>

<p class="lead">Next lesson: arithmetic, order of operations, and building a calculator with user input.</p>

<style>
.recap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  margin-top: 2.5rem;
}
</style>
