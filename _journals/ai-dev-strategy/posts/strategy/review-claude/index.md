---
title: "Review of the AI Development Strategy by Claude"
date: 2026-05-14 17:30:00 +0100
author: by Željko Obrenović (obren.io)
permalink: strategy-review-claude
timetoread: 30 min
excerpt: "An updated review of the AI development strategy after a second improvement pass, plus a peer take on the Codex and Gemini reviews. Covers the educational scaffolding added in this round, the new ADRs, the model-routing and migration-back paths, and what still has to land before promotion to enterprise standard."
icon: "assets/icons/review-claude.png"
---

> KEY POINTS:
> * The strategy has clearly moved through a second improvement pass since my previous review. The shape is the same; the connective tissue is stronger. New scaffolding sections ("From Prompt to Workflow," "What Changes When Agents Can Act," "How Agentic Risk Differs from Chatbot Risk," "Why Agentic Coding Needs Specific Policy") make the document readable by engineers who have not yet internalised the agentic-coding mental model — a real audience for an enterprise strategy.
> * The five **ADR-style decision records** are now in the tooling chapter, the **model-routing table** and **migration-back path** are concrete, the **risk register** now has owner and effectiveness-signal columns, the **AI policy** carries a Status block, and the **standards** chapter ships a worked exception ADR. Most of the editorial gaps from the previous pass are closed.
> * All three reviews now agree on the verdict: **Version 0.9, approve for controlled execution, do not yet treat as final enterprise policy**. The Codex review has been substantially rewritten and is now the strongest of the three for an execution-readiness gate — its 30/60/90-day plan and its eight control-validation tests are the most actionable artefacts produced across the three reviews. The Gemini review has moved into a "meta-review" framing whose substantive insight (large-context reasoning) is still worth absorbing, but whose synthesis claim is partly self-flattery.
> * The remaining gap is now almost entirely **execution evidence**: populated baselines, real pilot artefacts, registry rows with real owners, tested hooks and audit trails, Security/Legal sign-off on the policy, and a few diagrams to support visual learners. None of these are document edits.
> * One small **rendering risk** I flag below: the worked exception ADR uses `## Status`, `## Context`, etc. inside a fenced code block. The block is correctly fenced and the renderer will treat those as code; but readers skimming raw markdown may briefly think the chapter has duplicate top-level sections. Not a defect — worth knowing.

## How this review was done

I re-read every post in `_journals/ai-dev-strategy/posts/strategy/` end-to-end on 2026-05-14, after a second improvement pass. I cross-referenced against my previous review (`review-claude` v1), the Codex review (`review-codex`), and the Gemini review (`review-gemini`). I sampled the build pipeline to confirm the new Mermaid blocks and ADRs render. I deliberately did not re-litigate ground that is settled in the strategy; this review reports what changed, what works, what is still missing, and where I disagree with the peer reviews.

## What changed since the last pass

Comparing the strategy I reviewed last time with what is in the tree now, the biggest delta is **educational scaffolding**. The strategy has stopped assuming the reader knows what agentic coding is. Every major chapter now opens with a section that maps an agentic-coding idea onto a familiar engineering idea before continuing.

| Chapter | New scaffolding section | What it does |
| --- | --- | --- |
| Introduction | KEY POINTS expanded to flag the **chat/autocomplete → governed engineering workflow** shift | Sets the frame on page one |
| Strategic Principles | **From Prompt to Workflow** ladder (Prompt → Repeatable prompt → Agentic workflow) | Tells the reader why the document is platform-engineering shaped |
| Tooling Decision | **What choosing a default means** and **Tool concepts across Claude Code and Codex** tables | Stops two common misreadings ("it's a ban" and "this is unique to Claude Code") |
| Enablement | **The Enablement Stack as a System** — maps each primitive to a familiar engineering concept | The single best on-ramp for a reader who has not seen `CLAUDE.md`/Skills/MCP before |
| Target Engineering Model | **Platform readiness checklist** | Tells the platform team what it must own before agentic workflows scale |
| Use-Case Portfolio | **Workflow metrics** and **What is not yet allowed** | Calibrates what success looks like and where the leash stays short |
| Operating Model | **What Changes When Agents Can Act** | Names the old/new operating-model deltas explicitly |
| Roadmap | **How to Read the Roadmap** + **Example: how a workflow matures** | Anchors the five gates in a real workflow |
| AI Policy | **Status** block + **Why Agentic Coding Needs Specific Policy** | Marks the policy as draft pending sign-off and explains why a generic AI policy is insufficient |
| Standards | **Worked exception ADR** for a Lambda-vs-ECS exception | Turns the exception path from theoretical to copy-pasteable |
| Risks | **How Agentic Risk Differs from Chatbot Risk** + **Owner and Effectiveness signal** columns | Reframes risk for the agentic case and makes the register operational |
| Engineering Standards | **Maturity levels** unchanged but now anchored by the worked ADR | Standards-as-code is now a fully closed loop |

