---
status: accepted
revised: 2026-10-28
---

# Spec: Staged Rollout and Rollback

## Intent

Answer "how do you release a change to an agent safely, and what does rollback mean when actions and memories have already happened?" Give the reader a staged release process (offline gate → shadow → canary → ramp → full) in which every exposed stage has a pre-registered exit, a concurrent control and sticky assignment. Separate the two halves of rollback: a pointer move that stops new effects in minutes, and a **forward fix** that finds and repairs the effects the version already produced. Show, layer by layer, what rolling back a policy, prompt, model, tool contract, orchestration code, index or memory schema actually restores, and what preconditions (a served model, deployed workers, readable schemas) make the rollback target real. Use the Closewise model migration, forced by a provider retirement notice, as the worked example "done properly", including a canary defect the guardrails missed and its forward fix.

## Audience

Architects, platform leads and agent owners who ship new agent versions, including provider-forced model migrations, and risk owners who must sign the exposure. They know canary releases and feature flags from service engineering; they need the agent-specific parts: stateful stickiness, version-versus-tier separation, effects that outlive versions, and how to size a canary to what can be corrected.

## Success criteria

- [ ] Reader can name the five stages, what each measures and what each is blind to, and define canary (agent), rollback plan (agent) and forward fix.
- [ ] Reader can choose a rollout unit and assignment key (including nested cohorts) and explain why assignment must hold across runs that share state.
- [ ] Reader can design guardrails in four families with responses, and explain the stop/advance asymmetry (automation may roll back or hold; only a human advances).
- [ ] Reader can state, per layer, the precondition for a rollback and what it leaves behind, including the rollback target's expiry date and runs in flight.
- [ ] Reader can write a forward-fix playbook per effect class, with the effects query by manifest hash, and knows the rolled-back version never executes corrections.
- [ ] Reader can compute what a canary of a given size can detect, and why small regressions belong to the offline gate.
- [ ] Documented rollbacks (CrowdStrike 2024, OpenAI 2025, Anthropic 2025 and 2026) are dated and sourced, with the limit that none is a customer-side agent rollout.
- [ ] Ostrell numbers match the ledger (23 entities, ~1,900 entries/month, ~380 per close day, seven-working-day rule, suite v2 gate, Answerdesk profile B 5% canary in December 2027).

## Non-goals

- The manifest, alias drift and memory/state migration mechanics — [[versioning-agent-systems]].
- Suites, graders and the regression gate's statistics — [[building-agent-eval-suites]].
- Shadow mode's definition, promotion criteria, demotion triggers and the limited-autonomy tier canary — [[evidence-for-autonomy]].
- Compensation design and saga mechanics — [[partial-failure-and-compensation]]; workflow-code versioning — [[durable-agent-execution]].
- Ownership, on-call and the agent lifecycle — [[owning-agentic-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published study compares rollout strategies for LLM agents; the chapter states this and relies on release-engineering practice and vendor postmortems.
- None of the documented rollbacks is a customer-side agent rollout with external side effects; the "revert restores future behavior, not past output" lesson is the author's inference.
- Whether the CrowdStrike revert repaired already-affected hosts is not stated in the preliminary report; the chapter says only what the report says.
- Ostrell's Closewise migration ends in January 2028 as a plan; [[owning-agentic-systems]] may report the outcome.

## Decision log

- **2026-10-28** — Used "forward fix" for repairing effects, not for rolling the version forward; adopted Google CRE's "roll back first" for the version and listed the narrow exceptions.
- **2026-10-28** — Kept version canaries and tier canaries apart (re-gate the tier in shadow, then canary the version at fixed tiers), consistent with the D4 re-gating rule in [[evidence-for-autonomy]].
- **2026-10-28** — Made the Closewise example include a defect the harm guardrail could not see (approved misclassifications to a new account), so the forward-fix plan is exercised, not just described; exposure was nested (five entities, 50/50 by entry id).
- **2026-10-28** — Chose to hold the canary cohort through year-end rather than ramp or pause, with full rollout and a 5% holdback in January 2028 before the old model's retirement floor.

## Sources

- **Internal**
  - [[versioning-agent-systems]] — manifest, rollback by pointer, run stickiness, migration calendar and seven-working-day rule.
  - [[building-agent-eval-suites]] — suite v2 gate and its resolution; daily canary.
  - [[evidence-for-autonomy]] — shadow mode, demotion triggers, re-gating rule, the credit reversal drill.
  - [[task-state-and-checkpoints]], [[durable-agent-execution]], [[partial-failure-and-compensation]] — runs in flight and compensation.
- **Interview designs (design examples)**
  - `agentic-platform-foundations` step `eval-obs`; `agentic-legal-platform` step `workflows-eval`; `agentic-support-platform` step `compliance-eval`; `agentic-finance-platform` step `ledger`; `ai-coding-cli` step `cloud`; `agentic-healthcare-platform` step `eval`; `agentic-public-benefits-platform` step `rules`.
- **External**
  - Google SRE Workbook, "Canarying Releases" (2018); Hilton, "Reliable releases and rollbacks" (Google Cloud blog, 2017); Hodgson, "Feature Toggles" (2017); Argo Rollouts analysis docs.
  - CrowdStrike preliminary PIR (2024); OpenAI sycophancy rollback via Willison (2025); Anthropic postmortems (2025-09-17 and 2026-04-23); Replit coverage (The Register, 2025).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Closewise manifest labels prefixed per ruling 23 (`cw-2027.09.3`, `cw-2027.10.2`, `cw-2027.12.1`); Anthropic April 2026 postmortem quote and caching-bug description corrected against the source. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 4 regenerated without literal card counts (heap, folder, ledger reversal); alt text updated to match. *(AI-mediated session)*
