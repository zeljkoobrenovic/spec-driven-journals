---
status: accepted
revised: 2026-10-28
---

# Spec: Autonomy, Reversibility and the Cost of Being Wrong

## Intent

Give the reader a way to set an agentic system's boundaries by consequence, reversibility, duration and uncertainty, attached to **action classes** rather than to agents. The reader leaves able to classify any tool call by effect type (read, draft, reversible write, compensable write, irreversible write, external commitment), place it on a consequence–reversibility grid that sets a **tier ceiling** no evidence can lift, size its **blast radius** per action, per run and per detection window, and treat the model's self-reported confidence as a signal that may lower a tier but never raise it. The chapter owns autonomy tier, action class, the consequence–reversibility grid and blast radius (agent), and sets up the evidence machinery of [[evidence-for-autonomy]] without re-teaching it.

## Audience

Chief architects, platform leads and risk owners deciding what an agent may do without a person, and senior engineers registering tools on an agent platform. They know sagas, idempotency and access control; they need a defensible, enforceable scheme for "how much autonomy" that survives a design review and an incident review.

## Success criteria

- [ ] Reader can define autonomy tier (A0–A3 by the human's role and what the system must provide) and explain why tiers attach to action classes, not agents.
- [ ] Reader can classify an action into one of six effect types and explain why compensable is not reversible, why reversibility depends on context and time window, and why workspace undo is not world undo.
- [ ] Reader can use the consequence–reversibility grid to read a ceiling, distinguish ceiling from tier, and name the two levers (limits lower consequence; staging raises reversibility).
- [ ] Reader can compute a per-detection-window blast radius (per-action bound × rate × time to detect, capped by aggregate limits) for an A2 class.
- [ ] Reader can state what calibration research measured and why self-confidence may only lower a tier.
- [ ] The Ostrell tier register agrees with the ledger: tiers, the A1 cap on irreversible external commitments, the October 2027 credit promotion and account-brief demotion, and ch. 34's credit volumes and hold thresholds.
- [ ] The chapter has two mermaid diagrams, a requirements table, a failure table with detection, containment and recovery, trade-off tables and a short Across Domains section.

## Non-goals

- Promotion criteria, demotion triggers, shadow mode and autonomy reviews ([[evidence-for-autonomy]]).
- Approval-card design, approver metrics and oversight modes in depth ([[human-oversight-and-bounded-autonomy]]).
- Bounded loops, budgets and stop conditions ([[workflows-loops-and-autonomous-agents]]).
- Compensation mechanics and sagas ([[partial-failure-and-compensation]]); idempotency ([[retries-idempotency-and-concurrency]]).
- Locus of control and Mitchell's ladder ([[what-makes-a-system-agentic]]); the decision ladder ([[when-agents-are-justified]]).
- Threat modeling and the trifecta beyond a pointer ([[agent-threat-model]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should Ostrell's C1-irreversible cell stay at A3 (with a rate limit), or drop to A2 so that irreversibility always costs something? The chapter keeps A3 and leans on aggregate limits.
- The blast-radius formula is the author's heuristic; a later edition could cite a published risk-exposure model if one fits agents.
- Calibration evidence is for question answering; revisit if studies of action-level calibration in agents appear.

## Decision log

- **2026-10-28** — Defined tiers by the human's role (after Feng et al.) and attached them to action classes (after Parasuraman et al. and per-tool risk ratings), rather than adopting any single published level scale; rejected the SAE analogy as a template and kept only the operational-design-domain idea.
- **2026-10-28** — Made the grid set **ceilings** and left tiers to evidence, so this chapter and [[evidence-for-autonomy]] split cleanly; departed explicitly from vendor guidance that oversight lasts only "until confidence … grows".
- **2026-10-28** — Separated compensable from reversible, adopting the support design's three-class rule while rejecting its filing of small refunds as compensatable; classified replies as content-constrained representations after *Moffatt v. Air Canada*.
- **2026-10-28** — Adopted "uncertainty signals only lower" from the support and healthcare interview designs; presented the Kadavath / Xiong / Tian disagreement rather than choosing a winner.

## Sources

- **Internal**
  - [[what-makes-a-system-agentic]], [[when-agents-are-justified]], [[evidence-for-autonomy]], [[human-oversight-and-bounded-autonomy]], [[retries-idempotency-and-concurrency]] — neighbouring concepts and the canonical credit numbers.
  - Interview designs (design examples): `agentic-support-platform` steps `action-gate`, `txn-safety`; `agentic-finance-platform` steps `naive`, `ledger`; `agentic-healthcare-platform` steps 3 `calibration`, 5 `gate`; `agentic-public-benefits-platform` step 4 `gate`; `ai-coding-cli` step `safety`.
- **External**
  - Parasuraman, Sheridan and Wickens (2000); Feng, McDonald and Zhang (2025); Mitchell et al. (2025) — autonomy scales.
  - Kadavath et al. (2022); Xiong et al. (ICLR 2024); Tian et al. (EMNLP 2023) — confidence calibration.
  - Bainbridge (1983); Parasuraman and Manzey (2010); Goddard et al. (2012) — ironies of automation, automation bias.
  - OpenAI, *A practical guide to building agents* (2025) — tool risk ratings; Anthropic autonomy study (2026) — irreversible share, involvement by complexity.
  - Replit (2025), DataTalks.Club (2026), PocketOS (2026) incident reports; *Moffatt v. Air Canada* (2024).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: credit limits aligned to ruling 21 (one credit per technician visit, one pending proposal per ticket); turn vs exchange in the requirements table (ruling 19); cut repeated compounding/METR/Ord and TheAgentCompany material in favor of links; corrected the DataTalks.Club aftermath to the reported change (no Terraform commands by the agent). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
