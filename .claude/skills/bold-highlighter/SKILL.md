---
name: bold-highlighter
description: Add restrained bold emphasis to a post's prose (index.md or a modality file) so skim readers catch the main argument, preserving the author's wording, voice, and structure. Use when asked to highlight key phrases, make a post more skimmable, add bold emphasis, or apply a "bold highlighter" pass in _journals/*/posts/*/.
---

# Bold Highlighter

## Goal

Add a restrained skim path through a post's prose using Markdown `**bold**`
emphasis, so a reader skimming bold phrases catches the argument. Preserve the
author's wording, voice, headings, and structure — this is an **editorial pass,
not a rewrite** unless the user also asks for rewriting.

Operates on any prose file in a post folder: usually `index.md`, but also
`summary.md` or `dialog.md` when asked. It does not generate images or touch
`comics.md` panel art.

## Contract rules

- **`spec.md` is the contract; never edit it from this skill.** Emphasis must
  respect the spec's Audience and tone. A private reflective note wants *very*
  light emphasis (it is read slowly, not skimmed); an ADR or strategy post can
  carry more. Match the post's register before reaching for bold.
- **Preserve wording.** Only make a tiny grammar fix if it is needed to make a
  highlighted phrase read cleanly, and say so.
- **The renderer treats post content as trusted markdown** (`post.html`), so
  `**bold**` works inline anywhere normal markdown does — including inside table
  cells and list items. It does not work inside fenced code.
- Edit only the requested prose file. Do not touch `config.yaml`, the spec, or
  other modalities unless asked.

## Workflow

1. Read the target file (and skim `spec.md` for Audience/tone) enough to find the
   thesis, section claims, contrasts, risks, operating rules, and closing
   takeaway.
2. Add `**bold**` to the phrases that carry those ideas.
3. Prefer the shortest span that still reads — bold the **decisive phrase**, not
   the whole sentence.
4. Keep it readable for normal readers and useful for skimmers; most paragraphs
   need no bold at all.
5. Validate: `**` markers balanced; links, lists, blockquotes, tables, and the
   ADR status-highlight blockquote still render; no bold leaked into code or
   front matter.
6. Run `python3 _wiring/build.py` and confirm `[built] <journal>`. Report that
   the pass was **editorial only** (unless you also changed content).

## Highlighting rules

- Highlight the **thesis**, **main distinctions**, **operating principles**,
  **warnings**, **decision criteria**, and the **final takeaway**.
- Prefer **2–7 word** highlights. Use longer ones only for a compact thesis or a
  decisive question.
- At most **1–2 highlighted phrases per dense paragraph**; many paragraphs need
  none.
- In summaries or key-points blocks, 1–2 bold phrases per bullet.
- In lists, bold the **label or governing idea**, not every explanation.
- In tables, bold sparingly — only a decisive contrast.
- Preserve existing bold that works; only shorten or replace bold that is too
  broad.
- Do **not** bold headings (already prominent), code, command names, YAML front
  matter, or URLs.
- Do not split a Markdown link. If a linked title needs emphasis, wrap the whole
  link: `**[Title](url)**`. The same applies to cross-links — keep `[[name]]`
  intact; wrap the whole token if it must be emphasized.

## What to highlight

**Good targets:**

- Clear claims — `**relief is data, not a verdict**`
- Contrasts — `**reasons it is hard to leave, not reasons to stay**`
- Operating questions — `**would I freely choose this exact life again?**`
- Constraints / rules — `**prepare, do not leave**`
- Stable concepts the post returns to — `**the root**`, `**the funeral feeling**`
- A decisive closing takeaway

**Weak targets (avoid):**

- Generic intensifiers — "very important", "significant", "major"
- Long clauses padded with filler
- Proper nouns, unless the name itself is the point
- Whole paragraphs or long sentences
- Every occurrence of a repeated term — highlight it once per section at most

## Editing discipline

- Do not create a one-note post where every paragraph is bolded — that destroys
  the skim path it is meant to create.
- Keep highlighted phrases shorter when the surrounding sentence already gives
  context.
- Avoid stacking bold phrases back-to-back; it reads as shouting.
- Keep emphasis consistent: a core term bolded once in a section should not be
  bolded on every repetition.
- For posts with an existing ADR **Status / Decision** highlight blockquote, that
  block is already the scannable summary — do not pile extra bold into it.

## Anti-patterns

- Rewriting prose or "improving" wording under cover of a highlight pass.
- Editing `spec.md`, `config.yaml`, or unrequested modality files.
- Heavy emphasis on a private reflective post that is meant to be read slowly.
- Bolding inside fenced code, front matter, or URLs.
- Breaking a `[link](url)` or `[[cross-link]]` by bolding only part of it.
- Skipping the build / not reporting that the change was editorial only.
