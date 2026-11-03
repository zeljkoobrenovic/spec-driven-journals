---
status: accepted
revised: 2026-10-28
---

# Spec: Human Oversight and Bounded Autonomy

## Intent

Make human oversight of agents an engineered subsystem rather than a sentence in a design document. The reader leaves able to choose an oversight mode per action class (approve before, intervene during, review after, sample audit, monitor), design an approval gate whose card shows checkable facts, bind every approval to the exact action object, policy version and evidence shown, re-check it immediately before execution, route escalations to named roles with deadlines and safe terminal states, and measure approvers as carefully as the agent. The chapter states the book's single approval model (consistency ruling 6) and tells the Rubber Stamp story end to end. It must say plainly that no published study measures approval fatigue for LLM agents, so the design rests on human-factors evidence, vendor telemetry and the author's judgement.

## Audience

Chief architects, platform leads and risk owners who own A1 approval steps in support, finance, legal, HR or high-stakes agents, and who need to know whether those steps protect anything. Also security architects who rely on human confirmation as a control.

## Success criteria

- [ ] Reader can define oversight mode, approval gate, approval fatigue and escalation, and distinguish approval, escalation and handoff.
- [ ] Reader can state the book's approval rule (content-hash binding, approver identity, evidence shown, scope, expiry, revalidation, void on change of action, policy or evidence) and explain why time-only expiry and "no expiry" are rejected.
- [ ] Reader can list what an approval card must show first (effect, system-of-record facts with `as_of`, policy clause, check results, consequence) and why the model's rationale is demoted.
- [ ] Reader can cite the automation-bias evidence (Parasuraman & Manzey, Goddard et al., Bansal et al., Bainbridge) and the vendor approval data with their limits.
- [ ] Reader can map EU AI Act Art. 14(4) items to components and give the Annex III application date of 2 December 2027 under Regulation (EU) 2026/1744; can explain why measured oversight matters for GDPR Art. 22 after SCHUFA.
- [ ] The Rubber Stamp numbers match the ledger (4,812 approvals, 99.3%, 6 s median, 3.1% unjustified; Q3 fixes; ≤ €250 to A2 in October 2027) and agree with [[evidence-for-autonomy]] (612 audited, 7 unjustified, 31 of 38 approvers qualified).
- [ ] The chapter has a failure-scenario table with detection, containment and recovery, two trade-off tables, a requirements table, an Across Domains table and three mermaid diagrams.

## Non-goals

- Tier taxonomy, action classes and the consequence–reversibility grid ([[autonomy-and-consequence]]).
- Promotion criteria, demotion triggers and the autonomy review ([[evidence-for-autonomy]]).
- Conversation UX, confirmation dialogs as interface patterns and the escalation package's contents ([[agent-interaction-design]]).
- Ownership transfer and typed handoff payloads ([[coordination-and-handoffs]]).
- Policy-as-code engines, other enforcement points and evidence-log design ([[policy-enforcement-and-audit]]).
- Kill-switch and compensation mechanics ([[partial-failure-and-compensation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Seeded cards are adapted from airport threat image projection; there is no published evaluation for business approval queues. Watch for one.
- The Anderson et al. (CHI 2015) and *MIS Quarterly* (2018) habituation studies were cut from the article because their abstracts were not verified; restore them if verified.
- GDPR Article 22 amendments in the wider Digital Omnibus remain unresolved as of October 2026; update when an official text exists.
- Harmonized standards for AI Act Article 14 are still in preparation; they may set concrete expectations for oversight interfaces.

## Decision log

- **2026-10-28** — Introduced "review levels" (R1–R3) inside A1 to separate who approves from how much autonomy a class has, so the A0–A3 register is not overloaded.
- **2026-10-28** — Adopted one approval model for the book: hash-bound, evidence-referencing, expiring, revalidated at execution; rejected the sales design's non-expiring approvals and the benefits design's id-only binding.
- **2026-10-28** — Framed the Rubber Stamp as a card-design failure (13 of 15 unjustified credits were decidable from facts the card did not show), not as approver negligence, and made "the gate became informative because it became rare" the worked example's result.
- **2026-10-28** — Added seeded, never-executable cards as a measurement of approvers, citing threat image projection as the precedent; rejected minimum dwell timers.

## Sources

- **Internal**
  - [[autonomy-and-consequence]], [[evidence-for-autonomy]], [[retries-idempotency-and-concurrency]], [[durable-agent-execution]], [[versioning-agent-systems]], [[agent-observability]], [[prompt-injection-defense]], [[policy-enforcement-and-audit]].
  - Interview designs (design examples): `agentic-support-platform` steps `action-gate`, `escalation`; `agentic-sales-platform` step `send-gate`; `agentic-marketing-platform` step `brand-gate`; `agentic-finance-platform` step `maker-checker` and capacity; `agentic-legal-platform` step `attorney`; `agentic-hr-platform` steps `naive`, `hiring-gate`; `agentic-healthcare-platform` steps 5 `gate`, 7 `eval`; `agentic-public-benefits-platform` steps 4, 5, 7; `agentic-research-platform` step 4 `gate`; `ai-coding-cli` step `safety`.
  - `_research/brief-security-oversight.md` Part 5; `brief-domains-regulation.md` Parts 2–3, 5; `brief-foundations-autonomy.md` Parts 2, 6; `consistency-issues.md` items 6, 7, 8, 15, 17.
- **External**
  - Bainbridge (1983); Parasuraman, Sheridan & Wickens (2000); Parasuraman & Manzey (2010); Goddard et al. (2012); Bansal et al. (2021); Perry et al. (2023); Feng et al. (2025); Hofer & Schwaninger (2005).
  - Anthropic sandboxing (2025), auto mode (2026) and autonomy measurement (2026) posts; Meta Rule of Two (2025).
  - Regulation (EU) 2024/1689 Arts. 6(3), 14, 26; Regulation (EU) 2026/1744; GDPR Art. 22; CJEU C-634/21 SCHUFA; Amnesty International on the Dutch childcare-benefits scandal (2021).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: credit limit wording aligned with ruling 21; Digital Omnibus adoption date removed (unverified) and the Article 14 statement attributed to the Official Journal record. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
