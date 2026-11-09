---
theme: default
title: Dictionaries and sets
info: |
  Intro to Programming
  ReDI School 2026 - Week 8
drawings:
  persist: false
highlighter: shiki
transition: slide-left
preloadImages: false
mdc: true
fonts:
  mono: Fira Mono
---

<div class="absolute inset-0 bg-[#E8522A]" />

<div class="absolute top-6 left-8 flex items-center gap-3 text-white">
  <div class="w-10 h-10 bg-white rounded flex items-center justify-center">
    <svg viewBox="0 0 40 40" class="w-8 h-8" fill="#E8522A" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ReDI School logo">
      <rect x="4" y="4" width="14" height="14" rx="1"/>
      <rect x="22" y="4" width="14" height="14" rx="1"/>
      <rect x="4" y="22" width="14" height="14" rx="1"/>
      <rect x="22" y="22" width="14" height="14" rx="1"/>
    </svg>
  </div>
  <span class="text-lg font-semibold tracking-wide">ReDISchool</span>
</div>
<div class="absolute top-8 right-8 text-white text-lg font-medium">Week 8</div>

<div class="absolute bottom-32 left-12 right-12 text-white">
  <p class="text-xl font-light opacity-90 mb-2">Introduction to Programming - Fall 2026</p>
  <h1 class="text-6xl font-light leading-tight mb-6">Dictionaries and sets</h1>
  <p class="text-2xl font-light opacity-90 mt-4">Look things up by name. Keep only one of each.</p>
  <p class="text-xl font-light opacity-90 mt-4">Store prices, stock and votes in dictionaries, and use sets to find unique values.</p>
</div>

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 8 - Dictionaries and sets</div>

## Part 1: Dictionaries

Find a value by its name instead of by its position.

<div class="agenda [&_td]:py-1">

|  |  |
|---|---|
| 01 | Quick recap |
| 02 | Dictionaries are everywhere |
| 03 | Why not two lists? |
| 04 | Creating and reading |
| 05 | Changing a dictionary |
| 06 | Looping over a dictionary |
| 07 | Counting with a dictionary |

</div>

Practice: a café menu and a shop's stock.

---

# 01 - Quick recap

A list keeps values in order. We find a value by its **index**.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])            # apple

def count_long(words):
    count = 0
    for word in words:
        if len(word) > 5:
            count += 1
    return count

print(count_long(fruits))   # 2
```

Today, we find values by a **name** instead of a number.

---

# 02 - Dictionaries are everywhere

Many things in daily life connect a **key** to a **value**.

<div class="grid grid-cols-2 gap-6 mt-6">
<div>

**Phone contacts**

Ana → 0151 111

</div>
<div>

**Shop price list**

tea → 2 euros

</div>
<div>

**A dictionary book**

hello → a greeting

</div>
<div>

**School report**

maths → grade 2

</div>
</div>

You look up the key, and you get its value.

---

# The same idea in Python

A Python **dictionary** stores these pairs.

```python
contacts = {"Ana": "0151 111", "Ben": "0152 222"}
prices = {"tea": 2, "coffee": 3}
meanings = {"hello": "a greeting", "apple": "a round fruit"}
report = {"maths": 2, "English": 1}
```

```python
print(prices["coffee"])     # 3
print(report["English"])    # 1
```

You will use dictionaries in almost every Python program you write.

---

# 03 - Why not two lists?

We could keep items and prices in two lists.

```python
items = ["tea", "coffee", "cake"]
prices = [2, 3, 4]

position = items.index("coffee")
print(prices[position])     # 3
```

- We must keep both lists in the same order.
- Adding or removing an item means changing both lists.

A dictionary keeps each item **together with** its price:

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}
print(menu["coffee"])       # 3
```

---

# 04 - Creating a dictionary

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}
```

| Part | Meaning |
|---|---|
| `{ }` | Start and end of the dictionary |
| `"tea"` | A **key**: the name we look up |
| `:` | Connects a key to its value |
| `2` | A **value**: what we get back |
| `,` | Separates the key-value pairs |

Keys are often strings. Values can be anything: numbers, strings, lists...

An empty dictionary is `{}`.

---

# Reading a value

Put the key in square brackets.

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}

print(menu["tea"])          # 2
print(menu["cake"])         # 4
print(menu["pizza"])        # crashes!
```

```text
KeyError: 'pizza'
```

A **KeyError** means the key is not in the dictionary.

What will this print?

```python
print(menu["Tea"])
```

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Reading a value

