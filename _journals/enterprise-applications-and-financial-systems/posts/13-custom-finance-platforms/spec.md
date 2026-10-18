---
status: accepted
revised: 2026-10-18
---

# Spec: Why Enterprises Build Their Own Finance Platforms

## Intent

Open Part II by explaining when building proprietary finance capability is justified and, above all, where a custom platform must stop and the ERP begin. The reader should leave with five tested reasons to build, four burdens of owning, a boundary table and six mandatory boundary rules, the summarized-posting-with-drill-back integration pattern with control totals, a full cost-of-owning model, and an explicit per-component retirement test, all shown working on Northmere's Stayloft Finance Platform (SFP) with a keep/converge/retire decision table.

## Audience

Chief and enterprise architects, finance-systems architects and engineering directors who own or govern brand finance platforms; controllers and controls leads who must sign or test the numbers those platforms produce. They know software; they need the finance boundary and the decision discipline.

## Success criteria

- [ ] Reader can name the kinds of custom finance application (billing, commission, settlement and payouts, customer funds, revenue allocation, marketplace fees, ad billing) and why packages struggle with each.
- [ ] Reader can apply a test to each of the five reasons to build (volume and latency, product coupling, novel models, licensed-entity needs, cost at scale) and state the four burdens (control, audit, talent, regulatory change).
- [ ] Reader can state the boundary principle (custom owns operational financial facts; ERP owns the book of record) and the six rules, including "no posting to arbitrary GL accounts".
- [ ] Reader can follow the Lisbon booking (€600 / €90 / €510) through SFP's subledger entries, summarization, drill-back and four control-total hops.
- [ ] Reader can build a full cost-of-owning view (engineering, infrastructure, controls and audit, finance operations, regulatory change).
- [ ] Reader can run the five-question retirement test per component and read the SFP decision table (3 keep, 4 converge, 2 retire, plus Wayfare payout engine and Northmere Ads).
- [ ] Article has three mermaid diagrams, a trade-off table for the merchant subledger's home, Chief Architect's view, Questions to ask and Sources and Evidence.

## Non-goals

- Ledger internals: posting rules, invariants, idempotency, money representation, bi-temporality, hot-account engineering ([[designing-financial-ledgers]]).
- General build/buy criteria and vendor selection ([[build-versus-buy]]).
- The modernization pattern catalog and the stage-by-stage SFP migration ([[modernization-patterns]], [[incremental-modernization]]).
- PSP settlement and three-way matching ([[payments-to-ledger]]); authority matrices ([[systems-of-record]]); reconciliation catalog ([[traceability-and-reconciliation]]).
- Product depth on FI-CA, Oracle Accounting Hub and Workday Accounting Center (platform chapters).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The merchant subledger's target (FI-CA vs accounting hub) depends on the Q4 2027 convergence decision; the chapter recommends FI-CA conditional on a volume proof. Revisit when [[multiple-erps]] and [[sap-s4hana]] are written. *Resolved 2026-10-18:* [[multiple-erps]] records the 8 Dec 2027 accounting-hub decision; the chapter keeps its May 2027 recommendation as history with a forward note.
- Whether the traveler-funds ledger should move into Northmere Pay's ownership after 2029 is left open.
- SAP statements are kept minimal (brief-sap.md was not available); a reviewer should check FI-CA claims against that brief once it exists.

## Decision log

- **2026-10-18** — Classified SFP per component (nine verdicts) rather than per platform, because the platform mixes the most differentiating logic (commission rating) with commodity logic (invoice rendering); a single verdict would be wrong either way.
- **2026-10-18** — Kept the payout engine despite the FY2026 significant deficiency, separating a fixable control failure from a hard-to-replicate capability; it absorbs Wayfare's engine as the group payout service.
- **2026-10-18** — Made account determination the first boundary fix (moving it out of SFP in 2027), because it is cheap and removes the largest silent risk.
- **2026-10-18** — Rejected balance-only feeds and per-transaction GL posting as defaults in favor of summarized posting with drill-back and control totals.

## Sources

- **Internal**
  - [[where-finance-architecture-goes-wrong]] — Shadow Ledger, Audit Afterthought, Tool Overlap Creep; the 13-month drill-back retention illustration.
  - [[designing-financial-ledgers]] — next chapter; receives the ledger internals.
  - `_research/productscape-digest.md` §1.1, §1.2, §1.7, §4, §7; `brief-ea-integration-ledger.md` §3; `brief-payments.md`; `brief-oracle.md`; `brief-workday.md`; `brief-accounting-controls-regulation.md`.
- **External**
  - Oracle, *How Oracle Accounting Hub Cloud Works* — accounting hub pattern with drill-down.
  - Workday, *Accounting Center* — high-volume event accounting with summarized posting.
  - SAP Learning, *Implementing SAP Financial Contract Accounting* — FI-CA positioning for high volume.
  - Directive (EU) 2015/2366 Art. 10; European Commission, *VAT in the Digital Age* — licensed-entity and regulatory-change reasons.
  - Fowler, *Accounting Patterns*; Square, *Books*; Stripe, *Ledger* — published examples of custom ledgers.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: forward note that the FI-CA merchant-subledger recommendation was superseded by the Dec 2027 accounting-hub decision; bank-details authority worded as target state (SFP until 30 Jun 2028); payout date in the partner-app example 26 Apr; KYC expanded. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
