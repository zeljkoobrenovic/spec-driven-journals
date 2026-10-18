---
status: accepted
revised: 2026-10-18
---

# Spec: Payments-to-Ledger: Connecting Providers, Brand Platforms and the ERP

## Intent

Give the reader one end-to-end architecture that proves, for every payment accepted, where the money is now: provider adapters and canonical payment events, expected receivables in the subledger, staged clearing accounts per provider × legal entity × settlement currency in the general ledger, the three-way match (order ↔ provider line ↔ bank) with separate fee and FX legs, a written cut-off rule, reversal handling months later, an ownership split, and metrics. Then show, through Northmere's Keystone Year-1 program, that suspense drains when the causes of breaks are removed upstream, not when exception teams work faster. The chapter owns *payments-to-ledger*, *clearing account design* and the *three-way match*.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and payments-platform leads who own or review the path from PSPs to the ERP; controllers and heads of payments operations as secondary readers for the clearing design, aging rules and metrics. Readers are assumed to know the payment lifecycle ([[payments-fundamentals]]) and the provider data models ([[adyen]], [[stripe]]).

## Success criteria

- [ ] The €14 million suspense balance is decomposed item by item (February 2027, €14.2m) and the reader sees that in-flight money without expected dates was mistaken for suspense.
- [ ] A target architecture diagram shows PSP webhooks and reports → adapters → canonical events → subledger postings → clearing accounts → camt.053 via Kyriba → BlackLine matching → GL, with a responsibilities table that settles the "payments ledger" debate from [[finance-landscape]].
- [ ] Canonical events (`PaymentCaptured`, `PaymentSettled`, `PSPFeeCharged`, `RefundIssued`, `ChargebackReceived`, `ChargebackResolved`) are mapped for Adyen, Stripe and a typical local APM provider, with a mandatory key set and five adapter guarantees.
- [ ] Clearing-account design is justified (why entity, provider and currency; why not method), with illustrative stage accounts, the expected receivable concept, a lifecycle diagram and aging rules measured from the expected zero date.
- [ ] A worked local-APM example (Bali villa, IDR 4,850,000) runs all three legs plus fee and FX legs, with balanced postings, and contrasts the February 2027 failure.
- [ ] Month-end cut-off has one written rule, and in-flight money is shown as a dated reconciling item with a reconciliation that is not zero but fully explained.
- [ ] Refunds and chargebacks months later post to the current period linked to the original (the €420 chargeback), with four architectural requirements.
- [ ] Ownership RACI, six metrics with definitions, a root-cause tree that reconciles the BlackLine and Adyen chapters' analyses, a 2027 timeline diagram and measured Q4 2027 results consistent with [[ai-in-finance]] and [[blackline]].
- [ ] Trade-off table, failure modes (Suspense Gravity, Summarized Into Silence, matching on amount only), Chief Architect's view, questions, and a hand-off to [[finance-data-flows]].

## Non-goals

- The payment lifecycle, interchange++, APM semantics and dispute stages — [[payments-fundamentals]].
- Adyen's journal types, webhook consumer and batch 1047 arithmetic — [[adyen]]; Stripe's balance transaction and payout report — [[stripe]].
- Matching-rule mechanics and the 9→5 close plan — [[blackline]].
- Journal entries for the Lisbon booking and the €420 chargeback — [[accounting-for-architects]].
- The canonical event envelope and its governance — [[loosely-coupled-domains]]; the estate-wide reconciliation catalog — [[traceability-and-reconciliation]].
- Ledger-to-warehouse tie-out — [[finance-data-flows]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The €420 chargeback has two versions in neighboring chapters (debited 14 March in batch 1047 in [[adyen]]; received 13 June 2027 in [[accounting-for-architects]] and [[payments-fundamentals]]). This chapter uses the June/July version; the editor should reconcile [[adyen]].
- [[blackline]] uses batch 412 and booking reference `SL-LIS-0312` for the Lisbon payment, while the ledger and [[adyen]] use batch 1047, `NPY-270312-004418` and `SL-BK-9921347`. This chapter follows the ledger.
- Stage account numbers are illustrative; the representation of the provider (account vs dimension) depends on the group CoA v2 decision.
- The local APM provider data profiles are fictional composites, not descriptions of any real provider.

## Decision log

- **2026-10-18** — Made the *expected receivable with an expected zero date* the central concept, so that in-flight money becomes a dated reconciling item and "suspense" means only overdue or unidentified items.
- **2026-10-18** — Worked the three-way match on a local APM payment in IDR settled in USD instead of repeating the Adyen card batch already reconciled in [[adyen]] and [[blackline]].
- **2026-10-18** — Answered the [[finance-landscape]] "payments ledger" debate: Northmere Pay keeps a single-entry payment record store, SFP posts, S/4HANA holds clearing balances, BlackLine proves, FinDB analyses; FI-CA not used for merchant clearing because the merchant subledger moves in 2029.
- **2026-10-18** — Kept Q4 2027 results modest and consistent with [[ai-in-finance]] (about 24,000 exception lines in November, 58% missing references from two providers): APM unmatched at WD3 0.7%, not the 0.3% target.

## Sources

- **Internal**
  - [[payments-fundamentals]], [[adyen]], [[stripe]], [[blackline]], [[accounting-for-architects]], [[designing-financial-ledgers]], [[custom-finance-platforms]], [[finance-landscape]], [[integration-architecture]], [[ai-in-finance]], [[loosely-coupled-domains]], [[traceability-and-reconciliation]], [[finance-data-flows]].
  - `_research/brief-payments.md` (§1.14, §3.12, §4.3), `_research/brief-blackline-onestream.md` (A7), `_research/productscape-digest.md` (§1.2, §2.1 streams 1, 3, 4), `_research/scenario-ledger.md`.
- **External**
  - Adyen Docs: settlement details report, getting paid, payment accounting report.
  - Stripe Docs: payout reconciliation report, balance transaction object, disputes, payouts; Stripe engineering blog on its internal Ledger (2024).
  - BlackLine FY2025 Form 10-K; ING and DZ BANK camt.053 format descriptions; Directive (EU) 2015/2366.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Added a one-sentence cross-reference to the new Part V case study [[case-uber-payments]]. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: smoothed the [[case-uber-payments]] cross-reference and added the Uber source; fixed a double comma; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