```text
KeyError: 'Tea'
```

Keys must match exactly. `"Tea"` and `"tea"` are different keys.
<!-- solution:end -->

---

# Read safely

Check first with `in`:

```python
if "pizza" in menu:
    print(menu["pizza"])
else:
    print("Not on the menu")
```

Or use `.get(key, default)`. It returns the default when the key is missing.

```python
print(menu.get("tea", 0))     # 2
print(menu.get("pizza", 0))   # 0
```

`in` checks the **keys**, not the values:

```python
print("tea" in menu)          # True
print(2 in menu)              # False
```

---
class: knowledge-check-slide exercise-slide
---

# Exercise: Café menu · 5 min

You are building the till for a small café. A dictionary stores the price of each item.

1. Make a dictionary `menu`: tea costs 2, coffee costs 3 and cake costs 4.
2. Write `price_of(menu, item)`. It **returns** the item's price, or `0` if the item is not on the menu. Print the price of `"coffee"` and of `"pizza"`.
3. **(Advanced)** Write `order_total(menu, items)`. `items` is a list of item names. It **returns** the total price. Reuse `price_of`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
price_of(menu, "coffee")   # returns 3
price_of(menu, "pizza")    # returns 0
order_total(menu, ["tea", "cake", "tea"])
# returns 8
```

</div>
<div>

**Help**

```python
"tea" in menu            # True
menu.get("water", 0)     # 0
```

Starter: [exercises/08-dictionaries-and-sets/cafe-menu/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/cafe-menu)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Café menu

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}

def price_of(menu, item):
    return menu.get(item, 0)

print(price_of(menu, "coffee"))
print(price_of(menu, "pizza"))

def order_total(menu, items):
    total = 0
    for item in items:
        total += price_of(menu, item)
    return total
```

`if item in menu: return menu[item]` followed by `return 0` also works.
<!-- solution:end -->

---

# 05 - Changing a dictionary

Use `=` with a key. A new key is **added**; an existing key is **updated**.

```python
menu = {"tea": 2, "coffee": 3}

menu["cake"] = 4      # add a new item
menu["tea"] = 3       # update the price of tea
print(menu)           # {'tea': 3, 'coffee': 3, 'cake': 4}
```

Remove a pair with `del`, and count pairs with `len`:

```python
del menu["coffee"]
print(menu)           # {'tea': 3, 'cake': 4}
print(len(menu))      # 2
```

Each key appears **only once**. Setting it again replaces the old value.

---

# A function can change a dictionary

When we give a dictionary to a function, the function can change it.

```python
def raise_price(menu, item):
    menu[item] = menu[item] + 1

menu = {"tea": 2, "coffee": 3}
raise_price(menu, "tea")
print(menu)           # {'tea': 3, 'coffee': 3}
```

The function did not return anything, but `menu` changed.
Lists work the same way: `append` inside a function changes the caller's list.

---

# 06 - Looping over a dictionary

A `for` loop over a dictionary gives us the **keys**.

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}

for item in menu:
    print(item, menu[item])
```

```text
tea 2
coffee 3
cake 4
```

Only the values: `menu.values()`

```python
total = 0
for price in menu.values():
    total += price
print(total)          # 9
```

---

# Keys and values together: `.items()`

`.items()` gives each pair as a tuple. We unpack it in the loop.

```python
for item, price in menu.items():
    print(f"{item} costs {price} euros")
```

| Part | Meaning |
|---|---|
| `menu.items()` | Every pair: `("tea", 2)`, `("coffee", 3)`, ... |
| `item, price` | Unpacks each pair into two names |

```text
tea costs 2 euros
coffee costs 3 euros
cake costs 4 euros
```

The loop goes through the pairs in the order they were added.

---

# A list of dictionaries

Each dictionary can describe one thing. A list can hold many of them.

```python
students = [
    {"name": "Ana", "score": 18},
    {"name": "Ben", "score": 12},
]

for student in students:
    if student["score"] >= 15:
        print(student["name"], "passed")
```

```text
Ana passed
```

`student` is one dictionary, so `student["name"]` reads its name.

---
class: knowledge-check-slide exercise-slide
---

# Exercise: Shop stock · 15 min

You run a small corner shop. A dictionary stores how many of each item you have.

1. Write `restock(stock, item, amount)`. It adds `amount` to the item's count. A new item starts at `amount`. It returns nothing.
2. Write `sell(stock, item)`. If the item's count is above 0, take 1 away and **return** `True`. Otherwise **return** `False`.
3. **(Advanced)** Write `out_of_stock(stock)`. It **returns** a list of the items with a count of `0`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
stock = {"apples": 5, "bread": 1, "milk": 0}
sell(stock, "bread")      # returns True
sell(stock, "bread")      # returns False
restock(stock, "eggs", 6)
print(stock)
# {'apples': 5, 'bread': 0, 'milk': 0, 'eggs': 6}
out_of_stock(stock)       # returns ['bread', 'milk']
```

