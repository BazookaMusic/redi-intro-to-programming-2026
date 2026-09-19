# Project Guidelines

## Purpose and audience

- This repository contains Slidev lessons for beginner programming students at ReDI School.
- Use concise, plain language. Define jargon before using it and introduce one main idea at a time.
- Use **folder** as the primary learner-facing term. Explain once that **directory** means the same thing when the distinction matters.
- Keep literal application labels exact, such as `Open Folder...`.
- Keep instructions usable on Windows and macOS. Call out platform differences when commands or UI steps differ.
- Show commands in fenced code blocks so Slidev provides a copy button. Terminal examples should look realistic and match the taught sequence.

## Deck structure

- Treat `src/slides/` as the only editable source for decks and public assets.
- The no-solutions Markdown is generated in a temporary folder during preview or export and deleted automatically. Do not create or maintain a second source tree.
- Keep the root `slides_solutions/` and `slides_no_solutions/` directories artifact-only. They may contain exported PDFs and self-contained HTML files, never source Markdown or development files.
- After changing a source deck, asset, or theme, run `npm run build` and include both updated PDFs and HTML builds in the commit.
- Store images under `src/slides/public/images/` and reference them as `/images/...` in slide Markdown.
- Each Markdown file is an independent Slidev deck and must retain its document frontmatter.

## Development process

1. Run `npm install` after cloning the repository or when dependencies change.
2. Edit the source deck in `src/slides/`, shared assets in `src/slides/public/`, and only the theme owned by the deck author.
3. Preview the deck with solutions:

```sh
npm run dev:solutions -- src/slides/<deck>.md
```

4. Preview the generated learner deck without solutions:

```sh
npm run dev:no-solutions -- <deck>.md
```

5. Run `npm run build` to regenerate the solution and no-solution PDFs and self-contained HTML files for every deck.
6. Verify the four matching artifacts in `slides_solutions/` and `slides_no_solutions/`, then update the README lesson links and description when adding or renaming a deck.
7. Commit the source deck, owned assets or theme changes, README update, and generated artifacts together. Never commit temporary learner Markdown, `node_modules/`, or `dist/`.

## Adding a slide deck

- Create the deck as a top-level `src/slides/<NN>-<topic>.md` file. Use a zero-padded lesson number so decks sort in teaching order; the export script discovers only top-level `.md` files.
- Start from a nearby deck and keep the complete Slidev document frontmatter. The source filename becomes the filename of every generated PDF and HTML file.
- Put shared images in `src/slides/public/images/`. Use the deck owner's theme for reusable styles; do not edit another user's theme.
- Keep exercises outside solution markers and wrap each complete solution slide as described below.
- Preview both variants:

```sh
npm run dev:solutions -- src/slides/<deck>.md
npm run dev:no-solutions -- <deck>.md
```

- Run `npm run build`, then confirm that matching `<deck>.pdf` and `<deck>.html` files exist in both `slides_solutions/` and `slides_no_solutions/`.
- Add the lesson to the README table. Link the lesson name to the no-solutions GitHub Pages HTML file by default, add a separate `With solutions` HTML link, include a short description grounded in the deck's learning goals, and link both generated PDFs with absolute `raw.githubusercontent.com` URLs so they download reliably.
- Include the source deck, shared assets, README update, and all four generated artifacts in the same change.

## Exercises and solutions

- Exercise slides belong in both deck variants and must remain outside solution markers.
- Wrap the complete solution slide, including its leading `---` separator, with the exact markers documented in `README.md`:

```md
<!-- solution:start -->
---
class: knowledge-check-slide knowledge-solution-slide
---

# Solution

The answer goes here.
<!-- solution:end -->
```

- Use `knowledge-solution-slide` on solution slides for styling and semantics. The generator removes content by markers, not by title or class.
- Keep every start marker paired with one end marker. Do not nest solution markers.

## Design and code conventions

- Reuse established slide classes and layouts before introducing new ones.
- Treat each folder under `themes/` as owned by a GitHub user. Never modify another user's theme unless that owner explicitly requests it.
- `themes/clio/` belongs to GitHub user `bazookamusic`. Other contributors must use their own theme or keep one-off styles local to their deck.
- Put styles reused by multiple slides in the deck owner's theme. Keep a slide-local `<style>` block only for genuinely one-off layout rules.
- Preserve the existing visual language, CSS variables, spacing, and local formatting style.
- Use semantic HTML and meaningful image alt text.
- Keep slide content comfortably inside the fixed canvas. Leave generous space below content so browser controls or the macOS Dock cannot cover it in fullscreen; avoid overflow, overly small text, and dense paragraphs.
- Avoid unrelated refactors and do not edit generated dependencies or build artifacts.

## Validation

- Run `npm run build` after deck, theme, asset, script, or package changes. It must export matching PDFs and self-contained HTML files under `slides_solutions/` and `slides_no_solutions/`.
- Use `npm run dev:solutions -- src/slides/<deck>.md` to preview the source deck.
- Use `npm run dev:no-solutions -- <deck>.md` to generate a temporary learner deck and preview it.
- Do not commit `node_modules/` or `dist/`.
