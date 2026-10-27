---
theme: default
title: Introduction to Programming - Fall 2026
info: |
  ReDISchool Week 6 — Lists & Tuples
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
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<!-- Main content -->
<div class="absolute bottom-32 left-12 right-12 text-white">
  <p class="text-xl font-light opacity-90 mb-2">Introduction to Programming - Fall 2026</p>
  <h1 class="text-6xl font-light leading-tight mb-6">Lists &amp; Tuples 📋</h1>
  <p class="text-2xl font-light opacity-90 mt-4">
    One <span class="bg-white text-[#E8522A] font-semibold rounded px-2">variable</span>.
    Many <span class="bg-white text-[#E8522A] font-semibold rounded px-2">values</span>.
  </p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Agenda

<div class="agenda">

|  |  |
|---|---|
| 01 | Recap & Questions |
| 02 | Lists — create, read, change |
| 03 | Loops with lists |
| — | Break (15 min) |
| 04 | Tuples |
| 05 | More list methods |
| 06 | Homework |

</div>

Parts 02, 03, 04 and 05 have short exercises. ✍️

<style>
.agenda td { padding-top: 0.25rem; padding-bottom: 0.25rem; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## 01 - Recap from last week
<br>

Last week we covered:

- 🔁 **`for` loops** — `for i in range(5):` repeats a known number of times
- ⏳ **`while` loops** — repeat until a condition changes
- ⏭️ **`break` & `continue`** — exit a loop early or skip an iteration
- 📋 **Lists (sneak peek)** — `names = ["Anna", "Bruno", "Carla"]`
- 🔍 **Patterns** — filter, accumulate, find the max

Today we go deep on **lists**, **tuples**, and using **loops** with them.

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

<br>
<br>
<br>
<br>
<br>
<div class="font-bold text-center" style="font-size: 40px;">Questions?</div>

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">02 - Lists 📋</h1>
  <p class="text-2xl font-light opacity-90 mt-4">Create, read and change</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## What Is a List?
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

Imagine storing five friends' names:

- Without a list → one variable per name
- With 50 friends, that's 50 variables
- What if you don't know how many there are?

A **list** holds many values in **one variable**, in order, inside square brackets `[ ]`.

- The values are called **items**
- `len()` tells you how many items there are

</div>
<div>

```python
# Without a list
friend1 = "Anna"
friend2 = "Bruno"
friend3 = "Carla"

# With a list
friends = ["Anna", "Bruno", "Carla"]

print(friends)       # ['Anna', 'Bruno', 'Carla']
print(len(friends))  # 3
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Creating a List
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

- Square brackets `[ ]` with **commas** between items
- Can hold strings, numbers, booleans — or a mix
- An **empty list** `[]` is valid — add items later
- `len()` counts the items

</div>
<div>

```python
# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of numbers
scores = [12, 45, 7, 30, 18]

# Mixed types
mixed = ["Alice", 25, True]

# Empty list
cart = []

print(len(fruits))  # 3
print(len(cart))    # 0
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Reading Items by Index
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

Each item has a position number called an **index**, starting at **0**.

- `fruits[0]` — first item
- `fruits[1]` — second item
- `fruits[-1]` — last item
- `fruits[-2]` — second to last

Asking for an index that doesn't exist → `IndexError`

</div>
<div>

```python
fruits = ["apple", "banana", "cherry"]
#          index 0  index 1   index 2

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # cherry
print(fruits[-1])  # cherry - last item
print(fruits[-2])  # banana

# This crashes:
print(fruits[5])   # IndexError!
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Changing a List

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

Lists are **mutable** — you can change them after you create them.

- `fruits[i] = value` — replace an item
- `.append(value)` — add to the end
- `.remove(value)` — remove by value
- `.pop()` — remove and return the last item
- `in` — check if an item is in the list

</div>
<div>

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"      # replace banana
print(fruits)  # ['apple', 'mango', 'cherry']

fruits.append("orange")  # add to end
print(fruits)
# ['apple', 'mango', 'cherry', 'orange']

fruits.remove("mango")   # remove by value
print(fruits)  # ['apple', 'cherry', 'orange']

last = fruits.pop()      # remove last
print(last)    # orange

print("apple" in fruits)  # True
print("mango" in fruits)  # False
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 1 — Shopping List · 8 min

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div>
<div class="border-2 border-l-6 border-[#2e9e5b] rounded-lg px-5 py-3">

✍️ Start with this list and do each step in order, **printing the list after each change**:

```python
shopping = ["milk", "bread", "eggs"]
```

1. Add `"butter"` to the end
2. Replace `"bread"` with `"pasta"` (use its index)
3. Remove `"eggs"` from the list
4. Print how many items are left

</div>
</div>
<div>

Expected output:

```text
['milk', 'bread', 'eggs', 'butter']
['milk', 'pasta', 'eggs', 'butter']
['milk', 'pasta', 'butter']
3
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 1 — Solution
<br>

```python
shopping = ["milk", "bread", "eggs"]

shopping.append("butter")
print(shopping)       # ['milk', 'bread', 'eggs', 'butter']

shopping[1] = "pasta"
print(shopping)       # ['milk', 'pasta', 'eggs', 'butter']

shopping.remove("eggs")
print(shopping)       # ['milk', 'pasta', 'butter']

print(len(shopping))  # 3
```
<!-- solution:end -->

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">03 - Loops with lists 🔁</h1>
  <p class="text-2xl font-light opacity-90 mt-4">Visit every item, one by one</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Looping Over a List
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

You can loop over a list with `for`, just like with `range()`.

- No `range()` needed — just the list itself
- The loop variable takes **each item** in turn
- The loop runs **once per item**
- Same `for … in …` pattern as before

</div>
<div>

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
```

```text
I like apple
I like banana
I like cherry
```

```python
scores = [12, 45, 7, 30]

for score in scores:
    print(score)
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Looping with the Index — `enumerate()`

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

Normally a loop gives you the **item only**. Sometimes you also need to know **which position** you are at.

`enumerate()` gives you **both** at the same time — the position number and the item — so you don't have to count yourself.

By default the count starts at `0`. Use `start=1` to count from `1`.

</div>
<div>

```python
fruits = ["apple", "banana", "cherry"]

# With enumerate - position AND item
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

```text
0 apple
1 banana
2 cherry
```

```python
# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

```text
1. apple
2. banana
3. cherry
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Pattern 1 — Filter
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

**Filtering** means keeping only the items that match a condition.

1. Loop over **every** item
2. Use `if` to check the condition
3. Print (or collect) only the items that pass

</div>
<div>

```python
scores = [12, 45, 7, 30, 18]

for score in scores:
    if score > 15:
        print(score)
```

```text
45
30
18
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Pattern 2 — Accumulate & Find the Max

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

**Accumulating** — add up all the items.

**Finding the max** — keep the biggest seen so far.

Both follow the same shape:

1. Create a variable **before** the loop
2. Update it **inside** the loop
3. Use it **after** the loop

</div>
<div>

```python
scores = [12, 45, 7, 30, 18]

# Accumulate
total = 0
for score in scores:
    total = total + score
print(f"Total: {total}")      # 112
print(f"Average: {total / len(scores)}")  # 22.4

# Find the max
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(f"Highest: {highest}")  # 45
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 2 — Score Analyser · 10 min

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div>
<div class="border-2 border-l-6 border-[#2e9e5b] rounded-lg px-5 py-3">

✍️ Write a program that:

```python
scores = [8, 3, 15, 7, 21, 4, 9]
```

1. Prints every score **above 10**
2. Calculates and prints the **total** of all scores
3. Finds and prints the **highest** score

</div>
</div>
<div>

Expected output:

```text
15
21
Total: 67
Highest: 21
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 2 — Solution

<div class="grid grid-cols-2 gap-8 items-start mt-4">
<div>

```python
scores = [8, 3, 15, 7, 21, 4, 9]

for score in scores:
    if score > 10:
        print(score)

total = 0
for score in scores:
    total = total + score
print(f"Total: {total}")
```

</div>
<div>

```python
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(f"Highest: {highest}")
```

- Each part is its own loop: **filter**, **accumulate**, **find the max**.
- Starting `highest` at `scores[0]` works for any numbers.

</div>
</div>
<!-- solution:end -->

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">Break (15 min) ☕</h1>
</div>

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">04 - Tuples 🔒</h1>
  <p class="text-2xl font-light opacity-90 mt-4">Lists that never change</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## What Is a Tuple?

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

A **tuple** is like a list — but you **cannot change it** after you create it.

- Uses round brackets `( )` instead of `[ ]`
- **Immutable** — fixed once created
- Indexing, `len()`, `in` and looping work the same
- Use a tuple when the values should **never change**

|  | List | Tuple |
|---|---|---|
| Syntax | `[ ]` | `( )` |
| Can change? | ✅ Yes | ❌ No |

</div>
<div>

```python
# List - can be changed
fruits = ["apple", "banana"]
fruits[0] = "mango"   # works fine

# Tuple - cannot be changed
point = (10, 20)
point[0] = 99         # TypeError!

# When to use a tuple
days = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday",
        "Sunday")
location = (55.6761, 12.5683)  # lat, long
red = (255, 0, 0)              # RGB colour
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
.compact-code table { font-size: 0.9em; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Reading & Unpacking a Tuple
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

Reading works exactly like a list:

- `point[0]` — first item
- `point[-1]` — last item
- `len(point)` — number of items
- `in` — check if an item is there

**Unpacking** — give each item its own variable, in one line.

</div>
<div>

```python
point = (10, 20)
print(point[0])    # 10
print(point[-1])   # 20
print(len(point))  # 2

# Unpacking
x, y = (10, 20)
print(x)  # 10
print(y)  # 20

# Any size
name, age, city = ("Anna", 28, "Copenhagen")
print(name)  # Anna
print(city)  # Copenhagen
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Looping Over a Tuple
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

Looping works exactly the same as with lists.

You can **unpack** items directly in the loop header — very useful with a list of pairs.

</div>
<div>

```python
days = ("Monday", "Tuesday", "Wednesday")

for day in days:
    print(day)

# Unpack inside the loop
people = [("Alice", 28), ("Bruno", 34), ("Carla", 22)]

for name, age in people:
    print(f"{name} is {age} years old.")
```

```text
Alice is 28 years old.
Bruno is 34 years old.
Carla is 22 years old.
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 3 — Weekly Temperatures · 10 min

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div>
<div class="border-2 border-l-6 border-[#2e9e5b] rounded-lg px-5 py-3">

✍️ Write a program that:

```python
temperatures = (18, 21, 19, 24, 22, 17, 20)
days = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday",
        "Sunday")
