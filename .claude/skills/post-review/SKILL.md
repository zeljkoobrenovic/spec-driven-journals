---
name: post-review
description: Review a spec-driven journal post end to end — the spec, each modality (index/summary/dialog/comics), spec↔modality alignment, and cross-modality consistency — judging structure, argument quality, readability, repetition, language simplicity, grammar, and overall quality. Writes findings to REVIEW.md in the post folder. Use when asked to review, critique, audit, proofread, or quality-check a post, a spec, a modality, or the alignment between them in _journals/*/posts/*/.
---

# Post Review (writes `REVIEW.md`)

## Goal

Review one spec-driven post in `_journals/<journal>/posts/<slug>/` as a whole
system and record the findings in `REVIEW.md` in that same folder. The review
covers four layers:

1. **The spec** — is it a good contract? (structure, checkable criteria, no bloat)
2. **Each modality on its own** — `index.md`, and whichever of `summary.md`,
   `dialog.md`, `comics.md` exist — judged for quality.
3. **Spec ↔ modality alignment** — does each modality satisfy the spec's Intent,
   Success criteria, and Non-goals? Has the post drifted from the contract?
4. **Cross-modality alignment** — do the modalities tell the *same* story, in the
   same voice, with the same facts, framing, and terminology?

This skill is **read-and-report only**. It writes exactly one file — `REVIEW.md`
— and changes nothing else. It does not fix the post, edit the spec, or edit any
modality. Fixing is a separate, follow-up action the user decides on after
reading the review.

## Contract rules

- **Write only `REVIEW.md`.** Never edit `spec.md`, `index.md`, or any modality
  file from this skill. If the user wants fixes applied, that is a separate
  request handed to the authoring skills (`spec-creator`, `detailed-article`,
  `management-summary`, `podcast-dialog`, `explainer-comics`).
- **`REVIEW.md` is a sibling file the build ignores** (only the `_MODALITIES`
  allow-list renders as tabs), so writing it never affects the built site and
  needs no `config.yaml` change.
- **The spec is the contract.** Alignment is measured *against the spec*. When a
  modality and the spec disagree, report it as drift and say which one looks
  wrong — but do not decide the resolution; that is the author's call.
- **Judge, don't rewrite.** Findings name the problem and point at the location;
  they may suggest a direction, but the review is not a redraft. Keep proposed
  fixes to a phrase or a sentence, not paragraphs.

## Workflow

1. **Locate the post.** Confirm the folder under `_journals/<journal>/posts/<slug>/`.
   Inventory which files exist: `spec.md` (may be absent for trivial posts),
   `index.md` (required), and any of `summary.md`, `dialog.md`, `comics.md`.
2. **Read everything, in order:** `spec.md` first (the contract), then `index.md`,
   then each present modality. Read the whole of each — skimming misses repetition
   and drift, which are the highest-value findings.
