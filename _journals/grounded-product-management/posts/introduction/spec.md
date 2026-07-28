---
status: accepted
revised: 2026-07-27
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the journal: explain in one short essay what this journal is (Željko's
product-management operating model, written down — the product counterpart to
the Grounded Engineering Executive journal), why an engineering executive
writes a product journal at all (product and engineering are one delivery
system; an executive who cannot articulate how product decisions should be
made cannot partner with product), what a record looks like (quotable
principle, argued body, Checklist tab, Comic tab, linked spec), where the
material comes from (Foster & Nerlikar's *Build What Matters* and Cagan &
Jones's *EMPOWERED*, credited per record), and how different readers should
navigate the two sections. The intro is the front door — it orients, it does
not summarize all 14 records.

## Audience

First-time visitors: a CEO or peer executive deciding what to expect from
Željko on product; product managers who work with him; engineering leaders
building their own model; two-minute readers headed for the Comic tab.

## Success criteria

- [ ] **Orients in one skim** — the KEY POINTS block alone tells a reader
      what the journal is, how records are shaped, and how to use them.
- [ ] **The vision claim is explicit** — the principles are personal
      operating commitments, not neutral book summaries; Foster & Nerlikar
      and Cagan & Jones are credited as the grounding, not the authors of
      the vision.
- [ ] **The bridge is argued** — the post explains why an engineering
      executive writes a product journal, and cross-links the sibling
      journal's philosophy ([[inspected-trust]]).
- [ ] **The map is navigable** — both sections appear with all 14 records
      cross-linked via `[[slug]]`, so the intro doubles as a table of
      contents.
- [ ] **Record anatomy is explained** — highlight blockquote, ADR-shaped
      body, Checklist tab, Comic tab, spec link, draft status.
- [ ] **Short** — an essay of roughly 900–1,100 words (about 5 minutes),
      noticeably lighter than the records it introduces.

## Non-goals

- Not a summary of the 14 records — each record's highlight blockquote does
  that job on its own page.
- Not an ADR — this is the one essay-shaped post in the journal; it opens
  with KEY POINTS, not Status/Principle.
- Not a review of either book — the references stay scoped to what the
  journal actually uses.
- Not a reconciliation of the two books' disagreements — individual records
  handle tensions where they arise.

## Modalities

Article plus comic. There is no operating checklist to run — the checklist
modality stays out — but the intro carries the same visual layer as the
records it introduces: three inline explainer figures and a Comic tab
(shared VERA cast, introducing MILA) telling the why-a-product-journal
story.

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-27** — Essay shape (KEY POINTS opening) instead of the journal's
  ADR shape: the intro states no principle and decides nothing; forcing the
  Status/Principle highlight on it would dilute what that block means in the
  other 14 records. Same choice as the sibling journal's introduction.
- **2026-07-27** — The intro is the front door for a two-book journal: it
  must present *Build What Matters* (the vision-led operating loop) and
  *EMPOWERED* (empowered teams and product leadership) as two halves of one
  operating model, not as two book summaries — the map gets exactly two
  section bullets, one per book, each linking all seven records.

## Sources

- **Internal**
  - The 14 sibling records and their specs — the corpus this post
    introduces: [[dysfunctions]], [[customer-journey-vision]],
    [[product-strategy]], [[outcomes]], [[balanced-roadmap]],
    [[right-team]], [[right-processes]], [[coaching]], [[staffing]],
    [[product-vision-and-principles]], [[empowered-product-strategy]],
    [[team-topology]], [[team-objectives]], [[business-collaboration]].
- **External**
  - Ben Foster and Rajesh Nerlikar, *Build What Matters: Delivering Key
    Outcomes with Vision-Led Product Management* (Lioncrest Publishing,
    2020) — grounds the seven Build What Matters records.
  - Marty Cagan with Chris Jones, *EMPOWERED: Ordinary People,
    Extraordinary Products* (Wiley, 2020) — grounds the seven EMPOWERED
    records.

## Changelog

- **2026-07-27** — Comics modality (`comics.md`, VERA/MILA cast) staged and
  three inline illustration placeholders embedded in the article. *(Željko,
  AI-mediated session)*
- **2026-07-27** — Article written from this spec; spec and post agree.
  Status `accepted`. *(Željko, AI-mediated session)*
- **2026-07-27** — Initial spec. *(Željko, AI-mediated session)*
