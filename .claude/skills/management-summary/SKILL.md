---
name: management-summary
description: Write the management-summary modality (summary.md) of a spec-driven journal post from its spec.md and index.md, rendered as the Summary tab on the post page. Use when asked to add, write, or update a management summary, executive summary, TL;DR, or summary tab for a post in _journals/*/posts/*/.
---

# Management Summary (the `summary` modality)

## Goal

Write `summary.md` next to a post's `index.md` — a management summary that
renders as the **Summary** tab on the same post page. The audience is a
leader deciding whether this record affects them, not a reader of the full
article.

## Contract rules

- `spec.md` is the contract; `index.md` is the source content. **Never edit
  either from this skill.** If the article and spec disagree, flag the drift
  and summarize the *article* (it is what readers see), noting the mismatch
  to the user.
- The summary must not introduce claims that appear in neither the spec nor
  the article.

## Workflow

1. Read `spec.md` (Intent, Success criteria, Non-goals) and `index.md` in the
   target post folder. The post must already have an `index.md` — if not,
   write the article first (see the `detailed-article` skill).
2. Write `summary.md` in the format below.
3. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` contains `"key": "summary"`.
4. Tell the user the Summary tab is live at `<permalink>.html#summary`.

## Format

- **Length**: 300–500 words. If it wants to be longer, it is not a summary.
- **No title heading** — the post header (title, byline, tags, hero) is
  shared by all tabs. Start directly with content.
- **Optional front matter**: `timetoread: "2 min read"` (stored, not yet
  rendered).
- **Shape**:
  1. Open with the decision/principle itself in at most two sentences — a
     reader who stops here still knows the direction. (Source: the spec's
     Intent + the article's highlight blockquote.)
  2. `**What changes**` — 3–5 bullets: concrete consequences, keyed to the
     spec's Success criteria.
  3. `**What it costs**` — 1–3 bullets: trade-offs, obligations, or risks
     accepted (from the article's Rationale/Implications).
  4. `**What we are not doing**` — 1–3 bullets, keyed to the spec's
     Non-goals.
  5. Optional single closing line pointing at depth: e.g. *"The Article tab
     covers the rationale, anti-patterns, and examples."*
- Plain markdown only — no custom block fences, no images. Cross-links with
  `[[permalink]]` are fine and resolve like everywhere else.
- Tone: declarative, no hedging, no marketing language.
