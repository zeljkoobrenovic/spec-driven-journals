---
status: accepted
revised: 2026-10-20
---

# Spec: Who Owns What: Organizing Architecture Across Finance and Technology

## Intent

Answer the chapter question: which organizational design makes a finance architecture work? Argue that in finance the organization is part of the architecture (Conway's law produced Northmere's three ledgers, two payout engines and three billing approaches), and own the **finance-tech team topology** and the **architecture roles**. Give a Team Topologies design for finance technology (stream-aligned brand finance teams; ledger, integration, data and payments platforms; ERP, tax and close as complicated subsystems; architecture and controls engineering as enabling teams) with dated interaction modes; show how to close the Finance–IT gap (paired Finance and Technology owners, "Finance owns the rules, Engineering owns the platform", finance engineering as a discipline); set funding (persistent product core plus plateau tranches); show how a Chief Architect leads a matrix without line authority; assign recurring decisions in a RACI; define architect roles, ratios and career paths; and measure organizational health. The distinctive finance point: some organizational boundaries (segregation of duties, Finance approval of rules) are deliberate and must be kept, while queue-shaped handoffs should become services.

## Audience

Chief and enterprise architects, CTOs and brand engineering leaders, finance-systems directors and CFO/CAO staff who are designing or reorganizing finance-technology teams in a multi-brand group. They leave with a target topology they can adapt, a RACI for recurring cross-functional decisions, role definitions, and measures to tell whether the design works.

## Success criteria

- [x] Reader can explain how Conway's law shows up in a finance estate and which boundaries controls require (segregation of duties) versus which are queues.
- [x] Reader can type each finance-technology team (stream-aligned, platform, complicated subsystem, enabling) and set interaction modes with end dates (Figure 2 and the modes table).
- [x] A Northmere worked example with numbers: the e-wallet handoff trace (11 teams, 17 handoffs, ~65 working days, ~18 days of work) and its target (≤6 handoffs, ~3 weeks).
- [x] Reader can pair process/capability owners in Finance with product owners in Technology and state the rules/platform split.
- [x] A RACI with exactly one accountable party per row for 11 recurring decisions across Finance, Engineering, Security, Data, Payments, Controls, Tax/Treasury and Architecture.
- [x] Architect roles with counts that sum to Dana's ~30, career-path principles, and a finance-literacy hiring exercise.
- [x] Organizational health measures with baselines and targets; failure modes include the ivory tower, the ERP ticket queue and brand forks.
- [x] Trade-off table of four ways to organize finance technology, with a recommendation and its condition.

## Non-goals

- The architecture function's own decision rights and the 90-day plan ([[chief-architect-role]]).
- Review board, ADR, waiver and advice-forum mechanics ([[architecture-governance]]).
- Golden-path contents and standards text ([[principles-standards-reference]]); adapter kit and hub design ([[loosely-coupled-domains]]).
- Capability map and the definitions of capability and application owners ([[capability-mapping]]).
- Plateau funding mechanics ([[target-and-transition-states]]); program organization and SI model ([[finance-transformation]]).
- Ownership of AI agents in depth ([[ai-in-finance]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Communities of practice are credited to Wenger, McDermott and Snyder (2002) from prior knowledge; the Wenger-Trayner pages returned 403 during drafting. Verify before publication or replace with a fetched source.
- Architect ratio guidance is the author's judgment; no credible public benchmark was found. Keep it labeled as judgment.
- Financial Event Management still lacks a Finance owner in the scenario; a later chapter may resolve it.
- Payout-rule approval: the RACI gives accountability to the Head of Partner Settlement (capability owner) while Ingrid owns the partner-payout process; reviewers should confirm this matches [[controls-and-auditability]] and [[custom-finance-platforms]].

## Decision log

- **2026-10-18** — Opened with a handoff trace of a payment-method launch rather than the close, to show an organizational cost the close-walk chapters did not already cover, and to echo the payments-platform persona's "finance needed three months" trigger.
- **2026-10-18** — Made SFP's split into a stream-aligned Stayloft team plus ledger and payout platforms the central topology move, consistent with the 2027 ledger platform team in [[principles-standards-reference]] and the group payout service decision in [[custom-finance-platforms]].
- **2026-10-18** — Added controls engineering as a second enabling team, because the SFP remediation needed engineers building evidence patterns, while keeping change approval with Internal Controls.
- **2026-10-18** — Chose a hybrid funding model (persistent product core plus plateau tranches) to stay consistent with [[target-and-transition-states]], which funds platforms wholly as products from 2030.

## Sources

- **Internal**
  - [[chief-architect-role]], [[capability-mapping]], [[architecture-governance]], [[principles-standards-reference]], [[target-and-transition-states]], [[custom-finance-platforms]], [[controls-and-auditability]], [[loosely-coupled-domains]].
  - `_research/brief-ea-integration-ledger.md` §1.8–1.10; `_research/productscape-digest.md` §5 (personas, especially technology leadership, brand finance engineering lead and payments platform lead).
- **External**
  - Conway, "How Do Committees Invent?", *Datamation*, 1968; Fowler, "Conway's Law", 2022.
  - Skelton and Pais, *Team Topologies*, 2nd ed., IT Revolution, 2025; teamtopologies.com key concepts.
  - Bottcher, "What I Talk About When I Talk About Platforms", 2018; Narayan, "Products Over Projects", 2018.
  - Harmel-Law, "Scaling the Practice of Architecture, Conversationally", 2021; Hohpe, *The Software Architect Elevator*.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: payout ownership clarified (Head of Partner Settlement owns rules; Ingrid owns the payout process and executing platform), RACI payments column annotated; six STD-FIN standards. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass (follow-up): SFP subledger cut-over referred to as August 2027 (consistency item 24). *(AI-mediated session)*
- **2026-10-18** — Consistency pass: SFP subledger cut-over date set to 1 November 2027; calendar rule wording clarified where relevant. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Organizing Architecture Ownership Across Finance, Engineering, Security and Data" to "Who Owns What: Organizing Architecture Across Finance and Technology" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,629 → 5,622 words; lead now ties the chapter to Keystone's target state, the Chief Architect's matrix and [[ai-in-finance]]; 1 subheading renamed ("The e-wallet under the new topology"); buried topic sentences brought forward in the Conway lessons, ownership roles and matrix sections. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