In total this is the kind of edit that **moves the document from "specialists only" to "publishable to engineering leadership."** That is a non-trivial improvement.

The other substantial changes since my last review:

* The five **Strategic Decision Records** (ADR-AI-001 through 005) are now in the tooling-decision chapter and are short, structured, and reviewable.
* The **model-routing table** is concrete: PR review and self-service knowledge → Haiku; template generation and characterization tests → Sonnet; modernization-dossier composition and extraction planning → Opus. This is the level of specificity Codex flagged as missing.
* The **migration-back path** is operationalised in six numbered steps with a realistic time estimate ("two to three months of platform-team time").
* The **risk register** has owner and effectiveness-signal columns for every row; residual risk acceptance now has a named acceptor (Engineering leadership) and a cadence.
* The **AI policy** has a Status block calling itself v0.9 pending Security/Legal/Procurement sign-off — the right honesty for a draft.
* The **Operating model** has anti-pattern detection signals, backlog cadence, and an explicit funding-model recommendation.
* The **Roadmap** has dependency columns, pilot exit criteria, and the November 2026 tooling review as a named Phase 2 milestone.

This is a thorough close-out of the previous review backlog. The strategy is meaningfully stronger.

## What I still think is right

The core strategic moves are unchanged and continue to hold up:

1. **AI as modernization accelerator, not productivity tool.** This is still the single most important framing in the document. It survives every chapter and is now reinforced in the new scaffolding sections.
2. **Standardize the surface, keep knowledge portable.** The "Skills as durable knowledge, plugins as packaging" principle (now ADR-AI-003) is the right hedge against vendor lock-in without giving up the benefit of a default.
3. **MCP for theirs, Skills for ours.** ADR-AI-004 codifies what is now repeated in three chapters with consistent decision criteria. Good.
4. **Five rollout gates with explicit "what is not yet allowed" boundaries.** The Phase-1 leash (no auto-merge, no edits to stored procs without tests, no agent-authored event contracts) is well-calibrated.
5. **Standards-as-code with maturity levels.** Draft / Recommended / Default / Required / Deprecated is the right granularity, and the worked exception ADR proves the path is real.
6. **Risk register that treats agentic risk as a different class.** "How Agentic Risk Differs from Chatbot Risk" is the right re-frame. The owner + effectiveness signal columns make it operable.

## Where I would still push back

These are the sharp edges I would still raise in an internal review.

### 1. The strategy is now long enough to need a per-chapter table of contents

Several chapters cross 250 lines. The introduction, the enablement chapter, the tooling chapter, the landscape chapter, and the operating-model chapter all have enough sub-sections that a reader who skims will miss material. The journal renderer treats `##` and `###` as sectioning but does not generate a per-page table of contents. For documents of this length, that omission shows.

Two cheap options:

* Add a short *"In this chapter"* list of links to the major `##` headings at the top of each chapter that exceeds ~200 lines.
* Or render a simple sidebar TOC from the post's headings client-side in `_templates/post.html`. This is a one-time platform change, not a content edit, and it would help every long chapter equally.

### 2. The worked exception ADR in the standards chapter has a rendering footgun

The worked ADR is inside a fenced code block, which is correct, but the `## Status`, `## Context`, `## Decision`, etc. headings inside the block are visible to `grep` as if they were chapter headings. The rendered output is fine — they are styled as code. But:

* A search query like "Decision" in the index page may match the in-fence text and surface the standards chapter when the reader expected a real Decision section.
* An author skimming raw outline tooling (`grep '^##'`) will see ghost sections.

Two small fixes available: (a) indent the ADR with four spaces instead of a code fence so the headings cannot be confused; or (b) keep the fence and demote the inner headings to `**Status**`, `**Context**`, etc. without `##`. I lean toward (b) — it preserves the readable look and removes the ambiguity.

### 3. "What is not yet allowed" is great, but should be referenced from the roadmap and the policy

The Phase-1 leash is currently only in the use-case portfolio. The same list should be cross-linked from:

* the Roadmap, where Phase 1 already promises that "high-risk modernization work should stay mostly in Gates 1-3" — the explicit "not yet allowed" list is the operational version of that promise;
* the AI Policy, where the "Code and review" rules list the headline restrictions but not the operational rollout-phase nuances.

A one-line link from each is enough; the list itself stays where it is.

### 4. Hierarchical context is half-adopted

Gemini's review presses on this and is partly right (more in my opinion on that review below). The strategy now has the three-layer context model (Organization / Project / User), but it does not yet acknowledge that for large monorepos, the right pattern is **nested project context** — a `CLAUDE.md` at the repo root *plus* per-domain `CLAUDE.md` files for major subtrees. The Skill scope/promotion table covers this for Skills (Project / Domain / Org) but the equivalent for context files is implicit.

The fix is small: add one paragraph to the enablement chapter saying that for large repositories the project layer itself can be hierarchical, with examples of when that helps (multiple bounded contexts in one repo, vendored subtrees, generated code areas). This costs nothing and addresses Gemini's substantive point without adopting its conclusion.

### 5. The ADRs should have a stable home with sequential numbers

ADR-AI-001 through 005 currently live in the tooling-decision chapter. That is a reasonable starting position, but two issues will emerge:

* The journal's separate `_journals/decisions-log` already has its own numbering scheme (the existing decision log uses sequential numbers like ADR-0042 in examples). If the AI ADRs become enterprise records, they need to be reconciled with that scheme.
* Future ADRs (sixth, seventh, eighth) will not fit naturally inside the tooling chapter.

Recommendation: keep the ADRs inline for now, but plan to move them to `_journals/decisions-log` under a clear scheme (`AI-001`, `AI-002`, …) when the strategy gets formally approved. The chapter retains a short summary table that links to each.

### 6. Cost: the routing table is good; the budgeting is still abstract

The model-routing table is the right level of specificity for *which model* runs *which workflow*. What is still abstract is the **budget envelope** and the **alert path** for runaway sessions. Two concrete additions that would close this:

* A budget guardrail per workflow class (an order-of-magnitude monthly limit, even if the number is wrong on day one).
* A response playbook for cost alerts: who gets paged, who has the authority to pause an MCP server or downgrade a subagent, what the rollback looks like.

The risks chapter names cost runaway as an incident type; the operating model lists monthly cost review; the missing piece is the **what-runs-when-it-blows-up** detail.

### 7. The narrative arc is now strong; the visual arc is still thin

The Mermaid 4-layer engineering-model diagram and the 5-gate rollout diagram have landed and they help. There is still room for one more diagram: a single picture of **how the primitives compose in one session** (CLAUDE.md → Skill → MCP → subagent → hooks → output contract). The enablement chapter has the step-by-step table for the Kafka producer review, which is good prose — a diagram of the same flow would let executives see the system at a glance.

This is a polish item, not a blocker.

### 8. Pilot evidence is still the load-bearing missing element

Every editorial improvement still serves a strategy that has not yet run a pilot. The next iteration is not another scaffolding pass; it is real artefacts from the first three pilots. I would resist any temptation to keep editing.

## Opinion on the Codex review (updated)

The Codex review has been substantially rewritten. The earlier version was the structural-gap audit that did the heavy lifting between draft and Version 0.9; the current version is a much sharper **execution-readiness review** of the strategy in its current state. It is now the longest of the three reviews and, in my judgement, the one most useful to a decision-maker who has to choose between "approve for pilots" and "approve as enterprise standard."

### Where the new Codex review is strong

