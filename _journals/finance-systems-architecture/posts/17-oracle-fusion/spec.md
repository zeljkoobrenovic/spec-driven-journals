---
status: accepted
revised: 2026-10-18
---

# Spec: Oracle Fusion: An Accounting Hub for High-Volume Events

## Intent

Explain how Oracle Fusion Cloud ERP structures finance precisely enough for an architect to make design decisions (ledger anatomy, primary and secondary ledgers, reporting currencies, legal entities and balancing segments, the balances cube, Subledger Accounting, Accounting Hub, Revenue Management) and how to run Fusion alongside other major platforms: its integration surfaces, its quarterly update cycle as an architecture concern, and the Oracle products that overlap group platforms. The Northmere thread asks what Wayfare's Fusion estate should become inside a group converging on S/4HANA, and presents three options with Oracle-specific trade-offs and the Chief Architect's reasoning, without pre-empting the general coexistence patterns owned by [[multiple-erps]].

## Audience

Chief Architects, finance-systems and integration architects, and finance-transformation leaders who run Fusion, inherit it through an acquisition, or must decide its future in a multi-ERP group. They know enterprise software; they may not know Oracle's accounting vocabulary.

## Success criteria

- [x] Reader can explain the four choices a ledger fixes, which are irreversible, and why the chart of accounts is the only analytical vocabulary of the balances cube.
- [x] Reader can choose a secondary-ledger conversion level and justify it by cost.
- [x] Reader can describe Subledger Accounting's concepts and how Accounting Hub applies them to non-Oracle events, including its batch, file-centered loading model and unpublished throughput.
- [x] Reader can follow the €84.00 Wayfare rail ticket from four canonical events to balanced journals, and see the clearing account net to zero per ticket.
- [x] Reader can map each Fusion integration surface to its proper use, including the caution on the newer Data Extraction tool.
- [x] Reader can explain why quarterly updates make regression testing (integrations, controls, configuration, opt-in features) a permanent architecture cost.
- [x] Reader can name the Oracle capabilities that overlap Northmere's group platforms and decide each one.
- [x] Reader sees Wayfare's three options in a trade-off table with Dana's leaning and the conditions that would change it.

## Non-goals

- General ERP coexistence and convergence economics, two-tier ERP, Central Finance: [[multiple-erps]], [[sap-s4hana]].
- Posting-rule and accounting-engine theory: [[designing-financial-ledgers]].
- Reconciliation and consolidation platform comparisons: [[blackline]], [[onestream]].
- Revenue-recognition accounting itself: [[accounting-for-architects]].
- Agentic-control design in general: [[ai-in-finance]].
- Oracle licensing, pricing, NetSuite and EBS functional detail.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Re-verify the Data Extraction (26A) tool's official name and object coverage against current Oracle release notes; public sources are mostly A-Team and community posts as of October 2026.
- Re-check the AI agent line-up and packaging before any revision; the article cites the October 2025 announcement only.
- Confirm whether a journal-level secondary ledger in the group chart is practical at Wayfare's volume before presenting it as more than a possibility.
- The 2027 Q4 Keystone decision outcome should be reflected here once [[multiple-erps]] and later Part IV chapters settle it.

## Decision log

- 2026-10-18 — Framed the chapter around an acquired Oracle estate, because that is how most architects in multi-ERP groups meet Fusion.
- 2026-10-18 — Placed Revenue Management as the home for contract-shaped revenue and Accounting Hub for ticket-shaped revenue, stated as judgment.
- 2026-10-18 — Kept Wayfare's options Oracle-specific and gave Dana a leaning with explicit change-my-mind conditions rather than a verdict, so the Q4 decision stays with [[multiple-erps]].
- 2026-10-18 — Quoted Birmingham City Council only with the brief's sourced figures and their definitions, presented as a governance case.

## Sources

- Internal: [[multiple-erps]], [[designing-financial-ledgers]], [[sap-s4hana]], [[workday]], [[blackline]], [[onestream]], [[payments-to-ledger]], [[loosely-coupled-domains]], [[traceability-and-reconciliation]], [[controls-and-auditability]], [[ai-in-finance]].
- Research: `_research/brief-oracle.md`; `_research/productscape-digest.md` §4 and §8; `_research/scenario-ledger.md`.
- External: Oracle Fusion Financials 26C documentation (ledgers, balances cubes, Accounting Hub), 25D Revenue Management documentation, 26A segment labels and Accounting Hub What's New, Oracle ERP Cloud Adapter capabilities, Oracle A-Team integration guidance, ERP Today on 26C, CFOtech on the October 2025 agents, The Register and Computing on Birmingham City Council.

## Changelog

- 2026-10-18 — Initial spec and article written in an AI-mediated session.
- **2026-10-18** — Editorial review pass: forward note on the Dec 2027 convergence decision (Wayfare to S/4HANA, Oracle Accounting Hub not adopted), American spelling, timetoread. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Oracle Fusion Cloud ERP: Ledgers, Accounting Hub and Coexistence" to "Oracle Fusion: An Accounting Hub for High-Volume Events" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