</div>
<div>

**Help**

```python
stock.get("eggs", 0)      # 0
for item, count in stock.items():
    print(item, count)
```

Starter: [exercises/08-dictionaries-and-sets/shop-stock/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/shop-stock)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Shop stock

```python
def restock(stock, item, amount):
    stock[item] = stock.get(item, 0) + amount

def sell(stock, item):
    if stock.get(item, 0) > 0:
        stock[item] -= 1
        return True
    return False

def out_of_stock(stock):
    empty = []
    for item, count in stock.items():
        if count == 0:
            empty.append(item)
    return empty
```

`stock.get(item, 0)` means an unknown item counts as 0, so it never crashes.
<!-- solution:end -->

---

# 07 - Counting with a dictionary

How many times does each letter appear in `"banana"`?

```python
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1

print(counts)     # {'b': 1, 'a': 3, 'n': 2}
```

The key is the thing we count. The value is how many we have seen so far.

`counts.get(letter, 0)` gives the current count, or `0` the first time.

---

# Trace the count

```python
counts[letter] = counts.get(letter, 0) + 1
```

<div class="[&_td]:py-1 [&_th]:py-1">

| `letter` | `counts.get(letter, 0)` | `counts` afterwards |
|---|---|---|
| `b` | 0 | `{'b': 1}` |
| `a` | 0 | `{'b': 1, 'a': 1}` |
| `n` | 0 | `{'b': 1, 'a': 1, 'n': 1}` |
| `a` | 1 | `{'b': 1, 'a': 2, 'n': 1}` |
| `n` | 1 | `{'b': 1, 'a': 2, 'n': 2}` |
| `a` | 2 | `{'b': 1, 'a': 3, 'n': 2}` |

</div>

Let's count the letters of your name together.

---
layout: center
---

# Break

15 minutes

---

<div class="text-sm font-semibold text-[#E8522A] uppercase tracking-widest mb-4">Week 8 - Dictionaries and sets</div>

## Part 2: Sets

Keep one of each, and compare groups.

<div class="agenda [&_td]:py-1">

|  |  |
|---|---|
| 08 | What is a set? |
| 09 | Using sets |
| 10 | Comparing sets |
| 11 | Hangman with a set |
| 12 | Choosing a collection |
| 13 | Homework and questions |

</div>

Practice: count unique visitors and plan a party.

---

# 08 - What is a set?

A **set** is a collection where each value appears **only once**.

You already used one! In Hangman, `get_english_words_set` returned a set of words.

```python
colours = {"red", "blue", "red", "green"}
print(colours)        # {'blue', 'green', 'red'}
print(len(colours))   # 3
```

- No duplicates: the second `"red"` is ignored.
- No order: the printed order may be different on your computer.
- No index: `colours[0]` does not work.

---

# An empty set

`{}` is an empty **dictionary**, not a set.

```python
empty_dict = {}
empty_set = set()

print(type(empty_dict))   # <class 'dict'>
print(type(empty_set))    # <class 'set'>
```

A set uses curly brackets with values only.
A dictionary uses curly brackets with `key: value` pairs.

```python
{"tea", "coffee"}         # a set
{"tea": 2, "coffee": 3}   # a dictionary
```

---

# 09 - Using sets

<div class="grid grid-cols-2 gap-6">
<div>

```python
seen = set()
seen.add("Ana")
seen.add("Ben")
seen.add("Ana")       # already there, nothing changes

print(len(seen))      # 2
print("Ana" in seen)  # True

seen.remove("Ben")
print(seen)           # {'Ana'}
```

</div>
<div>

| Code | What it does |
|---|---|
| `s.add(x)` | Adds `x` if it is not there yet |
| `x in s` | `True` if `x` is in the set |
| `s.remove(x)` | Removes `x` (crashes if it is missing) |
| `len(s)` | How many values |

</div>
</div>

---

# Remove duplicates from a list

`set(a_list)` makes a set with one of each value.

```python
visits = ["Ana", "Ben", "Ana", "Cleo", "Ben"]
people = set(visits)

print(len(visits))    # 5 visits
print(len(people))    # 3 different people
```

