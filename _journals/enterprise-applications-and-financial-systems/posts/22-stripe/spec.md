---
status: accepted
revised: 2026-10-18
---

# Spec: Stripe: Programmable Payments, Billing and Connected Accounts

## Intent

Show a finance or enterprise architect how Stripe's object model shapes finance integration, and where Stripe's finance products should stop and the enterprise's ledger, reconciliation, tax and revenue policy begin. The reader should leave with one reconciliation unit (the balance transaction), a way to treat Connect charge types as accounting decisions, a product boundary register for Stripe, and a posting design they could adapt.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and payments engineering leads who already understand the payment lifecycle ([[payments-fundamentals]]) and need to connect Stripe to an ERP and a group close. Controllers and accounting-policy owners reviewing Connect or Stripe finance-product decisions are a secondary audience.

## Success criteria

- [x] Reader can explain why the BalanceTransaction (not the PaymentIntent, Charge or payout) is the reconciliation unit, using `fee_details`, `available_on`, `reporting_category` and `source`.
- [x] Reader knows the payout reconciliation report works only for automatic payouts, cannot itemize instant payouts, and can lag the cash.
- [x] Reader can compare direct, destination and separate charges and transfers (and `on_behalf_of`) on where funds land, who pays fees and who bears refunds and disputes, and can state the accounting consequence for a SaaS platform like Tablekin.
- [x] Reader knows Standard/Express/Custom are legacy and what Accounts v2 configurations and responsibilities are.
- [x] Reader can draw the boundary between Stripe Billing, Tax, Revenue Recognition, Sigma and Data Pipeline and the ERP, tax engine, reconciliation platform and data platform, with conditions for revisiting each.
- [x] Reader can state the webhook (signature, retries, no ordering) and idempotency rules and why API versions are a finance-governance concern (the Basil invoice change).
- [x] The Tablekin invoice ($249 + 3,120 × $0.25 = $1,029) is traced from meter to Workday journals and payout, with two clearing-account zero tests.
- [x] Stripe's internal Ledger is cited as an idea source and never implied to be a product.

## Non-goals

- The payment lifecycle, interchange++, chargeback mechanics and merchant of record in general ([[payments-fundamentals]]).
- Adyen's account structure and reports ([[adyen]]); only brief contrasts.
- Multi-PSP clearing design, the three-way match and the €14 million suspense program ([[payments-to-ledger]]).
- Transaction-matching configuration ([[blackline]]); Workday Accounting Center internals ([[workday]]).
- Billing platforms and tax engines as categories ([[satellite-platforms]]).
- Stripe Treasury, Issuing and Capital beyond a boundary row.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Re-verify before print: current Stripe API version (`2026-09-30.endive` as of October 2026), Accounts v2 gaps, Orchestration preview status, Metronome positioning, and payout reconciliation report suffixes.
- Should [[payments-to-ledger]] adopt Tablekin's two-clearing-account design (Stripe clearing plus cash in transit) as the group template for all PSPs?
- The Tablekin principal-versus-agent conclusion for payments revenue is fictional; [[accounting-for-architects]] may want to reference it as a worked judgment.

## Decision log

- **2026-10-18** — Built the chapter around one reconciliation unit (the balance transaction) rather than a product tour, because the contract makes it this chapter's owned concept; product sections are framed by where they stop.
- **2026-10-18** — Used a Tablekin destination-to-direct-charge migration as the Connect example, so the accounting consequence (gross versus net payments revenue, venue payable, dispute exposure) is concrete; rejected a generic three-column comparison alone.
- **2026-10-18** — Recommended against Stripe Revenue Recognition for Tablekin, and gave Stripe Tax a dated exception, with explicit reversal conditions, to show a boundary decision rather than a vendor verdict.
- **2026-10-18** — Fees and payout totals are labeled illustrative; no Stripe pricing is asserted.

## Sources

- **Internal**
  - [[payments-fundamentals]], [[adyen]], [[payments-to-ledger]] — lifecycle, neighbor contrast, program design.
  - [[workday]], [[blackline]], [[satellite-platforms]], [[redundancy-and-coupling]] — receiving systems and overlap register.
  - `_research/brief-payments.md` Part 3, `_research/brief-workday.md` §4, `_research/scenario-ledger.md`.
- **External**
  - Stripe documentation: balance transactions, reporting categories, payout reconciliation, payouts, Connect charges, fee-payer behavior, Accounts v2, usage-based billing, Tax, Revenue Recognition, Sigma, Data Pipeline, webhooks, idempotency, versioning, Basil changelog, Orchestration.
  - Ilya Ganelin, "Ledger: Stripe's system for tracking and validating money movement", Stripe engineering blog, 2024 — clearing-account-to-zero idea.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned the Wayfare rail ticket with the scenario ledger (agent, €6.72 net margin at ticket issue). *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: hedged the current Stripe API version (as of October 2026), expanded ASC 606 / IFRS 15 on first use; Wayfare ticket-issue recognition verified. *(AI-mediated session)*
