---
status: accepted
revised: 2026-10-21
---

# Spec: Booking.com: Experimentation, Connectivity and the Agency Model at Scale

## Intent

Read Booking.com's public record as an architecture case for chief architects of stays marketplaces, keeping documented fact, the author's interpretation and labeled inference visibly apart. The case lands three arguments. First, the published supply contract (OpenTravel 2003B plus B.XML and JSON; delta-only ARI; four per-property pricing models; pull-and-acknowledge reservations with a 30-minute email fallback) is the most durable part of an OTA's architecture and outlived a platform era. Second, experimentation works at Booking.com as a change-control mechanism, migrations included, but quality had to be measured before it improved. Third, the move from agency to merchant (70% of gross bookings in 2025) and the use of commission and programs in ranking have become regulated architecture (CNMC 2024, DMA 2024, AGCM 2026). Running through all three is how Booking.com's homes business (about 3.9 million of 4.4 million properties, 36% of room nights) differs from its hotel business, and what that means for the Hotel-Shaped Home pattern. After reading, the reader can use the case as evidence in their own design reviews without overstating what is known.

Productscape domains covered: none as a primary owner (Part X case). Touches TAM supply connectivity, inventory and rates, search ranking, booking delivery, payments and regulation, as reference evidence for the chapters that own them.

## Audience

Chief and principal architects, engineering directors and product leaders of OTAs, hosted-stays platforms, channel managers and PMS vendors who compete with, integrate with or are compared to Booking.com. They want the documented record, dated, and a clear line where evidence stops.

## Success criteria

- [ ] Every Booking.com claim carries a dated source (API documentation as "read October 2026"); pre-2023 sources are marked as dated and not used in the present tense.
- [ ] Inferences about undocumented internals (ARI ingestion, availability search, homes-to-merchant link) sit in labeled `INFERENCE, NOT DOCUMENTED` callouts.
- [ ] Covers the supply contract (formats, roomrate model and limits, ARI rules, pricing models, rate limits, reservation delivery and overbooking causes) with a delivery diagram.
- [ ] Covers experimentation (2017 paper, ET and about 1,000 experiments, quality measurement, infrastructure behind experiments, latency-conversion lesson) and the two-era platform table.
- [ ] Covers the money model (revenue-mix table 2023–2025, agency vs merchant, payout rails, Italian tax settlement) and ranking regulation (How we work, Preferred, CNMC, DMA, CJEU, AGCM, DSA).
- [ ] Has a homes-vs-hotels table for Booking.com's own two businesses and a judgement on the Hotel-Shaped Home pattern.
- [ ] Includes trade-offs, failure modes, a "Where the Public Evidence Stops" table, the Chief Architect's view, a comparison to the book's patterns and to Corvane's choices with ledger-consistent numbers, questions to ask, and a hand-off to [[case-airbnb]].
- [ ] Article at or under 8,500 words before Sources, aiming at the 5,000–7,000 case-study range.

## Non-goals

- Teaching connectivity, ARI modeling, ranking, experimentation, payments or regulation from first principles; the owning chapters ([[connectivity-and-channel-managers]], [[rates-and-availability-model]], [[stays-ranking]], [[stays-experimentation]], [[merchant-and-agency-models]], [[stays-regulation]]) do that.
- Describing Booking.com's availability search, reservation system or homes/hotels code split as fact; none is publicly documented.
- Genius and Preferred commission terms (partner pages inaccessible; vendor reports only).
- Agoda and other Booking Holdings brands ([[case-agoda-trip-com]]).
- A "Setting the scene at Corvane" or "Hotels and Homes" section (Part X rule); Corvane appears only in the final comparison.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The CNMC appeal, German damages cases and the Amsterdam hotel class action are unresolved as of October 2026; revisit before publication.
- The KDD 2019 paper is cited via Adrian Colyer's review; replace with the paper if it becomes accessible.
- The FY2025 10-K legal-proceedings note was not read; legal facts come from regulators and press.
- Whether Booking.com's OpenTravel acknowledgement implies PMS acceptance is not public; the chapter leaves it open.

## Decision log

- **2026-10-21** — Followed LISTED's case-study shape (how to read, timeline, themed sections, trade-offs, failure modes, evidence gaps, Chief Architect's view, comparison) rather than the Part II–VIII chapter template, per the Part X rules.
- **2026-10-21** — Made the supply contract the first deep section, because it is the best-evidenced part of the record and the most transferable; put availability search in its own short "goes dark" section with one labeled inference instead of spreading speculation.
- **2026-10-21** — Treated the homes business as a qualification of the Hotel-Shaped Home pattern (workable for unit-like homes, with grafted seams) rather than a refutation, and tied it to the One Stay "shared contracts, separate engines" decision.
- **2026-10-21** — Compared revenue-mix and merchant-share measures carefully (Booking.com: share of gross bookings; Roomstead: share of room nights) and noted the difference in the Corvane table.

## Sources

- **Internal**
  - [[connectivity-and-channel-managers]], [[reservation-lifecycle]], [[inventory-integrity]], [[rates-and-availability-model]], [[availability-engine]], [[stays-experimentation]], [[stays-ranking]], [[merchant-and-agency-models]], [[taxes-on-stays]], [[converging-two-marketplaces]], [[modernizing-a-live-marketplace]].
  - `_research/brief-booking-com.md` (primary); relevant parts of `brief-supply-connectivity.md`, `brief-availability-pricing.md`, `brief-payments-finance-tax.md`, `brief-host-partner-guest-service.md`, `brief-platform-data-ml.md`, `brief-search-discovery.md`; `scenario-ledger.md`.
- **External**
  - Booking Holdings Form 10-K FY2025 (2026); Booking.com Developers connectivity documentation (n.d., read October 2026); Booking.com "How we work" (2025); partner pages on Preferred and Payments by Booking.com (n.d.).
  - Booking.com Development blog and booking.ai (2026); SREcon EMEA slides (2024); CNCF case study (2020); AWS case study and Database Blog (n.d., 2026); Highload++ abstract (2017).
  - Lopez Kaufman et al. (2017); Mavridis et al. (2018); Colyer's review of the KDD 2019 paper (2019).
  - European Commission DSA and DMA pages (2023, 2024); CJEU Case C-264/23 (2024); AGCM PS13115 (2026); press on the CNMC fine (2024, 2025) and German litigation (2025).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: expanded CNCF and KDD on first use; spot-checked the AGCM release and the 30-minute reservation fallback (both confirmed). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