```

1. Prints each day and its temperature
2. Finds and prints the **highest** temperature
3. Prints the **average** (one decimal place)

**Need a hint?**

- `f"{value:.1f}"` shows one decimal place

</div>
</div>
<div>

Expected output:

```text
Monday: 18°C
Tuesday: 21°C
Wednesday: 19°C
Thursday: 24°C
Friday: 22°C
Saturday: 17°C
Sunday: 20°C
Highest: 24°C
Average: 20.1°C
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 3 — Solution

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

```python
temperatures = (18, 21, 19, 24, 22, 17, 20)
days = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday",
        "Sunday")

for i, temp in enumerate(temperatures):
    print(f"{days[i]}: {temp}°C")
```

- `enumerate()` gives the index `i`, so `days[i]` is the matching day.

</div>
<div>

```python
highest = temperatures[0]
for temp in temperatures:
    if temp > highest:
        highest = temp
print(f"Highest: {highest}°C")

total = 0
for temp in temperatures:
    total = total + temp
average = total / len(temperatures)
print(f"Average: {average:.1f}°C")
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>
<!-- solution:end -->

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">05 - More list methods 🧰</h1>
  <p class="text-2xl font-light opacity-90 mt-4">Sorting, searching and slicing</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## More List Methods

<div class="grid grid-cols-2 gap-8 items-start mt-4 compact-code">
<div>

**Sorting**

- `.sort()` — sorts the list **in place** (changes it)
- `.sort(reverse=True)` — sorts largest first
- `sorted(my_list)` — returns a sorted **copy**, the original stays the same

**Other useful methods**

- `.insert(i, value)` — add at a specific position
- `.index(value)` — find the position of an item
- `.count(value)` — how many times an item appears
- `.clear()` — remove all items

</div>
<div>

```python
scores = [30, 12, 45, 7, 18]
scores.sort()
print(scores)    # [7, 12, 18, 30, 45]
scores.sort(reverse=True)
print(scores)    # [45, 30, 18, 12, 7]

