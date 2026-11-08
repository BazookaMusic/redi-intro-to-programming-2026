# Functions: solutions

Try the [exercises](../../exercises/07-functions/README.md) first.
Each task folder contains a solved `exercise.py`. To check it, copy it and the
matching student `check.py` into a separate folder, then run `check.py`.

## Homework

### Homework 1: Ticket prices

[Solved program](homework-01-ticket-prices/exercise.py)

### Homework 2: High scores

[Solved program](homework-02-high-scores/exercise.py)

### Homework 3: Average score

[Solved program](homework-03-average-score/exercise.py)

### Homework 4: Roll a die

[Solved program](homework-04-roll-a-die/exercise.py)

## Classroom exercises

### Draw a face

[Solved program](draw-a-face/exercise.py)

Other choices of eyes and mouth are valid.

### Shopping budget

[Solved program](shopping-budget/exercise.py)

### Trace execution and scope

The output is:

```text
3
3
10
```

Inside the function call, the parameter `value` is `1`, so `result` is `3`.
The caller saves the returned `3` in `answer`. The global `value` stays `10`.

`result` is a local name: using it outside the function would cause a `NameError`.
Returning the value does not expose the local name to the caller.

### Lunch picker

[Solved program](lunch-picker/exercise.py)

### Words for Hangman

[Solved program](hangman-words/exercise.py)

### Mini project: Hangman

[Solved program](mini-project-hangman/exercise.py)

The three required functions are completed; `lives_bar` is supplied in the starter.
The skeleton reaches the player on the sixth mistake.

For Hangman, follow the exercise README's
[library setup](../../exercises/07-functions/README.md#running-hangman-with-the-english-word-collection)
in the folder where you run the solution. The matching checker works offline.
