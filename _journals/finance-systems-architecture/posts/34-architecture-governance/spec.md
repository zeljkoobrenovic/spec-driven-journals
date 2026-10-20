---
status: accepted
revised: 2026-10-20
---

# Spec: Architecture Governance That Speeds Decisions

## Intent

Open Part IV by building the governance machinery behind the decision rights set out in [[chief-architect-role]]. Governance is a decision system judged by lead time and the reopen rate, not by reviews held. It routes decisions by reversibility, reach and a few hard triggers, writes every decision in one record format, combines a review board (binding authority) with an advice forum (distributed learning), and makes a short list of mandatory standards bite through expiring waivers and conformance checks. It is wired into SOX change management, procurement, renewals and program gates, and it governs SaaS configuration and vendor releases as well as code. Northmere's first year (2027) is the worked example.

## Audience

Chief and enterprise architects, finance-systems leads and internal-controls leaders who run or redesign an architecture board in a federated, SOX-regulated finance estate. They leave with a routing taxonomy, an ADR template with finance-specific fields, a forum design, standard and waiver lifecycles, a gate map and a governance scorecard.

## Success criteria

- [x] Defines architecture governance, architecture decision record, review board and waiver (owned terms), and separates governance from IT change management, procurement and program steering.
- [x] Gives a decision taxonomy (reversibility × reach, plus five triggers) and Northmere's four paths with lead-time targets; decision-flow diagram.
- [x] Presents a full worked ADR (ADR-0007, payout rules as versioned configuration) with options, control impact assessment, advice received, confirmation and an addendum, consistent with [[controls-and-auditability]].
- [x] Compares review board and advice process in a trade-off table and shows how Northmere combines forum, board and design authority, without implying advice replaces change approval in ICFR scope.
- [x] Covers the standards lifecycle and waiver lifecycle with state diagrams, Northmere's six-standard catalog and a waiver register sample.
- [x] Covers conformance (automated fitness functions vs sampling), the SOX, procurement, renewal and program gates, and governance of SaaS configuration and vendor releases.
- [x] Gives governance metrics with gaming cautions, anti-patterns, a Chief Architect's view, Questions to ask, and hands off to [[principles-standards-reference]].

## Non-goals

- Decision rights, the operating-model choice and the function's scorecard ([[chief-architect-role]]): summarized, not repeated.
- Content of principles, standards and reference architectures ([[principles-standards-reference]]).
- Fitness functions as estate-health measurement and the debt register ([[technical-debt-and-fitness]]).
- The design authority as a transformation-program body ([[finance-transformation]]); team design and architect roles ([[organizing-for-architecture]]).
- The payout-rule remediation design itself ([[controls-and-auditability]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ADR, waiver and release-note templates should appear in the [[toolkit]]; the toolkit writer should reuse the field lists here.
- *Resolved 2026-10-18 (editor):* standards are STD-FIN-01..06, in force 1 April 2027; STD-FIN-01/-02 enforced from 1 July 2027 when the schema registry went live; STD-FIN-06 from Q3 2027 (as in [[principles-standards-reference]] and [[loosely-coupled-domains]]).
- Chapter 08 lists five control-plane requirements as "mandatory standards"; this chapter treats them as the five clauses of STD-FIN-05 (segregation of duties by design). A reviewer should confirm the framing reads consistently across both chapters.

## Decision log

- **2026-10-18** — Chose ADR-0007 (payout rules) over the payments-to-ledger matching scope as the worked record, because it shows the control impact assessment, a standard clause and a waiver created in one decision; kept the design detail in chapter 08 and showed only how the record carries it.
- **2026-10-18** — Used a decision-flow diagram centered on the single register and its downstream gates, rather than repeating chapter 01's materiality routing diagram.
- **2026-10-18** — Treated board, forum and design authority as three configurations sharing one secretariat and one record format, rather than as competing models.
- **2026-10-18** — Defined a standards lifecycle with a Trial state and the rule "no owner, no reference implementation, no conformance check, no mandate", and a waiver lifecycle with no indefinite state (second renewal escalates to the design authority).

## Sources

- **Internal**
  - [[chief-architect-role]] — decision rights, five standards, scorecard baseline (41 days, 3 of 11 reopened; targets 10/25).
  - [[controls-and-auditability]] — SFP significant deficiency, remediation design and timing, control impact assessment.
  - [[sap-s4hana]], [[application-portfolio]], [[ai-in-finance]], [[stripe]], [[capability-mapping]] — clean-core gate, decision-due dates, STD-FIN-06, Stripe Tax exception, reconciliation overlap.
  - `_research/brief-ea-integration-ledger.md` §1.7–1.9, §4.4; `_research/productscape-digest.md` §1.6, §2.1 stream 12.
- **External**
  - Michael Nygard, "Documenting Architecture Decisions" (2011).
  - MADR 4.0.0; Martin Fowler, "Architecture Decision Record" (2026); Thoughtworks Radar, Lightweight ADRs.
  - Andrew Harmel-Law, "Scaling the Practice of Architecture, Conversationally" (2021); *Facilitating Software Architecture* (O'Reilly, 2024).
  - Gregor Hohpe, *The Software Architect Elevator*.
  - Ford, Parsons, Kua, Sadalage, *Building Evolutionary Architectures*, 2nd ed. (2022).

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: standard IDs renamed STD-FIN-01..06 with canonical in-force and enforcement dates; per-standard waiver counts reconciled with ch. 35 (14 at Q3, 11 at year-end); bank-details advice aligned with the SFP→Northmere Pay authority move; American spelling. *(AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon batch credit wording / Stripe Tax waiver renewal with neighboring chapters. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,768 → 5,780 prose words; lead now ties the chapter to Part III's decisions and names the Part IV chapters that use its register; rollout paragraph moved under the catalog heading; teaser and back-reference openers replaced with their claims; headings unchanged; spec unchanged. *(AI-mediated session)*