A loop works on a set too:

```python
for person in people:
    print("Welcome,", person)
```

Remember: the loop order is not guaranteed.

---
class: knowledge-check-slide exercise-slide
---

# Exercise: Unique visitors · 5 min

A small museum writes down the name of every visitor at the door. Some people come more than once.

1. Write `unique_visitors(names)`. It **returns** how many different people visited. Use a set.
2. Print the result for `["Ana", "Ben", "Ana", "Cleo", "Ben"]`.
3. **(Advanced)** Write `first_visits(names)`. It **returns** a list of names in the order they first came, without duplicates. Use a set to remember who you have already seen.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
visits = ["Ana", "Ben", "Ana", "Cleo", "Ben"]
unique_visitors(visits)   # returns 3
first_visits(visits)
# returns ['Ana', 'Ben', 'Cleo']
```

</div>
<div>

**Help**

```python
seen = set()
seen.add("Ana")
print("Ana" in seen)      # True
```

Starter: [exercises/08-dictionaries-and-sets/unique-visitors/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/unique-visitors)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Unique visitors

```python
def unique_visitors(names):
    return len(set(names))

print(unique_visitors(["Ana", "Ben", "Ana", "Cleo", "Ben"]))

def first_visits(names):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result
```

The set answers "have I seen this before?". The list keeps the order.
<!-- solution:end -->

---

# 10 - Comparing sets

Ana and Max each have a set of friends.

<img src="/images/dictionaries-and-sets/friends-venn.svg" alt="Two overlapping circles. Only in Ana's friends: Ben. In both: Cleo and Dan. Only in Max's friends: Eva." class="mx-auto h-56 my-4">

```python
ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
```

---

# Union, intersection and difference

| Method | Meaning | Result |
|---|---|---|
| `ana_friends.union(max_friends)` | In **either** set | `{'Ben', 'Cleo', 'Dan', 'Eva'}` |
| `ana_friends.intersection(max_friends)` | In **both** sets | `{'Cleo', 'Dan'}` |
| `ana_friends.difference(max_friends)` | In Ana's, **not** in Max's | `{'Ben'}` |

Each method returns a **new** set. The original sets do not change.

---
class: knowledge-check-slide exercise-slide
---

# Exercise: Party guests · 10 min

Ana and Max are throwing a party together. Each of them has a set of friends to invite.

1. Write `common_friends(friends1, friends2)`. It **returns** the set of friends that are in both sets.
2. Write `all_guests(friends1, friends2)`. It **returns** a set of everyone invited, each person once. Print how many guests are invited.
3. **(Advanced)** Write `everyone(groups)`. `groups` is a list of sets. It **returns** one set with every guest from every group. Use a loop.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
common_friends(ana_friends, max_friends)
# returns {'Cleo', 'Dan'}
len(all_guests(ana_friends, max_friends))  # 4
everyone([{"Ben"}, {"Ben", "Cleo"}, {"Eva"}])
# returns {'Ben', 'Cleo', 'Eva'}
```

</div>
<div>

**Help**

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.union(b)          # {1, 2, 3, 4}
a.intersection(b)   # {2, 3}
```

Starter: [exercises/08-dictionaries-and-sets/party-guests/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/party-guests)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Party guests

```python
def common_friends(friends1, friends2):
    return friends1.intersection(friends2)

def all_guests(friends1, friends2):
    return friends1.union(friends2)

ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
print(len(all_guests(ana_friends, max_friends)))

def everyone(groups):
    guests = set()
    for group in groups:
        guests = guests.union(group)
    return guests
```
<!-- solution:end -->

---

# Shorter set operators

You have used the set methods. The same operations also have shorter forms:

| Method | Operator | Meaning |
|---|---|---|
| `a.union(b)` | `a \| b` | In either set |
| `a.intersection(b)` | `a & b` | In both sets |
| `a.difference(b)` | `a - b` | In `a`, but not in `b` |

Both forms return a new set. The method names can be easier to read when you are learning.

---

# 11 - Hangman with a set

Last week, we stored the guessed letters in a list.

```python
guessed_letters = []
guessed_letters.append("i")
```

A set fits better: each letter can only be guessed once, and the order does not matter.

```python
guessed_letters = set()
guessed_letters.add("i")
guessed_letters.add("i")       # no duplicate