3. **Skim 1–2 neighboring posts** in the same journal only if you need the house
   voice as a baseline (e.g. to judge whether a tone finding is real or just the
   journal's normal register).
4. **Run the four review layers** below, collecting findings as you go. Tag each
   finding with a severity and a precise location (file + section/panel/line).
5. **Write `REVIEW.md`** in the post folder using the template below. If a
   `REVIEW.md` already exists, read it first and **replace** it with a fresh
   review dated today — keep a short "Previous review" note at the bottom only if
   prior findings remain unaddressed, so the history of unresolved issues is
   visible.
6. **Report a tight summary to the user**: the counts by severity and the top 3–5
   findings. Do not paste the whole file back; point them at `REVIEW.md`.
7. **Do not run the build** — nothing rendered changed. (Mention it only if the
   review surfaced a build-affecting problem, e.g. a broken `[[link]]` or a
   missing panel image.)

## What to review (the four layers)

### Layer 1 — The spec as a contract

- **Structure**: does it follow the template sections (Intent, Audience, Success
  criteria, Non-goals, Modalities, Open questions, Decision log, Sources,
  Changelog)? Are Context/Structure used well if present?
- **Checkable criteria**: is each Success criterion something a reviewer can
  verify against the post, or is it Intent prose with a checkbox? Flag vague,
  overlapping, or un-testable criteria.
- **Bloat**: is the spec longer than the post warrants? Accreted duplication,
  resolved Open questions left dangling, broken line-wraps.
- **Internal consistency**: Intent ↔ Success criteria ↔ Non-goals ↔ Structure all
  agree; no section contradicts another.

### Layer 2 — Each modality on its own

Judge every present modality (`index`, and any of `summary`/`dialog`/`comics`)
against these dimensions. The bar differs by modality (an article is exhaustive;
a summary is tight; a dialog is audible; a comic is mostly visual) — judge each
against *its own* purpose, but the dimensions are constant:

- **Structure & flow**: is the order logical? Does each section earn its place
  and hand off cleanly to the next? Are there orphaned or out-of-place passages?
- **Argument quality**: are claims supported? Are there gaps, non-sequiturs,
  unstated assumptions, or conclusions the body never sets up? Does the strongest
  counter-argument get a fair hearing where the piece needs one?
- **Ease of reading & following**: can a first-time reader follow the thread
  without re-reading? Are transitions present? Is the cognitive load reasonable?
- **Repetition & redundancy**: passages that repeat a point already made, filler
  that adds words but no meaning, two sentences doing one sentence's work. This is
  high-value — call out the specific repeated beats.
- **Language simplicity**: needlessly complex words, tangled sentences, jargon
  where plain words exist, sentences that are too long to parse in one pass.
- **Grammar & mechanics**: agreement, tense consistency, punctuation, broken
  markdown, typos, malformed `[[links]]`, image refs that don't resolve.
- **Overall quality**: does it achieve its modality's purpose? Would the intended
  reader be well served?

Modality-specific checks:

- **`index`** — the house record shape where applicable (status highlight,
  MADR-inspired order); section headings in **Title Case** (principal words
  capitalized; `a/the/and/to/by/in/of` lowercase unless first; first word after
  a colon capitalized); cross-links present and resolving; figures captioned.
- **`summary`** — actually short (the modality's target length); leads with the
  decision/answer; nothing a leader needs is missing, nothing they don't need is
  included.
- **`dialog`** — the two voices stay distinct and each carries a real position;
  it sounds spoken, not like prose with names attached; it covers the spec's
  load-bearing beats without becoming a lecture.
- **`comics`** — panel count and caption length fit the form; captions match their
  alt text and images; every referenced panel image file exists; the visual
  metaphor is consistent panel to panel.

### Layer 3 — Spec ↔ modality alignment

- Walk the spec's **Success criteria** one at a time and mark each
  **met / partially met / unmet**, citing where in which modality it is satisfied
  (or noting that it is not). The primary obligation falls on `index`, but a
  criterion may be satisfied across modalities — say which.
- Check the spec's **Non-goals**: does any modality drift into territory the spec
  fences off?
- Check **Intent & Audience**: does the post land what the Intent describes, in
  the voice the Audience implies?
- If the post has moved beyond the spec, this is **drift**: note it, and recommend
  the spec be marked `status: drifted` (but do not edit the spec).

### Layer 4 — Cross-modality alignment

The modalities are the same story told different ways; they must not contradict
each other. Check:

- **Facts & framing**: the same claims, numbers, names, and structure across all
  modalities. A point reframed in one but not the others is a finding.
- **Terminology**: the same load-bearing phrases used consistently (e.g. if the
  article calls something "the root," the others should not rename it).
- **Voice & tone**: consistent register and point of view across modalities,
  allowing for the form (a comic is terser than an article, but not a different
  *person*).
- **Coverage parity**: every load-bearing beat present in `index` shows up,
  appropriately compressed, in the modalities that should carry it — and no
  modality introduces a major beat the others (and the spec) lack.
- **Stale propagation**: when one modality was recently edited, did the change
  reach the others? A new section in `index` with no echo anywhere else is the
  classic drift signal.

## Severity scale

- **blocker** — wrong, misleading, contradicts another modality or the spec, or
  breaks the build (broken link, missing panel image). Fix before publishing.
- **major** — real quality problem: a weak or unsupported argument, a confusing
  structure, a Success criterion unmet, a notable repetition.
- **minor** — polish: a clunky sentence, a small redundancy, light over-complex
  wording.
- **nit** — typo, punctuation, a single awkward word. Group these; don't let them
  drown the substantive findings.

## `REVIEW.md` format

Write the file with this shape. Keep findings concrete and located; a finding the
author cannot find in the text is useless.

```markdown
# Review: <post title>

**Reviewed:** <YYYY-MM-DD> · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, summary.md, dialog.md, comics.md *(list only those present)*

## Verdict

One short paragraph: overall quality, whether it is publish-ready, and the single
most important thing to address.

## Findings by severity

**Counts:** blocker N · major N · minor N · nit N

### Blockers
- **[file · location]** Problem stated plainly. *Suggested direction (one phrase).*

### Major
- **[file · location]** …

### Minor
- **[file · location]** …

### Nits
- **[file · location]** … *(group freely)*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| <short name> | met / partial / unmet | <file · section> |

Non-goals respected: <yes / list any breaches>
Drift: <none / describe; recommend spec `status: drifted` if so>

## Cross-modality alignment

- **Facts & framing:** <consistent / discrepancies>
- **Terminology:** <consistent / drift>
- **Voice & tone:** <consistent / drift>
- **Coverage parity:** <even / which beat is missing where>

## Layer-by-layer notes

### Spec
### index.md
### summary.md  *(only sections for modalities present)*
### dialog.md
### comics.md

*(2–5 bullets each: the substantive observations behind the findings above.)*

## Previous review

*(Only if a prior REVIEW.md existed: list its findings that are still
unaddressed. Omit this section entirely on a first review or when all prior
findings are resolved.)*
```

## Anti-patterns

- Editing the post, spec, or any modality. This skill writes `REVIEW.md` only.
- Rewriting passages instead of pointing at them — keep suggested fixes to a
  phrase, not a redraft.
- Vague findings ("the flow is off") with no location. Every finding names a file
  and a section/panel/line.
- Drowning real problems in nits. Group trivia; lead with substance.
- Reviewing modalities in isolation and skipping Layers 3 and 4 — the alignment
  layers are the reason this skill exists and the easiest to skip.
- Judging a summary for not being exhaustive or a comic for being terse — judge
  each modality against *its own* purpose.
- Running the build or touching `config.yaml` — nothing rendered changed.
