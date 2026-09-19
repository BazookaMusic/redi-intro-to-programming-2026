# Intro to Programming

Course slides for the 2026 Intro to Programming class at ReDI School, built with [Slidev](https://sli.dev/).

## Student slides

Choose a lesson below. These versions do not contain solutions.

| Lesson | PDF | Interactive HTML |
| --- | --- | --- |
| 01 · Git and GitHub | [Open PDF](slides_no_solutions/01-github-desktop.pdf) | [Download HTML](slides_no_solutions/01-github-desktop.html?raw=1) |

The PDF opens directly on GitHub. For the interactive version, download the HTML file and open it in a browser. It works offline.

## Teacher slides

These versions include exercise solutions:

| Lesson | PDF | Interactive HTML |
| --- | --- | --- |
| 01 · Git and GitHub | [Open PDF](slides_solutions/01-github-desktop.pdf) | [Download HTML](slides_solutions/01-github-desktop.html?raw=1) |

## Requirements

The following tools are only needed to edit or export the slides:

- Node.js 20.12 or newer
- npm

## Development

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

## Solutions

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

## Adding a deck

Add each new deck to `src/slides/`:

```text
src/slides/
├── 01-introduction.md
├── 02-variables.md
└── 03-conditionals.md
```

Each file is an independent Slidev deck with its own frontmatter and slides.

## Export student artifacts

```sh
npm run build
```

This temporarily generates the learner Markdown and exports every deck as a PDF and static HTML:

- `slides_solutions/` contains PDFs and HTML with solutions.
- `slides_no_solutions/` contains PDFs and HTML without solutions.

Each HTML deck is one self-contained file that works offline. These two root folders are for generated student artifacts only. Do not put source Markdown or development files in them.
