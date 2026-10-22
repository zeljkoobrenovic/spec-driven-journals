---
status: accepted
revised: 2026-10-21
---

# Spec: When Plans Change: Modifications, Cancellations and Policies

## Intent

Show chief architects how to build change and cancellation flows that are fair, consistent and cheap to operate across an OTA and a hosted-stays marketplace. The chapter argues three things: a cancellation policy is **versioned data frozen on the reservation** (with a guest-facing and a supplier-facing snapshot where they differ) and **one deterministic cancellation policy engine** evaluates it for every channel; a modification is a **new reservation version** driven through re-pricing, payments and supplier acknowledgement as a saga; and mass disruptions are **declared events** (class, place, window, booking cutoff, party filter, funding) applied as a batch with self-service, under the funding rule "waive what you hold, request what you do not". The reader leaves able to review a change and cancellation design, and to say what the group should decide before the next disruption.

Productscape domains covered: TAM `self` (Self-Service Changes & Recovery: Eligibility and Policy Engine, Recovery Flow Orchestration, Change Decision API); HSM `reso` (partially: refunds, host cancellations and disruption overrides; claims and case handling belong elsewhere).

Owns: **cancellation policy engine**, **extenuating circumstances** (declared disruption events), **self-service change**.

## Audience

Chief and enterprise architects of travel groups, booking and post-booking platform leads, payments and customer-service engineering leads, and product directors who own cancellation policy. They know sagas and versioned data; they need the stays-specific shape: three parties, money held in different places by payment model, supplier-defined versus platform-defined policies, and the consumer law that bounds them.

## Success criteria

- [x] Reader can define a cancellation policy as typed time windows, explain policy snapshots and why a reservation may need guest-facing and supplier-facing policies, with the dated Booking Holdings 10-K evidence.
- [x] Reader can sketch the policy engine as a pure function (inputs, decision record, rules: every channel asks, local time, replayable) and the components around it with contracts.
- [x] Reader can classify modifications (re-price, re-check, supplier acceptance, policy carry-over) and explain why a change is a new version rather than cancel-and-rebook, with Expedia Rapid and Airbnb documentation.
- [x] Reader can describe host and property cancellations, relocation as a linked reservation, and supplier-reported no-shows.
- [x] Reader can design a declared-event registry and batch path, and apply the funding table across agency, merchant and facilitated payments.
- [x] Reader can state the relevant EU law: no withdrawal right for accommodation (CRD Art. 16(l)), PTD Art. 12 termination rights and 14-day refunds, the 2020 voucher recommendation, and the 2026 amendment's status.
- [x] The Corvane ATC strike weekend (5–7 June 2027) and the redesign (Clause, Disruption Policy v1) have consistent numbers matching the ledger, with two worked examples (Carmen Ruiz's Seville listing; a Hotel Miradouro merchant booking).
- [x] The "Hotels and Homes" section has a specific table and a judgement on what to share (engine, registry, orchestrator, override types) and what to keep per brand (policy content, supplier messages, host penalties).

## Non-goals

- The reservation state machine, delivery to properties and no-show transitions (`reservation-lifecycle`).
- The booking saga, idempotency and instant book versus request to book (`checkout-orchestration`).
- Refund execution, chargebacks, credits accounting and reconciliation (`refunds-and-reconciliation`).
- Case management, relocation decisions and support surge operations, including the King's Day relocations (`customer-service`).
- Payment plans, deferred charges and virtual card mechanics (`stay-payments`); payment-model choice (`merchant-and-agency-models`).
- Price composition and policy display on the property page (`property-page-and-room-selection`).
- Short-term-rental enforcement that forces cancellations (`stays-regulation`); guest guarantee and damage claims (`protection-and-incidents`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The text of Directive (EU) 2026/1024 amending the PTD was not reviewed; the chapter cites only the Commission's summary and press coverage. Verify voucher and refund changes against the Official Journal.
- The SiteMinder "full overlay" description of modify notifications comes from a search excerpt; the OpenTravel specification itself was not fetched.
- The date Airbnb renamed its extenuating circumstances policy to Major Disruptive Events is not stated on the help page.
- Whether a marketplace should extend disruption remedies to transport events at all is a commercial choice; the chapter presents Corvane's choice, not a norm.

## Decision log

- **2026-10-21** — Used the ledger's ATC strike weekend (5–7 June 2027) as the disruption instead of the "volcanic-ash weekend" named in PLAN, because the ledger is canonical and the strike already appears in `dynamic-pricing`. A transport event also sharpens the point that documented disruption policies (Airbnb's) exclude transport, so the marketplace must decide in advance.
- **2026-10-21** — Built the chapter around one engine, one change path and one event registry rather than around policy tiers, because the costly failures are inconsistency and misdirected funding, not refund arithmetic.
- **2026-10-21** — Made the funding rule ("waive what you hold, request what you do not") the hinge between payment models and policy, and showed the cost of breaking it on agency and merchant bookings.
- **2026-10-21** — Defined Nookaway's cancellation tiers and host-fee schedule as fictional values distinct from Airbnb's documented ones, and recorded them in the ledger.

## Sources

- **Internal**
  - [[rates-and-availability-model]] — cancellation policy as typed windows; snapshot at booking.
  - [[merchant-and-agency-models]] — payment arrangement and who holds the money.
  - [[stay-payments]] — payment plans, Pay Later charge dates, virtual card activation.
  - [[reservation-lifecycle]], [[checkout-orchestration]] — versions, delivery, sagas.
  - [[customer-service]], [[refunds-and-reconciliation]], [[dynamic-pricing]], [[calendar-sync]] — neighbors for cases, money, pricing effects and the Seville host fee.
- **External**
  - Airbnb Help Center articles 475, 1320, 990, 913 (live, fetched October 2026); Airbnb FY2020 and FY2025 10-Ks.
  - Booking Holdings FY2020 and FY2025 10-Ks; Booking.com terms (2025) and Connectivity documentation.
  - Expedia Rapid Hard Change and cancellation-policy documentation; Expedia FY2020 10-K.
  - Directives 2011/83/EU, 2005/29/EC, (EU) 2015/2302; Commission Recommendation (EU) 2020/648; European Commission PTD page.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,902 to 8,488 words; ATC strike figures checked against the ledger and customer-service; duplicate no-show and SiteMinder material moved to reservation-lifecycle links; unused sources removed; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