# sorted() - keeps the original
original = [30, 12, 45, 7, 18]
copy = sorted(original)
print(original)  # [30, 12, 45, 7, 18]
print(copy)      # [7, 12, 18, 30, 45]

names = ["Anna", "Bruno", "Carla"]
names.insert(1, "Dina")
print(names)  # ['Anna', 'Dina', 'Bruno', 'Carla']
print(names.index("Bruno"))  # 2
print(names.count("Anna"))   # 1
```

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Slicing a List
<br>

<div class="grid grid-cols-2 gap-8 items-start">
<div>

Just like strings, you can **slice** a list to get a section of it.

- `scores[start:stop]` — from `start` up to (not including) `stop`
- `scores[:3]` — from the beginning up to index 3
- `scores[2:]` — from index 2 to the end
- `scores[-2:]` — the last 2 items

Slicing gives a **new** list — the original is unchanged.

</div>
<div>

```python
scores = [10, 20, 30, 40, 50]

print(scores[1:4])  # [20, 30, 40]
print(scores[:3])   # [10, 20, 30]
print(scores[2:])   # [30, 40, 50]
print(scores[-2:])  # [40, 50]

# Sorted + sliced = top 3
scores.sort(reverse=True)
print(scores[:3])   # [50, 40, 30]
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 4 — Top Scores · 10 min

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div>
<div class="border-2 border-l-6 border-[#2e9e5b] rounded-lg px-5 py-3">

