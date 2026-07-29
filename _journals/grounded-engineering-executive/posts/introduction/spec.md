---
status: accepted
revised: 2026-07-29
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the journal: explain in one short essay what this journal is (a written
vision of how Željko operates as an engineering executive), why it exists in
written form (alignment is cheaper in writing; a written operating model is
inspectable — including by the people it affects), what a record looks like
(quotable principle, argued rationale, runnable Checklist tab, Comic tab),
where the material comes from (Will Larson's *The Engineering Executive's
Primer* and its per-chapter checklists, with explicit credit), and how
different readers should navigate the six core sections and two appendices.
The intro is the front door — it orients, it does not summarize all 35
records.

## Audience

First-time visitors: a CEO or peer executive deciding whether to read
further; engineering leaders exploring the operating model; Željko's own
team looking for the "why written down?" explanation.

## Success criteria

- [ ] **Orients in one skim** — the KEY POINTS block alone tells a reader
      what the journal is, how records are shaped, and how to use them.
- [ ] **The vision claim is explicit** — the principles are personal
      operating commitments, not neutral book summaries; Larson is credited
      as the grounding, not the author of the vision.
- [ ] **The map is navigable** — all six core sections and both appendices
      appear with their posts cross-linked via `[[slug]]`, so the intro
      doubles as a table of contents.
- [ ] **Record anatomy is explained** — highlight blockquote, ADR-shaped
      body, Checklist tab, Comic tab, draft status.
- [ ] **Short** — an essay of roughly 900–1,100 words (about 5 minutes),
      noticeably lighter than the records it introduces.

## Non-goals

- Not a summary of the 35 records — each record's highlight blockquote does
  that job on its own page.
- Not an ADR — this is the one essay-shaped post in the journal; it opens
  with KEY POINTS, not Status/Principle.
- Not a review of Larson's book — the references stay scoped to what the
  journal actually uses.

## Modalities

Article plus comic. There is still no operating checklist to run — the
checklist modality stays out — but the intro carries the same visual layer
as the records it introduces: three inline explainer figures and a Comic
tab (shared VERA/LEO cast) telling the why-write-it-down story.

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-26** — Visual layer added after all: the intro gets the journal's
  standard three inline figures and a Comic tab, superseding the earlier
  article-only choice — a reader landing on the front door should see the
  same modalities the records ship. The checklist modality stays excluded
  (nothing to run).
- **2026-07-26** — Essay shape (KEY POINTS opening) instead of the journal's
  ADR shape: the intro states no principle and decides nothing; forcing the
  Status/Principle highlight on it would dilute what that block means in the
  other 21 records.
- **2026-07-26** — Wired as a new "Start Here" section at the top of
  `config.yaml` rather than into an existing section, so the reading order
  presents orientation before the first principle.

## Sources

- **Internal**
  - The 35 sibling records and their specs — the corpus this post
    introduces.
- **External**
  - Will Larson, *The Engineering Executive's Primer* (O'Reilly, 2024) —
    the book whose chapter checklists ground every record in this journal.
  - lethain.com — the freely available companion essays credited per
    record.

## Changelog

- **2026-07-29** — Spec reconciled with appendix growth: Intent, map
  criterion, Non-goals, and Sources now say six core sections plus two
  appendices and 35 records; article map line and Figure 3 caption updated
  to match. *(Željko, AI-mediated session)*
- **2026-07-26** — Map, lead, and sources updated again for the second
  appendix, "Appendix: Team Topologies" (nine records grounded in Skelton &
  Pais). *(Željko, AI-mediated session)*
- **2026-07-26** — Map, lead, and sources updated for the new "Appendix: An
  Elegant Puzzle" section (five records grounded in Larson's earlier book).
  *(Željko, AI-mediated session)*
- **2026-07-26** — Comics modality (`comics.md`, VERA/LEO cast) and three
  inline explainer illustrations added; images generated with Gemini.
  *(Željko, AI-mediated session)*
- **2026-07-26** — Article written from this spec; spec and post agree.
  Status `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec. *(Željko, AI-mediated session)*
