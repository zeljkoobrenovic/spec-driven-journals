---
status: accepted
revised: 2026-10-18
---

# Spec: Preventing Redundant Capabilities and Unnecessary Coupling

## Intent

Give the reader a working mechanism for keeping a finance estate from drifting back into duplication and brittle dependency once the capability map and portfolio have exposed it. The chapter owns two artifacts: the **capability overlap register** (every duplicate carries an owner, volume, cost, control impact, a decision verb and a date) and the **coupling taxonomy for finance** (temporal, schema, semantic, release, contractual, organizational). Its central argument is that redundancy and coupling trade against each other: removing a duplicate concentrates dependency on the survivor, so consolidation must happen behind published interfaces, with configuration rather than forks. Northmere's decision to collapse its two partner-payout engines shows both halves at once.

## Audience

Chief and enterprise architects, integration architects and finance-systems leaders who already have a capability map and a portfolio, and need the governance and design discipline that keeps them true; controllers and controls leads who must live with the reconciliations and control tests that duplication and coupling create.

## Success criteria

- [ ] Reader can name five mechanisms by which redundancy accumulates (acquisition, vendor bundling, "free" capability, team autonomy, transitions without end dates) and the counter to each.
- [ ] Reader can apply the "would we choose the second one today" test and the decision table to tell legitimate duplication (resilience, regulatory separation, different business models, dated transition, separability) from waste.
- [ ] Reader can build an overlap register with the listed fields and the five verbs (Accept, Converge, Retire, Contain, Prevent), and read Northmere's October 2027 excerpt.
- [ ] Reader can classify a dependency by the six coupling types, with a finance example and remedy for each, and explain why semantic coupling is the most expensive.
- [ ] Reader can state the seven design rules and how each is enforced, and compute three coupling measures (change coupling, fan-in/out, incident propagation) from existing data.
- [ ] Reader can follow the payout-engine collapse: options, the execution split by funding entity, gated stages, risks and controls, economics.
- [ ] Article has four mermaid diagrams (register lifecycle, overlap map, coupling heat, collapse sequence), trade-off tables, governance hooks, Chief Architect's view, Questions to ask, Sources and Evidence; hands off to [[loosely-coupled-domains]].

## Non-goals

- Building the capability map and heat map, and the first description of the four overlaps ([[capability-mapping]]).
- Portfolio scoring, TIME, TCO, rationalization waves and decommissioning criteria ([[application-portfolio]]).
- The canonical event model, adapter kit and schema registry ([[loosely-coupled-domains]]); control totals and reconciliation catalog ([[traceability-and-reconciliation]]).
- Authority matrices ([[systems-of-record]]); ERP convergence patterns ([[multiple-erps]]); vendor exit plans ([[vendor-portfolio-strategy]]); team design ([[organizing-for-architecture]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The decision on Northmere's three integration technologies is left as "decision due Q4 2027" in the register; [[loosely-coupled-domains]] should close it.
- Whether Wayfare supplier funds fall outside e-money safeguarding is stated as Northmere's position (Wayfare is merchant of record and collects its own fares); a regulatory reviewer should confirm the framing.
- Coupling metric baselines are illustrative; [[technical-debt-and-fitness]] may adopt them as fitness functions and should keep the numbers consistent.

## Decision log

- **2026-10-18** — Built on the capability-mapping chapter's four overlaps rather than re-describing them; the register adds the decision, volume, control-impact and date fields and splits rows by scope (payouts appear three times with three verbs).
- **2026-10-18** — Added "Contain" and "Prevent" to the obvious accept/converge/retire verbs, so the register can freeze an implementation pending a dependency and record rejected duplications (Stripe RevRec, Adyen platform payouts, Oracle tax for new markets).
- **2026-10-18** — Used six coupling types instead of the contract's five, adding organizational coupling, because Northmere's Wayfare convergence queues on one team; named semantic coupling as the most expensive and illustrated it with a booking-date redefinition that broke no interface.
- **2026-10-18** — Made the payout collapse the worked decision because it shows the redundancy–coupling trade-off directly; kept payment execution split by funding entity as a deliberate, legitimate duplication.

## Sources

- **Internal**
  - [[capability-mapping]], [[application-portfolio]], [[custom-finance-platforms]], [[blackline]], [[onestream]], [[workday]], [[oracle-fusion]], [[stripe]], [[adyen]], [[satellite-platforms]] — the overlaps, decisions and dates the register records.
  - `_research/brief-ea-integration-ledger.md` (DDD, Conway, fitness functions, exactly-once), `brief-blackline-onestream.md` §C, `brief-payments.md` §4, `brief-satellites-ai.md` §A.1 and §A.5, `brief-sap.md` §5, `productscape-digest.md`.
- **External**
  - Martin Fowler, "Integration Database" — shared-database coupling.
  - Hyrum's Law — implicit interface dependence.
  - Vlad Khononov, *Balancing Coupling in Software Design* — strength, distance, volatility.
  - CodeScene documentation, "Change coupling" — measuring co-change from history.
  - SAP, clean-core levels A–D — direct table writes rated Level D.
  - Eric Evans, *DDD Reference*; *Team Topologies* 2nd ed.; *Building Evolutionary Architectures* 2nd ed.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: integration-technology register row now records the June 2027 design-authority decision instead of "decision due Q4 2027"; added closing hand-off heading; American spelling. *(AI-mediated session)*
- **2026-10-18** — Consistency pass: calendar alignment (payout cohorts April–May 2029; fiscal-year-start exception stated). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
