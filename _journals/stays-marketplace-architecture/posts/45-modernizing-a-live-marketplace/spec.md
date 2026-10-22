---
status: accepted
revised: 2026-10-21
---

# Spec: Changing the Engine in Flight: Modernizing a Live Stays Marketplace

## Intent

Answer the chapter's question: how do you move a live booking platform to a new architecture without losing bookings or money? The chapter argues that a stays migration is a sequence of seams (contract, consumers, logic, writes, reservations in flight) rather than a project with a cutover date, that parallel runs must be judged by explained differences including money, and that long booking windows and post-stay tails make in-flight reservation migration, not drain alone, the deciding design problem. After reading, an architect can order a monolith exit, design price and reservation parallel runs, plan a cohort-based write cutover with batched migration of future reservations, define rollback and a point of no return, and choose progress metrics that measure safe promises rather than migrated code.

Productscape domains covered: none as a product brick; the chapter is a leadership chapter that cuts across TAM `book`, `invt`, `rsrv` and HSM `book`, `trip` (reservation ownership during migration) and the platform foundations. It owns **in-flight reservation migration** and **parallel run (stays)**.

## Audience

Chief and enterprise architects, principal engineers and engineering directors at OTAs and hosted-stays marketplaces who own or fund a monolith exit. They know the strangler fig, CDC and dual reads; they need the stays-specific problems (reservations with future dates, partner identifiers and sequences, money in flight) and a plan shape they can defend to a CFO.

## Success criteria

- [x] Defines seam, system of record, projection, parallel run (shadow and dual), in-flight reservation migration, drain, reverse sync and point of no return, and shows with booking-window arithmetic why drain alone misses a dated retirement.
- [x] Gives the contract-first architecture (Figure 1), a component ownership table, the ownership register and the identifier rules.
- [x] Covers three kinds of parallel run (availability, price, reservation state) with a worked price shadow run and money comparison.
- [x] Cites dated public migrations: Airbnb Monorail to SOA (2018–2019), Booking.com Perl fragments and data lake (2026), Expedia front-end consolidation and Vrbo's slower recovery (2023–2024), Agoda price cache and post-booking (2026), with a labeled inference where evidence stops.
- [x] Works Corvane's Keystone Exit Plan consistently with the ledger and earlier chapters (Stayline stages, Clause, offer kernel, Courier, commission invoicing on Fathom, Corvane ID, end-2029 target), with the 13 December 2027 open-book comparison and the Portugal cohort numbers.
- [x] Includes a trade-off table, the "Hotels and Homes" comparison with a sharing judgement, failure modes, the Chief Architect's view and 10 questions; three mermaid diagrams with captions.
- [x] Stays under 8,500 words before Sources and Evidence (about 7,200).

## Non-goals

- Outbox, CDC translator mechanics and event governance — [[event-driven-stays]].
- The reservation state machine, delivery and Stayline's design — [[reservation-lifecycle]].
- Idempotency and the checkout saga — [[checkout-orchestration]].
- Context boundaries and anti-corruption layers in general — [[stays-bounded-contexts]].
- Whether to converge the two marketplaces — [[converging-two-marketplaces]]; team design for the migration — [[organizing-stays-engineering]].
- Cloud migration and failover of Keystone's data centers — [[global-scale-and-reliability]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company has published how it moved confirmed future reservations between systems of record; the chapter's method is labeled as inference and recommendation. Revisit if a primary source appears.
- Expedia's filings do not explain Vrbo's slower recovery after re-platforming; the chapter's reading is labeled as the author's.
- Roomstead's open book (5.6 million) and its 16-month horizon are illustrative estimates derived from the ledger's booking-window figures; the chapter added them to the ledger.
- Web search was unavailable; Fowler's 2024 page was fetched, other facts come from the research briefs.

## Decision log

- **2026-10-21** — Scoped Corvane's target to Keystone's reservation module, leaving the catalog and Partner Hub web module for 2030+, to stay consistent with the ledger's "reservation module retired by end of 2029" and to make scope explicit as a lesson.
- **2026-10-21** — Built Wave 1 entirely from dates already committed in chapters 21, 23, 24, 28, 33 and 34, so the plan composes rather than invents new commitments.
- **2026-10-21** — Chose market cohorts by property location as the cutover unit, far-future-first arrival batches, a 14-day drain edge and a 90-day signed point of no return, as labeled judgement.
- **2026-10-21** — Kept the Hotels and Homes section (optional in Part IX) because the Burrow move in 2028 has distinct risks (Pay Later stored credentials, calendar claims).

## Sources

- **Internal**
  - [[reservation-lifecycle]], [[event-driven-stays]], [[checkout-orchestration]], [[stays-bounded-contexts]], [[availability-engine]], [[changes-and-cancellations]], [[payouts-and-settlement]], [[refunds-and-reconciliation]], [[stay-payments]], [[stays-experimentation]].
  - `_research/brief-airbnb.md` 2.1; `brief-platform-data-ml.md` 3.1–3.4, 4.1; `brief-booking-com.md` 2.1, 2.7; `brief-expedia-agoda-tripcom.md` 1.3, 6.4, 7; `scenario-ledger.md`.
- **External**
  - Fowler, Strangler Fig Application (2024).
  - Tai, The Great Migration (InfoQ, 2018); InfoQ summary (2019).
  - Booking.com Engineering, Node.js at scale (2026); data-lake migration (2026).
  - Expedia Group 10-K FY2022 (2023) and FY2023 (2024); Q1 2024 results (2024).
  - Agoda Engineering, price cache (2026); post-booking coupling (2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Checkout attempt contract timing aligned with its March–April 2027 rollout. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
