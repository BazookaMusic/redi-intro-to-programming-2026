# 06 · Lists and Tuples exercises

These exercises come from the [Lists and Tuples slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/06-lists-and-tuples.html). When you finish, compare your work with the [solutions](../../solutions/06-lists-and-tuples/).

New to this? Follow [How to clone this repository to get access to exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026#clone-repository) and [How to do exercises and check my answers](https://github.com/BazookaMusic/redi-intro-to-programming-2026#do-exercises) first.

## Homework

Do these at home after the lesson.

### Homework 1: Favourite foods

**Folder:** [`homework-01-favourite-foods`](homework-01-favourite-foods/)

Create a list of 5 foods you like. Loop through it and print each one with its position number, starting from 1.

Example output:

```text
1. pizza
2. sushi
3. pasta
4. tacos
5. soup
```

### Homework 2: Sum of a list

**Folder:** [`homework-02-sum-of-a-list`](homework-02-sum-of-a-list/)

Use a loop to calculate the sum of all numbers in this list. Do not use the built-in `sum()` function.

Example output:

```text
108
```

### Homework 3: Count the long words

**Folder:** [`homework-03-count-long-words`](homework-03-count-long-words/)

Loop through the list and count how many words have more than 4 letters. Print the count.

Example output:

```text
3
```

### Homework 4: Tuple unpacking

**Folder:** [`homework-04-tuple-unpacking`](homework-04-tuple-unpacking/)

Loop through the list of `(name, age)` tuples and print a sentence for each person.

Example output:

```text
Alice is 28 years old.
Bruno is 34 years old.
Carla is 22 years old.
```

### Homework 5: Reverse a list

**Folder:** [`homework-05-reverse-a-list`](homework-05-reverse-a-list/)

Without using `.reverse()` or slicing, use a loop to print the items of this list in reverse order.

Hint: use `range(len(colours) - 1, -1, -1)`

Example output:

```text
yellow
blue
green
red
```

### Homework 6: Remove duplicates

**Folder:** [`homework-06-remove-duplicates`](homework-06-remove-duplicates/)

Loop through the `numbers` list and build a new list with no duplicates. Keep the first time each number appears. Use `in` to check if it is already in your new list.

Example output:

```text
[1, 3, 2, 4, 5]
```

### Homework 7: Count vowels in a word

**Folder:** [`homework-07-count-vowels`](homework-07-count-vowels/)

Ask the user to type a word. Loop through each letter and count how many times each vowel (a, e, i, o, u) appears. Print the count for each vowel.

Example input:

```text
programming
```

Example output:

```text
a: 1
e: 0
i: 1
o: 1
u: 0
```

### Homework 8: Sorted leaderboard

**Folder:** [`homework-08-sorted-leaderboard`](homework-08-sorted-leaderboard/)

Find the top 3 players by score and print their names and scores in order. Sort the list by score first. You can use `key=lambda p: p[1]` as an optional shortcut.

Example output:

```text
1. Bruno — 91
2. Dina  — 88
3. Carla — 67
```

### Homework 9: Build a shopping list

**Folder:** [`homework-09-build-a-shopping-list`](homework-09-build-a-shopping-list/)

Keep asking the user to type an item. Add each item to a list. When they type `done`, stop and print the full list.

Example input:

```text
milk
bread
done
```

Example output:

```text
Your list: ['milk', 'bread']
```

### Homework 10: Two-list comparison

**Folder:** [`homework-10-two-list-comparison`](homework-10-two-list-comparison/)

Print only the names that appear in both lists.

Example output:

```text
Bruno
Dina
```

## Classroom exercises

We do these together during the lesson.

### Exercise 1: Shopping list

**Folder:** [`shopping-list`](shopping-list/)

Start with this list and do each step in order, printing after each one:

1. Add `"butter"` to the end.
2. Replace `"bread"` with `"pasta"` (use its index).
3. Remove `"eggs"` from the list.
4. Print how many items are left.

Example output:

```text
['milk', 'bread', 'eggs', 'butter']
['milk', 'pasta', 'eggs', 'butter']
['milk', 'pasta', 'butter']
3
```

### Exercise 2: Score analyser

**Folder:** [`score-analyser`](score-analyser/)

Write a program that:

1. Prints every score above 10.
2. Calculates and prints the total of all scores.
3. Finds and prints the highest score.

Example output:

```text
15
21
Total: 67
Highest: 21
```

### Exercise 3: Weekly temperatures

**Folder:** [`weekly-temperatures`](weekly-temperatures/)

Write a program that:

1. Prints each day and its temperature: `Monday: 18°C`
2. Finds and prints the highest temperature.
3. Calculates and prints the average temperature (one decimal place).

Example output:

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

### Exercise 4: Top scores

**Folder:** [`top-scores`](top-scores/)

Write a program that:

1. Sorts the scores from highest to lowest.
2. Prints the top 3 scores (use slicing).
3. Prints the lowest score.
4. Prints how many scores are above 50.

Example output:

```text
Top 3: [91, 89, 76]
Lowest: 11
Scores above 50: 5
```

### Mini project: Student report

**Folder:** [`mini-project-student-report`](mini-project-student-report/)

For each student:

1. Calculate their average score.
2. Print their name, average, and whether they passed (average >= 60).

At the end, print the name of the student with the highest average.

Example output:

```text
Alice  — average: 85.0 — Passed
Bruno  — average: 61.7 — Passed
Carla  — average: 91.3 — Passed
Dina   — average: 46.7 — Did not pass
Top student: Carla
```
