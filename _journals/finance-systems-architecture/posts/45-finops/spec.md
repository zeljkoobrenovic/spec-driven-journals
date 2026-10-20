---
status: accepted
revised: 2026-10-20
---

# Spec: FinOps Meets the Ledger: Technology Spend as Financial Data

## Intent

Answer the question "how does cloud, SaaS and AI spend become trustworthy financial data?" as a finance-architecture problem, not a cost-cutting guide. The chapter treats provider billing data as subledger data under a contract (FOCUS), allocation as master data mapped to the group chart of accounts, and the month-end path (snapshot, accrual, true-up, commitment amortization, intercompany recharge, tie-out) as a posting service with versioned rules outside the finance data platform. It ends with unit cost as a governed metric anchored in the closed ledger, used to test Keystone's savings claims and the finance estate's own run cost. It owns the concepts *FOCUS*, *showback and chargeback*, *cloud cost allocation* and *unit cost*.

## Audience

Chief and enterprise architects, finance-systems and data architects, FinOps practitioners who must hand data to Finance, and controllers who own the accrual, classification and intercompany policy for technology spend. FP&A and tax leads are a secondary audience.

## Success criteria

- [x] Reader can explain FinOps as the 2026 Framework defines it (technology, not only cloud; categories and scopes; finance persona; maturity targets) and why the seam to the ledger is usually undesigned (78% of FinOps teams report to CTO/CIO).
- [x] Reader can name FOCUS's ledger-relevant columns with exact spelling, state that 1.4 is current but providers mostly emit 1.2, and explain `BilledCost` (payables view) versus `EffectiveCost` (expense view; no `AmortizedCost` column), `ChargeCategory` and `ChargeClass = Correction`.
- [x] Five accounting questions (timing, prepaid, capitalization, P&L line, whose cost) plus marketplace purchases are answered as policy choices, with standards cited accurately (ASU 2018-15; ASU 2025-06 from secondary sources; IFRIC March 2021) and treatments marked as judgement.
- [x] A FOCUS-to-ledger data-flow diagram and an allocation-hierarchy diagram, plus a month-end sequence diagram.
- [x] Northmere worked example with ledger-consistent figures: accrual and true-up, Savings Plan purchase and amortization, prepaid roll-forward, tie-out breaks, intercompany recharge by entity, unit cost per Stayloft booking, wave 0 hosting savings test, AI token cost per exception.
- [x] RACI for the cloud economics team, brand engineering, FP&A, controller, procurement, tax and finance data; trade-off table for showback, chargeback and intercompany recharge.
- [x] Failure modes include tag sprawl (The Doppelgänger Record), Spreadsheet Glue allocation and cost in the wrong P&L line; Chief Architect's view; 10 questions; sources.
- [x] Links to OWNED's [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) and [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs) for decision tactics without repeating them.

## Non-goals

- Cloud and AI purchasing tactics, unit choice for investors and commitment sizing — OWNED's [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) and [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs).
- Application TCO method and rationalization waves — [[application-portfolio]].
- Chart of accounts design and master-data management styles — [[finance-data-architecture]].
- Intercompany mechanics, netting and transfer pricing in general — [[global-scale]].
- FinDB architecture, governed metrics and ledger-to-warehouse tie-out in general — [[finance-data-flows]].
- Agent controls — [[ai-in-finance]]; vendor dependency and exit — [[vendor-portfolio-strategy]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Azure FOCUS 1.2 general availability was not confirmed; re-check before freezing the manuscript.
- ASU 2025-06 is cited from Deloitte and Eide Bailly summaries; its effect on hosting-arrangement implementation costs is stated as an inference.
- Should the sub-account register and the tag standard appear in the toolkit as templates?
- A 2026 Gartner Magic Quadrant and FOCUS 1.5 may change tooling statements; the chapter deliberately avoids tool rankings.

## Decision log

- **2026-10-18** — Framed the chapter around the seam between billing data and the books, not optimization; optimization tactics are delegated to OWNED.
- **2026-10-18** — Kept FinDB "the book for nothing": allocation and journal generation sit in a posting service with a rule store, consistent with [[finance-data-flows]] and the posting-pipeline golden path.
- **2026-10-18** — Made NTI the cloud payer so chargeback becomes intercompany, with pass-through at cost separated from the cost-plus engineering-services charge (a tax decision, shown as such).
- **2026-10-18** — Followed the provider's days-based amortization pattern for Savings Plans as a stated policy choice, to keep the ledger tied to `EffectiveCost`.

## Sources

- **Internal**
  - [[application-portfolio]] — six-component TCO, $118M license and hosting, wave 0, decommissioning criteria.
  - [[finance-data-architecture]] — group CoA v2 dimensions, master-data authorities, Finance Data Council.
  - [[finance-data-flows]] — FinDB charter, governed metric parts, tie-out.
  - [[global-scale]] — intercompany originator, netting, transfer pricing.
  - [[technical-debt-and-fitness]], [[vendor-portfolio-strategy]], [[ai-in-finance]], [[designing-financial-ledgers]].
  - OWNED, [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) and [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs).
- **External**
  - FinOps Foundation: Framework (2026), Invoicing & Chargeback, Allocation, Personas, Maturity, State of FinOps 2026, State of Tokenomics.
  - FOCUS specification 1.4 and column definitions (EffectiveCost, ChargeCategory).
  - AWS, Microsoft and Google Cloud billing documentation (FOCUS exports, Savings Plans, amortized views, CUD changes, tag backfill).
  - IFRIC Update March 2021; Deloitte on ASU 2018-15 and ASU 2025-06; PwC on the OECD low value-adding services approach; TBM taxonomy.

## Changelog

- **2026-10-18** — Initial spec and article (new Part IV chapter 39a, folder 45). Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Technology Spend as Financial Data: FinOps Meets the Ledger" to "FinOps Meets the Ledger: Technology Spend as Financial Data" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,263 → 7,285 prose words; outline unchanged; lead now ties the chapter to [[technical-debt-and-fitness]] and names what it builds on and feeds; four first sentences brought forward (prepaid treatment, capitalization, summarized journals, account hierarchy); announce and filler sentences cut. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
