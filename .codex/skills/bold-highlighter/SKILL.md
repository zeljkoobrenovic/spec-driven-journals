---
name: bold-highlighter
description: Add concise bold emphasis to articles, blog posts, markdown notes, documentation pages, and long-form prose so skim readers can catch the main argument. Use when asked to highlight key phrases, make an article more skimmable, add bold emphasis, improve skim reading, or apply a "bold highlighter" pass to prose while preserving the author's wording and structure.
---

# Bold Highlighter

## Goal

Add a restrained skim path through the article using Markdown bold emphasis. Preserve the author's argument, voice, headings, and structure unless the user also asks for rewriting.

## Workflow

1. Read the article enough to identify the thesis, section claims, contrasts, risks, practical rules, and closing takeaway.
2. Add `**bold**` to phrases that carry those ideas.
3. Prefer shorter highlighted spans where they still make sense. Bold the decisive phrase, not the whole sentence.
4. Keep the result readable for people who read normally and useful for people who skim.
5. Validate that Markdown bold markers are balanced and that code, front matter, links, and tables still render correctly.

## Highlighting Rules

- Highlight the article's **thesis**, **main distinctions**, **operating principles**, **warnings**, **decision criteria**, and **final takeaway**.
- Prefer 2-7 word highlights. Use longer highlights only for a compact thesis or decisive question.
- Use 1-2 highlighted phrases per dense paragraph at most. Many paragraphs need none.
- In key-points blocks or summaries, add 1-2 bold phrases per bullet.
- In lists, bold the label or governing idea, not every explanation.
- In tables, bold sparingly. Avoid cluttering comparison tables unless emphasis clarifies a decisive contrast.
- Preserve existing bold if it already works. Replace or shorten existing bold only when it is too broad.
- Do not bold headings just to add emphasis; headings are already prominent.
- Do not bold code, command names, YAML front matter, URLs, or fenced code blocks.
- Do not split Markdown links. If a linked title itself needs emphasis, wrap the whole link: `**[Title](url)**`.

## What To Highlight

Good targets:

- Clear claims: `**the model is part of the product material**`
- Contrasts: `**better model does not mean better product**`
- Operating questions: `**Should this still exist in this shape?**`
- Constraints: `**evaluation before enthusiasm**`
- Risks: `**a false sense of progress**`
- Stable concepts: `**durable product identity**`
- Repeated section motifs that help orientation: `**short seasons**`, `**unstable model materials**`, `**customer evidence**`

Weak targets:

- Generic intensifiers: "very important", "significant", "major"
- Long clauses that include filler words
- Proper nouns unless the name itself is the point
- Whole paragraphs or long sentences
- Every occurrence of a repeated term

## Editing Discipline

- Preserve wording unless a tiny grammar fix is necessary to make the highlighted phrase read cleanly.
- Do not create a one-note article where every paragraph has bold text.
- Keep highlighted phrases shorter when the surrounding sentence already provides context.
- Avoid stacking bold phrases back-to-back in a way that makes the prose look shouted.
- Keep emphasis consistent: if the article's core term is highlighted once in a section, do not highlight every repetition.

## Validation

After editing:

- Run a quick count or scan to confirm `**` markers are balanced.
- Check nearby Markdown around links, lists, blockquotes, and tables.
- Rebuild or render the article if the repo has a normal build command.
- Report that the pass was editorial only unless content was also changed.
