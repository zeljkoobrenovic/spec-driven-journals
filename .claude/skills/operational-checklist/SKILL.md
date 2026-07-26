---
name: operational-checklist
description: Write the checklist modality (checklist.md) of a spec-driven journal post — the operational working checklist behind the record, rendered as the Checklist tab on the post page. Use when asked to add, write, update, or extract a checklist, working checklist, or checklist tab for a post in _journals/*/posts/*/.
---

# Operational Checklist (the `checklist` modality)

## Goal

Write `checklist.md` next to a post's `index.md` — the operational working
checklist behind the record, rendered as the **Checklist** tab on the same
post page. The article argues the principle; the checklist is the part you
*run*: the concrete moves, grouped and ordered for use, stripped of
rationale. The audience is someone who already buys the principle and is
executing it today.

## Contract rules

- `spec.md` is the contract; `index.md` is the argument. **Never edit either
  from this skill.** If the spec names a source checklist document (e.g. a
  PDF under the journal's `sources/`), that source is authoritative for the
  checklist's content and grouping — reproduce it faithfully; do not invent,
  merge, or drop items.
- Without a source checklist document, distill the checklist from the
  article's practices (What This Means in Practice, Anti-Patterns inverted
  into checks) — but add no obligation the article does not support.
- If `index.md` still embeds the full checklist as a body section (older
  posts), flag it: the section should move here, leaving the article to
  reference the Checklist tab. Moving it is the caller's decision unless the
  request already asks for the migration.

## Workflow

1. Read `spec.md` (Intent, Success criteria, Sources) and `index.md` in the
   target post folder. Read the source checklist document if the spec names
   one. The post must already have an `index.md` — if not, write the article
   first (see the `detailed-article` skill).
2. Write `checklist.md` in the format below.
3. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` contains `"key": "checklist"`.
4. Tell the user the Checklist tab is live at `<permalink>.html#checklist`.

## Format

- **No title heading** — the post header (title, byline, tags, hero) is
  shared by all tabs. Start directly with content.
- **Optional front matter**: `timetoread: "3 min read"` (stored, not yet
  rendered).
- **Shape**:
  1. One short framing line in italics — what this checklist is for and when
     to run it, e.g. *"The working checklist behind this principle. The
     Article tab carries the rationale."*
  2. `### ` sections mirroring the source checklist's grouping (or the
     natural phases of the practice: prepare → do → review). Keep the source
     order — it usually encodes sequence.
  3. `- [ ]` task bullets, one action per bullet, imperative or first-person
     interrogative as the source has it — the renderer shows these as real
     checkboxes (clickable, state not persisted). Use plain `-` bullets only
     for lines that are notes rather than checks (reminders, OK / Not-OK
     contrasts).
  4. Nested bullets (two-space indent) for sub-items; **bold** lead-ins for
     named sub-groups within a section.
- Keep every item scannable: no paragraphs, no rationale sentences — if an
  item needs explaining, the explanation belongs in the article.
- Cross-links with `[[permalink]]` are fine and resolve like everywhere else.
- Tone: operational and declarative. This is the tab a reader keeps open
  while doing the work.
