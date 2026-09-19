# Intro to Programming

Course slides for the 2026 Intro to Programming class at ReDI School, built with [Slidev](https://sli.dev/).

## Requirements

- Node.js 20.12 or newer
- npm

## Development

Install the dependencies:

```sh
npm install
```

Start the deck with solutions:

```sh
npm run dev:solutions -- slides_solutions/01-github-desktop.md
```

Or start the generated deck without solutions:

```sh
npm run dev:no-solutions -- slides_no_solutions/01-github-desktop.md
```

Slidev opens the selected deck in your browser. After changing a source deck, restart the no-solutions command to regenerate its learner version.

## Solutions

Always edit decks in `slides_solutions/`. The files in `slides_no_solutions/` are generated, so do not edit them directly.

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

Then generate the learner decks:

```sh
npm run generate:no-solutions
```

This copies the decks and public assets to `slides_no_solutions/` and removes everything between the solution markers.

## Adding a deck

Add each new deck to `slides_solutions/`, then run the generation command:

```text
slides_solutions/
├── 01-introduction.md
├── 02-variables.md
└── 03-conditionals.md
```

Each file is an independent Slidev deck with its own frontmatter and slides.

## Production build

```sh
npm run build
```

This regenerates the learner decks and builds both versions under `dist/solutions/` and `dist/no-solutions/`.
