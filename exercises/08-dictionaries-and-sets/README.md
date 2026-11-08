# Dictionaries and sets

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

Each checker works with just `exercise.py` and `check.py`.

## Homework

### Homework 1: Vote counter

[Open the task folder](homework-01-vote-counter/)

Your class votes on where to go for a trip. Each vote is a place name in a list.

1. Write `count_votes(votes)`. It **returns** a dictionary: each place and its
   number of votes.
2. Print the result for `["zoo", "museum", "zoo", "park", "zoo", "park"]`.
3. **(Advanced)** Write `winner(counts)`. It **returns** the place with the most
   votes. Loop over `counts.items()`.

**Expected input and output**

```python
votes = ["zoo", "museum", "zoo", "park", "zoo", "park"]
count_votes(votes)    # returns {'zoo': 3, 'museum': 1, 'park': 2}
winner({'zoo': 3, 'museum': 1, 'park': 2})   # returns 'zoo'
```

Your program prints:

```text
{'zoo': 3, 'museum': 1, 'park': 2}
```

**Help**

```python
counts = {}
counts["zoo"] = counts.get("zoo", 0) + 1
```

### Homework 2: Phone book

[Open the task folder](homework-02-phone-book/)

You are building a phone book app. It stores each friend's name and phone number.

1. Write `add_contact(book, name, number)`. It adds the contact, or updates the
   number if the name exists. It returns nothing.
2. Write `find_number(book, name)`. It **returns** the number, or `"Unknown"`.
3. Write `remove_contact(book, name)`. If the name is in the book, delete it and
   **return** `True`. Otherwise **return** `False`.
4. **(Advanced)** Write `names_starting_with(book, letter)`. It **returns** a list
   of the names that start with `letter`.

**Expected input and output**

```python
book = {"Ana": "0151 111", "Ben": "0152 222"}
find_number(book, "Zoe")              # returns 'Unknown'
add_contact(book, "Zoe", "0153 333")
find_number(book, "Zoe")              # returns '0153 333'
remove_contact(book, "Ben")           # returns True
remove_contact(book, "Ben")           # returns False
names_starting_with(book, "Z")        # returns ['Zoe']
```

**Help**

```python
del book["Ana"]
name = "Zoe"
print(name[0])         # Z
```

### Homework 3: Word counter

[Open the task folder](homework-03-word-counter/)

You are writing a tool that shows which words a text repeats.

1. Write `count_words(sentence)`. It **returns** a dictionary: each word and how
   many times it appears.
2. Print the result for `"the cat and the dog and the bird"`.
3. **(Advanced)** Write `repeated_words(sentence)`. It **returns** a set of the
   words that appear more than once. Reuse `count_words`.

**Expected input and output**

```python
count_words("the cat and the dog")
# returns {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
repeated_words("the cat and the dog and the bird")
# returns {'the', 'and'}
```

Your program prints:

```text
{'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
```

**Help:** `split()` turns a sentence into a list of words.

```python
words = "the cat sat".split()
print(words)    # ['the', 'cat', 'sat']
```

### Homework 4: Shopping cart project

Copy the code from the starter: [homework-04-shopping-cart/exercise.py](homework-04-shopping-cart/exercise.py).
[Open the task folder](homework-04-shopping-cart/).

You are building a small online shop. `PRICES` stores each item's price.
The cart is a dictionary: item → quantity.

1. Write `add_to_cart(cart, item, quantity)`. If the item is not in `PRICES`,
   **return** `False`. Otherwise add `quantity` to the item in the cart and
   **return** `True`.
2. Write `cart_total(cart)`. It **returns** the total price of everything in the
   cart.
3. **(Advanced)** Write `sale_total(cart, sale_items)`. `sale_items` is a set.
   Those items cost half price. It **returns** the total.

**Expected input and output**

```python
cart = {}
add_to_cart(cart, "apple", 3)   # returns True
add_to_cart(cart, "apple", 2)   # cart is now {'apple': 5}
add_to_cart(cart, "pizza", 1)   # returns False
add_to_cart(cart, "cheese", 1)  # returns True
cart_total(cart)                # returns 10
sale_total(cart, {"cheese"})    # returns 7.5
```

**Help**

```python
PRICES["cheese"]          # 5
cart.get("apple", 0)      # 0 if not in the cart
for item, quantity in cart.items():
    print(item, quantity)
```

The starter supplies the shop loop and the receipt below your functions.

### Homework 5: Products by category (Advanced)

Copy the code from the starter: [homework-05-products-by-category/exercise.py](homework-05-products-by-category/exercise.py).
[Open the task folder](homework-05-products-by-category/).

A shop has a list of products. Each has a name and a category.
Make a list of product names for each category.

1. Write `products_by_category(products)`. It **returns** a dictionary where
   each category is a key and its value is a list of product names. Keep the
   names in the order they appear in `products`.
