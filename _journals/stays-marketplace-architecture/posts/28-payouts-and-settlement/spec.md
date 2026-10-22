---
status: accepted
revised: 2026-10-21
---

# Spec: Paying the Supply Side: Payouts, Commissions and Settlement

## Intent

Answer the chapter question from PLAN: how does money reach hotels and hosts correctly, on time and auditably? The chapter argues that one double-entry settlement ledger per partner is the only place that decides who is owed what. A payout engine pays only what that ledger shows as available, and commission invoices, deductions, holds and partner statements are postings on, or views of, the same ledger. It covers both settlement directions: payables to hosts and merchant-model hotels, and agency commission receivables from hotels. It also covers the release rules, holds and KYC and tax-identity gates that make payouts a risk control. The reader leaves able to draw the settlement architecture, name its contracts, and judge which parts two marketplace types can share.

Owns: **payout**, **settlement ledger**, **commission invoice**, **partner statement**.

Productscape domains covered: TAM `paym` (Partner Remittance and Reconciliation), TAM `sett` (Settlement Ledger Core, Finance Adjustment Workflow, in part); HSM `paym` (Host payout ledger); HSM `coho` (payout beneficiaries, in part).

## Audience

Chief architects, payments and finance-engineering leads, and principal engineers at OTAs and hosted-stays marketplaces who own, or are about to rebuild, payouts, remittance or commission invoicing. They know ledgers and payment providers in general; they need the stays-specific shape: release at check-in, deductions after cancellation, virtual cards, agency commission collection, co-host splits.

## Success criteria

- [ ] Reader can name the three money paths (hosted stays, OTA merchant, OTA agency) and what each demands from settlement, including that one partner can sit in two of them.
- [ ] Reader can draw the settlement architecture (earnings calculator, settlement ledger, release scheduler, beneficiary registry, payout engine, commission invoicing, statements) and state each component's "must not".
- [ ] Reader can explain the payable state machine (pending, available, held, in transit, paid, reversed) and why holds are balance states, not payout flags.
- [ ] The Corvane worked example reconciles to the ledger: Carmen's €244.40 payout after the €130 fee, the Novaks' €1,041.60 host payable split between owner and co-host, and Prinsenkade's April net position of €45,218.
- [ ] Every Airbnb, Booking.com, Expedia, Agoda, Stripe and Adyen claim carries a dated source; internals not documented are stated as not public.
- [ ] A trade-off table covers release timing, hotel rails, commission collection and ledger ownership.
- [ ] The "Hotels and Homes" table and judgement say what to share (ledger, beneficiary registry, rails) and what not (release policy, statements, collection).
- [ ] Reader will not leave thinking the payout system computes amounts.

## Non-goals

- Choosing between merchant and agency models, payment licensing and the commercial-agent exclusion: [[merchant-and-agency-models]].
- Guest pay-in, pay later, SCA, card-on-file and virtual-card issuing mechanics at checkout: [[stay-payments]].
- Refund funding, chargebacks, FX gains and losses, three-way reconciliation and month-end close: [[refunds-and-reconciliation]].
- Tax calculation, VAT on commission, tourist tax remittance, DAC7 report content and ViDA: [[taxes-on-stays]].
- Double-entry ledger internals (posting rules engine, reversals, summarization): RECONCILED's [[designing-financial-ledgers]] and [[payments-to-ledger]].
- Fraud detection and account-takeover defenses in depth: [[travel-fraud]]; protection-program claims: [[protection-and-incidents]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Booking.com's bank-transfer payout timing after check-out comes only from integrator guides; the chapter avoids it.
- Expedia virtual-card rules rest on integrator documentation; the chapter cites only Expedia's 10-K supplier terms.
- Whether Corvane Payments opts out of verification of the payee for bulk payouts is left as a design question, not a ledger fact.

## Decision log

- **2026-10-21** — Built the chapter around one settlement ledger with narrow engines around it, rather than separate "host payouts" and "hotel remittance" sections, because the Prinsenkade case (agency and merchant in one month) shows that two modules cannot produce one balance.
- **2026-10-21** — Reused three canonical examples (Seville €130 fee, Novak booking, King's Day €1,600 recovery) instead of inventing a new incident, so the money threads across Part VI stay consistent.
- **2026-10-21** — Included the Instant Payments Regulation (verification of the payee, instant sending from October 2025), verified against CELEX 32024R0886, because it changes payout fraud controls; the brief did not cover it.
- **2026-10-21** — Left chargebacks and reconciliation to chapter 30 and mentioned the €1.8 million gap only as a virtual-card lifecycle consequence.

## Sources

- **Internal**
  - [[merchant-and-agency-models]], [[stay-payments]], [[refunds-and-reconciliation]], [[taxes-on-stays]] — neighbouring Part VI chapters.
  - [[reservation-lifecycle]], [[partner-onboarding]], [[travel-fraud]], [[stays-trust-and-safety]], [[converging-two-marketplaces]] — dependencies.
  - `_research/brief-payments-finance-tax.md`, `brief-airbnb.md`, `brief-booking-com.md`, `brief-host-partner-guest-service.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Airbnb, Booking Holdings and Expedia Group 10-K filings for fiscal 2025 (2026) — balances held for customers, deferred merchant bookings, supplier terms.
  - Airbnb Payments Terms (2026) and help center — payout timing, holds, recovery, arrival by method.
  - Airbnb Engineering posts (2018, 2022, 2026) — batch payouts, idempotent orchestration, payout and ledger subdomains.
  - Booking.com payouts documentation and partner pages (fetched October 2026) — rails, gross and net payouts, virtual-card activation, mixed model.
  - Agoda Growth Program (2025) — commission deducted from payouts or invoiced on departed room nights.
  - Stripe Connect and Adyen for Platforms documentation — split and held payouts on rented payment infrastructure.
  - Directive (EU) 2021/514 (DAC7) and Regulation (EU) 2024/886 (instant payments, verification of the payee).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: consistency check of fees, payout timing and Prinsenkade/Carmen figures (all match the ledger); American spelling (aging, license, fulfill, program). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