print("i" in guessed_letters)  # True
```

The rest of the game still works: `letter in guessed_letters` checks a set just like a list.

---

# 12 - Choosing a collection

| | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Looks like | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| Keeps order | Yes | Yes | Yes | No |
| Duplicates | Allowed | Allowed | Keys unique | Not allowed |
| Can change | Yes | No | Yes | Yes |
| Find a value by | Index | Index | Key | `in` only |

---

# Which collection would you use?

Choose a list, tuple, dictionary or set.

1. The songs in a playlist, in order
2. Each country and its capital
3. The different words used in a book

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Choosing a collection

1. **List**: the order matters, and a song can appear twice.
2. **Dictionary**: look up a capital by its country.
3. **Set**: we want each word only once.
<!-- solution:end -->

---

# 13 - Homework

Five tasks. Each has an `exercise.py` and its own `check.py`.

| Task | Practise |
|---|---|
| 1. Vote counter | Counting with a dictionary |
| 2. Phone book | Adding, reading and deleting entries |
| 3. Word counter | Counting words, then a set of repeated words |
| 4. Shopping cart project | Dictionaries and sets in a small shop program |
| 5. Products by category | Collecting product names in lists inside a dictionary |

Folder: [exercises/08-dictionaries-and-sets/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets)

---
class: knowledge-check-slide exercise-slide
---

# Homework 1: Vote counter

Your class votes on where to go for a trip. Each vote is a place name in a list.

1. Write `count_votes(votes)`. It **returns** a dictionary: each place and its number of votes.
2. Print the result for `["zoo", "museum", "zoo", "park", "zoo", "park"]`.
3. **(Advanced)** Write `winner(counts)`. It **returns** the place with the most votes. Loop over `counts.items()`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
votes = ["zoo", "museum", "zoo",
         "park", "zoo", "park"]
count_votes(votes)
# returns {'zoo': 3, 'museum': 1, 'park': 2}
winner({'zoo': 3, 'museum': 1, 'park': 2})
# returns 'zoo'
```

</div>
<div>

**Help**

```python
counts = {}
counts["zoo"] = counts.get("zoo", 0) + 1
```

Folder: [homework-01-vote-counter/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/homework-01-vote-counter)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Vote counter

```python
def count_votes(votes):
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts

print(count_votes(["zoo", "museum", "zoo", "park", "zoo", "park"]))

def winner(counts):
    best_place = ""
    best_count = 0
    for place, count in counts.items():
        if count > best_count:
            best_place = place
            best_count = count
    return best_place
```
<!-- solution:end -->

---
class: knowledge-check-slide exercise-slide
---

# Homework 2: Phone book

You are building a phone book with names and numbers.

1. Write `add_contact(book, name, number)` to add or update a contact. It returns nothing.
2. Write `find_number(book, name)` to **return** the number, or `"Unknown"`.
3. Write `remove_contact(book, name)` to delete it and **return** `True`, or **return** `False` if missing.
4. **(Advanced)** Write `names_starting_with(book, letter)` to **return** a list of names starting with `letter`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
book = {"Ana": "0151 111", "Ben": "0152 222"}
find_number(book, "Zoe")    # returns 'Unknown'
add_contact(book, "Zoe", "0153 333")
find_number(book, "Zoe")    # returns '0153 333'
remove_contact(book, "Ben") # returns True
remove_contact(book, "Ben") # returns False
names_starting_with(book, "Z")  # ['Zoe']
```

</div>
<div>

**Help**

```python
del book["Ana"]
name = "Zoe"
print(name[0])         # Z
```

Folder: [homework-02-phone-book/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/homework-02-phone-book)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Phone book

```python
def add_contact(book, name, number):
    book[name] = number

def find_number(book, name):
    return book.get(name, "Unknown")

def remove_contact(book, name):
    if name in book:
        del book[name]
        return True
    return False

def names_starting_with(book, letter):
    names = []
    for name in book:
        if name[0] == letter:
            names.append(name)
    return names
```
<!-- solution:end -->

---
class: knowledge-check-slide exercise-slide
---

# Homework 3: Word counter

You are writing a tool that shows which words a text repeats.

1. Write `count_words(sentence)`. It **returns** a dictionary: each word and how many times it appears.
2. Print the result for `"the cat and the dog and the bird"`.
3. **(Advanced)** Write `repeated_words(sentence)`. It **returns** a set of the words that appear more than once. Reuse `count_words`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
count_words("the cat and the dog")
# {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
repeated_words("the cat and the dog and the bird")
# returns {'the', 'and'}
```

</div>
<div>

**Help:** `split()` turns a sentence into a list of words.

