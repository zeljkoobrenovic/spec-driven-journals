---
status: accepted
revised: 2026-10-28
---

# Spec: Back Office: Finance, Legal and HR Agents

## Intent

Show what the back office (finance, legal, HR) demands of an agentic system beyond the platform's general mechanisms, and run those mechanisms end to end on one Closewise accrual. The chapter's claim: back-office agents write into systems of record that other functions own, under duties that rest on named professionals and on calendars the agent does not control. So the agent proposes into a staging store, a principal independent of every maker approves the exact content hash, deterministic code writes to the system of record and reads it back, and the decision record is built for an auditor, a court or a regulator. The same spine serves all three sub-domains, but the gate means different things (all effects, finalized work product, adverse outcomes), and the chapter makes that choice explicit. After reading, an architect can review a back-office agent design against its consequence profile and its domain controls: separation of duties, privilege and confidentiality, and employment-law limits.

## Audience

Architects, principal engineers and platform leads designing or reviewing finance, legal or HR agents, and the risk owners (controllers, general counsel, HR leads) who must defend those agents to auditors and regulators. They know ERP, CLM and HRIS integration and the platform chapters; they need the domain synthesis, the evidence and the decision rules.

## Success criteria

- [ ] Reader can state the back-office consequence profile (five properties plus calendar coupling) and explain how it differs across finance, legal and HR.
- [ ] Reader can draw the back-office spine and name the three gate semantics, with what each lets through.
- [ ] Reader can trace one Closewise accrual from evidence to ERP receipt (sequence diagram), naming the owning chapter of each mechanism, with ledger-consistent numbers (23 entities, ~1,900 a month, ~380 per working day, working day 5, 48-working-hour timer, posting key, September 2027 close figures, Alias Drift figures).
- [ ] Reader can explain the Clausewise and Peoplepoint contrasts: finalize gate, `legal_privileged` routing and ethical walls; no employment decision in the action space and an Article 6(3) assessment tied to the tool list.
- [ ] At least three failure scenarios with detection, containment and recovery; a controls table per action class including SoD, privilege and employment-law controls.
- [ ] Documented evidence is dated and sourced: Mata v. Avianca (2023), Ayinde/Al-Haroun (2025), Magesh et al. (2024 preprint), Heppner (2026, secondary), SOX §404, SR 26-2 (2026), AI Act Annex III with the Regulation (EU) 2026/1744 date, GDPR Art. 22 and SCHUFA (2023); where evidence stops is stated.
- [ ] "What Transfers to Other Domains" names concrete transfers and non-transfers.

## Non-goals

- Re-teaching task state, durable execution, idempotency, compensation, identity, approval-gate design or the evidence log: [[task-state-and-checkpoints]], [[durable-agent-execution]], [[retries-idempotency-and-concurrency]], [[partial-failure-and-compensation]], [[agent-identity-and-least-privilege]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]].
- Ledger design and accounting mechanics: the RECONCILED book ([[designing-financial-ledgers]]).
- Payments, collections and procurement agents (Ostrell has none; Invoice Chaser was cancelled).
- Clinical and public-benefits decisions: [[domain-high-stakes-decisions]].
- Legal advice; the regulatory readings are architectural inferences.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Heppner opinion was read only through law-firm summaries; re-check against the opinion text before a revision.
- The status of GDPR Article 22 amendments in the wider Digital Omnibus is contested in secondary sources; the chapter cites the 2016 text.
- The Annex III application date (2 December 2027) has moved once; re-verify.
- Whether US bank supervisors issue agent-specific model-risk guidance after SR 26-2.
- No published production evaluation of finance-close, contract-review or HR-helpdesk agents; revisit if one appears.

## Decision log

- **2026-10-28** — Framed the chapter around an audit-committee review (23 November 2027) so the domain's controls are answers to the questions risk owners actually ask, and so the Annex III date has a concrete stake.
- **2026-10-28** — Named three gate semantics (all-effects, finalize, adverse-outcome) instead of picking one, because the interview designs disagree and the disagreement is a domain choice, not an error; adopted the HR design's 30% contradiction as the illustration.
- **2026-10-28** — Synthesized the Closewise flow from existing chapters (ledger "Additions by chapter") with links rather than re-teaching; the one traced entry (€18,640) is labeled illustrative.
- **2026-10-28** — Rejected A2 posting for recurring accruals in the trade-offs (register ceiling and preventive-control audit expectation); recommended deterministic ERP templates first, then bounded batch approval.

## Sources

- **Internal**
  - [[agents-in-the-enterprise]], [[agent-identity-and-least-privilege]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]], [[durable-agent-execution]], [[task-state-and-checkpoints]], [[models-and-the-model-gateway]], [[domain-customer-operations]] — mechanisms and the consequence-profile frame.
  - Interview designs: `agentic-finance-platform` (steps `ledger`, `pipeline`, `maker-checker`, `idempotency`, `decision-record`, `exceptions`), `agentic-legal-platform` (`grounding`, `pipeline`, `citation-gate`, `attorney`), `agentic-hr-platform` (`hiring-gate`, capacity), via `_research/digest-back-office.md`.
- **External**
  - Mata v. Avianca (S.D.N.Y. 2023); Ayinde v. Haringey and Al-Haroun v. QNB, [2025] EWHC 1383 (Admin); Magesh et al. (arXiv 2405.20362, 2024) — legal hallucination evidence.
  - United States v. Heppner (S.D.N.Y. 2026), via McGuireWoods and Proskauer alerts; ABA Formal Opinion 512 (2024), via The Bar Examiner — privilege and confidentiality.
  - 15 U.S.C. 7262; SR 26-2 (2026) — finance controls and model risk.
  - Regulation (EU) 2024/1689 and 2026/1744; GDPR Art. 22; CJEU C-634/21 SCHUFA — employment and automated decisions.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: removed the 'illustrative date' label from the canonical 23 November 2027 audit committee; tied the Peoplepoint tool-change example to the November 2027 performance-summary request in [[domain-high-stakes-decisions]]. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
