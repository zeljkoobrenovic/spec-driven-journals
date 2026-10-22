---
status: accepted
revised: 2026-10-22
---

# Spec: Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel

## Intent

Show chief architects how a stays marketplace detects and stops fraud on both sides of the booking. The chapter argues three things. First, stays fraud decisions should be **timed to the points of no return** (guest payment, virtual card activation, check-in, payout release, message delivery) rather than concentrated at checkout, because a stay is consumed weeks after it is sold. Second, the **partner account is the perimeter**: the best-documented travel fraud of 2023–2025 hijacked hotel extranets and used the platform's own messaging to phish guests, so phishing-resistant sign-in, session risk, action step-up and a messaging guard are fraud controls. Third, a group should run **one shared risk spine** (signals, entity graph, features, risk service, case management, outcome store) with **per-marketplace decision policies**, because attackers cross brands while losses and liability differ by business model. The reader leaves able to review a fraud design for an OTA, a hosted-stays marketplace or a group that runs both.

Productscape domains covered: TAM `trst` (Fraud and Abuse Controls; Risk Signal Feed as input; Integrity Operations only as fraud case handling), HSM `trst` (risk scoring). Identity and verification (TAM `trst` identity service, HSM `idvr`) belong to `identity-accounts-and-access`; protection and incident workflow (HSM `trst`) to `protection-and-incidents`.

Owns: **extranet takeover**, **booking risk score**.

## Audience

Chief and enterprise architects of travel groups, trust-and-safety and payments engineering leads, principal engineers on checkout, messaging and partner tools, and engineering directors who must fund fraud work across two marketplaces. They know card payments and generic risk scoring; they need the stays-specific shape: delayed fulfillment, business-model-dependent liability, partner accounts and messaging as attack surface.

## Success criteria

- [ ] Reader can list the stays fraud typology and say, for each type, who loses first under agency, merchant and hosted-stays models.
- [ ] Reader can explain points of no return and apply the rule "decide at the point of no return, not at the point of sale", including where it fails (non-refundable, same-day, instant payout, messaging).
- [ ] Reader can sketch the risk spine components and the booking risk score's inputs, calibrated output and decision contract.
- [ ] Reader can describe the documented 2023–2025 extranet takeover chain with dated sources and the four control layers (sign-in, session, action step-up, messaging guard).
- [ ] Reader can explain why stays fraud labels are slow and biased, and what a holdout and an insult-rate metric fix.
- [ ] The Corvane extranet phishing wave (November 2027: 230 properties, 4,100 guests, 310 paid, €212,000) is told with consistent numbers, and the redesign (booking risk scores as Warden detectors, Partner Shield) shows the architectural fix.
- [ ] The "Hotels and Homes" section has a specific table and a judgement: share the spine, graph and messaging guard; keep policies per marketplace.
- [ ] Every company claim carries a dated source; inferences are labeled.

## Non-goals

- The trust platform, trust decision API, enforcement and integrity operations in general (`stays-trust-and-safety`).
- Identity verification levels, partner role and delegation model, authentication product design (`identity-accounts-and-access`, `extranets-and-host-tools`).
- Reservation screening for parties, damage claims and incident response (`protection-and-incidents`).
- Payment mechanics, SCA exemptions and chargeback accounting (`stay-payments`, `refunds-and-reconciliation`).
- Message threads and delivery (`trip-and-messaging`); review fraud (`reviews-and-reputation`).
- Generic risk-scoring service design for marketplaces (LISTED `fraud-prevention`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source describes any OTA's or hosted-stays platform's booking risk decision (model, latency, actions); the risk spine is labeled reference architecture.
- Booking.com's 2023 figures (85 million fraudulent reservations blocked, 1.5 million phishing attempts) are a company statement relayed by the press.
- Airbnb's 2018 "targeted friction" engineering post could not be retrieved and is not cited.
- Expedia's Fraud Prevention as a Service (2024) is cited as an announcement only; its contents are undocumented here.
- Card-scheme dispute windows for future services are stated as common practice, not cited from scheme rules.

## Decision log

- **2026-10-21** — Built the chapter around *points of no return* rather than around a fraud-type catalogue, because delayed fulfillment is what makes stays fraud architecture different from retail; the typology is kept as one table organized by who loses first.
- **2026-10-21** — Made the extranet takeover chain the central documented case and the Corvane scene, because it is the best-evidenced travel fraud and it crosses identity, messaging and customer service; rejected a stolen-card scene that would have duplicated `stay-payments`.
- **2026-10-21** — Kept generic risk-service design short and linked to LISTED `fraud-prevention`; spent the depth on stays-specific signals, the decision contract and timing.
- **2026-10-21** — Placed Corvane's booking risk scores as per-brand detectors on **Warden** (the group trust platform owned by `stays-trust-and-safety`) rather than inventing a second risk service, and named the extranet program *Partner Shield*, built on Corvane ID and Threadline; recorded in the scenario ledger.

## Sources

- **Internal**
  - [[stays-trust-and-safety]] — trust platform and decision API this chapter's spine plugs into.
  - [[extranets-and-host-tools]], [[partner-onboarding]], [[identity-accounts-and-access]] — role model, verification, authentication.
  - [[stay-payments]], [[merchant-and-agency-models]], [[payouts-and-settlement]], [[refunds-and-reconciliation]] — liability, card activation, payout timing.
  - [[promotions-and-loyalty]] — Autumn Cities coupon and Circle credit figures.
  - [[fraud-prevention]], [[messaging-and-leads]] — LISTED depth.
  - `_research/brief-trust-safety-regulation.md` (Parts 2–4, 10), `brief-payments-finance-tax.md` (Part 5), `brief-airbnb.md` (8.3–8.5), `brief-booking-com.md`, `brief-platform-data-ml.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Secureworks/Sophos (2023), KrebsOnSecurity (2024), ESET (2024), Microsoft Threat Intelligence (2025) — the extranet takeover chain.
  - NIST SP 800-63B-4 (2025) — phishing-resistant authentication.
  - Airbnb Form 10-K and identity-graph post (2026), Booking Holdings Form 10-K (2026), AWS blog on Booking.com's feature platform (2026), Booking.com Messaging API documentation — public record.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: timetoread 35→37; phishing-wave, Partner Shield, Autumn Cities and Circle-credit figures checked against the ledger; no text changes needed. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,207 → 5,916 prose words (−4.7%; fact-dense chapter); opening now ties the chapter to Part VII's trust-platform argument and names the identity chapter that follows; third/first-party fraud definitions cut (audience knows them); Hotels and Homes judgement merged into one paragraph; Failure Modes cut to one-liners pointing at the sections that argue them; one subheading renamed (Fraud, abuse and chargebacks). *(AI-mediated session)*
