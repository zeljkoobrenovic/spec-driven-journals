---
status: accepted
revised: 2026-10-22
---

# Spec: Introduction: Architecture for Decisions About One Car

## Intent

Open the book with its argument and its map. The page states the central idea, that **a vehicle data and dealer SaaS platform sells decisions about one physical car** (what it is, what happened to it, what it is worth, what to pay, what to ask, where to advertise it and who now owns it), and that the architecture is judged by how reliably the facts beneath those decisions travel: keyed to the right car, with known source and license, fresh enough for the decision, and corrected everywhere they spread. It introduces the two halves (vehicle data services and dealer SaaS), the rule for what they share (the car, the customer and the meter) and what they keep apart (release cadence, workflow, external contracts), and the market comparison rule (one core, market adapters and rule sets, four columns: NL/BE, DE, UK, US). It then gives the reader the means to use the book: the ten parts as a learning path including the JOURNEYS part, a routing table from concrete decisions to chapters, the six kinds of statement, the provenance of the material (a Productscape model of a real company used as a research map; VWE only as a public case), Axleby in one paragraph, the fifteen failure patterns, and the living-journal note.

Productscape bricks covered: none as a product brick; the page is a preface over the whole model and points to [[domain-coverage]] for the brick-to-chapter map.

## Audience

Chief and enterprise architects of vehicle-data companies, dealer-software vendors and groups that run both; principal and staff engineers; data, valuation, integration and platform leads; product and engineering directors of portals, lessors, insurers and dealer groups. They are architecture-literate and need the argument and a route to the chapter for the decision on their desk, not definitions of caches or event streams.

## Success criteria

- [x] Opens with IN THIS PAGE / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE callouts and exactly three KEY POINTS, followed by a generic (non-Axleby) scene that poses an architecture question about one car's facts.
- [x] States the decisions-about-one-car argument with a decision table and the four properties of a fact fit to decide on, plus one mermaid diagram.
- [x] Explains the two halves and the share/keep-separate rule in a table, grounded in the KEY POINTS of [[vehicle-data-ecosystem]] and [[dealer-and-data-economics]].
- [x] Explains the market comparison rule with the four-column market shapes and examples of "one core, many adapters" drawn from written chapters.
- [x] Summarizes all ten parts in one table with each part's argument, describes the JOURNEYS part, and includes a second mermaid diagram.
- [x] Has a routing table of 12–18 decisions whose starting chapters were checked against those chapters' KEY POINTS, using only valid permalinks.
- [x] Explains the six kinds of statement in a table, with dated examples of why company and regulatory claims carry dates (Auto Trader's FY2025 and FY2026 results on Deal Builder; EU Data Act and Battery Regulation application dates).
- [x] States provenance, Axleby in one paragraph consistent with the ledger, the fifteen failure patterns in their four families, the living-journal note, and a hand-off to [[where-vehicle-platforms-go-wrong]]; 3,500–5,000 words before Sources and Evidence (about 4,750 excluding mermaid source).

## Non-goals

- The failure patterns in depth — [[where-vehicle-platforms-go-wrong]].
- Axleby's brands, volumes, systems, cast and incidents — [[meet-axleby]].
- The brick-by-brick coverage map and the reasons for each addition — [[domain-coverage]].
- The ecosystem history, economics, capability map and bounded contexts — Part I chapters.
- Per-chapter market comparisons — each chapter's "Across Markets" section.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Part introductions, Part I chapters 3–4, chapter 34, the JOURNEYS chapters and most of Part IX were not written when this page was drafted; their part arguments and routing rows follow PLAN.md contracts and must be rechecked against their KEY POINTS once they exist.
- `part-1` … `part-10`, `toolkit`, `glossary`, `bibliography` and `domain-coverage` resolve to other journals until this book's pages exist; they must resolve in-journal before publication.
- The "What the Book Leaves to Others" list (DMS accounting/parts/service, lending and insurance, new-car sales) should be aligned with [[domain-coverage]] once it is written.

## Decision log

- **2026-10-22** — Mirrored BOOKED's introduction (scene, audience, argument, organization table, routing table, evidence, provenance, running example, living journal), with "IN THIS PAGE" callouts as in this book's other preface pages, and without a failure-patterns callout.
- **2026-10-22** — Opened with a generic dealer-desk scene (three papers that disagree about one car) instead of an Axleby scene, so the argument stands before the fictional group is introduced.
- **2026-10-22** — Replaced BOOKED's three sharing grades with a two-column share/keep-separate table, because PLAN and [[vehicle-data-ecosystem]] state the rule as share facts, accounts, meters, licenses and events; keep cadence, workflow and external contracts.
- **2026-10-22** — Added a "Five Markets, One Core" section and a six-row evidence table (including labeled assumptions), because market comparison and assumption labeling are this book's distinctive disciplines.

## Sources

- **Internal**
  - `PLAN.md` (Positioning, Provenance, Structure, Comparison discipline, Preface contract); `_research/style-guide.md`; `_research/scenario-ledger.md`; `_research/productscape-digest.md` §1.
  - KEY POINTS and excerpts of all chapters written by 2026-10-22; [[where-vehicle-platforms-go-wrong]]; [[meet-axleby]]; "Across Markets" sections of [[vehicle-identity]], [[registers-and-official-data]], [[billing-and-metering]], [[privacy-and-retention]].
- **External**
  - Auto Trader Group plc, full-year results FY2025 (2025) and FY2026 (2026).
  - Regulation (EU) 2023/2854 (Data Act), Art. 50; Regulation (EU) 2023/1542 (batteries), Art. 77.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned part summaries with chapter key points, added three routing rows (security, privacy, AI agents), corrected the fitness-function list, Carfax ownership and the authorized-information-provider term, preface callout label. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
