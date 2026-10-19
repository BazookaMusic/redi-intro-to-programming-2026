# 05 · Loops exercises

These exercises come from the [Loops slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/05-loops.html). When you finish, compare your work with the [solutions](../../solutions/05-loops/).

New to this? Follow [How to clone this repository to get access to exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026#clone-repository) and [How to do exercises and check my answers](https://github.com/BazookaMusic/redi-intro-to-programming-2026#do-exercises) first.

## Homework

Do these at home after the lesson.

### Homework 1: Count to 20

**Folder:** [`homework-01-count-to-20`](homework-01-count-to-20/)

Use a loop to print the numbers from 1 to 20, one per line.

Example output:

```text
1
2
3
...
18
19
20
```

### Homework 2: Say hi to your friends

**Folder:** [`homework-02-say-hi-to-friends`](homework-02-say-hi-to-friends/)

Use a loop to go through the `friends` list in `exercise.py`. For each friend, print one line in this format: `Hi, [name]`

Example output:

```text
Hi, Anna
Hi, Bruno
Hi, Carla
```

### Homework 3: Countdown by twos

**Folder:** [`homework-03-countdown-by-twos`](homework-03-countdown-by-twos/)

Use a loop to count down from 20 to 2 in steps of 2, one number per line. After the loop, print `Done!`

Example output:

```text
20
18
16
14
12
10
8
6
4
2
Done!
```

### Homework 4: Add it up

**Folder:** [`homework-04-add-it-up`](homework-04-add-it-up/)

Use a loop to add up all the numbers from 1 to 100. After the loop, print the total.

Example output:

```text
5050
```

### Homework 5: Count the vowels

**Folder:** [`homework-05-count-the-vowels`](homework-05-count-the-vowels/)

Use a loop to count how many vowels (a, e, i, o, u) are in the word `"programming"`. After the loop, print the count.

Example output:

```text
3
```

### Homework 6: Even or odd?

**Folder:** [`homework-06-even-or-odd`](homework-06-even-or-odd/)

Use a loop to go through the `numbers` list in `exercise.py`. For each number, print whether it is even or odd, in this format: `[number] is even` or `[number] is odd`

Hint: `number % 2` gives the remainder after dividing by 2. It is 0 for even numbers.

Example output:

```text
3 is odd
8 is even
15 is odd
22 is even
7 is odd
```

### Homework 7: Number grid

**Folder:** [`homework-07-number-grid`](homework-07-number-grid/)

Use loops to print a 5 by 5 grid. Each row shows the numbers 1 to 5, separated by spaces.

Hint: `print(number, end=" ")` prints a value and a space without starting a new line. `print()` on its own ends the row.

Example output:

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

### Homework 8: Multiplication table

**Folder:** [`homework-08-multiplication-table`](homework-08-multiplication-table/)

Use loops to print the multiplication table for the numbers 1 to 5. Print one line for each pair of numbers, in this format: `[a] * [b] = [result]`

An empty line after each group makes the table easier to read. It is optional.

Example output:

```text
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5

2 * 1 = 2
2 * 2 = 4
...
5 * 4 = 20
5 * 5 = 25
```

### Homework 9: The largest number

**Folder:** [`homework-09-largest-number`](homework-09-largest-number/)

Use a loop to find the largest number in the `numbers` list in `exercise.py`. After the loop, print it.

Example output:

```text
19
```

### Homework 10: Numbers and squares

**Folder:** [`homework-10-numbers-and-squares`](homework-10-numbers-and-squares/)

Use a loop to go through the numbers from 1 to 10. For each number, print the number and its square, separated by a space. The square of a number is the number multiplied by itself.

Example output:

```text
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
10 100
```

### Homework 11: FizzBuzz

**Folder:** [`homework-11-fizzbuzz`](homework-11-fizzbuzz/)

Use a loop to go through the numbers from 1 to 20. For each number, print one line:

- `Fizz` if the number is a multiple of 3
- `Buzz` if the number is a multiple of 5
- `FizzBuzz` if the number is a multiple of both 3 and 5
- otherwise, the number itself

Example output:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

## Classroom exercises

We do these together during the lesson.

### Exercise 1: Lap counter

**Folder:** [`for-lap-counter`](for-lap-counter/)

A runner does 4 laps. Use a `for` loop to print "Lap 1 done" to "Lap 4 done".
Then print "Race finished!" once.

Hint: `{i + 1}` makes laps start at 1.

Example output:

```text
Lap 1 done
Lap 2 done
Lap 3 done
Lap 4 done
Race finished!
```

### Exercise 1 (advanced): Last lap

**Folder:** [`for-lap-counter-advanced`](for-lap-counter-advanced/)

The runner now does `laps = 5` laps. Use a `for` loop to print one line per lap. Mark the last lap with " - last lap!". Then print "Race finished!" once.

Hint: the last lap is when `i + 1` equals `laps`.

Example output:

```text
Lap 1 done
Lap 2 done
Lap 3 done
Lap 4 done
Lap 5 done - last lap!
Race finished!
```

### Exercise 2: Even numbers with for

**Folder:** [`for-even-numbers`](for-even-numbers/)

Use a `for` loop to print every even number from 0 to 20, including 20, one per line.

Example output:

```text
0
2
4
6
8
10
12
14
16
18
20
```

### Exercise 2 (advanced): Leap years

**Folder:** [`for-even-numbers-advanced`](for-even-numbers-advanced/)

A leap year comes every 4 years. Use a `for` loop to print every leap year from 2000 to 2040, including 2040. After the loop, print the next leap year.

Hint: after the loop, the loop variable still holds its last value.

Example output:

```text
2000 is a leap year
2004 is a leap year
2008 is a leap year
2012 is a leap year
2016 is a leap year
2020 is a leap year
2024 is a leap year
2028 is a leap year
2032 is a leap year
2036 is a leap year
2040 is a leap year
Next leap year: 2044
```

### Exercise 3: Savings goal

**Folder:** [`while-savings-goal`](while-savings-goal/)

You start with 0 euros and save 15 euros every week. Use a `while` loop to keep saving until you have at least 100 euros. Each week, print the week number and your savings. When the loop ends, print how many weeks it took.

Example output:

```text
Week 1: 15 euros
Week 2: 30 euros
Week 3: 45 euros
Week 4: 60 euros
Week 5: 75 euros
Week 6: 90 euros
Week 7: 105 euros
Goal reached in 7 weeks!
```

### Exercise 3 (advanced): Growing savings

**Folder:** [`while-savings-goal-advanced`](while-savings-goal-advanced/)

You save 10 euros in week 1, then 5 more each week (10, 15, 20, ...). Use a `while` loop to keep saving until you have at least 100 euros. Each week, print how much you saved and your total. At the end, print how many weeks it took.

Example output:

```text
Week 1: saved 10, total 10 euros
Week 2: saved 15, total 25 euros
Week 3: saved 20, total 45 euros
Week 4: saved 25, total 70 euros
Week 5: saved 30, total 100 euros
Goal reached in 5 weeks!
```

### Exercise 4: Squares between 10 and 50

**Folder:** [`squares-between-10-and-50`](squares-between-10-and-50/)

Print the squares of 1, 2, 3, ... one per line. Use a `for` loop with `range(1, 100)`. Use `continue` to skip squares smaller than 10. Use `break` to stop when a square is bigger than 50.

Example output:

```text
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
```

### Exercise 4 (advanced): Cubes between 10 and 500

**Folder:** [`squares-between-10-and-50-advanced`](squares-between-10-and-50-advanced/)

Print the cubes (`n * n * n`) of 1, 2, 3, ... one per line. Use a `for` loop with `range(1, 100)`. Use `continue` to skip cubes smaller than 10. When a cube is bigger than 500, print "Stopped at" and the number, then use `break`.

Example output:

```text
3 * 3 * 3 = 27
4 * 4 * 4 = 64
5 * 5 * 5 = 125
6 * 6 * 6 = 216
7 * 7 * 7 = 343
Stopped at 8
```

### Exercise 5: Skip the zeros

**Folder:** [`skip-the-zeros`](skip-the-zeros/)

Use a loop to print each score from the `scores` list in `exercise.py`, one per line. Skip every score that is 0.

Example output:

```text
10
25
8
3
```

### Exercise 5 (advanced): Clean shopping list

**Folder:** [`skip-the-zeros-advanced`](skip-the-zeros-advanced/)

Use a loop to go through the `items` list in `exercise.py`. Skip items that are empty or only spaces. Print the others without the extra spaces, starting with a capital letter.

Example output:

```text
Milk
Bread
Eggs
```

### Exercise 6: Wrong phone number

**Folder:** [`wrong-phone-number`](wrong-phone-number/)

A sign-up form collected the phone numbers in the `phones` list in `exercise.py`. Every valid number has exactly 11 digits. Use a loop to find the first number that doesn't. Save it in a variable, then print it after the loop.

Example output:

```text
First wrong number: 0162345678
```

### Exercise 6 (advanced): Wrong phone number and its position

**Folder:** [`wrong-phone-number-advanced`](wrong-phone-number-advanced/)

Every valid phone number has exactly 11 digits. Use a loop to find the first number in the `phones` list in `exercise.py` that doesn't, and count its position in the list (the first number is 1, the second is 2, ...). After the loop, print the number and its position. If every number is fine, print "All numbers look fine" instead.

Example output:

```text
First wrong number: 0162345678 (position 4)
```

### Exercise 7: Average score

**Folder:** [`average-score`](average-score/)

Use a loop to add up all the scores in the `scores` list in `exercise.py`. Then divide the total by the number of scores and print the average.

Example output:

```text
Average: 7.0
```

### Exercise 7 (advanced): Average of passing scores

**Folder:** [`average-score-advanced`](average-score-advanced/)

Only scores of 5 or more pass. Use a loop to add up the passing scores in the `scores` list in `exercise.py` and count them. Then print how many passed and their average.

Example output:

```text
Passing scores: 3
Average of passing scores: 8.0
```
