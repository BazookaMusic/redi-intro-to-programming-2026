<h1 align="center">Intro to Programming</h1>

<p align="center">
	<img src=".github/assets/redi-copenhagen-banner.svg" width="720" alt="A cheerful laptop with code, Copenhagen buildings, and ReDI School colors">
</p>

**Welcome!** Pick a lesson, open it in your browser, and start exploring.

## Lessons

Choose a lesson below. Open the slides in your browser or download them as a PDF.

| Lesson | Description | Slides |
| --- | --- | --- |
| 01 · Git and GitHub | Learn about files, folders, and paths, then use Git, GitHub Desktop, and the terminal to save and share code. | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/01-github-desktop.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/01-github-desktop.pdf) |
| 02 · Variables and Data Types | Learn about print(), variables, the four basic data types, type conversion, and reading user input. | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/02-variables.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/02-variables.pdf) |
| 03 · Arithmetic and User Input | Learn arithmetic operators, order of operations, abs() and round(), reading keyboard input, and converting between types. | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/03-arithmetic.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_no_solutions/03-arithmetic.pdf) |

<details>
<summary><strong>Show slides with solutions</strong></summary>

These slides include the answers. Try the questions first!

| Lesson | Slides with solutions |
| --- | --- |
| 01 · Git and GitHub | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/01-github-desktop.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/01-github-desktop.pdf) |
| 02 · Variables and Data Types | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/02-variables.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/02-variables.pdf) |
| 03 · Arithmetic and User Input | [Open](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_solutions/03-arithmetic.html) · [PDF](https://raw.githubusercontent.com/BazookaMusic/redi-intro-to-programming-2026/main/slides_solutions/03-arithmetic.pdf) |

</details>

## Exercises

Lesson 01's exercises are in one README. From Lesson 02, each exercise folder has `exercise.py` for your code and `check.py` to check your answer. To run a Python exercise, follow [How to clone this repository to get access to exercises](#clone-repository), then [How to do exercises and check my answers](#do-exercises).

| Lesson | Exercises |
| --- | --- |
| 01 · Git and GitHub | [Open exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/01-git-and-github) |
| 02 · Variables and Data Types | [Open exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/02-variables-and-data-types) |
| 03 · Arithmetic and User Input | [Open exercises](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/exercises/03-arithmetic-and-user-input) |

<details>
<summary><strong>Show exercise solutions</strong></summary>

These folders contain the answers. Try the exercises first!

| Lesson | Solutions |
| --- | --- |
| 01 · Git and GitHub | [Open solutions](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/solutions/01-git-and-github) |
| 02 · Variables and Data Types | [Open solutions](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/solutions/02-variables-and-data-types) |
| 03 · Arithmetic and User Input | [Open solutions](https://github.com/BazookaMusic/redi-intro-to-programming-2026/tree/main/solutions/03-arithmetic-and-user-input) |

</details>

## Tutorials

Click a tutorial title to expand it and see the instructions.

<details id="clone-repository">
<summary><strong>How to clone this repository to get access to exercises</strong></summary>

You need [Git](https://git-scm.com/downloads) to copy the repository.

### Open a terminal

On Windows, open **Start**, search for **PowerShell**, and press Enter. On macOS, open **Applications → Utilities → Terminal**. A terminal is where you type commands.

Type the commands below one line at a time. Press **Enter** after each line to run it, and wait for it to finish before typing the next line. Text after `#` is a note for you; the terminal ignores it.

### Make a folder in Documents

On Windows (PowerShell):

```powershell
cd "$HOME\Documents"  # Go to Documents
mkdir "ReDI Projects" # Make a new folder
cd "ReDI Projects"    # Go into the new folder
```

On macOS:

```sh
cd "$HOME/Documents"  # Go to Documents
mkdir "ReDI Projects" # Make a new folder
cd "ReDI Projects"    # Go into the new folder
```

If `ReDI Projects` already exists, skip the `mkdir` command. If Windows cannot find Documents, open it in File Explorer and use its full path in quotes for the first `cd` command.

### Clone the repository

In your new `ReDI Projects` folder, run these commands on either computer:

```sh
git clone https://github.com/BazookaMusic/redi-intro-to-programming-2026.git # Copy the repository
cd redi-intro-to-programming-2026 # Go into the copied folder
```

You now have a copy of the repository in Documents → ReDI Projects.

</details>

<details id="do-exercises">
<summary><strong>How to do exercises and check my answers</strong></summary>

### Work on an exercise in VS Code

You need Python 3 and VS Code. After [cloning the repository](#clone-repository):

1. In VS Code, choose **File → Open Folder...**.
2. Browse to **Documents → ReDI Projects → redi-intro-to-programming-2026 → exercises**. Choose a lesson, then open one exercise folder. You should see `exercise.py` and `check.py` in VS Code.
3. Open `exercise.py`, write your code below the instructions, and save it with **Ctrl+S** (Windows) or **Command+S** (macOS).
4. Choose **Terminal → New Terminal** in VS Code. The terminal opens at the bottom, in your exercise folder.

On macOS, type this in the VS Code terminal and press Enter:

```sh
python3 check.py
```

On Windows, type this in the VS Code terminal and press Enter:

```powershell
py check.py
```

</details>

## For teachers

<details>
<summary>Show teacher instructions</summary>

Use this section when adding, editing, previewing, or exporting slide decks.

### Practice solutions

The solved exercises in `solutions/` mirror the student exercise folders. For Python lessons, each task folder contains only a completed `exercise.py`; the matching `check.py` stays in `exercises/`. Lessons without Python tasks use one `README.md` for exercises and one for solutions.

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

</details>
