---
title: "Review of the AI Development Strategy by Claude"
date: 2026-05-14 17:30:00 +0100
author: by Željko Obrenović (obren.io)
permalink: strategy-review-claude
timetoread: 9 min
excerpt: "A focused Claude review of the AI development strategy after the second improvement pass. The strategy is much clearer and ready for controlled execution, but still needs evidence, owners, controls, and pilot artifacts before enterprise promotion."
icon: "assets/icons/review-claude.png"
---

> KEY POINTS:
> * The second improvement pass made the strategy substantially more readable. It now teaches agentic coding before asking readers to accept the operating model.
> * The strategy is ready for controlled execution, not final enterprise standardization.
> * Most remaining gaps are execution evidence: real baselines, real pilot artifacts, registry rows, tested controls, policy sign-off, and cost data.
> * Codex's updated review is the strongest execution gate. Gemini's multi-model framing is useful, but should remain a hypothesis to test.

## Review Method

This review reread the AI development strategy after the second improvement pass and compared it with the Codex and Gemini reviews. It focuses on what changed, what is now strong enough, and what still blocks promotion from pilot strategy to enterprise standard.

## Verdict

The strategy is now a credible Version 0.9.

It should be approved for controlled pilots with explicit evidence gates. It should not yet become mandatory enterprise policy because the operating model has not been proven in real repositories with real controls, owners, metrics, and cost data.

## What Is Now Strong

| Area | Why it works |
| --- | --- |
| Educational framing | The strategy explains agentic coding as a workflow, not as chatbot use. |
| Tooling decision | Claude Code is framed as the 2026 default, with review and migration-back paths. |
| Governance | The strategy now talks about hooks, permissions, registries, and audit trails instead of only principles. |
| Reusable knowledge | Skills, MCP servers, subagents, and templates are treated as assets that compound. |
| Human accountability | The policy keeps production decisions with accountable humans. |
| Roadmap | The plan is closer to implementation, with clearer sequencing and review points. |

The most important change is audience empathy. A reader who has not internalized agentic coding can now follow the logic.

## Remaining Gaps

The blockers are practical:

1. **Evidence baselines.** The strategy needs current measures for delivery, quality, modernization, cost, and review effort.
2. **Pilot artifacts.** The first pilots should publish prompts, Skills, diffs, test evidence, review notes, and lessons learned.
3. **Registry reality.** Skills, MCP servers, hooks, templates, approved tools, and exceptions need real entries with owners.
4. **Control validation.** Hooks, permission modes, audit trails, and CI checks must be tested, including failure cases.
5. **Policy sign-off.** Security, Legal, Data Protection, and engineering leadership need explicit approval boundaries.
6. **Cost model.** The strategy needs workflow-level cost tracking, not only license or token estimates.
7. **Visual support.** A few diagrams would help readers see the operating model and control flow.

None of these require a larger narrative. They require execution.

## Peer Review View

Codex's review is the strongest readiness gate because it converts concerns into an evidence backlog and a 30/60/90-day plan.

Gemini's review is most useful where it challenges the single-tool default. Its large-context and multi-model points are worth testing, but they should not change the default operating model without pilot evidence.

The reviews now agree on the core posture: controlled pilots first, enterprise standard later.

## What To Change Next

The next iteration should be smaller and more evidential:

* Add a compact decision index that links the strategy chapters and ADRs.
* Add pilot evidence pages instead of more explanatory prose.
* Add owner names and dates to roadmap items.
* Add a control-validation checklist with pass/fail evidence.
* Add a cost and capacity section grounded in pilot data.
* Make the six-month tooling review impossible to miss.

## Final Recommendation

Keep the strategy as the guiding document for pilots. Do not keep expanding it to answer every concern in prose.

The promotion criterion should be:

> The strategy becomes enterprise standard only after pilots show measurable value, controls work in practice, ownership is funded, and exceptions are manageable.
