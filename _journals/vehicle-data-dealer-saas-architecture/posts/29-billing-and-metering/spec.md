---
status: accepted
revised: 2026-10-22
---

# Spec: Subscriptions, Lookups and No-Hit-No-Fee: Billing and Metering

## Intent

Show how a group that sells both module subscriptions per rooftop and vehicle data per call, report and register transaction should meter, rate, invoice and collect, so that every invoice line is correct and explainable. The chapter's argument: the service that knows the outcome records an immutable, idempotent usage event at the business moment; one rating engine prices it against a versioned price book, contracts and entitlements; billing runs as a ledger whose lines trace back to events; and the same events carry upstream cost, so cost to serve and pass-through come from one source. After reading, the reader can design a usage event schema, place outcome classification and pricing correctly, and plan a shadow-rated migration from legacy billing paths.

The chapter owns **usage event**, **rating engine** and **price book**.

Productscape bricks covered: `bill` (Subscription and Transaction Billing), with the billing edges from `vhis`, `rdwt`, `vapi`, `fenr` and the `subscription-and-usage-ledger` data asset.

## Audience

Chief architects, principal engineers and billing or finance-systems leads at vehicle-data companies and dealer-software vendors, especially groups assembled by acquisition that bill from several systems. They know event-driven systems and idempotency; they need the vehicle-specific rules (no-hit-no-fee, re-opens, register confirmations, pass-through fees, rooftop allowances) and the decisions that keep billing explainable.

## Success criteria

- [x] The reader can explain why outcome classification belongs in product services and pricing in one rating engine, using the No-Hit Credit (€186,000 to 41 API clients) as evidence.
- [x] The chapter defines the usage event with a full schema (derived event id, business key, outcome, fact version, upstream costs, license reference) and the business moment.
- [x] No-hit-no-fee is made precise: hit definition per product, one call per client request reference, a 30-day re-open rule distinct from deduplication.
- [x] The rating order (price selection, outcome, re-open, allowances, tiers, minimums, credits), proration, pooled group allowances and credits with reason codes are covered.
- [x] The invoice lifecycle, SEPA Core vs B2B and Bacs collection (with PSD2 refund periods cited to CELEX), billing as a ledger and IFRS 15 basics are covered.
- [x] An Axleby worked example (Brandsma's October 2027 bill, shadow-rated) has arithmetic that adds up and matches ledger prices.
- [x] Failure handling covers duplicates, missing and incomplete events, misclassification, conflicting contract changes, late events, register confirmations, partial invoice runs, collection failures and data corrections.
- [x] Trade-off table, requirements table, three mermaid diagrams and an Across Markets table (NL/BE, DE, UK, US) with e-invoicing, collection and tax differences.

## Non-goals

- Tenant hierarchy and rooftop modeling ([[tenancy-and-dealer-groups]]).
- Entitlement and authorization design ([[identity-access-and-entitlements]]).
- License and purpose checks; the chapter only carries a `licence_ref` ([[data-licensing-and-governance]]).
- Cost per lookup and capacity economics in depth ([[scale-and-cost]]).
- API gateway design, rate limits and quotas ([[vehicle-data-apis]]).
- Ledger design and payment rails in depth (finance book: [[designing-financial-ledgers]], [[payments-fundamentals]]).
- Consumer payments in Odolo ([[consumer-vehicle-checks]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- German e-invoicing dates rest on IHK and KPMG summaries, not the BMF letter itself.
- The SEPA pre-notification period is cited from a payment-provider guide; the EPC rulebook was not readable (HTTP 403).
- Whether register fees passed through are agent (net) revenue is stated as typical judgement; confirm with auditors and the finance chapter.
- Whether the UK e-invoicing roadmap was published at Budget 2026 was not verified.

## Decision log

- **2026-10-22** — Opened with the No-Hit Credit decomposed into three divergences (empty history, partial specification, retries) so that the retry case shows the problem is where metering happens, not only how no-hit is defined. Rejected opening with a generic pricing-model survey.
- **2026-10-22** — Recommended building Meterline and rating in-house and buying commodity edges (tax, Peppol delivery, payment connectors), with explicit reversal conditions; rejected an unconditional "buy a usage-billing product" recommendation because register confirmations, pass-through and pooled allowances are core domain.
- **2026-10-22** — Used a shadow-rated October 2027 bill for Brandsma as the worked example, so the legacy-vs-Meterline difference (re-open rule living only in the UI) shows a concrete migration finding.
- **2026-10-22** — Kept revenue recognition to a data-export table; accounting depth belongs to the finance book.

## Sources

- **Internal**
  - [[meet-axleby]] — prices, systems, the No-Hit Credit, Meterline as a One Dossier Year 1 deliverable.
  - [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[data-licensing-and-governance]], [[scale-and-cost]], [[journey-data-correction]] — neighbors this chapter hands off to.
  - `_research/brief-saas-tenancy-billing.md` Part 7; `_research/brief-platform-apis-operations.md` 1.6, 2.3, Part 5; `_research/brief-dealer-workflows-economics.md` Part 10; `_research/brief-case-autotrader-carfax-vwe.md` 1.2, 2.3, 3.4.
- **External**
  - Stripe, Metronome and Orb metering documentation — idempotency windows, counter vs query-based billing, catch-up adjustments.
  - Directive (EU) 2015/2366 (PSD2), Articles 71, 76, 77 — direct-debit refund periods.
  - IFRS 15 — five-step model.
  - Autotrader Group FY2026 results; Mobility Global 10-Q (2026); CDK Global 10-K (2021); VWE price pages — public pricing structures.
  - Belgian FPS Finance, IHK Stuttgart/KPMG, HM Treasury Budget 2025, European Commission ViDA, *South Dakota v. Wayfair* — market differences in invoicing and tax.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Brandsma October 2027 bill corrected for Sales Admin taken since January 2027 (total €722.80), report usage shown on the Lotwise invoice per the editor line, lookup mix (70% internal, 780,000 external a day) added, Velto hub change no longer moves rooftops between legal entities, acronyms. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (neighbors). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