* **It is now a proper companion to the strategy, not a backlog of fixes.** The structure — Overall Assessment, Method, Executive Verdict, What Improved, Highest-Priority Remaining Gaps, Assessment by Strategy Area — mirrors the strategy itself and lets a reader cross-check chapter by chapter. The traffic-light verdict table is calibrated correctly.
* **The "P0 gaps" list is the right list.** Real baselines, three pilots with evidence, real registry rows, tested controls, and funded named owners are exactly the load-bearing missing pieces. The list is short enough to be actionable and concrete enough to be falsifiable.
* **The "make controls actually run" item is the most operationally useful single recommendation in any of the three reviews.** Eight specific control-validation tests (secret-scan blocks known secrets, audit hook writes to the central store, unapproved MCP servers are rejected, write-capable MCP requires workflow approval, AI-assisted PRs include traceability, CI rejects missing tests for business-critical generated changes, prompt-injection fixtures are included in subagent evaluation, incident handling preserves session logs) — this is what "governance as configuration" needs to mean in practice.
* **The recommendation to keep the November 2026 tooling review non-negotiable, with a fixed evidence pack, closes a real gap.** Without the evidence pack defined in advance, the six-month cadence becomes a meeting about preferences.
* **The 30/60/90-day plan is concrete and well-sequenced.** Naming the lead, picking pilots, populating baselines, and creating first registry rows in the first 30 days; producing the first dossier/scorecard/complexity report in 60 days; moving low-risk workflows to Gate 3 and running a controlled large-context comparison in 90 days. This is what a working pilot plan looks like.
* **The recommendation to add a compact decision index** is small but high-leverage. It addresses the same problem I raised about long chapters needing better navigation.

### Where I would push back on the new Codex review

* **The Codex review's own length is now becoming a risk.** At ~22 minutes reading time it is approaching the size of two or three strategy chapters, and the review's own warning — "the document can look complete before the operating system behind it exists" — applies recursively to long reviews. The strongest parts (P0 gaps, validation tests, 30/60/90 plan) would survive being half the length.
* **"Pending validation" is doing too much work in the executive verdict.** Eight of the fourteen rows are Green or Green/Amber, but the policy, operating-model, and operating-readiness rows are Amber largely because of signatures, names, and funding that no review can produce. The verdict table risks suggesting that the strategy is one rewrite away from Green when in fact it is one organisational decision away — a different blocker.
* **Codex now hedges on rechecking dated sources.** The status note says "I did not re-verify external vendor documentation during this pass." That is honest, but it means the dated-comparison principle the review itself champions cannot be enforced from inside the review. The November 2026 review will need fresh source-checking.
* **The Codex review's opinion of its peers is a little asymmetric.** It marks the Claude review as "stronger of the two" while also noting that some of the Claude review's findings are now stale — fair. But it treats the Gemini review as a *useful counterweight* without weighing the Gemini review's specific weaknesses (advocacy framing, dated window claim, over-engineered tiering pattern). I think Codex is right that Gemini's large-context point is worth taking seriously; it is less explicit about which parts of the Gemini review to discount.

### Net view

The Codex review is now **the right document to send to engineering leadership** with the strategy itself. It is the most aligned with the strategy's current shape, the clearest on what still has to land, and the most useful for the 30/60/90-day phase. Its older self was an editorial audit; its current self is an execution-readiness gate. Both versions did the right work for the moment they were written in.

## Opinion on the Gemini review (updated)

The Gemini review has changed mode. The earlier version was a tool-perspective review with one substantive insight (large-context reasoning) wrapped in advocacy. The current version is presented as a **"meta-review"** that critiques the other two reviews and offers a synthesis. The mode change is worth noting because it changes how the review should be used.

### What the new Gemini review gets right

