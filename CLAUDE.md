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
- Never edit `src/slides_no_solutions/` directly. It is a generated, ignored intermediate directory.
- Keep the root `slides_solutions/` and `slides_no_solutions/` directories artifact-only. They may contain exported PDFs, never Markdown, images, or development files.
- After changing a source deck, asset, or theme, run `npm run build` and include both updated PDFs in the commit.
- Store images under `src/slides/public/images/` and reference them as `/images/...` in slide Markdown.
- Each Markdown file is an independent Slidev deck and must retain its document frontmatter.

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
- Put styles reused by multiple slides in `themes/clio/styles/clio.css`. Keep a slide-local `<style>` block only for genuinely one-off layout rules.
- Preserve the existing visual language, CSS variables, spacing, and local formatting style.
- Use semantic HTML and meaningful image alt text.
- Keep slide content within the fixed canvas: avoid overflow, overly small text, and dense paragraphs.
- Avoid unrelated refactors and do not edit generated dependencies or build artifacts.

## Validation

- Run `npm run generate:no-solutions` after source changes. Confirm the command reports the expected number of removed solution slides.
- Run `npm run build` after deck, theme, asset, script, or package changes. It must export matching PDFs under `slides_solutions/` and `slides_no_solutions/`.
- Use `npm run dev:solutions -- src/slides/<deck>.md` to preview the source deck.
- Use `npm run dev:no-solutions -- src/slides_no_solutions/<deck>.md` to regenerate and preview the learner deck.
- Do not commit `node_modules/` or `dist/`.
