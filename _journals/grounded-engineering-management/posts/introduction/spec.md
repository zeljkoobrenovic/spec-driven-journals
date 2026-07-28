---
status: accepted
revised: 2026-07-28
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Orient the reader in the journal: what it is (my engineering-management
operating model written down as records across the whole ladder), why an
executive writes the ladder down (management quality at scale is a systems
property; the records tell managers what I hold them to and tell everyone
else what they may expect from their manager), where the material comes from
(Fournier's *The Manager's Path*, Zhuo's *The Making of a Manager*, Orosz's
*The Software Engineer's Guidebook*, and Kate Matsudaira's operational
excellence article), and how to read it. The map must make the journal's
distinctive feature visible: the management ladder and the engineer career
ladder covered side by side, meeting at the tech lead role and the
manager–report contract.

## Audience

Engineers and managers in my organization; peer executives comparing
operating models; my own manager. First-person declarative.

## Success criteria

- [x] **KEY POINTS blockquote** with exactly three bullets: what the journal
      is, that every record ships its checklist, and that it is an operating
      manual, not a book report.
- [x] **The map is complete** — every record in config.yaml is crosslinked
      by slug in The Map section.
- [x] **The two-ladders framing is explicit** — tech-lead/pragmatic-tech-lead
      and management-101/own-your-career named as the meeting points.
- [x] **Sibling journals are linked** — engineering-executive and
      people-management-tools introductions referenced for the charter.
- [x] **Credit is explicit** — References name all three books and Kate
      Matsudaira's article.

## Non-goals

- Not a summary of any single record — each record argues for itself.
- Not a book review — the sources are credited and recommended, not
  evaluated.
- Not the concrete people-management instruments — those live in the
  [[introduction]] of grounded-people-management-tools and its records.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — Organized the journal by source book (as in
  grounded-product-management) rather than by theme, because the sources are
  chapter checklists and the books' own arcs — the ladder, the first-line
  fundamentals, the engineer career — are the natural reading orders.
- **2026-07-28** — Kept the Software Engineer's Guidebook records in a
  management journal, framed as the expectations and coaching guidance a
  manager holds engineers to, so the journal covers both sides of the
  manager–engineer contract instead of only the manager's side.

## Sources

- **Internal**
  - `sources/engineering-manager-path/` — 8 Manager's Path chapter
    checklists plus the operational excellence checklist.
  - `sources/making-of-a-manager/` — 12 Making of a Manager checklists.
  - `sources/software-engineering-guidebook/` — 10 Software Engineer's
    Guidebook checklists.
- **External**
  - Camille Fournier, *The Manager's Path* (O'Reilly, 2017).
  - Julie Zhuo, *The Making of a Manager* (Portfolio/Penguin, 2019).
  - Gergely Orosz, *The Software Engineer's Guidebook* (2023).
  - Kate Matsudaira, "Software Managers' Guide to Operational Excellence".

## Changelog

- **2026-07-28** — Comics modality added (comics.md, Comic tab, shared
  VERA/ARLO cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-07-28** — Initial spec and article written; spec and post agree.
  Status `accepted`. *(Željko, AI-mediated session)*