```python
words = "the cat sat".split()
print(words)    # ['the', 'cat', 'sat']
```

Folder: [homework-03-word-counter/](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/08-dictionaries-and-sets/homework-03-word-counter)

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Word counter

```python
def count_words(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(count_words("the cat and the dog and the bird"))

def repeated_words(sentence):
    repeated = set()
    for word, count in count_words(sentence).items():
        if count > 1:
            repeated.add(word)
    return repeated
```
<!-- solution:end -->

---
class: knowledge-check-slide exercise-slide
---

# Homework 4: Shopping cart project

Copy the code from the starter: [homework-04-shopping-cart/exercise.py](https://github.com/BazookaMusic/redi-intro-to-programming-2026/blob/main/exercises/08-dictionaries-and-sets/homework-04-shopping-cart/exercise.py)

You are building a shop. `PRICES` stores each price; the cart stores each quantity.

1. Write `add_to_cart(cart, item, quantity)`. Add the quantity and **return** `True`, or **return** `False` if the item is not in `PRICES`.
2. Write `cart_total(cart)` to **return** the total price of the cart.
3. **(Advanced)** Write `sale_total(cart, sale_items)` to **return** the total with half-price items from the set `sale_items`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
cart = {}
add_to_cart(cart, "apple", 3)   # True
add_to_cart(cart, "apple", 2)   # cart: {'apple': 5}
add_to_cart(cart, "pizza", 1)   # False
add_to_cart(cart, "cheese", 1)  # True
cart_total(cart)                # 10
sale_total(cart, {"cheese"})    # 7.5
```

</div>
<div>

**Help**

```python
PRICES["cheese"]          # 5
cart.get("apple", 0)      # 0 if not in the cart
for item, quantity in cart.items():
    print(item, quantity)
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Shopping cart project

```python
def add_to_cart(cart, item, quantity):
    if item not in PRICES:
        return False
    cart[item] = cart.get(item, 0) + quantity
    return True

def cart_total(cart):
    total = 0
    for item, quantity in cart.items():
        total += PRICES[item] * quantity
    return total

def sale_total(cart, sale_items):
    total = 0
    for item, quantity in cart.items():
        price = PRICES[item]
        if item in sale_items:
            price = price / 2
        total += price * quantity
    return total
```
<!-- solution:end -->

---
class: knowledge-check-slide exercise-slide
---

# Homework 5: Products by category (Advanced)

Copy the code from the starter: [homework-05-products-by-category/exercise.py](https://github.com/BazookaMusic/redi-intro-to-programming-2026/blob/main/exercises/08-dictionaries-and-sets/homework-05-products-by-category/exercise.py)

A shop has a list of products. Each has a name and a category.

1. Write `products_by_category(products)` to **return** a dictionary: each category is a key and its value is a list of product names, in their original order.
2. Print the result for `PRODUCTS`.
3. **(Advanced)** Write `categories_with_multiple(products)` to **return** the set of categories with more than one product. Reuse `products_by_category`.

<div class="grid grid-cols-2 gap-6">
<div>

**Expected input and output**

```python
products_by_category(PRODUCTS)
# {'fruit': ['apple', 'banana'],
#  'bakery': ['bread', 'cake'],
#  'dairy': ['milk']}
categories_with_multiple(PRODUCTS)
# {'fruit', 'bakery'}  # order may differ
```

</div>
<div>

**Help**

```python
product = {"name": "apple",
           "category": "fruit"}
product["category"]   # 'fruit'
names = []
names.append(product["name"])
```

</div>
</div>

<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution: Products by category

```python
def products_by_category(products):
    result = {}
    for product in products:
        category = product["category"]
        if category not in result:
            result[category] = []
        result[category].append(product["name"])
    return result

print(products_by_category(PRODUCTS))

def categories_with_multiple(products):
    result = set()
    for category, names in products_by_category(products).items():
        if len(names) > 1:
            result.add(category)
    return result
```
<!-- solution:end -->

---

# The main ideas

- A **dictionary** connects keys to values: `{"tea": 2}`.
- Read with `d[key]`, or safely with `in` and `d.get(key, default)`.
- Add or update with `d[key] = value`; remove with `del d[key]`.
- Loop over pairs with `for key, value in d.items():`.
- Count things with `counts[x] = counts.get(x, 0) + 1`.
- A **set** keeps one of each value: `set(a_list)` removes duplicates.
- Compare sets with `union`, `intersection` and `difference`.

---
layout: center
---

# Questions?
