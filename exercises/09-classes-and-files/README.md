# Classes and files

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

## Classroom exercises

### Predict the output

This is a thinking task, so it has no task folder.

What two lines are printed?

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
bella = Dog("Bella", 5)
bella.age = 6

print(rex.age)
print(bella.name, bella.age)
```

### Wallet

[Open the task folder](wallet/)

You are building a wallet. Every wallet has an owner and an amount of money in
Danish Kroner.

1. Write a class `Wallet`. It should be initialized with an owner (string) and
   money (a number) and save them as attributes.
2. Create a wallet for `"Ana"` with 200 DKK and a wallet for `"Ben"` with
   125 DKK. Store them in the variables `ana` and `ben`.
3. Print each wallet's owner and money: first Ana's owner and money, then
   Ben's.
4. **(Advanced)** Put both wallets in a list and use a loop to print every owner
   and their money, like `Ana has 200 DKK`.

**Expected input and output**

```python
ana = Wallet("Ana", 200)
print(ana.owner)          # Ana
print(ana.money)          # 200
ben = Wallet("Ben", 125)
print(ben.money)          # 125
```

Your program prints (steps 3 and 4):

```text
Ana
200
Ben
125
Ana has 200 DKK
Ben has 125 DKK
```

**Help**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
print(rex.name)
```

### Wallet methods

Copy the code from the starter: [wallet-methods/exercise.py](wallet-methods/exercise.py).
[Open the task folder](wallet-methods/).

Our wallet is not useful yet. Let's allow it to receive money and pay for
things. The `Wallet` class from the previous exercise is already in the
starter. Add the new methods to it.

1. Add a method `receive(amount)` that adds `amount` to `money`.
2. Add a method `has_enough_money(price)` that returns `True` if `money` is at
   least `price`, otherwise `False`.
3. Add a method `pay(price)`. If `money` is at least `price`, it subtracts
   `price` from `money` and returns `True`. Otherwise it returns `False` and
   does not change `money`.
4. **(Advanced)** Add a method `pay_all(prices)` that calls `pay` for each price
   in the list and returns how many prices were paid.

**Expected input and output**

```python
wallet = Wallet("Ana", 200)
wallet.receive(50)             # money 250
wallet.has_enough_money(300)   # False
wallet.pay(100)                # True, money 150
wallet.pay(400)                # False, money 150
wallet.pay_all([50, 200, 30])  # 2, money 70
```

**Help**

```python
class Dog:
    def eat(self):          # changes an attribute
        self.hungry = False

    def is_hungry(self):    # returns a value
        return self.hungry
```

### Shopping list

[Open the task folder](shopping-list/)

Your shopping list is saved in a file, one item per line. Write code that reads
it.

1. Create a file called `shopping_list.txt` in VS Code, in the same folder as
   `exercise.py`. Add a few lines with stuff you want to buy next week, one item
   per line. For example:

   ```text
   cheese
   bread
   toothbrush
   ```

2. Write `print_list(filename)`. It reads the file and prints every item in the
   file, without empty lines between them.
3. **(Advanced)** Write `has_item(filename, item)`. It reads the file and
   **returns** `True` if `item` is on the list, otherwise `False`.

**Expected input and output**

If `shopping_list.txt` contains:

```text
bread
milk
eggs
```

```python
print_list("shopping_list.txt")           # prints bread, milk and eggs, one per line
has_item("shopping_list.txt", "milk")     # returns True
has_item("shopping_list.txt", "cheese")   # returns False
```

**Help**

```python
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
```

`.strip()` removes the `"\n"` at the end of a line.

For `has_item`, check `line.strip() == item`.

### What is in `shopping.txt`?

This is a thinking task, so it has no task folder.

What is in the file after these lines run?

```python
with open("shopping.txt", "w") as file:
    file.write("tea\n")

with open("shopping.txt", "a") as file:
    file.write("milk\n")

with open("shopping.txt", "w") as file:
    file.write("bread\n")

with open("shopping.txt", "a") as file:
    file.write("eggs\n")
```

### Add to the shopping list

[Open the task folder](shopping-list-write/)

Now you want to change your shopping list from Python. Write code that saves a
new list and adds items to it.

1. Write the function `save_list(filename, items)`: `filename` is the name of
   the file, such as `"shopping.txt"`. `items` is a list of strings. It
   **writes** each item into the file, one per line. Anything already in the
   file is **replaced**.
2. Write the function `add_item(filename, item)`: `item` is one string. It
   **adds** `item` to the end of the file. The old items **stay**.
3. **(Advanced)** Write the function `add_items(filename, items)`: `items` is a
   list of strings. It **adds** each item to the end of the file. Use
   `add_item`.

**Expected input and output**

```python
save_list("shopping.txt", ["bread", "milk"])
add_item("shopping.txt", "eggs")
add_items("shopping.txt", ["cheese", "apples"])
```

`shopping.txt` afterwards:

```text
bread
milk
eggs
cheese
apples
```

**Help**

```python
with open(filename, "w") as file:
    file.write(item + "\n")
```

`"w"` replaces the file. `"a"` adds to the end.

Use a `for` loop to write every item in a list.

[See the solutions after trying the tasks](../../solutions/09-classes-and-files/README.md).
