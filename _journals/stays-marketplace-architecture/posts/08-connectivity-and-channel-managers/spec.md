---
status: accepted
revised: 2026-10-21
---

# Spec: Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards

## Intent

An accommodation marketplace sells against a copy of availability, rates and inventory (ARI) that someone else's software asserts: a PMS, a CRS or a channel manager. This chapter lands that fact and its consequences. The reader should leave able to design a connectivity gateway that does more than parse XML: one that normalizes partner dialects into one internal command, validates every value against what the marketplace knows about the property (not only against a schema), applies updates in order per property, reconciles its copy with the partner's view, proves that each reservation reached the hotel's PMS, and scores partners on all of this so that connectivity becomes a product with consequences. The Corvane thread is the €12 rate at Hotel Miradouro, where both the channel manager (Corvane Connect) and the channel (Roomstead) belong to the same group, which also raises the governance question of neutrality.

Productscape domains covered: TAM `conn` (Connectivity & Partner APIs), TAM `invt` (inventory sync and supply integrity controls, ingestion side only), HSM `apix` (Partner APIs & Channel Connectivity, in the Hotels and Homes comparison).

## Audience

Chief architects, principal engineers and supply/connectivity leads of OTAs and channel-manager or PMS vendors. They know distributed systems; they may not know the hotel stack, OpenTravel, or how the large channels' public contracts differ. They should walk away with a gateway reference architecture, a guard taxonomy, a partner-health model and a set of design-review questions.

## Success criteria

- [ ] Reader can name the systems in the hotel stack (PMS, CRS, channel manager, RMS, booking engine, GDS/switch), say which one asserts which part of the truth, and explain why push beats pull for direct supply (look-to-book).
- [ ] Reader can explain why "OpenTravel-compliant" does not mean interoperable, using dated public examples (Booking.com 2003B + B.XML, AlpineBits 2015A, date-range conventions, Expedia IDs only).
- [ ] Reader can design the seven gateway responsibilities (edge, normalize, validate, sequence, store, reconcile, deliver) with boundaries, and the partner registry behind them.
- [ ] Reader can explain why semantic guards (sibling band, property envelope) catch the €12 error that schema, absolute bounds and same-product history miss, and choose between reject, hold-with-last-good-value and hold-closed.
- [ ] Reader can state the ordering, idempotency and reconciliation rules (per-property lanes, absolute values, message-ID dedup, digests, diffed full sync) and the delivery rules for reservations (outbox, per-version order, PMS-number acknowledgement, sticky fallback).
- [ ] Reader can define a partner health score from gateway data and name the levers that give it consequences.
- [ ] The Hotels and Homes section contrasts Roomstead's Switchyard with Nookaway's partner API and iCal using ledger numbers, and makes a specific sharing judgement.
- [ ] Every company claim carries a dated source; Corvane numbers match the ledger.

## Non-goals

- The ARI data model itself (rate plans, restrictions, LOS pricing, derived rates): [[rates-and-availability-model]].
- The availability cache, offer computation and price accuracy: [[availability-engine]].
- Overbooking, allotments, concurrency on sale and walking guests (King's Day in depth): [[inventory-integrity]].
- The reservation aggregate and state machine: [[reservation-lifecycle]]; outbox and event design in general: [[event-driven-stays]].
- iCal and multichannel hosts (the Seville double booking): [[calendar-sync]].
- Property and room mapping across suppliers and bedbank content: [[content-and-media]].
- Partner-account takeover and extranet phishing: [[travel-fraud]].
- Metasearch price feeds and demand-side distribution APIs: [[demand-channels]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Expedia's current supply documentation sits behind a partner portal; the chapter relies on a December 2025 archived copy for AR and Booking Notification. Re-check if the portal becomes readable.
- No company publishes ARI message volumes or ARI push-to-bookable latency; the chapter uses only Agoda's 2024 burst figure and Corvane's fictional numbers.
- Booking.com connectivity partner tier criteria are known only from partner press releases.
- The OpenTravel and HTNG specification texts were not read directly; message semantics come from implementers' documentation.

## Decision log

- **2026-10-21** — Framed the chapter around the gateway (Switchyard) rather than around the channel manager, because the reader is usually on the marketplace side; the channel manager is covered as the counterparty and through Corvane Connect's own fixes.
- **2026-10-21** — Made "hold" a first-class outcome with two variants (last good value vs closed) instead of the usual reject/accept binary, because the €12 incident and the replay figures show that human review cannot scale to the hold volume.
- **2026-10-21** — Kept reservation delivery in this chapter at the protocol level (outbox, ordering, acknowledgement, fallback) and left the reservation state machine to [[reservation-lifecycle]], to avoid duplicating the aggregate.
- **2026-10-21** — Treated Corvane owning both a channel and a channel manager as a governance decision (neutrality rule) rather than a technical one; rejected giving Corvane Connect a privileged integration path.

## Sources

- **Internal**
  - [[meet-corvane]] and the scenario ledger — Roomstead connectivity volumes, Corvane Connect, the €12 rate, King's Day.
  - [[rates-and-availability-model]], [[availability-engine]], [[inventory-integrity]], [[reservation-lifecycle]], [[calendar-sync]] — neighbouring ownership.
- **External**
  - Booking.com Connectivity API documentation (n.d., live October 2026) — formats, limits, delta rule, price bounds, read-back, reservation queue and fallback, certification, Homes endpoint sunset.
  - Expedia Group supply documentation (2025 archived; supply hub live 2026) — AR scope, Booking Notification semantics, no direct property connections.
  - Google Hotel Ads delivery modes (2025) and ARI reference (2025) — the four delivery models; delta semantics.
  - Oracle OHIP (2021, n.d.) and Mews (n.d.) — PMS-side event delivery.
  - Agoda engineering (2020, 2024) — pull QPS budgets and push burst volume.
  - Hospitality Net (2016) — look-to-book.
  - AlpineBits, OpenTravel, HTNG sources — standards landscape.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,210 to 8,461 words (repetition, scene-setting, failure modes, Chief Architect's view, one question merged), aligned forum name and King's Day date with the ledger, expanded OTA/GDS, verified Booking.com reservation-delivery and price-bound claims. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: aligned the hold-states alt text with the single Held state the image shows. *(AI-mediated session)*
