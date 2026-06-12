---
name: detailed-article
description: Write or revise the detailed main article (index.md) of a spec-driven journal post from its spec.md contract, following the house record style (status highlight, MADR-inspired sections, cross-links). Use when asked to write, draft, expand, or revise a post's main article, index.md, or "the article modality" in _journals/*/posts/*/.
---

# Detailed Article (the `index` modality)

## Goal

Write or revise `index.md` — the detailed main article of a post — from the
sibling `spec.md`. The article is the **required, default modality**: every
post has one, and it is the default tab on the rendered post page. Other
modalities (`summary.md`, `dialog.md`, `comics.md`) are derived from the spec
and this article; when the article changes substantively, flag sibling
modality files that may now be stale.

## Contract rules

- `spec.md` is the contract. **Never edit spec.md from this skill.** If the
  requested article diverges from the spec's Intent or Success criteria, stop
  and say so — either the user updates the spec first (spec-first rule) or
  narrows the request.
- If the post already exists and has moved beyond its spec, flag the drift:
  suggest setting the spec's `status: drifted` and updating `revised:` — but
  let the user make that edit decision.
- `permalink:` and `id:` front matter never change once published.

## Workflow

1. Read `spec.md` (Intent, Audience, Success criteria, Non-goals, Modalities,
   Sources) and the existing `index.md` if present.
2. Skim 1-2 neighboring posts in the same journal for tone and section shape.
3. Write/revise `index.md` following the house style below.
4. Walk the spec's Success criteria one by one and verify each against the
   draft; report the checklist to the user.
5. If this is a new post, wire it into `_journals/<journal>/config.yaml`
   (add `- <slug>/index.md` under the right section).
6. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` exists and embeds `"key": "index"`.

## House style

- **Front matter**: `title`, `date`, `author`, `excerpt`, `permalink`,
  `timetoread`, `tags`; ADR-shaped posts also carry `id` and
  `status: <state>:<colour>` (e.g. `proposed:orange`, `accepted:green`).
- **Opening highlight** before the first `## Heading`:

  ```markdown
  > **Status**: PROPOSED
  >
  > **Decision**: One paragraph stating the decision clearly enough that a
  > reader gets the direction before reading the body.
  ```

  Use `**Principle**` instead of `**Decision**` for principle posts. Keep the
  visible status aligned with the front-matter `status:` value.
- **Body order (MADR-inspired)**: `Statement`/`Decision` → `How to Read This`
  → `Rationale` → `Implications` → `What This Means for Teams` →
  `Anti-Patterns` → `Examples` → `Related Principles`/cross-links →
  `Scope and Revisiting` → `Authoritative References`. Sections may be
  omitted, but keep the order.
- **Tables of contrasts** ("What it says / What it does **not** say") and
  grouped bullets read well in the rendered HTML — prefer them over long
  prose.
- **Cross-link** related records with `[[permalink]]` rather than ad-hoc
  text references. Link liberally — unresolved `[[slugs]]` survive the build
  as visible TODOs.
- **Tone**: declarative. Records are read by humans and by AI tools as
  context.
- Image references stay journal-root-relative (`assets/images/...`); put
  files in the post's own `assets/` folder.
