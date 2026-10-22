---
status: accepted
revised: 2026-10-22
---

# Spec: Drawing the Lines: Bounded Contexts for Stays

## Intent

Closing chapter of Part I (MARKETPLACE). It turns the capability map of [[stays-capability-map]] into a decomposition: where the service and team boundaries of a stays platform should go, and which of them a group running both an accommodation marketplace and a hosted-stays marketplace can share. The chapter must establish three ideas: boundaries go where the meaning of a night changes; the **offer** and the **reservation** are the two aggregates that carry the guest's promise and must be computed or frozen once and read by everyone else; and across hotels and homes a group should share contracts and money, trust and identity services, not one supply model. The reader leaves able to classify subdomains per marketplace type, draw a context map with named relationships (anti-corruption layers toward channel managers, PMSs, iCal and monoliths; open host services; published language), and test a proposed shared component against "share a language, not a database".

Owns: **offer**, **context map**, **reservation aggregate** (briefly; deep in [[reservation-lifecycle]]).

Productscape domains covered: all bricks of both models as inputs to the context list (TAM 34, HSM 21), with emphasis on TAM `invt`, `book`, `room`, `paym`, `sett`, `conn` and HSM `book`, `cala`, `paym`, `apix`, `comp`, and both models' residuality separations.

## Audience

Chief and enterprise architects of travel groups, principal engineers and engineering directors who are planning a decomposition of a stays monolith or deciding what two marketplace brands should share. They know DDD vocabulary loosely and need it applied precisely to stays, with concrete boundaries, relationships and ownership.

## Success criteria

- [ ] Defines subdomain (core, supporting, generic), bounded context, ubiquitous language, context map, the relationship patterns, aggregate and domain event in a few paragraphs, without re-teaching DDD at length.
- [ ] Shows with a table that the same subdomain can be core for an OTA and supporting for a hosted-stays marketplace, and draws the sharing rules from it.
- [ ] Lists candidate contexts for a stays platform with what each owns and must not do, and links each to the chapter that goes deep.
- [ ] Defines the offer (five parts, computed, immutable, short-lived) and fixes the reservation aggregate's boundary (what it contains and what belongs to other aggregates), with a diagram.
- [ ] Draws a context map with named relationships, including anti-corruption layers toward partner systems, iCal and monoliths, and a table of shared kernels to avoid.
- [ ] Gives dated public evidence (Airbnb 2018, 2022, 2026; Agoda 2025, 2026; Expedia 2024; Booking.com 2026 and connectivity docs) with inferences labeled.
- [ ] Works the Corvane example (the April 2027 tracing exercise, Context Map v1, the decisions that followed) with ledger-consistent numbers.
- [ ] Includes a trade-off table, a hotel-versus-home comparison table, failure modes, the Chief Architect's view and 6–10 questions; at least two diagrams (illustrated).

## Non-goals

- The reservation state machine, delivery and acknowledgement in depth ([[reservation-lifecycle]]).
- The booking saga, holds and idempotency ([[checkout-orchestration]]).
- The supply data model of properties, room types, units and listings ([[property-and-listing-model]]).
- Event contract design, outbox and CDC mechanics ([[event-driven-stays]]).
- Team topologies and governance structures ([[organizing-stays-engineering]]) and the full convergence decision ([[converging-two-marketplaces]]).
- The payment arrangement's fields and resolver ([[merchant-and-agency-models]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should the change-and-cancellation policy evaluator become one group engine, or stay one evaluator per marketplace behind a shared vocabulary? Left to [[changes-and-cancellations]].
- Whether reviews should become a shared context (double-blind host reviews vs one-sided hotel reviews) is not decided in Map v1; [[reviews-and-reputation]] may revisit.
- The chapter's word count runs above the 7,500-word guide because of two large tables (candidate contexts and Map v1); a later pass could merge them.

## Decision log

- **2026-10-21** — Chose "the meaning of a night" as the organizing word (Fowler's "meter") rather than "booking", because chapter 39 owns the two definitions of a booking and "night" spans supply, inventory, money and tax.
- **2026-10-21** — Treated the offer as a context and an aggregate in its own right, rather than as a step of search or checkout, to anchor the Price Drift and Policy Spaghetti arguments used by chapters 12, 20 and 26.
- **2026-10-21** — Set the Corvane scene as a two-day tracing exercise (28–29 April 2027) after the April commission audit, and Context Map v1 on 5 May 2027, so the ledger's later forum decisions (place registry, Fathom, payment arrangement, offer kernel, search contract, Stayline) read as boundaries on that map.
- **2026-10-21** — Classified search and ranking and change and cancellation policy as shared contracts, consistent with the One Stay capability map's six shared contracts, and the reservation as a shared contract that later becomes one service (Stayline), consistent with the ledger.

## Sources

- **Internal**
  - [[stays-capability-map]] — capability inputs and the One Stay capability map.
  - [[property-and-listing-model]], [[connectivity-and-channel-managers]], [[calendar-sync]], [[rates-and-availability-model]], [[availability-engine]], [[property-page-and-room-selection]], [[merchant-and-agency-models]], [[payouts-and-settlement]], [[taxes-on-stays]] — components and decisions the map must match.
  - `_research/productscape-digest.md`, `brief-platform-data-ml.md`, `brief-booking-reservations.md`, `brief-airbnb.md`, `brief-expedia-agoda-tripcom.md`, `scenario-ledger.md`.
- **External**
  - Evans, *Domain-Driven Design* (2003); Vernon, *Implementing Domain-Driven Design* (2013); Fowler, "BoundedContext" (2014) and "DDD_Aggregate" (2013); DDD Crew, Context Mapping; Conway (1968).
  - Tai, "The Great Migration", QCon 2018; Airbnb, "Rebuilding Payment Orchestration" (2022), "Pay as a Local" (2026), "Scaling beyond one" (2026).
  - Agoda, post-booking coupling post (2026) and multi-product booking engine (2025); Expedia 10-K for 2023; Booking.com Node.js post (2026) and connectivity documentation.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 10,432 to 8,500 words; Context Map v1 checked against capability map v2 (Clause supersedes per-engine policy evaluators; Vouch; Waypoint and place registry as two contexts); subdomain rule 3 example corrected to offer composition; unsourced Booking.com/Expedia monolith claim removed. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,443 → 5,436 prose words; opening now states the chapter closes Part I and names the chapters that build on the map; two skim-path paragraphs now open with their claim; one needless sentence cut; unclosed quotation in Question 1 fixed. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 5,443 → 5,162 prose words (HEAD → now, both passes); Failure Modes compressed to one-line bullets pointing to the sections that handle each, keeping the May 2027 metasearch figures and the €3.4 million debit balances; Chief Architect's view, the lead, the "what a night means" close and the closing hand-off stripped of restatements; duplicate "no public context map" intro and the repeated "platforms are not contexts" line removed. *(AI-mediated session)*
