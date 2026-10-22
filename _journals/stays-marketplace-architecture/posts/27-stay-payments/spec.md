---
status: accepted
revised: 2026-10-22
---

# Spec: Paying for a Future Night: Payment Orchestration for Stays

## Intent

Show chief architects how a stays marketplace takes payment for a night consumed weeks or months later. The chapter argues that a stays payment is a **versioned payment plan of future obligations**, not a checkout transaction, and that one orchestration layer should own stored credentials, deferred charges, virtual cards, deposits and holds, currency handling and disputes, publishing every state change on a payment state feed that the reservation, the ledger and payouts consume. It makes Strong Customer Authentication concrete for stays (why most exemptions do not fit, why the stored-credential setup at checkout decides whether later charges work) and explains virtual cards as an issuing system attached to the reservation lifecycle. The reader leaves able to review a payment design for pay later, merchant bookings and multi-currency guests.

Productscape domains covered: TAM `paym` (Traveler Payment Orchestration, Payment State Feed; Payment Model Normalization only as it touches timing — the model choice belongs to `merchant-and-agency-models`), TAM `acct` (saved payment context, briefly); HSM `paym` (Payment orchestration).

Owns: **deferred charge**, **virtual card** (VCC), **payment orchestration (stays)**.

## Audience

Chief and enterprise architects of travel groups, payments and checkout leads, principal engineers on booking and finance platforms, and engineering directors deciding whether to offer pay-later options or move to merchant payments. They know card payments in general; they need the stays-specific shape: time, policy coupling, two supply sides.

## Success criteria

- [ ] Reader can explain payment timing options (pay now, pay later, pay in parts, pay at property, third-party installments) and what the marketplace holds under each, with dated public examples.
- [ ] Reader can explain CIT versus MIT, the role of the scheme transaction reference, and why SCA RTS exemptions (Art. 14, 16, 17, 18 with the Annex thresholds) rarely cover a stays basket.
- [ ] Reader can sketch the payment plan model, the orchestration components with their contracts, the deferred-charge state machine and the payment state feed events.
- [ ] Reader can describe virtual card activation, resizing and voiding, and why activation policy is a risk setting (linked to the €1.8 million gap).
- [ ] Reader can compare deposit designs (pre-authorization, collected deposit, post-stay MIT) and name where each conversion happens across three currencies.
- [ ] The Corvane worked example (Semana Santa Pay Later declines, March 2027) has consistent numbers, and the redesign (Payment Plans v1) shows the architectural fix.
- [ ] The "Hotels and Homes" section has a specific table and a judgement on what to share (guest side and plumbing) versus keep separate (supply-side rails).
- [ ] Every company claim carries a dated source; inferences are labeled.

## Non-goals

- Choosing merchant versus agency and licensing (`merchant-and-agency-models`).
- Payouts, commissions, settlement ledger and partner statements (`payouts-and-settlement`).
- Refund flows, chargeback accounting, three-way reconciliation and the €1.8 million gap investigation (`refunds-and-reconciliation`).
- Tax calculation and tax in the price (`taxes-on-stays`).
- The booking saga, inventory holds and checkout idempotency including the 212 duplicates (`checkout-orchestration`).
- Cancellation policy models and the policy engine (`changes-and-cancellations`).
- Payment fraud screening (`travel-fraud`); protection program and claims (`protection-and-incidents`).
- General card-payment mechanics, interchange, provider internals (RECONCILED: `payments-fundamentals`, `adyen`, `stripe`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Card-scheme MIT rules and EBA Q&A were not fetched; the chapter relies on Stripe's SCA guide for the MIT construct. A reviewer may want a scheme or EBA primary source.
- Expedia's virtual card charging window comes from integrator documentation only.
- The dispute-window statement for future services is phrased as common practice; scheme rules were not cited.
- PSD3/PSR treatment of pay-later and marketplace collection is not covered; revisit when final texts are adopted.

## Decision log

- **2026-10-21** — Built the chapter around a *payment plan* (versioned obligations) rather than around PSP flows, because time and policy coupling are what distinguish stays from retail; rejected a provider-by-provider structure that RECONCILED already covers.
- **2026-10-21** — Chose a Nookaway Pay Later failure caused by a missing stored-credential setup (not a PSP outage) as the scene, so the lesson is architectural (a chargeability gate and decline classification) rather than "add a second acquirer".
- **2026-10-21** — Used Semana Santa 2027 (21–28 March) for timing; kept Nookaway's pay-later rules (10-day lead, deadline lapse) distinct from Airbnb's documented 72-hour rule to avoid mirroring a real product.
- **2026-10-21** — Placed the virtual-card activation lesson here and the €1.8 million reconciliation itself in `refunds-and-reconciliation`.

## Sources

- **Internal**
  - [[merchant-and-agency-models]] — who is merchant of record; this chapter takes it as input.
  - [[checkout-orchestration]], [[changes-and-cancellations]] — amounts and policy deadlines the plan carries.
  - [[payouts-and-settlement]], [[refunds-and-reconciliation]], [[taxes-on-stays]] — downstream money chapters.
  - [[payments-fundamentals]], [[payments-to-ledger]], [[designing-financial-ledgers]], [[adyen]], [[stripe]] — RECONCILED depth.
  - `_research/brief-payments-finance-tax.md`, `brief-airbnb.md`, `brief-booking-com.md`, `brief-expedia-agoda-tripcom.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Directive (EU) 2015/2366 (PSD2) Art. 75 and 97; Delegated Regulation (EU) 2018/389 Art. 14, 16, 17, 18 and Annex (fetched 2026-10-21); Regulation (EU) 2019/518.
  - Airbnb: FY2025 10-K; Reserve Now, Pay Later posts (17 and 23 February 2026, fetched 2026-10-21); Payments Terms (2026); engineering posts 2016, 2018, 2019, 2022, 2026.
  - Booking Holdings FY2025 10-K; Payments by Booking.com partner page; Booking.com connectivity and Demand API payment docs; Booking.com Terms (2025).
  - Expedia Group FY2025 10-K; Rapid property-collect and vacation-rentals docs; Agoda MPBE post (2025).
  - Stripe SCA guide and Connect charges docs; Adyen marketplaces docs.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Hotel Miradouro VCC example aligned to its 15% commission (€382.50, €510 after an added night) instead of a generic 82% net; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,662 → 7,278 prose words; opening merged into one lead paragraph plus a place-in-book paragraph naming inputs (checkout, cancellation) and consumers (payouts, refunds); Payment orchestration definition moved from Concepts into Architecture; Failure Modes cut to the three failures not shown earlier; repeated feed and activation statements removed. *(AI-mediated session)*
