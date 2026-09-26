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
| [03 · Arithmetic and User Input](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/03-arithmetic.html) | Learn arithmetic operators, order of operations, abs() and round(), reading keyboard input, and converting between types. | [With solutions](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/03-arithmetic.html) | [Without solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/03-arithmetic.pdf) · [With solutions](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/03-arithmetic.pdf) |

## Practice

[Lesson 03's mini project and homework](exercises/03-arithmetic-and-user-input/) have one folder per task. You need Python 3 to work on them. Open a folder, read the instructions at the top of `exercise.py`, and write your code below them. Open a terminal in that folder to check your work.

On macOS:

```sh
python3 check.py
```

On Windows:

```sh
py check.py
```

If you copy an exercise, keep `exercise.py` and `check.py` together in the same folder. You do not need any other files. Run the checker with Python as shown above, not with `./check.py`; this avoids executable-permission errors.

Use `input("...")` to ask questions and `print()` for the requested answer lines. The checker supplies any requested input. If the answers do not match, it shows what it expected and what your program printed.

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