* **The summary characterisations of Codex and Claude are accurate.** "Codex's focus is on Strategic Rigor and Readiness" and "Claude's focus is on Operational Fidelity and Workflow Composition" are fair short reads of what each review actually does. A reader skimming all three will arrive at the same impression.
* **The agentic-tiering frame remains the substantive contribution.** Even after the strategy added the model-routing table, Gemini's "Research → Plan → Act → Validate" framing is still a useful pedagogical lens. Different model strengths fit different phases of the loop, and naming the phases in those terms gives architects a vocabulary that the model-routing table alone does not provide.
* **The serverless cost-complexity scorecard idea is a small, concrete addition** that the strategy could absorb without restructuring. Combining AWS billing data with CloudWatch logs to rank Lambda functions by expense-and-complexity is the kind of evidence-based scorecard the Node landscape currently lacks.
* **The recommendation to seed the registries with the first five Skills as part of Phase 1** lines up exactly with Codex's P0 ask and with my own backlog. Three reviews now converge on this.

### Where I would still push back on the new Gemini review

* **The "meta-review" framing tilts the balance.** A review that critiques other reviews and offers itself as the synthesis is making a stronger claim than it earns. The Codex and Claude reviews are not just complementary lenses; they cover material that the Gemini review skips (e.g., Codex on funding and named owners, Claude on the ADR-in-code-block rendering footgun, both on the Phase-1 leash). Treating the three as equal partners in a synthesis under-represents the asymmetry.
* **The "highly self-referential regarding the tool choice" critique of the Claude review is partly fair, partly not.** It is true that my earlier review spent fewer words on the .NET large-context case than the Gemini view would have liked. It is also true that the strategy's exception process and now-concrete model-routing table already cover the practical case the Gemini review names. A fair critique would weigh that.
* **The "Codex prioritises registries and ADRs over technical reasoning" reading is not quite right.** Codex's emphasis on registries is precisely because the technical reasoning of agentic modernization fails when the agent's tools, context, and outputs are not governed. Calling that "the lens of a Policy Officer" misreads what registries do in this strategy.
* **The advocacy framing has receded but not disappeared.** The "Multi-Model Perspective" framing is more even-handed than the earlier version, but the conclusion still routes Research to Gemini, Execution to Claude, and Validation to "Codex/Specialized Models" — which is exactly the recommendation a Gemini-authored review would make. The same insight could be expressed tool-neutrally (e.g., "large-context analysis tier" and "agentic-loop tier") without naming preferred vendors.
* **The context-window argument is, as I noted before, decaying.** The current review still leans on it. By the November 2026 strategy review, this argument may need to be re-anchored to whatever the then-current window sizes and caching behaviours are.

### Net view

The Gemini review's substantive contribution remains the **agentic-tiering / large-context** observation, and the controlled large-context pilot in the .NET estate is the right way to test it. The meta-review framing is mostly self-flattery; read past it and the underlying argument is worth one experiment, not a structural change to the tooling decision. The serverless cost-complexity scorecard idea is a useful small addition the strategy could absorb.

## Where the three reviews agree

* Verdict is **Version 0.9, approve for controlled execution, do not yet finalize as enterprise policy**.
* The thesis (AI as modernization accelerator) is right and well-defended.
* The enablement stack (Skills, MCP, subagents, hooks, registries) is the most operationally distinct part of the strategy.
* Pilots are the missing evidence layer.
* Registries must be **populated**, not just specified.
* The Claude Code default is defensible for 2026, with a real six-month review.
* A controlled large-context pilot for the .NET monolith is worth running.

## Where they differ now

| Question | Codex (updated) | Gemini (updated) | Claude (this review) |
| --- | --- | --- | --- |
| Mode of review | Execution-readiness gate with 30/60/90-day plan | Meta-review and strategic synthesis | Peer review and critique of the other reviews |
| Biggest remaining gap | Baselines, pilots, registry rows, hook validation, named owners, sign-off | Multi-model orchestration not yet operationalised | Execution evidence; a few lingering presentation issues (ADR-in-code-block, long-chapter TOC, visual arc) |
| View on tooling default | Pragmatic default; six-month review must be evidence-based | Default is right today but the org should "adopt multi-model orchestration" | Default is right; the existing exception process and model-routing table already handle multi-model cases; promote routing rules based on pilot evidence |
| Sharpest agentic-specific risk called out | Untested controls and "paper maturity" — the document running ahead of the operating system | Instruction entropy / context drift across `CLAUDE.md`, Skills, subagents, hooks | Confidence-laundering: an agent that cites sources can still be wrong, and the evidence rule must be enforceable, not aspirational |
| Recommended next concrete artefact | The 30/60/90-day plan: name the lead, pick pilots, populate baselines, create first registry rows, test hooks | A `governance-linter` and a serverless cost-complexity scorecard | Pilot evidence from the .NET stored-proc and Java/Kafka pilots, ADR migration to `_journals/decisions-log`, and the eight backlog items below |
| Opinion on the other reviews | Claude review is the strongest enterprise-readiness review; Gemini review is useful as a counterweight but should be treated as a hypothesis | Claude review is brilliant on workflow composition but self-referential on tool choice; Codex review prioritises registries over technical reasoning | Codex review is now the right companion document for leadership; Gemini's substantive insight is large-context, not the meta-review framing |

