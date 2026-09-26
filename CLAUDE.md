# Claude Code Instructions

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
- Add the lesson to the README using its current layout. Include its title, a short description grounded in the deck's learning goals, and links to both HTML and PDF versions with and without solutions. Use GitHub Pages URLs for HTML and absolute `raw.githubusercontent.com` URLs for PDFs.
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

## Standalone practice exercises

- If a deck includes exercises, create standalone exercises **and solutions for every in-class and take-home task**, including homework and projects; add bonus exercises when requested.
- In each lesson's exercise `README.md` and any README-based solutions file, list homework first under `## Homework`, in homework-number order. Then list the tasks done during the lesson under `## Classroom exercises`, in slide order. Put extra bonus tasks that are not in the slides last, under `## Bonus`. Use `###` headings for the tasks.
- Mirror each task under `exercises/<NN>-<lesson-title>/<task-name>/` and `solutions/<NN>-<lesson-title>/<task-name>/`. The student folder contains an unsolved `exercise.py` and a standalone `check.py`; the solution folder contains only a simply solved `exercise.py`.
- For lessons without Python tasks, such as Git or terminal practice, put all tasks in `exercises/<NN>-<lesson-title>/README.md` and their answers in `solutions/<NN>-<lesson-title>/README.md` instead.
- A Python lesson can also include tasks that need no code, such as telling expressions and statements apart. Describe them only in the lesson's exercise `README.md`, with no task folder, and put their answers in `solutions/<NN>-<lesson-title>/README.md`. When you insert a homework task, renumber the later homework headings, folders, starter comments, and tests so the numbers still match.
- For Python lessons, add `exercises/<NN>-<lesson-title>/README.md` that links to the root README tutorials for cloning and checking answers, then lists every task using the grouping above, with a link to its folder and the description and example output copied from its `exercise.py` comments. Update it whenever a task's comments change.
- Start each student `exercise.py` with a plain-language task in comments, at least one accurate example output (and sample input if needed), and `# Write your solution below.` Use only concepts taught so far.
- Make each `check.py` work with only the two files in its folder: no shared helper or third-party packages. Supply test input when the task uses `input()`, compare printed output, and show both expected and actual output on failure. Accept students' own values where the task lets them choose.
- Test by copying each `check.py` with its matching solved `exercise.py` into a temporary folder and running the checker. Also check that an unsolved starter fails with helpful feedback.
- Keep the student-facing README exercise links up to date: link each lesson's exercise `README.md` and solutions parent folder (or solutions `README.md`), not each task. Explain how to open a task folder in VS Code and run `check.py` using **Terminal → New Terminal**.

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
