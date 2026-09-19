# Intro to Programming

Course slides for the 2026 Intro to Programming class at ReDI School, built with [Slidev](https://sli.dev/).

## Slides

Students can open the PDFs directly:

- [Git and GitHub slides](slides_no_solutions/01-github-desktop.pdf)
- [Git and GitHub slides with solutions](slides_solutions/01-github-desktop.pdf)

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
npm run dev:no-solutions -- src/slides_no_solutions/01-github-desktop.md
```

Slidev opens the selected deck in your browser. After changing a source deck, restart the no-solutions command to regenerate its learner version.

## Solutions

Always edit decks in `src/slides/`. The Markdown in `src/slides_no_solutions/` is generated, so do not edit it directly.

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

Then generate the learner Markdown:

```sh
npm run generate:no-solutions
```

This copies the decks and public assets to `src/slides_no_solutions/` and removes everything between the solution markers.

## Adding a deck

Add each new deck to `src/slides/`:

```text
src/slides/
├── 01-introduction.md
├── 02-variables.md
└── 03-conditionals.md
```

Each file is an independent Slidev deck with its own frontmatter and slides.

## Export PDFs

```sh
npm run build
```

This regenerates the learner Markdown and exports every deck as a PDF:

- `slides_solutions/` contains PDFs with solutions.
- `slides_no_solutions/` contains PDFs without solutions.

These two folders are for student artifacts only. Do not put Markdown, images, or development files in them.
