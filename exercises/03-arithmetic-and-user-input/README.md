# 03 · Arithmetic and User Input exercises

These exercises come from the [Arithmetic and User Input slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/03-arithmetic.html). When you finish, compare your work with the [solutions](../../solutions/03-arithmetic-and-user-input/).

New to this? Follow [How to clone this repository to get access to exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026#clone-repository) and [How to do exercises and check my answers](https://github.com/BazookaMusic/redi-intro-to-programming-2026#do-exercises) first.

## VAT calculator

**Folder:** [`vat-calculator`](vat-calculator/)

VAT is a tax that is added to a price. Ask the user to enter a price. Add 21% VAT: `total = price * 1.21`

Round the total to 2 decimal places and print one line in this format:
`Price with VAT: €[total]`

Example input: 10

Example output:

```text
Price with VAT: €12.1
```

## Mini project: Personal calculator

**Folder:** [`mini-project-calculator`](mini-project-calculator/)

Ask the user for two numbers. Print their sum, difference (first minus second), product, quotient rounded to 2 decimal places, remainder, and first number to the power of the second number, in that order. Label the six lines `Sum`, `Difference`, `Product`, `Quotient`, `Remainder`, and `Power`, with a colon after each label. The second number will not be zero.

Example input: 10, then 3

Example output:

```text
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.33
Remainder: 1.0
Power: 1000.0
```

## Homework 1: All operators

**Folder:** [`homework-01-all-operators`](homework-01-all-operators/)

Create `a = 17` and `b = 5`. Print the results of all seven operations: addition, subtraction, multiplication, division, whole-number division, remainder, and power, in that order. Label the lines `Sum`, `Difference`, `Product`, `Quotient`, `Whole number division`, `Remainder`, and `Power`, with a colon after each label.

Example output:

```text
Sum: 22
Difference: 12
Product: 85
Quotient: 3.4
Whole number division: 3
Remainder: 2
Power: 1419857
```

## Homework 2: Average

**Folder:** [`homework-02-average`](homework-02-average/)

Create three test scores: `score1 = 70`, `score2 = 85`, and `score3 = 90`. Calculate their average and round it to 1 decimal place. Print one line with the label `"Average:"`.

Example output:

```text
Average: 81.7
```

## Homework 3: abs() practice

**Folder:** [`homework-03-temperature-difference`](homework-03-temperature-difference/)

Create `morning_temp = -3` and `afternoon_temp = 9`. Use `abs()` to print the positive difference between the temperatures. Print one line with the label `"Temperature difference:"`.

Example output:

```text
Temperature difference: 12
```

## Homework 4: Discount calculator

**Folder:** [`homework-04-discount-calculator`](homework-04-discount-calculator/)

Ask the user for a price and a discount percentage. A discount of 15 means 15% off. Calculate the final price after the discount and round it to 2 decimal places. Print one line with the label `"Final price:"`.

Example input: 80 for the price, then 15 for the discount percentage

Example output:

```text
Final price: 68.0
```

## Homework 5: BMI calculator

**Folder:** [`homework-05-bmi-calculator`](homework-05-bmi-calculator/)

Ask the user for their weight in kilograms and height in metres. Calculate BMI: `weight / height ** 2`. Round it to 1 decimal place. Print one line with the label `"BMI:"`.

Example input: 70 for the weight, then 1.75 for the height

Example output:

```text
BMI: 22.9
```

## Homework 6: Seconds converter

**Folder:** [`homework-06-seconds-converter`](homework-06-seconds-converter/)

Ask the user for a whole number of seconds. Use `//` to find the number of full minutes and `%` to find the leftover seconds. Print two lines with the labels `"Minutes:"` and `"Seconds:"`.

Example input: 125

Example output:

```text
Minutes: 2
Seconds: 5
```

## Homework 7: Extend the personal calculator

**Folder:** [`homework-07-extended-calculator`](homework-07-extended-calculator/)

Ask the user for two numbers. Print their sum, difference (first minus second), product, quotient rounded to 2 decimal places, remainder, first number to the power of the second number, and whole-number division (first `//` second), in that order. Label the seven lines `Sum`, `Difference`, `Product`, `Quotient`, `Remainder`, `Power`, and `Whole number division`, with a colon after each label. The second number will not be zero.

Example input: 10, then 3

Example output:

```text
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.33
Remainder: 1.0
Power: 1000.0
Whole number division: 3.0
```
