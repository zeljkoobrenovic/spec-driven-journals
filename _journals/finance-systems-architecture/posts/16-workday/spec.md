---
status: accepted
revised: 2026-10-18
---

# Spec: Workday: The Org Chart Behind the Ledger

## Intent

Answer where Workday belongs in an enterprise finance estate: as HCM, as Financials, or both. The chapter explains Workday's design as an architect meets it: one metadata-driven object model, configured business processes, worktags and the Foundation Data Model in place of an account string, Accounting Center for external transactions, and an integration surface with published limits and a release cadence nobody can defer. It establishes the HCM-as-master pattern, and it shows through Northmere how to decide whether an acquired Workday Financials tenant stays, moves or becomes a governed second tier.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders who run Workday HCM beside SAP or Oracle, or who inherited Workday Financials through an acquisition. They should leave able to design a worktag model against a group chart, size integrations against Workday's limits, and frame the tiering decision with explicit conditions.

## Success criteria

- [ ] Reader can explain worktags, driver and balancing worktags, spend and revenue categories and account posting rules, and contrast them with a segment-based chart of accounts (table).
- [ ] Reader can follow a worked worktag redesign for the Tablekin $1,029 invoice, including the journal and the rule-based mapping to the group chart.
- [ ] Reader knows what Accounting Center documents (Prism ingestion tables, batches, rules, summarized posting, drill-back) and what it does not publish (throughput, latency, retention, corrections, licensing).
- [ ] Reader can state the HCM-as-master pattern, including which objects finance masters, with a flow diagram for Northmere.
- [ ] Reader can size integrations against the documented extract quotas, throttling and EIB limits, and plans release regression as a standing process.
- [ ] Every vendor claim is dated and sourced; AI-agent and Data Cloud statements carry availability status as of October 2026.
- [ ] The A/B/C trade-off table is present, and Dana's recommendation is stated conditionally with a fallback.

## Non-goals

- General ledger design, posting rules and accounting-hub theory ([[designing-financial-ledgers]]).
- Two-tier ERP and convergence patterns in general ([[multiple-erps]]).
- Master-data governance in general ([[finance-data-architecture]], [[systems-of-record]]).
- Stripe's object model and balance transactions ([[stripe]]); OneStream consolidation ([[onestream]]).
- SoD and ICFR concepts ([[controls-and-auditability]]); AI governance ([[ai-in-finance]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Accounting Center throughput, correction handling and licensing after the Prism-to-Data Cloud repackaging are not public; revisit if Workday publishes them.
- Data Cloud general availability for finance data is targeted for 2027R1; recheck before publication.
- Effective dating and organization-type detail rest on practitioner documentation, not a Workday architecture statement.
- Whether Workday's October 2026 Accounting Agent subsumes earlier announced finance agents is unstated by Workday.

## Decision log

- **2026-10-18** — Framed the Northmere decision as three options (stay, move to S/4HANA, governed second tier) rather than stay-or-move, because the real architectural choice is tiering, not vendor preference.
- **2026-10-18** — Gave Tablekin its own Financials tenant separate from the group HCM tenant, so the chapter can show the cost of losing Workday's shared-object model (copied approvers, two release cycles).
- **2026-10-18** — Kept Accounting Center claims to what Workday documents and added an explicit "not published" table instead of estimating performance.
- **2026-10-18** — Dropped a deeper treatment of Extend and Workday Build; they matter less to finance architecture than integration limits and release cadence.

## Sources

- **Internal**
  - `_research/brief-workday.md` — primary factual base and evidence markers.
  - `_research/productscape-digest.md` §4, §8 — Workday's slot in the platform map.
  - `_research/scenario-ledger.md` — Northmere facts, Tablekin invoice.
  - [[build-versus-buy]], [[multiple-erps]], [[designing-financial-ledgers]], [[stripe]], [[oracle-fusion]].
- **External**
  - Workday, *Financial Management datasheet* (2024) — scope, BPF, multibook.
  - Workday, *Accounting Center* product page and administrator guide — accounting sources, Prism ingestion, summarized posting.
  - Workday, *Integration and Web Service Limits* (read October 2026) — quotas, throttling, EIB limits.
  - Workday, *From Prism to Data Cloud* — packaging and phased availability.
  - Workday newsroom, February 2025 to October 2026 — agents and availability.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: Agent System of Record press-release link moved from the q4cdn PDF to Workday newsroom with verbatim quote, American spelling (license, program), timetoread. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Workday: Financials, People and the Organizational Backbone" to "Workday: The Org Chart Behind the Ledger" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
