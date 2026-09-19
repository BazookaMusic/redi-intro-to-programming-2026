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

Start a presentation by passing its Markdown file:

```sh
npm run dev -- slides/01-introduction.md
```

Slidev opens the deck in your browser and updates it as you edit the file.

## Adding a deck

Add a uniquely named Markdown file to `slides/`, for example:

```text
slides/
├── 01-introduction.md
├── 02-variables.md
└── 03-conditionals.md
```

Each file is an independent Slidev deck with its own frontmatter and slides.

## Production build

```sh
npm run build
```

All decks are built to separate folders under `dist/`, named after their Markdown files.
