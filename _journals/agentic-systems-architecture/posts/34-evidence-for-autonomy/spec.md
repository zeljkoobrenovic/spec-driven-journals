---
status: accepted
revised: 2026-10-28
---

# Spec: From Evidence to Autonomy: Deployment Gates and Autonomy Decisions

## Intent

Close Part VIII by connecting evidence (evaluation, shadow runs, audited approvals, online metrics) to two decisions: whether a version ships at its current tiers (release decision) and whether an action class moves up or down a tier (autonomy decision). The reader leaves able to design autonomy as a runtime setting per action class bound to an exact agent version manifest, to write pre-registered promotion criteria with confidence bounds and expected-loss figures, to wire automatic demotion triggers and holds, and to run an autonomy review with named risk owners. The chapter must say plainly that no company has published evidence linking offline evals to production autonomy changes, so the mechanism is the author's judgement built from research, release engineering and regulatory analogies.

## Audience

Chief architects, platform leads and evaluation leads who own an agent platform and must answer a business owner's request to "let the agent do it without approval". Also risk owners (support, finance, legal) who must sign such a decision and want to know what they are signing.

## Success criteria

- [ ] Reader can distinguish a release decision from an autonomy decision and say who makes each.
- [ ] Reader can define deployment gate, promotion criterion, demotion trigger and shadow mode, and name the blind spot of each evidence generator (offline, shadow, suggestion, audited approval, limited autonomy).
- [ ] Reader can write a promotion criterion with metric, population, evidence source, confidence bound, minimum sample and implied expected loss, and explain why first-line approval rates are not valid evidence.
- [ ] Reader can apply the rule of three to judge whether a sample size supports a claimed failure rate.
- [ ] Reader can place the tier register, policy enforcement point, demotion monitor and evaluation service in an architecture where automation may lower but never raise autonomy.
- [ ] The Ostrell October 2027 review matches the ledger: credits ≤ €250 A1 → A2, quote drafting stays A1 (external-commitment cap), account briefs demoted A3 → A2 after the Stale Price Book.
- [ ] The chapter includes a failure-scenario table with detection, containment and recovery, trade-off tables, an Across Domains table and three mermaid diagrams.

## Non-goals

- Evaluation levels, pass^k and benchmark critique in depth ([[evaluating-agentic-systems]]).
- Building suites, graders and CI regression gates ([[building-agent-eval-suites]]).
- Trace design and operational metrics ([[agent-observability]]).
- Approval-gate UX and approver fatigue in depth ([[human-oversight-and-bounded-autonomy]]).
- Canary mechanics, rollout percentages and rollback plans ([[staged-rollout-and-rollback]]).
- The tier taxonomy and the consequence–reversibility grid ([[autonomy-and-consequence]]).
- Standing ownership and the agent registry lifecycle ([[owning-agentic-systems]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should re-gating a new manifest to an already-held tier ever be automatic for back-office classes, or only in customer operations? The chapter allows it for Answerdesk under criteria the risk owner signed in advance.
- Whether Feng et al.'s autonomy certificates or any regulator's equivalent are adopted by 2027; the chapter treats them as a proposal.
- The FDA PCCP details rely on a law-firm summary; check the FDA guidance text before a later edition quotes it.

## Decision log

- **2026-10-28** — Framed the chapter around two decision types (release vs autonomy) rather than one "promotion gate", because the interview designs conflate version promotion and tier promotion and the cost of error differs.
- **2026-10-28** — Adopted "automation may lower, only humans may raise" as the central asymmetry; rejected fully automatic promotion on criteria except for restoring a tier on a new manifest under pre-signed re-gating criteria.
- **2026-10-28** — Required independent audit (second reviewer) as the correctness label for A1 → A2, instead of approval rates, to turn the Rubber Stamp into the chapter's main lesson on circular evidence.
- **2026-10-28** — Added the Ostrell rule that an incident invalidating an evidence assumption demotes the class even without harm, to explain the canonical account-brief demotion.

## Sources

- **Internal**
  - [[autonomy-and-consequence]], [[versioning-agent-systems]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]], [[staged-rollout-and-rollback]] — tiers, manifests, approvals, enforcement and rollout this chapter builds on.
  - Interview designs (design examples): `agentic-platform-foundations` step `eval-obs` (promotion contract); `ai-coding-harness` steps `scale` and `drift`; `agentic-healthcare-platform` step 7 `eval`; `agentic-public-benefits-platform` step 7 `compliance-eval`.
  - `_research/brief-evaluation-observability.md` §6, `brief-foundations-autonomy.md` Parts 2, 4, 6, `brief-security-oversight.md` Part 5, `brief-performance-economics-evolution.md` §2.6.
- **External**
  - Feng, McDonald & Zhang, *Levels of Autonomy for AI Agents* (2025) — autonomy separate from capability; certificates renewed on change.
  - Yao et al., *τ-bench* (2024) — pass^k.
  - Anthropic, *Measuring agent autonomy* (2026) and *Quantifying infrastructure noise* (2026) — habit-driven autonomy; gate noise.
  - Zhu et al., *Agentic Benchmark Checklist* (2025) — grader flaws.
  - Hanley & Lippman-Hand (1983) — rule of three.
  - EU AI Act Art. 3(23) and 43(4); FDA PCCP final guidance (December 2024, via Ropes & Gray); Anthropic RSP; Google SRE Workbook canarying.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: credit limits per consistency ruling 21 (one credit per technician visit, one pending proposal per ticket); C5 names the 200-case gate sample of the 1,200-variant injection suite (ruling 26); heading "Pre-registration in June" matches the 28 June date; typo and internal "evaluation brief" wording fixed. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
