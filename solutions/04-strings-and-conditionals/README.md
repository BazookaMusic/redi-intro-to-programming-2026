# 04 · Strings and Conditionals solutions

Try the [exercises](../../exercises/04-strings-and-conditionals/README.md) first, then check your work here. The solutions for the Python tasks are in the task folders above.

## Classroom exercises

### Predict the output

**Snow, 2°, windy** prints `🧥 Wear a hood, it's windy!`

- `"snow"` matches the outer `if`, so Python goes inside.
- `2 < 0` is `False`, so the first inner check fails.
- `wind == "yes"` is `True`, so the `elif` runs.

**Sun, -5°** prints `🧤 Wear gloves!`

- `"sun"` is not rain or snow, so Python skips the whole inner block.
- `-5 < 0` is `True`, so the outer `elif` runs.
