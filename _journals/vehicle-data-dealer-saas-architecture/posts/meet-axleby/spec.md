---
status: accepted
revised: 2026-10-22
---

# Spec: Meet Axleby: A Data Business and a Software Business Under One Roof

## Intent

Introduce the fictional running example once, in one place, so that every chapter can open with an Axleby scene without re-explaining the group. The page presents Axleby Group as a composite of common industry patterns (not a disguised company): its history by acquisition, its five brands and two halves (vehicle data services and dealer SaaS), its business models and illustrative 2027 prices, its markets and customers, its 2026 volumes, its 2027 systems landscape, the cast with pronouns, the eleven recurring incidents with the chapter that owns each, the six problems it starts 2027 with and the One Dossier program. After reading, the reader can follow any chapter's worked example and knows where each recurring number comes from.

Productscape bricks covered: none as a topic; the page frames the scenario in which all bricks are later discussed.

## Audience

Chief and enterprise architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors, portals, lessors and dealer groups. They need a coherent, believable landscape to reason about, not a primer on cars or SaaS.

## Success criteria

- [x] Every Axleby fact (revenue, brands, prices, customer counts, volumes, systems, cast, incidents, One Dossier scope and dates) agrees with `_research/scenario-ledger.md`; revenue lines sum to €214 million.
- [x] Labels Axleby fictional in the callouts, the opening and the Sources section, and states it is not VWE, Autotelex, Cox, CDK, Auto Trader, DAT or Carfax; no incident is attributed to a real register.
- [x] Includes a mermaid landscape diagram and a "two vehicle keys, three logins" diagram, each with a captioned point.
- [x] The cast table gives pronouns; customers and partners are listed separately.
- [x] The eleven recurring incidents appear in one table with date, numbers, pattern and owning chapter as a cross-link.
- [x] Each of the six 2027 problems names its failure pattern and the chapters that work it.
- [x] Preface-style callouts ("IN THIS PAGE, YOU WILL"); no "Across Markets" section; about 5,000 words before Sources.

## Non-goals

- The industry's real history and participants — [[vehicle-data-ecosystem]].
- The failure patterns themselves — [[where-vehicle-platforms-go-wrong]].
- Designing any of the systems named — each chapter owns its system (for example Anchor in [[vehicle-identity]], Meterline in [[billing-and-metering]]).
- The One Dossier program as a program (sequencing, capability map v2) — [[one-platform-from-many-products]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Chapters may append facts to the ledger after this page was written (for example capability-map counts, team sizes); a review pass should fold canonical additions that matter to the whole book back into this page.
- The ledger's Lotwise and Showroomly revenue per rooftop is higher than the list prices imply (groups, fees, add-ons); the page deliberately does not compute revenue per rooftop. [[dealer-and-data-economics]] should reconcile it if it uses the figure.

## Decision log

- **2026-10-22** — Mirrored BOOKED's `meet-corvane` structure (glance, history, brands, volumes, landscape, people, problems, program, recurring examples) but replaced its prose paragraph per example with one table, because eleven incidents with owners read faster as rows and keep the page near 5,000 words.
- **2026-10-22** — Added a separate "two vehicle keys, three logins" subsection and diagram, because that property, not the system list, is what the dealer feels and what One Dossier's Year 1 attacks.
- **2026-10-22** — Stated that Axleby Portal accounts serve both the Axleby Data portal and Axleby Trade, to reconcile "five products" with "three login systems"; appended to the ledger.
- **2026-10-22** — Kept the Plate Enumeration Attack as a threat rather than forcing it into a failure pattern, pointing to License Blindness as the nearest.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — every Axleby fact.
  - `PLAN.md` — the chapter that owns each incident and term.
  - BOOKED's `meet-corvane` page (stays-marketplace-architecture) — structure and conventions.
- **External**
  - None; real registers and suppliers are named only as what they are, and sourced in the chapters that use them.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: added the group platforms the chapters introduce, the CISO and four recurring partners, 2027 milestones, v2 and retirement dates, Lotwise revenue composition and VAT-inclusive Odolo prices; aligned the Lost Leads wording with the editor line. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
