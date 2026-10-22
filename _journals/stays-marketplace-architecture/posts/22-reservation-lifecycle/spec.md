---
status: accepted
revised: 2026-10-21
---

# Spec: The Life of a Reservation: State Machines, Delivery and Operations

## Intent

Answer the chapter's question: what happens to a reservation between booking and check-out, and how do the guest, the marketplace and the property or host stay in agreement? The chapter treats the reservation as a long-lived, versioned, multi-party agreement replicated into systems the marketplace does not own. It separates four state dimensions (commercial, delivery, stay, money) with one owner each, defines delivery as acceptance by the property's system rather than receipt by an intermediary, adds pre-arrival verification, and shows how stay facts (arrival, no-show, stayed, completed) trigger money, reviews and regulatory reporting through events. After reading, an architect can design the reservation aggregate, its state machine and clocks, the delivery tracker, the exception rules and the completion triggers, and can say what a group should share across an OTA and a hosted-stays marketplace.

Productscape domains covered: TAM `invt` (Reservation State Machine module), TAM `rsrv` (Reservation Work Queue, Reservation Exception Controls), TAM `book` (Reservation API, Reservation Event Feed, booking-state management after commit), HSM `book` (reservation orchestration after commit), HSM `trip` (reservation timeline service). The chapter fills the model gap that neither model defines the reservation entity or its states.

## Audience

Chief architects, principal engineers, booking, connectivity and partner-operations leads at OTAs and hosted-stays marketplaces, and the payments and finance engineers who consume stay facts. They know outboxes, event streams and state machines; they need the travel vocabulary (acknowledgement, PMS confirmation number, no-show reporting, stayed, completion) and a defensible model that works for both marketplace types.

## Success criteria

- [x] Defines reservation, reservation version, booking snapshot, reservation delivery, acknowledgement, confirmation numbers, no-show, stayed, completion and reservation exception, and explains why a single status field fails.
- [x] Gives a commercial state machine (Figure 1) with modification as a version, cancellation with cause, reversible no-show, and an explicit completed state, labeled as reference model, plus a table of clocks with owners and expiry actions.
- [x] Gives the delivery state machine (Figure 3) with three acknowledgement levels and argues acceptance with a PMS number as the only closing state, citing Booking.com and Expedia partner documentation with dates.
- [x] Covers pre-arrival verification (read-back, arrivals manifest, human confirmation), supplier-originated transitions (Booking.com no-show and invalid-card windows), the reservation event catalog, exception rules, and the stay triggers evidenced by the Airbnb, Booking Holdings and Expedia 10-Ks.
- [x] Covers auditability and retention with DAC7 record retention, the EU STR Regulation's activity data and GDPR storage limitation.
- [x] Works the Hotel Miradouro missing-reservations case with consistent fictional numbers (19 Roomstead reservations, 33 failed messages, €390 walk, 1,040 of 260,000 disagreements) and replays it under the redesign; works the Novak lifecycle with ledger numbers.
- [x] Includes a trade-off table, the "Hotels and Homes" section with a judgement on what to share, failure modes, the Chief Architect's view and 10 questions to ask; three mermaid diagrams with captions.

## Non-goals

- The booking saga, idempotency keys, instant book and request to book mechanics — [[checkout-orchestration]].
- Cancellation policy models, modification flows and mass disruptions — [[changes-and-cancellations]].
- Itinerary, check-in instructions, messaging and notification routing — [[trip-and-messaging]].
- Case management and recovery decisions — [[customer-service]].
- Transport-level delivery (push versus pull, ordering, rate limits, certification programs) — [[connectivity-and-channel-managers]].
- Oversell prevention, walking and relocation — [[inventory-integrity]].
- The exception work-queue design and delegation — [[extranets-and-host-tools]].
- Outbox, change data capture and event-schema governance — [[event-driven-stays]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company publishes its internal reservation state machine or delivery tracker; the chapter labels its reading of public contracts as inference. Revisit if a primary engineering source appears.
- Expedia's Booking Notification requirements and SiteMinder's pmsXchange pages were seen only as search excerpts (login-gated); quotations from them are tagged accordingly.
- No public channel documents a reservation read-back or arrivals manifest as a partner obligation; the manifest is presented as the author's recommendation.
- Measured rates of "booking not found at check-in" are not published by any company; the 0.4% Corvane figure is fictional.

## Decision log

- **2026-10-21** — Split reservation state into four dimensions (commercial, delivery, stay, money) with one writer each, instead of one extended status enum, because the Miradouro failure and the April 2027 commission audit both came from one field carrying several meanings.
- **2026-10-21** — Treated modification as a version of a confirmed reservation, not a state, and relocation as a linked reservation owned by [[inventory-integrity]], to keep the state machine small and auditable.
- **2026-10-21** — Introduced Stayline as the One Stay reservation service, staged as an event-fed tracker (Q4 2027) before becoming the system of record (Nookaway 2028, Roomstead 2029), consistent with the ledger's Keystone retirement target; rejected a big-bang move out of Keystone.
- **2026-10-21** — Recommended versions plus an outbox over full event sourcing, and the arrivals manifest over read-back as the general pre-arrival check, both as labeled judgement.

## Sources

- **Internal**
  - [[connectivity-and-channel-managers]] — Switchyard delivery rules, 10-minute escalation, neutrality rule.
  - [[extranets-and-host-tools]] — exception queue, 20-minute rule, three-hour escalation.
  - [[inventory-integrity]] — relocation as a linked reservation; acknowledgement watermark.
  - [[merchant-and-agency-models]], [[stay-payments]], [[payouts-and-settlement]], [[taxes-on-stays]] — payment arrangement, virtual cards, payouts, Novak amounts.
  - `_research/brief-booking-reservations.md` Parts 1, 2, 4, 6, 7, 9; `brief-supply-connectivity.md` Part 3; `brief-trust-safety-regulation.md` 8.1, 9.6; `brief-platform-data-ml.md` (SpinalTap); `productscape-digest.md` (`invt`, `rsrv`, `book`, `trip`).
- **External**
  - Booking.com Connectivity, Reservations API overview, acknowledgement and retrieval pages, B.XML Reporting API (n.d.) — delivery, fallback, no-show and invalid-card windows.
  - Expedia Group Developer Hub, Hard Change and Manage Booking API (n.d.) — itinerary identity through modifications; property-made changes.
  - Airbnb, Booking Holdings and Expedia Group Form 10-K filings for 2025 (2026) — money follows the stay.
  - Council Directive (EU) 2021/514; Regulation (EU) 2024/1028; Regulation (EU) 2016/679 — retention and reporting.
  - Airbnb Engineering, SpinalTap (2018) — change data capture.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 10,191 to 8,499 words; event table aligned with event-driven-stays (one reservation.versioned event with change types, separate delivery events); DAC7 and GDPR expanded; duplicate evidence table folded into prose. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
