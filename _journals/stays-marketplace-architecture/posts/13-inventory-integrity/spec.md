---
status: accepted
revised: 2026-10-21
---

# Spec: Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency

## Intent

Answer the chapter's question: how does a stays marketplace prevent selling inventory that does not exist, and what does it do when it happens anyway? The chapter separates three problems the industry calls "overbooking" (a hotel's deliberate overbooking, an accidental oversell, the double booking of a one-unit home) and gives each its own machinery in four layers: **guarantee** at the commit point where the marketplace owns the truth, **shorten** the windows it cannot close, **detect** oversells before arrival, and **recover** through walk, relocation, compensation and cost recovery. After reading, an architect can say where the no-double-sale guarantee lives for each kind of unit, why holds and locks are not that guarantee, and how to measure and govern oversells per connection and host.

Productscape domains covered: TAM `invt` (Supply Integrity Controls, reservation-state backbone), TAM `rsrv` (Reservation Exception Controls: overbooking, no-show), HSM `cala` (availability accuracy). The chapter also fills the model gap that HSM has no integrity layer and that neither model names the reservation system of record for an oversold or relocated reservation.

## Audience

Chief architects, principal engineers and inventory, booking and connectivity leads at OTAs and hosted-stays marketplaces, plus customer-service and partner-operations leaders who own the failure path. They know transactions, sharding and distributed locks; they need the travel vocabulary (allotment, free sale, walk, relocation) and a defensible design for each marketplace type.

## Success criteria

- [x] Defines free sale, allotment (with release date), inventory hold, overbooking, oversell, double booking, walk and relocation, and keeps deliberate overbooking separate from oversell in data, metrics and terms.
- [x] Shows the commit-point guarantee for a one-unit listing (uniqueness or exclusion constraint) and for a hotel room type (conditional multi-night decrement), with the acknowledgement-watermark rule for supplier counts, labeled as recommendation.
- [x] Explains holds with TTL and distributed locks as efficiency devices, citing Expedia Rapid hold-and-resume and Kleppmann's fencing-token argument.
- [x] Covers cross-channel windows with documented intervals (Booking.com polling and fallback, Airbnb iCal import) and four window controls, including the auto-replenishment trade-off from Booking.com's documentation.
- [x] Works both canonical Corvane cases with ledger numbers: King's Day (47 minutes, 9 rooms, 4 Roomstead guests, €2,150, €1,600 recovered) and Seville (€1,360, €1,780, €420, €130).
- [x] Gives an oversell metric set, a concurrency trade-off table, a window-policy table, a liability matrix and the "Hotels and Homes" comparison with a judgement on what to share.
- [x] Three mermaid diagrams with captions; 6–10 questions to ask; dated sources.

## Non-goals

- iCal mechanics, polling tiers and conflict-window probability — [[calendar-sync]].
- The booking saga, idempotency keys, instant book and request to book — [[checkout-orchestration]].
- Reservation delivery, acknowledgement and the state machine beyond the oversell case — [[reservation-lifecycle]].
- Connectivity standards, certification and update ordering in depth — [[connectivity-and-channel-managers]].
- Availability caching and price accuracy — [[availability-engine]].
- Support case tooling for relocations — [[customer-service]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company publishes its internal inventory-locking or double-booking prevention design; the chapter labels the reading of public contracts as inference. Revisit if a primary engineering source appears.
- Booking.com's contractual relocation obligation (who pays) was not found in fetchable partner terms.
- No authoritative, recent industry figure for hotel walk rates or OTA oversell rates exists; the Riasi (2018) survey rests on a 3.77% response rate.
- Airbnb's iCal import interval is documented as three hours on an undated help page that has changed before.

## Decision log

- **2026-10-21** — Framed the chapter around three problems (overbooking, oversell, double booking) rather than one "overbooking" topic, because the controls, owners and liability differ; rejected a single oversell taxonomy keyed by marketplace type.
- **2026-10-21** — Chose "guarantee, shorten, detect, recover" as the architecture spine, and made the store-owning-the-truth the only guarantee; holds and distributed locks are presented as efficiency devices.
- **2026-10-21** — Introduced the acknowledgement watermark and a property-sharded allocation ledger beside Tally as Corvane recommendations, because Tally's per-date partitioning cannot decrement several nights atomically.
- **2026-10-21** — Keyed integrity policy to unit cardinality, not brand, so Roomstead's single-unit apartments get the hosted-stays posture; shared the failure path (case model, relocation service, liability matrix, metrics) but not the commit mechanism.

## Sources

- **Internal**
  - [[rates-and-availability-model]], [[availability-engine]] — the claims the commit point reads.
  - [[calendar-sync]] — Seville window mechanics and Calendar Sync v2.
  - [[connectivity-and-channel-managers]] — King's Day queue replay; certification.
  - [[checkout-orchestration]], [[reservation-lifecycle]], [[customer-service]] — holds in the saga, acknowledgement, relocation workflow.
  - `_research/brief-availability-pricing.md` Part 10, `brief-booking-reservations.md` Parts 5, 8, 9, `brief-supply-connectivity.md` Parts 3, 5, 6; `productscape-digest.md` (`invt`, `rsrv`, `cala`, stressor `insv`).
- **External**
  - Booking.com Connectivity, *Troubleshooting overbookings* (n.d.) — causes, reservation-timeline race, auto-replenishment, relocation.
  - Expedia Group Rapid, *Hold and Resume* and *Common error responses* (n.d.) — holds and sold-out outcomes.
  - PostgreSQL 18 documentation, *Range Types* — exclusion constraints.
  - Martin Kleppmann, *How to do distributed locking* (2016) — fencing tokens.
  - Riasi (2018) and eCornell/Kimes — overbooking as revenue control.
  - Airbnb Help Center articles 99, 990, 3218; Vrbo Help — iCal interval, host penalties, guest rehousing.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,923 to under 8,500 words (merged the window-policy table into prose, cut repeated vendor evidence and restated controls), removed code-block wrappers around mermaid fences, dropped an unverifiable IDeaS integration-guide citation and an Agoda "reportedly" claim, dated Airbnb fee facts "as of 2026", timetoread 35 min. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the three-kinds-of-overbooking figure without the "$" coin. *(AI-mediated session)*
