---
status: accepted
revised: 2026-10-21
---

# Spec: Turning an Offer Into a Booking: Checkout Orchestration

## Intent

Show chief architects how a stays marketplace turns a quote into exactly one confirmed booking across inventory, payment and supplier, when every step can time out. The chapter argues that checkout is a **booking saga** with a deliberately placed **pivot**, compensations before it and retries after it; that one guest intention needs one **server-minted checkout attempt** used as the idempotency key at every hop; and that **unknown outcomes** are a state resolved by lookup, never by compensation or a retry with a new key. It also places the remaining checkout concerns: instant book versus request to book, eligibility, the frozen terms snapshot, guest details and identity, the placement of fraud and risk checks, and performance. The reader leaves able to review a booking path for duplicates, phantom bookings and paid-but-unconfirmed states.

Productscape domains covered: TAM `book` (Checkout UI, Reservation API, Checkout State and Eligibility, Policy and Disclosure Layer, Reservation Orchestration); HSM `book` (Reservation orchestration, Checkout experience, trust screening before confirmation).

Owns: **booking saga**, **idempotency key (stays)**, **instant book**, **request to book**.

## Audience

Chief and enterprise architects of travel groups, checkout and booking leads, payments engineers and principal engineers who own the path from "Book" to confirmation. They know sagas and idempotency in general; they need the stays-specific shape: multiple payment models, supplier-owned inventory, host decisions and long waits.

## Success criteria

- [ ] Reader can draw the booking saga's components with contracts and place the pivot for agency, merchant, facilitated, pay-later, request-to-book and pull-model flows.
- [ ] Reader can explain why the key must name the guest's intention (a server-minted checkout attempt) and list the derived key at each hop, with dated public examples (Stripe, IETF draft, Expedia Rapid, Airbnb Orpheus).
- [ ] Reader can design the unknown-outcome state: no compensation, no new-key retry, lookup with a deadline, honest guest messaging, timeout budget from the outside in.
- [ ] Reader can compare instant book and request to book with documented Airbnb, Booking.com and Vrbo designs.
- [ ] Reader can place eligibility, terms snapshot and risk checks, and explain why terms are frozen by version.
- [ ] The Corvane 212-duplicate incident (14 January 2027) is told with ledger-consistent numbers and the February 2027 checkout attempt contract fixes it; the Novak booking is walked through with ledger numbers.
- [ ] The "Hotels and Homes" section has a specific table and a judgement: share the contract, idempotency, terms snapshot, unknown handling and metrics; keep the sagas separate.
- [ ] Every company claim carries a dated source; inferences are labeled.

## Non-goals

- Inventory commit mechanics, holds in depth, oversell and relocation (`inventory-integrity`).
- Price-check mechanics and offer computation (`availability-engine`); total-price display (`property-page-and-room-selection`).
- Reservation state machine after confirmation, delivery and acknowledgement (`reservation-lifecycle`).
- Payment plans, SCA, stored credentials, virtual cards (`stay-payments`); merchant versus agency (`merchant-and-agency-models`).
- Cancellation policy engine and package-travel consequences (`changes-and-cancellations`).
- Fraud models and screening models (`travel-fraud`, `stays-trust-and-safety`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No stays company documents its internal booking saga or pivot placement; the chapter's saga is labeled as reference architecture. A reviewer may want more public evidence (for example Agoda or Trip.com engineering posts) if any appears.
- The Orpheus mechanism comes from a 2024 secondhand summary; the original 2019 post body was not readable.
- The IETF Idempotency-Key draft (-07, October 2025) has expired as a draft; check whether a later revision or RFC exists before publication.
- The latency targets and unknown-resolution deadlines are illustrative Corvane settings, not industry benchmarks.

## Decision log

- **2026-10-21** — Built the chapter around the 212-duplicate incident as an idempotency-*naming* failure (client keys per HTTP request) rather than a PSP outage, so the lesson is the server-minted checkout attempt and the unknown state, not "add a second acquirer".
- **2026-10-21** — Chose "authorize, commit, capture" as the reference order and made pivot placement a per-flow table, rejecting a single universal saga, because agency, merchant, facilitated, request-to-book and pull-model flows have genuinely different points of no return.
- **2026-10-21** — Recommended orchestration before the pivot and choreography after it; rejected a fully event-choreographed booking path because the unknown state needs one owner.
- **2026-10-21** — Kept Corvane's checkout API (Turnstile) as a layer in front of Keystone's checkout module, consistent with earlier chapters that place Roomstead's checkout pricing logic in Keystone.

## Sources

- **Internal**
  - [[property-page-and-room-selection]] — the quote contract handed to checkout.
  - [[availability-engine]] — price check and the 15-minute binding quote.
  - [[inventory-integrity]] — allocation ledger, hold durations, commit point.
  - [[merchant-and-agency-models]] — payment arrangement on the offer.
  - [[stay-payments]] — payment plans, SCA, Payment Plans v1.
  - [[reservation-lifecycle]] — hand-off after confirmation.
- **External**
  - Stripe idempotent requests (live docs) and Stripe blog (2017) — key semantics.
  - IETF draft-ietf-httpapi-idempotency-key-header-07 (2025) — standard header behavior.
  - Microsoft Azure Architecture Center, Saga pattern (2025); Garcia-Molina and Salem (1987) — saga and pivot.
  - Expedia Group Rapid docs (hold and resume, error responses) — holds, partner reference, 90-second timeout, 30-minute retrieval.
  - Booking.com Request to Book, Airbnb Help Center, Vrbo Help — booking modes.
  - Airbnb Engineering: Orpheus (2019), payment orchestration (2022), Skipper (2026); Airbnb Newsroom anti-party (2022).
  - SCA RTS 2018/389; EC UCPD guidance (2021); Package Travel Directive 2015/2302.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,679 to 8,492 words (repeated redesign list, performance and source detail condensed); pending-reservation compensation aligned with reservation-lifecycle's declined-or-expired state; PSD2 expanded; Lisbon under-13 exemption hedged; Package Travel amendment date verified. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
