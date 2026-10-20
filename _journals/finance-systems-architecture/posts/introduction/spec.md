---
status: accepted
revised: 2026-10-20
---

# Spec: Introduction: Architecture Where Every Number Must Reconcile

## Intent

Open **RECONCILED: Architecting Finance Systems** by telling the reader what the book is for, whom it serves, why it is called RECONCILED and how to find the chapter that answers the decision already on their desk. Frame the book's problem with a scene a Chief Architect recognizes (the CFO's "why nine days?" question, which turns out to be an architecture question), set up the five reconciliations that [[long-term-evolution]] pays off without repeating that synthesis, and explain how to read the evidence: documented fact, industry practice, the author's recommendation and the fictional Northmere.

## Audience

Chief and Enterprise Architects, finance-systems and solution architects, integration architects, senior engineering and platform leaders, and finance-transformation leaders (the PLAN positioning). Assumes architecture literacy; assumes no accounting training and says that Part I supplies it.

## Success criteria

- [ ] Opens with IN THIS SECTION, YOU WILL and exactly three KEY POINTS, followed by `<br>`; front matter has date 2026-10-18, permalink `introduction` and a one-sentence excerpt.
- [ ] Opening scene: the CFO's nine-day-close question shown to be an architecture question; Northmere introduced as fictional.
- [ ] States who the book is for and what it assumes and does not assume.
- [ ] Explains the title: reconciliation defined, the design claim stated, the five reconciliations listed briefly, with ch. 43 named as the place that closes the loop.
- [ ] Explains why the book exists (the gap between vendor documentation and EA practice; the Chief Architect's vantage point) and hands to [[where-finance-architecture-goes-wrong]].
- [ ] Explains vendor-neutrality, the four evidence labels and how to tell them apart, "as of October 2026", and the living journal with "View spec" links and changelogs.
- [ ] Structure table (Part | Question | Chapters) covering preface, Parts I–IV, Part V and reference; a routing table "Start With the Decision in Front of You" with 10–14 realistic rows using only valid permalinks.
- [ ] A six-term glossary teaser (ledger, subledger, reconciliation, close, system of record, PSP) pointing to [[glossary]]; guidance on using Northmere and the [[toolkit]]; a first-person provenance note that does not name the source company; a closing hand-off to [[where-finance-architecture-goes-wrong]] and [[meet-northmere]]. 3,000–4,000 words.

## Non-goals

- The failure patterns themselves ([[where-finance-architecture-goes-wrong]]).
- Northmere's full description, cast and numbers ([[meet-northmere]]).
- The closing synthesis of the five reconciliations and the "ten things to remember" ([[long-term-evolution]]).
- Part-level learning paths ([[part-1]] to [[part-4]] introductions).
- Vendor capability claims; Part II chapters own and source them.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should the introduction carry a full contents list, as OWNED's does, or is the site index enough?

## Decision log

- **2026-10-18** — Modeled on OWNED's introduction (scene, audience, why it exists, routing table, glossary teaser, provenance note) but replaced its ownership framing with the RECONCILED argument and the evidence-label table the style guide requires.
- **2026-10-18** — Listed the five reconciliations as questions, not as chapter maps, so that [[long-term-evolution]] keeps the payoff (the mapping to chapters and the sixth reconciliation).
- **2026-10-18** — Routing table starts ERP selection at [[build-versus-buy]] and AI pilots at [[ai-in-finance]]'s controls argument, and says why, to model the book's capability-first and controls-first stance.
- **2026-10-18** — Did not link `part-5` because its introduction does not exist yet; Part V is reached through [[case-uber-payments]].

## Sources

- **Internal**
  - `PLAN.md` — positioning, title rationale, structure, provenance.
  - `_research/style-guide.md` — evidence discipline and page format.
  - [[meet-northmere]], [[where-finance-architecture-goes-wrong]], [[part-1]]–[[part-4]], [[long-term-evolution]], [[toolkit]], [[glossary]], [[bibliography]] and the KEY POINTS of every chapter.
  - OWNED's introduction (`_journals/private-techuity/posts/introduction/index.md`) as the structural model.
- **External**
  - None; vendor and regulatory facts are sourced in the chapters that own them.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Reading-order table and Figure 3 updated for the renamed parts (INTEGRATION, LEADERSHIP, PRACTICE). *(AI-mediated session)*
- **2026-10-19** — Title renamed to "Introduction: Architecture Where Every Number Must Reconcile" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the mermaid diagram with a generated illustration (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Book title renamed from "RECONCILED: Enterprise Architecture for Financial Systems" to "RECONCILED: Architecting Finance Systems" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 3,157 → 3,140 words; no headings renamed; three paragraph openings made to state their point (Why This Book Exists ×2, the evidence-label paragraph). Spec: removed the answered Open question on `part-5` (the structure table now links it). *(AI-mediated session)*