✍️ Write a program that:

```python
scores = [42, 17, 89, 55, 23, 76, 34, 91, 60, 11]
```

1. Sorts the scores from **highest to lowest**
2. Prints the **top 3** scores (use slicing)
3. Prints the **lowest** score
4. Prints how many scores are **above 50**

</div>
</div>
<div>

Expected output:

```text
Top 3: [91, 89, 76]
Lowest: 11
Scores above 50: 5
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Exercise 4 — Solution
<br>

```python
scores = [42, 17, 89, 55, 23, 76, 34, 91, 60, 11]

scores.sort(reverse=True)
print("Top 3:", scores[:3])   # Top 3: [91, 89, 76]
print("Lowest:", scores[-1])  # Lowest: 11

count = 0
for score in scores:
    if score > 50:
        count = count + 1
print(f"Scores above 50: {count}")
```

<br>

- After sorting from highest to lowest, the **lowest** score is the **last** item: `scores[-1]`.
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Common Mistakes (1/2)

<div class="grid grid-cols-2 gap-8 items-start mt-4">
<div>

**1. Index starts at 0, not 1**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # banana - NOT apple
```

**2. Index out of range**

```python
print(fruits[5])  # IndexError!
# Only 0, 1, 2 exist
```

</div>
<div>

**3. Trying to change a tuple**

```python
point = (10, 20)
point[0] = 99  # TypeError!
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Common Mistakes (2/2)

<div class="grid grid-cols-2 gap-8 items-start mt-4">
<div>

**4. `append()` returns `None` — don't assign it**

```python
cart = []
cart = cart.append("milk")  # WRONG
print(cart)  # None!

cart = []
cart.append("milk")         # RIGHT
print(cart)  # ['milk']
```

</div>
<div>

**5. Changing a list while looping over it**

```python
# WRONG - unpredictable
for n in numbers:
    numbers.remove(n)

# RIGHT - collect into a new list
result = []
for n in numbers:
    if n % 2 != 0:
        result.append(n)
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Mini Project — Student Report 🛠️

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start compact-code">
<div>
<div class="border-2 border-l-6 border-[#2e9e5b] rounded-lg px-5 py-3">

✍️ For each student:

1. Calculate their **average** score
2. Print their name, average, and whether they **passed** (average ≥ 60)

At the end, print the name of the student with the **highest** average.

```python
students = [
    ("Alice", [85, 92, 78]),
    ("Bruno", [60, 55, 70]),
    ("Carla", [95, 88, 91]),
    ("Dina",  [40, 52, 48]),
]
```

</div>
</div>
<div>

Expected output:

```text
Alice  — average: 85.0 — Passed
Bruno  — average: 61.7 — Passed
Carla  — average: 91.3 — Passed
Dina   — average: 46.7 — Did not pass
Top student: Carla
```

**Need a hint?**

- `f"{name:<6}"` pads the name to 6 characters

</div>
</div>

<style>
.compact-code pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Mini Project — Solution

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start compact-code">
<div>

```python
students = [
    ("Alice", [85, 92, 78]),
    ("Bruno", [60, 55, 70]),
    ("Carla", [95, 88, 91]),
    ("Dina",  [40, 52, 48]),
]

best_name = ""
best_average = 0
for name, scores in students:
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)

    result = "Passed" if average >= 60 else "Did not pass"
    print(f"{name:<6} — average: {average:.1f} — {result}")

    if average > best_average:
        best_average = average
        best_name = name

print(f"Top student: {best_name}")
```