2. Print the result for `PRODUCTS`.
3. **(Advanced)** Write `categories_with_multiple(products)`. It **returns** a
   set of categories with more than one product. Reuse `products_by_category`.

**Expected input and output**

```python
products_by_category(PRODUCTS)
# returns {'fruit': ['apple', 'banana'], 'bakery': ['bread', 'cake'], 'dairy': ['milk']}
categories_with_multiple(PRODUCTS)   # returns {'fruit', 'bakery'}
```

The order of a set may be different. Your program prints:

```text
{'fruit': ['apple', 'banana'], 'bakery': ['bread', 'cake'], 'dairy': ['milk']}
```

**Help**

```python
product = {"name": "apple", "category": "fruit"}
product["category"]   # 'fruit'
names = []
names.append(product["name"])   # names is ['apple']
```

## Classroom exercises

### Reading a value

This is a thinking task, so it has no task folder.

What will this print?

```python
menu = {"tea": 2, "coffee": 3, "cake": 4}
print(menu["Tea"])
```

### Café menu

[Open the task folder](cafe-menu/)

You are building the till for a small café. A dictionary stores the price of each item.

1. Make a dictionary `menu`: tea costs 2, coffee costs 3 and cake costs 4.
2. Write `price_of(menu, item)`. It **returns** the item's price, or `0` if the
   item is not on the menu. Print the price of `"coffee"` and of `"pizza"`.
3. **(Advanced)** Write `order_total(menu, items)`. `items` is a list of item
   names. It **returns** the total price. Reuse `price_of`.

**Expected input and output**

```python
price_of(menu, "coffee")                    # returns 3
price_of(menu, "pizza")                     # returns 0
order_total(menu, ["tea", "cake", "tea"])   # returns 8
```

Your program prints:

```text
3
0
```

**Help**

```python
"tea" in menu            # True
menu.get("water", 0)     # 0
```

### Shop stock

[Open the task folder](shop-stock/)

You run a small corner shop. A dictionary stores how many of each item you have.

1. Write `restock(stock, item, amount)`. It adds `amount` to the item's count.
   A new item starts at `amount`. It returns nothing.
2. Write `sell(stock, item)`. If the item's count is above 0, take 1 away and
   **return** `True`. Otherwise **return** `False`.
3. **(Advanced)** Write `out_of_stock(stock)`. It **returns** a list of the items
   with a count of `0`.

**Expected input and output**

```python
stock = {"apples": 5, "bread": 1, "milk": 0}
sell(stock, "bread")      # returns True
sell(stock, "bread")      # returns False
restock(stock, "eggs", 6)
print(stock)              # {'apples': 5, 'bread': 0, 'milk': 0, 'eggs': 6}
out_of_stock(stock)       # returns ['bread', 'milk']
```

**Help**

```python
stock.get("eggs", 0)      # 0
for item, count in stock.items():
    print(item, count)
```

### Unique visitors

[Open the task folder](unique-visitors/)

A small museum writes down the name of every visitor at the door.
Some people come more than once.

1. Write `unique_visitors(names)`. It **returns** how many different people
   visited. Use a set.
2. Print the result for `["Ana", "Ben", "Ana", "Cleo", "Ben"]`.
3. **(Advanced)** Write `first_visits(names)`. It **returns** a list of names in
   the order they first came, without duplicates. Use a set to remember who you
   have already seen.

**Expected input and output**

```python
visits = ["Ana", "Ben", "Ana", "Cleo", "Ben"]
unique_visitors(visits)   # returns 3
first_visits(visits)      # returns ['Ana', 'Ben', 'Cleo']
```

Your program prints:

```text
3
```

**Help**

```python
seen = set()
seen.add("Ana")
print("Ana" in seen)      # True
```

### Party guests

[Open the task folder](party-guests/)

Ana and Max are throwing a party together. Each of them has a set of friends to invite.

1. Write `common_friends(friends1, friends2)`. It **returns** the set of friends
   that are in both sets.
2. Write `all_guests(friends1, friends2)`. It **returns** a set of everyone
   invited, each person once. Print how many guests are invited.
3. **(Advanced)** Write `everyone(groups)`. `groups` is a list of sets. It
   **returns** one set with every guest from every group. Use a loop.

**Expected input and output**

```python
ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
common_friends(ana_friends, max_friends)       # returns {'Cleo', 'Dan'}
len(all_guests(ana_friends, max_friends))      # 4
everyone([{"Ben"}, {"Ben", "Cleo"}, {"Eva"}])  # returns {'Ben', 'Cleo', 'Eva'}
```

Your program prints:

```text
4
```

**Help**

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.union(b)          # {1, 2, 3, 4}
a.intersection(b)   # {2, 3}
```

### Choosing a collection

This is a thinking task, so it has no task folder.

Would you use a list, a tuple, a dictionary or a set?

1. The songs in a playlist, in order
2. Each country and its capital
3. The different words used in a book

[See the solutions after trying the tasks](../../solutions/08-dictionaries-and-sets/README.md).
