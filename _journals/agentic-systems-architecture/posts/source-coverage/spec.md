---
status: accepted
revised: 2026-10-28
---

# Spec: Source Coverage: The Interview Designs Behind This Book

## Intent

A Reference page that makes the provenance of every interview-derived design example in the book traceable. It explains what the author's system-design interview project is and the rule for using it (design exercises, not deployed systems; labeled inline; cited by path and step; numbers illustrative). It maps the twelve agentic interview designs to the book's parts and chapters in one matrix, and gives each source a section: what it designs, its evolution path (step ids and titles), the patterns the book adopted with the chapters that use them, where the book departs from or reconciles it (with the consistency-log ruling), its weaknesses as the research digests found them, and its exact path. It closes with what the interview sources did not cover and which external research filled each gap. After reading, a reviewer can check any design-example claim against its source step and see why the book differs.

## Audience

Reviewers and readers checking where a mechanism came from; future writers extending the book; the author, when the interview designs change.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; exactly three KEY POINTS; a FAILURE PATTERNS block with exact pattern names (The Agent Committee, Ambient Authority, The Fire-and-Forget Action); `<br>`; a lead.
- [x] States the provenance rule (evidence kind 7), the citation format, that REVIEW.md files predate the JSON (ruling 13) and that Ostrell is fictional and distinct from the design examples.
- [x] A coverage matrix of all 12 sources × Parts I–XI with linked chapter numbers, built from a search of chapters 01–44, plus a per-source summary of steps, chapters cited, mentions, REVIEW.md date and closest Ostrell counterpart.
- [x] One section per source (all twelve) with evolution path, a patterns table with `[[link]]` chapters, departures citing rulings, weaknesses and the exact `system-design-interviews/data/book/<dir>/interview.json` path.
- [x] Reports honestly that every source is cited (fewest: marketing, 5 chapters).
- [x] A gaps section naming multi-agent research decomposition (ruling 12) and the other uncovered topics, with the chapters and external sources used instead.
- [x] Fictional disclaimer; only valid permalinks; 4,000–7,000 words of prose.

## Non-goals

- Re-teaching any mechanism; each pattern row links to the chapter that owns it.
- Listing external sources in full; [[bibliography]] and the chapters carry them.
- Templates ([[toolkit]]) and definitions (glossary).
- Treating any interview number as a measurement.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only.

## Open questions

- The matrix is a text search for the source directory name; a chapter that paraphrases a source without naming it is not counted. Re-run the search after chapter revisions.
- The "closest Ostrell counterpart" column is the author's mapping; revisit if [[meet-ostrell]] changes.
- If the interview JSON files change after 2026-10-28, re-check the evolution paths and weaknesses.

## Decision log

- **2026-10-28** — Chapter numbers in the matrix are plain links (`NN`) instead of `[[…]]`, because full titles would make a 12 × 11 matrix unreadable; the per-source tables use `[[…]]`.
- **2026-10-28** — Each source section follows one fixed shape (designs, path, patterns table, departures, weaknesses, path) so the page works as a lookup.
- **2026-10-28** — Weaknesses come from the digests' checked lists, not from REVIEW.md, per ruling 13.
- **2026-10-28** — The healthcare, benefits and research designs are kept outside Ostrell and labeled as contrast designs.

## Sources

- Internal: `PLAN.md` (Provenance), `_research/style-guide.md` (evidence kind 7), `_research/consistency-issues.md` (rulings 1–24), `_research/digest-platform-and-coding.md`, `digest-customer-facing.md`, `digest-back-office.md`, `digest-high-stakes-and-research.md`; [[meet-ostrell]], [[toolkit]], [[bibliography]], [[planning-and-decomposition]], [[single-and-multi-agent-designs]].
- Interview sources: `system-design-interviews/data/book/{agentic-platform-foundations, ai-coding-cli, ai-coding-harness, agentic-support-platform, agentic-sales-platform, agentic-marketing-platform, agentic-finance-platform, agentic-legal-platform, agentic-hr-platform, agentic-healthcare-platform, agentic-public-benefits-platform, agentic-research-platform}/interview.json`.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 0 conceptual figures (article-illustrator). *(AI-mediated session)*
