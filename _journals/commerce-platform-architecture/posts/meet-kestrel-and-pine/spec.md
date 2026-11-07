---
status: accepted
revised: 2026-11-07
---

# Spec: Meet Kestrel & Pine

## Intent

Introduce the fictional running example once, in one place, so that every chapter can open with a Kestrel & Pine scene without re-explaining the company. The page presents Kestrel & Pine as a composite of patterns common among growing omnichannel brands (not a disguised company): its growth 2016–2027 mapped to the four scale stages, its four business lines and 2026 figures, the catalog and the Ridgewalker jacket, its channels and customers, the volumes every design is sized against, the January 2027 systems landscape (with its two gaps, no OMS and no PIM, and the stock sync chain), the cast with pronouns, the ten incidents with their failure patterns and owning chapters, the Waypoint decisions W1–W8, and the five recurring worked examples. After reading, a newcomer knows the book's vocabulary at first-contact depth, can follow any chapter's worked example and knows where each recurring number comes from.

## Audience

Readers new to commerce architecture: engineers, product managers, analysts, consultants and leaders who have just joined a merchant, a vendor or an agency. The engineer or architect who, like Noor Visser, has to make decisions about systems they did not choose benefits most; the page is written at her altitude. It is many readers' first contact with WMS, ERP, POS, PSP, OMS, PIM, EDI, DESADV, SSCC, iPaaS, available-to-promise and system of record, so each is explained in one plain clause.

## Success criteria

- [x] Every Kestrel & Pine fact (revenue, lines, prices, counts, volumes, systems, cast, incidents, Waypoint scope and dates, worked-example dates and amounts) agrees with `_research/scenario-ledger.md`; the business lines sum to €48.0 million.
- [x] Labels Kestrel & Pine, Bergzicht Outdoor and Veluwe Capital fictional in the callouts, the lead and the Sources line; systems are named by role, never by vendor.
- [x] A reader new to the field can define every term the page uses from the page alone; every acronym is expanded on first use.
- [x] Two mermaid diagrams with captions: the systems landscape (showing the WMS → ERP → platform → connector stock chain and the absence of an OMS and a PIM) and Eva's jacket as a sequence across the systems.
- [x] The ten incidents each carry their numbers, the failure pattern named exactly as in the style guide, and the owning chapter as a `[[link]]`.
- [x] W1–W8 appear in one table with decision, what changes and when; the cast table gives pronouns and names Noor Visser as the reader's stand-in.
- [x] Preface-style callouts ("IN THIS SECTION, YOU WILL"), exactly three KEY POINTS; no failure-pattern block, no "Across Scale Stages" section, no take-away tiers; closes with a hand-off to [[part-1]].
- [x] Prose within 2,500–3,500 words; total with tables under the 6,500-word cap.

## Non-goals

- The failure patterns themselves and how they chain — [[where-commerce-platforms-go-wrong]].
- The order's journey step by step — [[journey-of-an-order]]; the four journeys in full — [[part-9]].
- Designing or justifying any Waypoint decision; each owning chapter does that ([[inventory-and-availability]], [[order-management]], [[product-information]], [[build-buy-or-assemble]], [[events-consistency-and-reconciliation]], [[edi-and-e-invoicing]], [[commerce-data-and-analytics]], [[ai-and-agentic-commerce]]).
- The scale stages as a model — [[commerce-scaling-stages]]; the business-model economics — [[commerce-business-models]].
- Real-company evidence; this page cites none and the Sources section says so.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Chapters may append canonical facts to the ledger after this page was written (for example illustrative latencies, team details, 2027 peak-plan numbers); a review pass should fold additions that matter book-wide back into this page.
- The timeline fixes a few dates the ledger gives only by "since" year (the agency in 2017, the iPaaS and the connector in 2021, Ruben Alves in 2022); they are consistent with the ledger's "Since" columns but a reviewer should confirm no chapter needs them earlier.

## Decision log

- **2026-11-07** — Mirrored the `meet-axleby` structure (glance, history, products, channels, volumes, landscape, people, problems, program, examples, usage) but wrote the ten incidents as a numbered list rather than a table, because each needs two or three sentences that define a term (DESADV, SSCC) at the point the newcomer meets it, and a table cell cannot carry that.
- **2026-11-07** — Collapsed the growth timeline to one row per scale stage rather than one per year, to keep the page within length while still showing which system arrived at which stage.
- **2026-11-07** — Drew the second diagram as a sequence of Eva's jacket across systems rather than a second structural view, so the page shows the order's journey once before Part I walks it, and so the handoffs the book calls "joins" are visible as arrows.
- **2026-11-07** — Kept the Card-Testing Night as a trust failure outside the sixteen patterns, as the ledger does, rather than forcing it under The Secret Agent.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — every Kestrel & Pine fact.
  - `PLAN.md` — the Preface contract and the chapter that owns each incident and term.
  - `_research/style-guide.md` — page format, failure-pattern names, term list, valid permalinks.
  - `meet-axleby` (vehicle-data-dealer-saas-architecture) — structure and conventions of a "meet the company" page.
- **External**
  - None; the page is entirely fictional and cites no company evidence.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Eva's late delivery made explicit, American spelling, timetoread. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