## Updated executive verdict

| Dimension | Rating (this pass) | Δ from previous pass |
| --- | --- | --- |
| Strategic thesis | Green | unchanged |
| Landscape grounding | Green | unchanged |
| Target architecture | Green / Amber | upgraded — platform-readiness checklist landed |
| Tooling decision | Green | upgraded — model routing, migration-back path, "what choosing a default means," and Tool-concepts table all landed |
| Enablement stack | Green / Amber | upgraded — "Enablement Stack as a System" map plus Subagent-vs-Skill table close the conceptual gap |
| Workflow portfolio | Green / Amber | upgraded — workflow metrics and "what is not yet allowed" landed |
| Landscape strategies | Green / Amber | upgraded — data migration discipline, TFS-to-Git mechanics, Kafka end-to-end example, CI before/after sketch all landed |
| Operating model | Green / Amber | upgraded — anti-pattern detection signals, backlog cadence, funding-model recommendation landed |
| Roadmap | Green / Amber | upgraded — dependency columns, pilot exit criteria, November 2026 milestone landed |
| AI policy | Amber | unchanged content-wise but now carries a Status block; sign-off still pending |
| Engineering standards | Green | upgraded — worked exception ADR landed |
| Risks and mitigations | Green | upgraded — owner and signal columns, agentic-vs-chatbot framing landed |
| Appendices | Green / Amber | upgraded — duplicated material removed, appendices now reference-only |
| Presentation and narrative | Green / Amber | upgraded — educational scaffolding throughout; visual arc still slightly under-served |
| Publication readiness | Green / Amber | upgraded — one rendering footgun (ADR-in-code-block), no other blockers I can see |

Overall: **the strategy is now publication-ready as Version 0.9**. The remaining steps are execution, not editing.

## Concrete next-iteration backlog

In priority order, none of these are document edits except the last two:

1. **Run Pilot 1 and Pilot 2** to first artefact each. The .NET capability map and the Java service scorecard are the two highest-leverage proofs.
2. **Populate the baseline** with measured values for the pilot domains. The columns are right; the rows are still placeholders.
3. **Stand up one worked row in each registry** (MCP, Skill, subagent, hook), with a real owner and a real review date.
4. **Get the AI policy approved** by Security, Legal, and Procurement and record the approval in the Status block.
5. **Run the secret-scan and license-check hooks** against a known-secret/known-violation fixture and publish the result.
6. **Add the cross-links from "What is not yet allowed"** into the Roadmap and AI Policy chapters.
7. **Demote the ADR-in-code-block headings** in the standards chapter to bold lines to remove the rendering footgun.
8. **Fold the large-context observation from the Gemini review** into the enablement chapter as a one-paragraph nuance, not as a tooling pivot.

After these eight, the strategy should be in shape to move from Version 0.9 to Version 1.0.

## Final word

The strategy has done something rare for an enterprise AI document at this length: it has stayed sharp about its own thesis through multiple revision passes. The thesis — *AI as a governed accelerator for a specific modernization target* — is now reinforced by an enablement stack readers can build, a tooling decision they can defend, a risk register they can operate, and a roadmap they can sequence. The peer reviews from Codex and Gemini have each contributed: Codex on editorial discipline, Gemini on the multi-model question. Neither contradicts the strategy as written.

What remains is the part that is hardest to write into a document: **the operating system behind the strategy has to be built**. The next review of this strategy should be written *after* the first pilot dossier exists.
