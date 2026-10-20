---
status: accepted
revised: 2026-10-20
---

# Spec: Introduction: Reading Uber's AI Infra as Records

## Intent

Open the book. Explain why a case-study journal about one company's internal AI developer infrastructure is worth reading, where its material comes from (the 14 October 2026 *Pragmatic Engineer* episode, widened by Uber's written 2026 sources, its older engineering record and dated industry evidence), and how to use it. The reader leaves knowing which chapter to open first for the decision in front of them, how the four parts form a path, how every chapter is structured, and how to read the evidence labels that separate Uber's own account from documented fact, industry comparison, labeled inference and the author's recommendation.

## Audience

CTOs, VPs of Engineering, platform and developer-experience leads, staff and principal engineers, engineering managers, and security or FinOps leads who are deciding what AI developer infrastructure to build, buy or skip. Most will not read front to back; the page must route them.

## Success criteria

- [x] Credits the source episode fully: title, publisher, date, host, guest, URLs, and the episode's arc by timestamp.
- [x] Explains how the book extends the episode (four layers table) and how disagreements between the episode and written sources are handled, with two concrete examples.
- [x] A "start with the decision in front of you" routing table maps at least 15 decisions to an owning chapter and a follow-up chapter, using only valid permalinks.
- [x] The four parts are presented as a path (diagram plus table listing every chapter).
- [x] The five evidence labels are defined with wording and an example each; number conventions (source, date, definition; "as of October 2026") are stated.
- [x] States what the book will not do (no inside knowledge, no invented internals, no vendor ranking, no ROI promise).
- [x] Uses `IN THIS BOOK, YOU WILL`, WHY IT MATTERS and exactly three KEY POINTS; no BUILT ON line.

## Non-goals

- The thesis and dependency map ([[the-harness-is-the-easy-part]]).
- Dates and reconciliation of disputed dates ([[timeline]]).
- The sequenced playbook, readiness assessment and roadmap ([[the-retrofit-playbook]]).
- Explaining any single system in depth (Parts I–IV).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should the routing table be regenerated from the chapters' "Owns" lists when chapters are added?
- Should the size bands (≈50, 500, 5,000) be complemented by the playbook's ≈200 and ≈2,000 bands across the book?

## Decision log

- **2026-10-20** — Organized the routing table by the reader's decision rather than by system, because most readers arrive with a problem, not a system name.
- **2026-10-20** — Included an evidence-classification flowchart, because the labels are the book's main reading convention and the single-source risk is its main weakness.
- **2026-10-20** — Kept Medisetty's "still pretty early" closing remark as the dating caveat for the whole book.

## Sources

- **Internal**
  - [[the-harness-is-the-easy-part]], [[timeline]], [[minion]], [[the-retrofit-playbook]], [[system-catalog]], [[glossary]].
- **External**
  - *The Pragmatic Engineer* podcast "Uber's AI infra, from the inside", 14 Oct 2026, and show notes.
  - Uber Blog: "Running a Software Factory Efficiently at Uber Scale" (Aug 2026), "Designing MCP Gateway" (Oct 2026), JUnit migration (Apr 2026), SLATE (2022); AI Engineer World's Fair 2026 talk; PE "How Uber uses AI for development" (Mar 2026).
  - Stripe Minions (Feb 2026); DORA 2025.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
