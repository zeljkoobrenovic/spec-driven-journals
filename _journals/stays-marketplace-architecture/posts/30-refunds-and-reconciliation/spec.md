---
status: accepted
revised: 2026-10-22
---

# Spec: Closing the Books: Refunds, Chargebacks and Reconciliation

## Intent

Closing chapter of Part VI (MONEY). It must establish that a stays marketplace proves where every euro is by reconciling three kinds of record, transaction by transaction and daily: the **business record** (reservation, payment arrangement version, payment plan), the **ledger**, and the **external evidence** (PSP reports, bank statements, issuer files, payout rails, partner payments). It must also establish that every refund has a payee and a funder recorded together, that chargebacks are ledger lifecycles with causes and recoveries, that FX results arise on refunds, cards and disputes as well as payouts, and that corrections go through a typed, approved finance adjustment workflow. The reader leaves able to specify what "reconciled" means for each money flow and to design the refund, dispute, adjustment and close processes around one ledger.

Productscape domains covered: TAM `sett` (Finance Adjustment Workflow; settlement records), TAM `paym` (Partner Remittance and Reconciliation; refunds and disputes); HSM `paym` (refunds, payout ledger) and `reso` (refunds and disputes as case outcomes, context only).

## Audience

Chief architects, payments and finance-engineering leads, and finance-operations leaders of OTAs and hosted-stays marketplaces who own or depend on reconciliation, refunds and the month-end close; also CFO-adjacent readers who need the systems view of losses and controls.

## Success criteria

- [ ] Defines refund, refund funding, recovery, chargeback, FX result, reconciliation, three-way reconciliation (stays), finance adjustment, suspense, unclaimed funds and close.
- [ ] Gives a refund funding matrix and shows refund orchestration with funding recorded in the same transaction, using canonical Corvane cases (Seville, King's Day) with ledger-consistent numbers.
- [ ] Explains chargeback timing for future services, ledger treatment, allowances and liability by payment model, with dated sources (Stripe docs, Booking Holdings, Expedia and Airbnb 10-Ks).
- [ ] Presents a reconciliation architecture (ingestion, matcher, exception queues, adjustment workflow, close) and a table of reconciliations with their three legs and typical breaks; covers safeguarding with official EU sources.
- [ ] Works the canonical €1.8M virtual-card gap: breakdown, root cause (no business leg), recovery, fixes and results.
- [ ] Includes at least three diagrams (illustrated), a trade-off table, the "Hotels and Homes" table with a judgement, failure modes, the Chief Architect's view and 6–10 questions.
- [ ] Labels the reference architecture as inference where it touches real companies; Airbnb engineering evidence is dated and flagged as old.

## Non-goals

- Cancellation policy models and the policy engine ([[changes-and-cancellations]]).
- Dispute evidence assembly, SCA, payment plans and virtual-card activation design ([[stay-payments]]).
- Payout rails, settlement ledger accounts, commission invoicing and partner statements ([[payouts-and-settlement]]).
- Tax determination and remittance ([[taxes-on-stays]]); fraud screening ([[travel-fraud]]); protection claims handling ([[protection-and-incidents]]).
- General double-entry ledger design (finance book: [[designing-financial-ledgers]], [[payments-to-ledger]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Card-scheme dispute windows are cited from Stripe's documentation, not from Visa or Mastercard rules; a later pass could cite scheme rules directly.
- National rules on unclaimed funds in the EU are not surveyed; the chapter states only the EMD2 redemption right and US escheatment risk.
- The Expedia reserve quote comes from the valuation-accounts schedule; Expedia's separate "reserve for chargebacks and cancellations" sentence sits in its air revenue policy and is deliberately not used for lodging.

## Decision log

- **2026-10-21** — Defined "three-way reconciliation (stays)" as business record ↔ ledger ↔ external evidence, rather than Airbnb's platform ↔ processor ↔ bank, because the canonical €1.8M gap passes the classic check and fails only against the reservation.
- **2026-10-21** — Gave the €1.8M gap a four-row breakdown (canceled-but-charged, modified-but-charged, stale reservation numbers, un-revalued FX) consistent with stay-payments' description, and recorded the recovery outcome and Plumbline in the ledger.
- **2026-10-21** — Framed refunds around "payee vs funder" with a funding matrix, reusing canonical Seville and King's Day numbers instead of inventing new refund incidents.
- **2026-10-21** — Kept the ATC strike weekend to the canonical 6,200 requests as a failure-mode illustration, leaving its detailed story to other chapters.

## Sources

- **Internal**
  - [[meet-corvane]], scenario ledger — €1.8M gap, Seville, King's Day, Dubrovnik, phishing wave, 212 duplicates, ATC strike.
  - [[merchant-and-agency-models]], [[stay-payments]], [[payouts-and-settlement]], [[taxes-on-stays]] — arrangement record, payment plans and VCC lifecycle, Fathom accounts and debit balances, tax liabilities.
  - [[changes-and-cancellations]], [[customer-service]], [[travel-fraud]], [[protection-and-incidents]] — neighbours that own policy, recovery decisions, fraud and claims.
- **External**
  - Booking Holdings, Expedia Group and Airbnb 10-Ks for FY2025 (2026) — allowances, reserves, chargeback expense, refund classification, FX remeasurement, escheatment.
  - Airbnb Engineering (2016, 2018, 2026) — double-entry pipeline, three-way reconciliation, settlement and reconciliation subdomain.
  - Airbnb Terms and Payments Terms (2026); Booking.com Terms (2025) — refund rules and recoveries.
  - Stripe dispute documentation and Adyen settlement-reconciliation documentation (n.d., read 2026).
  - Directive 2009/110/EC (EMD2) and Directive (EU) 2015/2366 (PSD2) — safeguarding and redemption.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,434 to 8,491 words (repeated definitions, quotations and failure modes condensed); FX gap period corrected to three years; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,185 → 5,877 prose words (−5%); no headings renamed; Failure Modes cut from six bullets to three (restated mitigations folded into one line); announce/recap sentences and a repeated "refund is two events" paragraph removed; two figure captions shortened. *(AI-mediated session)*
