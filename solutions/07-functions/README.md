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

### Pizza slices

[Solved program](pizza-slices/exercise.py)

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

### Circle area

[Solved program](circle-area/exercise.py)

### Pokemon stats

[Solved program](pokemon-stats/exercise.py)

### Mini project: Pokemon battle

[Solved program](mini-project-pokemon-battle/exercise.py)

Both function bodies and both loop gaps are completed. The supplied lookup-error
handling is unchanged. The game fetches each fighter's data before the battle,
not on every turn.

For the Pokemon programs, follow the exercise README's
[real-data setup](../../exercises/07-functions/README.md#running-the-pokemon-programs-with-real-data)
in the folder where you run the solution. The matching checkers also work offline.

## Teacher note

The lesson uses `pokebase==1.4.1`. A live check found that `pypokedex==1.6.0`
fails while parsing changed sprite data from PokeAPI, before returning the stats.
`pokebase` was checked against live stats and a complete battle.
External services can change; try the live example before teaching the lesson.
