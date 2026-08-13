---
status: accepted
revised: 2026-08-13
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Grounded Platforms journal: explain that it is my platform operating
model written down as records — one record per source chapter checklist —
covering both the engineering of internal platforms (why they exist, the four
pillars, the team, the product mindset, operations, planning, rearchitecting,
stakeholders, success) and the strategy around platforms (understanding,
strategy, design, organization, implementation, growth). Give the reader the
map of the two sections, say where the material comes from (Camille Fournier
and Ian Nowland's *Platform Engineering*; Gregor Hohpe's *Platform Strategy*),
and explain how to read the journal: article for the argument, Checklist tab
for the runnable part.

## Audience

Platform and infrastructure leaders and engineers in my organization (so they
know the bar their platform work is held to); application-team leads who
consume platforms (so they know what they are entitled to expect); peer
executives comparing operating models; anyone building their own model from
the same sources.

## Success criteria

- [x] **The journal's charter is stated** — my platform operating model as
      records, not a book report; first person; each record names its
      revisiting conditions.
- [x] **The two-book structure is explicit** — Platform Engineering
      (Fournier & Nowland) for building and running platforms, Platform
      Strategy (Hohpe) for the strategic frame, and why the two belong in one
      journal.
- [x] **The map lists every record** with `[[slug]]` cross-links by section.
- [x] **The reading guide works for each audience** — platform leaders,
      platform engineers, application teams, executives.
- [x] **Credit is explicit** — both books named in the references.

## Non-goals

- Not a summary of either book — each record carries its own material; this
  post is only the map.
- Not a platform inventory or a statement about any specific internal
  platform — the records are the model, not the catalog.
- Not the sibling journals' ground: engineering-management, people-management
  tools, and executive operating model live in their own journals.

## Modalities

- [ ] `checklist.md` — operational checklist *(no checklist by design; the intro is the map, not a record)*
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Journal created with 16 records from the chapter checklists
  of two books: Camille Fournier & Ian Nowland, *Platform Engineering*
  (O'Reilly, 2024), and Gregor Hohpe, *Platform Strategy: Innovation Through
  Harmonization* (Leanpub, 2024) — read through a practitioner-executive lens,
  as with the sibling journals.
- **2026-08-12** — Two sections rather than interleaving: the books answer
  different questions (how to build and run vs. why and whether), and the
  seams between them are cross-linked record to record instead.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/` — ten chapter checklists from
    *Platform Engineering*.
  - `sources/checklists/platform-strategy/` — six chapter checklists from
    *Platform Strategy*.
- **External**
  - Camille Fournier & Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024).
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024).

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 2 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec and article written; spec and post agree.
  Status `accepted`. *(Željko, AI-mediated session)*
