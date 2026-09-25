<h1 align="center">Intro to Programming</h1>

<p align="center">
	<img src=".github/assets/redi-copenhagen-banner.svg" width="720" alt="A cheerful laptop with code, Copenhagen buildings, and ReDI School colors">
</p>

**Welcome!** Pick a lesson, open it in your browser, and start exploring.

## Lessons

Choose a lesson below. The lesson name opens the browser slides without solutions.

| Lesson | Description | Teacher slides | PDFs |
| --- | --- | --- | --- |
| [01 · Git and GitHub](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/01-github-desktop.html) | Learn about files, folders, and paths, then use Git, GitHub Desktop, and the terminal to save and share code. | [With solutions](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/01-github-desktop.html) | [Without solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/01-github-desktop.pdf) · [With solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/01-github-desktop.pdf) |
| [02 · Variables and Data Types](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/02-variables.html) | Learn about print(), variables, the four basic data types, type conversion, and reading user input. | [With solutions](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/02-variables.html) | [Without solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/02-variables.pdf) · [With solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/02-variables.pdf) |

## Exercises

Practise at your own pace. Each exercise has its own folder with a starter file and tests.

| Exercises | Description |
| --- | --- |
| [Python for loops](exercises/python-for-loops/) | 10 exercises from easy to hard: `range()`, lists, adding up numbers, loops inside loops, shapes and grids. |

### How to use the exercises

Each exercise has its own folder. (A **directory** is the same thing as a folder.) In each folder you find three files:

- `README.md`: the task, the expected output, a hint and a link to the solution.
- `exercise.py`: write your code here. Some files already have code to start with.
- `test_exercise.py`: a **test**. A test is a small program that checks your code. Do not change it.

We use a tool called **pytest** to run the tests. Set it up once before your first exercise.

> [!IMPORTANT]
> Do not move the exercise folders. The tests only work if the folders stay where they are.

### Set up pytest (only once)

1. In VS Code, choose `File` > `Open Folder...` and open the `exercises` folder.
2. Choose `Terminal` > `New Terminal`. The terminal opens inside the `exercises` folder.
3. Run the setup script.

On macOS:

```sh
python3 setup_exercises.py
```

On Windows:

```sh
python setup_exercises.py
```

If `python` does not work on Windows, use `py` instead of `python` in every command.

When setup works, you see a message like this:

```text
Using Python 3.13.1
Installing pytest. This can take a minute...
Done! pytest 9.1.1 is installed.
You can now check your answers from any exercise folder:
    macOS:    python3 -m pytest
    Windows:  python -m pytest
```

You only do this once on each computer.

### Work on an exercise

1. In VS Code, choose `File` > `Open Folder...` and open the exercise folder, for example `exercises/python-for-loops/01-counting-sheep`. The list of all exercises is in [Python for loops](exercises/python-for-loops/).
2. Open `README.md` in the folder and read the task and the expected output. To see it nicely formatted, press `Ctrl+Shift+V` on Windows or `Cmd+Shift+V` on macOS.
3. Write your code in `exercise.py` and save the file.
4. Choose `Terminal` > `New Terminal`.
5. Run your code to see what it prints. Then run the tests.
6. Stuck? Open the **Hint** in the exercise's `README.md`. Try again before you open the **Solution** link.

On macOS:

```sh
python3 exercise.py
python3 -m pytest
```

On Windows:

```sh
python exercise.py
python -m pytest
```

### Read the test result

When your answer is correct, pytest shows a dot (`.`) for each test and the word `passed`:

```text
test_exercise.py ..                                                      [100%]

============================== 2 passed in 0.03s ===============================
```

When something is wrong, pytest shows `F` for each failed test and the word `failed`. Read the part under `FAILURES`. It shows what is different. For example:

```text
test_exercise.py F.                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_prints_numbers_from_1_to_5 ________________________
Your output has 4 lines, but 5 lines were expected.

Expected output:
    1
    2
    3
    4
    5

Your output:
    1
    2
    3
    4
=========================== short test summary info ============================
FAILED test_exercise.py::test_prints_numbers_from_1_to_5 - Failed: Your outpu...
========================= 1 failed, 1 passed in 0.03s ==========================
```

Change your code, save the file, and run the tests again.

Some tests also read your code. For example, `test_uses_a_for_loop` fails if your code has no for loop.

## For teachers

Use this section when adding, editing, previewing, or exporting slide decks.

### Requirements

The following tools are only needed to edit or export the slides:

- Node.js 20.12 or newer
- npm

### Development

Install the dependencies:

```sh
npm install
```

Start the deck with solutions:

```sh
npm run dev:solutions -- src/slides/01-github-desktop.md
```

Or start the generated deck without solutions:

```sh
npm run dev:no-solutions -- 01-github-desktop.md
```

Slidev opens the selected deck in your browser. The no-solutions command creates temporary Markdown and removes it when the preview closes.

### Solutions

Always edit decks in `src/slides/`. This is the only source copy.

Wrap each complete solution slide with these markers:

```md
<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution

The answer goes here.
<!-- solution:end -->
```

During preview or export, the build scripts create temporary learner Markdown and remove everything between the solution markers. The temporary files are deleted automatically.

### Adding a deck

Add each new deck to `src/slides/`:

```text
src/slides/
├── 01-introduction.md
├── 02-variables.md
└── 03-conditionals.md
```

Each file is an independent Slidev deck with its own frontmatter and slides.

### Export student artifacts

```sh
npm run build
```

This temporarily generates the learner Markdown and exports every deck as a PDF and static HTML:

- `slides_solutions/` contains PDFs and HTML with solutions.
- `slides_no_solutions/` contains PDFs and HTML without solutions.

Each HTML deck is one self-contained file that works offline. These two root folders are for generated student artifacts only. Do not put source Markdown or development files in them.

### Adding exercises

Exercises live in `exercises/`, grouped by topic:

```text
exercises/
├── conftest.py              # shared pytest fixtures
├── pytest.ini               # pytest settings for every exercise
├── setup_exercises.py       # installs pytest for students
└── python-for-loops/
    ├── README.md            # overview, key words, list of exercises
    ├── 01-counting-sheep/
    │   ├── README.md        # task, expected output, hint, solution link
    │   ├── exercise.py      # starter file students edit
    │   └── test_exercise.py # pytest tests for exercise.py
    └── solutions/
        └── 01-counting-sheep/
            └── exercise.py  # solution, same file name as the starter
```

- Give each exercise a zero-padded folder, such as `01-counting-sheep`, with an `exercise.py` starter file and a `test_exercise.py` file.
- Test output with the `check_program` fixture. Test the rules in separate tests that read the file: `check_uses_for_loop` requires a for loop, and `check_does_not_use` bans names such as `max`.
- When students build a grid, give the starter file a function that returns it, and test the function with `check_grid` for several sizes. Printing a hardcoded answer then cannot pass.
- Put each exercise's task, expected output, and hint in a `README.md` in its folder. Put the hint in a `<details>` block. List every exercise in the topic README, and link each exercise to the next one.
- Write hints as nudges, such as a guiding question or a pattern to notice. Never put solution code or step-by-step instructions in a hint.
- Put each solution in `solutions/<exercise-folder>/` with the same file name as the starter, and link to it from the exercise README. Students open only the exercise folder, so the solution stays out of sight until they look for it.
- Make sure every starter file fails its tests and every solution passes them. From the topic folder, run the tests on the starter files, then on the solutions:

```sh
python3 -m pytest
python3 -m pytest --solutions
```
