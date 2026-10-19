---
status: accepted
revised: 2026-10-18
---

# Spec: Changing the Engine in Flight: Modernization Patterns for Finance

## Intent

Close Part I with the pattern vocabulary for changing a live finance estate without breaking its books. The reader should leave with six dispositions adapted to finance, the ERP migration approaches (greenfield, brownfield, selective data transition, Central Finance first) and their trade-offs, the distinction between replication hubs and accounting hubs as stranglers for ledgers, the incremental displacement patterns translated to finance, the parallel run as a gate with variance classes and exit criteria, data migration and retention choices, the period-boundary cut-over rule with blackout windows, and decommissioning as an archive-and-sequence design. Northmere supplies three cases: the Wayfare EBS archive decommissioning, a candid review of the 2025 FI-CA agency billing displacement, and the 2,300 custom objects in a greenfield S/4HANA.

## Audience

Chief and enterprise architects, finance-systems architects and transformation leads who must choose how a ledger, subledger or ERP is replaced or retired; controllers and controls leads who must sign the first close and evidence the migration. They know migration patterns from software; they need the finance-specific constraints.

## Success criteria

- [ ] Reader can assign one of six dispositions (retain, retire, rehost, replatform, refactor, replace) per component, with its finance-specific catch, and relate it to the TIME verdict.
- [ ] Reader can compare greenfield, brownfield, selective data transition and Central Finance first in a trade-off table, and explain why greenfield does not by itself deliver a clean core.
- [ ] Reader can explain why a replication hub (Central Finance) and an accounting hub (Oracle Accounting Hub, Workday Accounting Center) strangle different things, and why a hub needs a dated retirement plan.
- [ ] Reader can apply event interception, legacy mimic, transitional architecture, branch by abstraction and revert to source to a finance case, and knows parallel run is not a named Thoughtworks pattern.
- [ ] Reader can design a parallel run: variants, four variance classes, exit criteria and sign-off.
- [ ] Reader can choose a data migration option, prove it with control totals and a migration clearing account, and reconcile retention with GDPR Article 17(3).
- [ ] Reader can pick a cut-over date using "close in the old, open in the new", the second-month-of-quarter rule and a blackout calendar.
- [ ] Reader can lay out an archive plan (what, how long, form, access) and the decommissioning sequence for a retired ledger.

## Non-goals

- The full stage-by-stage migration of Stayloft's merchant subledger, stage-gate design, hypercare and people ([[incremental-modernization]]).
- Program leadership, business case, SI model and testing strategy for an ERP transformation ([[finance-transformation]]).
- The Central Finance versus accounting-hub decision itself and ERP coexistence models ([[multiple-erps]]).
- Decommissioning evidence checklist and portfolio waves ([[application-portfolio]]); debt measurement and clean-core fitness ([[technical-debt-and-fitness]]); S/4HANA internals ([[sap-s4hana]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Practitioner-knowledge items (brownfield step names, SDT tooling, Central Finance mechanics) were not re-verified on help.sap.com; spot-check before publication.
- Whether SAP's October 2026 statement on transition-option subscriptions to 2035 has been confirmed in the SAP Note referenced by the press release.
- Retention periods beyond the Netherlands and Germany are not quoted; a later revision could add a verified table for Wayfare's other jurisdictions.

## Decision log

- **2026-10-18** — Used six dispositions instead of AWS's seven, folding relocate into rehost and renaming repurchase as replace, because finance replacements are often a different kind of product.
- **2026-10-18** — Framed hubs by what they strangle (replication hub: the ledger from the reporting side; accounting hub: account determination) rather than by vendor, to stay vendor-neutral and to leave the Q4 2027 decision open for [[multiple-erps]].
- **2026-10-18** — Made the 2025 FI-CA displacement an honest retrospective (quarter-end first close, rounding policy, wholesale partner migration, 13 months of history, transitional code without expiry) so the patterns are shown failing for non-pattern reasons.
- **2026-10-18** — Recommended the second month of a fiscal quarter as the default cut-over, rejecting year-end (Big-Bang Bravado) and the third month; accepted the first month only with spare capacity.

## Sources

- **Internal**
  - [[application-portfolio]] — EBS archive in wave 1, colocation end, decommissioning evidence checklist, retention examples.
  - [[custom-finance-platforms]] — SFP components, 2025 FI-CA agency move, rounding difference.
  - [[finance-data-architecture]] — 2027 partner registry match figures.
  - [[where-finance-architecture-goes-wrong]] — Big-Bang Bravado and the rejected 1 January 2029 cut-over.
  - `_research/brief-ea-integration-ledger.md` §4; `brief-sap.md` §1.5, §2.14, §5, §6; `brief-oracle.md` §2.4, §3.7, §8.1; `brief-workday.md` §4; `brief-accounting-controls-regulation.md` §5; `productscape-digest.md` §4.2, §7.
- **External**
  - Fowler, *Strangler Fig* (2024) and the 2019 rename; *BranchByAbstraction* (2014).
  - Cartwright, Horn and Lewis, *Patterns of Legacy Displacement* and *Transitional Architecture*.
  - AWS Prescriptive Guidance, *About the migration strategies* — the seven Rs.
  - SAP News on ECC maintenance, the transition option and clean-core levels; Oracle EBS Premier Support; Oracle Accounting Hub and Workday Accounting Center documentation.
  - GDPR Article 17; business.gov.nl and Haufe on Dutch and German retention.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: SAP News short links replaced with canonical article URLs and titles (transition-option update dated 13 Oct 2026 verified); custom-code triage reconciled with the sap-s4hana April 2027 ATC baseline (690 retired out of ~1,240 not executed). *(AI-mediated session)*
- **2026-10-18** — Consistency pass: SFP subledger cut-over date set to 1 November 2027; calendar rule wording clarified where relevant. *(AI-mediated session)*
- **2026-10-18** — Consistency pass: calendar alignment (payout cohorts April–May 2029; fiscal-year-start exception stated). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Modernization Patterns for Legacy Finance Systems" to "Changing the Engine in Flight: Modernization Patterns for Finance" at the author's request. *(AI-mediated session)*