</div>
<div>

- Each item is a tuple, so `name, scores` unpacks it in the loop header.
- The **inner** loop adds up one student's scores.
- `best_name` and `best_average` remember the best student seen so far.

</div>
</div>

<style>
.compact-code pre { font-size: 11px !important; line-height: 1.3 !important; }
</style>
<!-- solution:end -->

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## What We Learned Today

<div class="learned">

✅ A **list** `[ ]` holds many values in order — **mutable**, so you can change it

✅ Items have an **index** starting at `0`. Use `-1` for the last item

✅ `.append()`, `.remove()`, `.pop()` add and remove items

✅ Loop over a list with `for item in my_list:` — no `range()` needed

✅ `enumerate()` gives you the index and the item together

✅ Patterns: filter, accumulate, find the max — create **before**, update **inside**, use **after**

✅ A **tuple** `( )` is like a list but **immutable** — for values that should never change

✅ `.sort()` sorts in place, `sorted()` returns a sorted copy

✅ Slicing `my_list[1:4]` gives you a section of the list

</div>

<style>
.learned p { margin: 0.35rem 0; }
</style>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

<br>
<br>
<br>
<br>
<br>
<div class="font-bold text-center" style="font-size: 40px;">Questions?</div>

---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">06 - Homework! 🏠</h1>
  <p class="text-2xl font-light opacity-90 mt-4">📌 Commit your work to GitHub when you're done!</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 1 — Favourite Foods

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Create a list of **5 foods** you like. Loop through it and print each one with its position number, **starting from 1**.

</div>
<div>

Expected output (with your own foods):

```text
1. pizza
2. sushi
3. pasta
4. tacos
5. soup
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 2 — Sum of a List

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Use a loop to calculate the sum of all numbers in this list. Do **not** use the built-in `sum()` function.

```python
numbers = [4, 8, 15, 16, 23, 42]
```

</div>
<div>

Expected output:

```text
108
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 3 — Count the Long Words

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Loop through the list and count how many words have **more than 4 letters**. Print the count.

```python
words = ["cat", "elephant", "dog",
         "tiger", "ox", "penguin"]
```

</div>
<div>

Expected output:

```text
3
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 4 — Tuple Unpacking

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Loop through the list of `(name, age)` tuples and print a sentence for each person.

```python
people = [("Alice", 28), ("Bruno", 34),
          ("Carla", 22)]
```

</div>
<div>

Expected output:

```text
Alice is 28 years old.
Bruno is 34 years old.
Carla is 22 years old.
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 5 — Reverse a List

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Without using `.reverse()` or slicing, use a loop to print the items of this list in **reverse order**.

```python
colours = ["red", "green", "blue", "yellow"]
```

**Need a hint?**

- Use `range(len(colours) - 1, -1, -1)`

</div>
<div>

Expected output:

```text
yellow
blue
green
red
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 6 — Remove Duplicates

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Loop through the list and build a **new list** that has no duplicates. Keep the **first** time each item appears.

```python
numbers = [1, 3, 2, 3, 4, 1, 5, 2]
```

**Need a hint?**

- Use `in` to check if the item is already in your new list

</div>
<div>

Expected output:

```text
[1, 3, 2, 4, 5]
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 7 — Count Vowels in a Word

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Ask the user to type a word. Loop through each letter and count how many times each vowel (`a`, `e`, `i`, `o`, `u`) appears. Print the count for each vowel.

</div>
<div>

Expected output (for `programming`):

```text
a: 1
e: 0
i: 1
o: 1
u: 0
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 8 — Sorted Leaderboard

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Find the **top 3** players by score and print their names and scores in order.

```python
players = [("Alice", 42), ("Bruno", 91),
           ("Carla", 67), ("Dina", 88),
           ("Erik", 55)]
```

**Need a hint?**

- Sort the list by score first. You can use `key=lambda p: p[1]`.

</div>
<div>

Expected output:

```text
1. Bruno — 91
2. Dina  — 88
3. Carla — 67
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 9 — Build a Shopping List

<div class="grid grid-cols-[2fr_3fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Keep asking the user to type an item. Add each item to a list. When they type `done`, stop and print the full list.

</div>
<div>

Expected output:

```text
Add item (or 'done' to finish): milk
Add item (or 'done' to finish): bread
Add item (or 'done' to finish): done
Your list: ['milk', 'bread']
```

</div>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 6 — Lists &amp; Tuples</div>

## Homework 10 — Two-List Comparison

<div class="grid grid-cols-[3fr_2fr] gap-6 mt-4 items-start">
<div class="border-2 border-l-6 border-[#E8522A] rounded-lg px-5 py-3">

🏠 Print only the names that appear in **both** lists.

```python
list_a = ["Alice", "Bruno", "Carla", "Dina"]
list_b = ["Bruno", "Erik", "Dina", "Fatima"]
```

</div>
<div>

Expected output:

```text
Bruno
Dina
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-2">Week 6 — Lists &amp; Tuples</div>

## Homework Solutions — 1 to 4

<div class="grid grid-cols-2 gap-x-6 gap-y-1 homework-solutions">
<div>

**1 · Favourite foods**

```python
foods = ["pizza", "sushi", "pasta", "tacos", "soup"]

for i, food in enumerate(foods, start=1):
    print(f"{i}. {food}")
```

**2 · Sum of a list**

```python
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for number in numbers:
    total = total + number
print(total)
```

</div>
<div>

**3 · Count the long words**

```python
words = ["cat", "elephant", "dog",
         "tiger", "ox", "penguin"]

count = 0
for word in words:
    if len(word) > 4:
        count = count + 1
print(count)
```

**4 · Tuple unpacking**

```python
people = [("Alice", 28), ("Bruno", 34),
          ("Carla", 22)]

for name, age in people:
    print(f"{name} is {age} years old.")
```

</div>
</div>

<style>
.homework-solutions p { margin: 0.4rem 0 0.15rem; }
.homework-solutions pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>
<!-- solution:end -->

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-2">Week 6 — Lists &amp; Tuples</div>

## Homework Solutions — 5 to 7

<div class="grid grid-cols-2 gap-x-6 gap-y-1 homework-solutions">
<div>

**5 · Reverse a list**

```python
colours = ["red", "green", "blue", "yellow"]

for i in range(len(colours) - 1, -1, -1):
    print(colours[i])
```

**6 · Remove duplicates**

```python
numbers = [1, 3, 2, 3, 4, 1, 5, 2]

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
```

</div>
<div>

**7 · Count vowels in a word**

```python
word = input("Type a word: ").lower()

for vowel in "aeiou":
    count = 0
    for letter in word:
        if letter == vowel:
            count = count + 1
    print(f"{vowel}: {count}")
```

`.count()` works on strings too: `word.count(vowel)`.

</div>
</div>

<style>
.homework-solutions p { margin: 0.4rem 0 0.15rem; }
.homework-solutions pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>
<!-- solution:end -->

<!-- solution:start -->
---
class: knowledge-solution-slide
---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-2">Week 6 — Lists &amp; Tuples</div>

## Homework Solutions — 8 to 10

<div class="grid grid-cols-2 gap-x-6 gap-y-1 homework-solutions">
<div>

**8 · Sorted leaderboard**

```python
players = [("Alice", 42), ("Bruno", 91),
           ("Carla", 67), ("Dina", 88),
           ("Erik", 55)]

players.sort(key=lambda p: p[1], reverse=True)

for i, player in enumerate(players[:3], start=1):
    name, score = player
    print(f"{i}. {name:<5} — {score}")
```

`key=lambda p: p[1]` tells `.sort()` to compare each player's **score**.

</div>
<div>

**9 · Build a shopping list**

```python
items = []
while True:
    item = input("Add item (or 'done' to finish): ")
    if item == "done":
        break
    items.append(item)
print(f"Your list: {items}")
```

**10 · Two-list comparison**

```python
list_a = ["Alice", "Bruno", "Carla", "Dina"]
list_b = ["Bruno", "Erik", "Dina", "Fatima"]

for name in list_a:
    if name in list_b:
        print(name)
```

</div>
</div>

<style>
.homework-solutions p { margin: 0.4rem 0 0.15rem; }
.homework-solutions pre { font-size: 12px !important; line-height: 1.35 !important; }
</style>
<!-- solution:end -->

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
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 6</div>

<!-- Main content -->
<div class="absolute bottom-32 left-12 right-12 text-white">
  <h1 class="text-6xl font-light leading-tight mb-6" style="font-size: 60px;">🎉 See you next week!</h1>
</div>
