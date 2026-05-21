---
id: "ORG-PRIN-AI-OUTPUT-MUST-BE-GOVERNED"
status: draft:gray
title: "Practice Principle: AI Output Must Be Governed"
date: 2026-05-16
author: Organization Tech Strategy
permalink: ai-output-must-be-governed
timetoread: 12 min
excerpt: "AI-generated code, configuration, and documentation at Organization is treated as draft input. Human accountability does not move. Every AI change flows through the same engineering standards, reviews, tests, observability, and security gates as human work, plus AI-specific controls: scoped permission modes, hooks, secrets handling, approved tool registries, and audit trails. The principle is simple: AI accelerates engineering work; it does not relax engineering governance."
tags: practices, ai, claude-code, governance, policy, accountability, security
logo: "assets/images/ai-output-must-be-governed/logo.jpeg"
logo_credit: "Inspired by Organization's AI policy and AI engineering standards"
icon: "assets/icons/ai-output-must-be-governed.png"
---

> **Status**: DRAFT
>
> **Principle**: AI-generated output - code, infrastructure, configuration, documentation, automation - is **draft input**, not authoritative work. It is reviewed, tested, and accepted by a named human accountable for the change. AI agents operate inside scoped permissions, with explicit hooks, approved tool registries, secrets handling, and audit trails. The acceleration AI provides is real; the engineering bar AI must clear is not lowered.

## Statement

At Organization:

* **Human accountability for AI-generated changes is non-negotiable.** A named human reviews, approves, and owns the result.
* **AI output goes through the same engineering gates as human output.** Tests, CI checks, security scans, observability, code review, ADRs.
* **AI agents have scoped capabilities.** Permission modes, hook scripts, allowlists for commands, MCP servers, subagents, and tool registries.
* **Sensitive data is classified before AI access.** What may be sent to a model is a policy decision, not a developer decision.
* **Audit trails exist.** Who used which agent, with which tools, on which repository, generating which changes, approved by whom.
* **Default agent is Claude Code**; other agents only by exception.

The principle integrates AI into Organization's existing governance rather than carving out a separate, lighter regime for it.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| AI output is draft input. | AI output is untrustworthy. |
| Humans approve and own changes. | Humans must hand-write every line. |
| AI agents run in scoped modes. | AI agents are tightly caged. |
| Engineering gates apply equally to AI. | AI gets an extra, harsher gate. |
| Audit trails are kept. | All AI use is surveilled. |

The principle aims to make AI a normal, governed development tool. It rejects both "AI is special and must be banned" and "AI is special and gets to skip the rules".

## How to Apply This Principle

Use this principle to:

* Explain why AI output is draft input, even when it looks correct.
* Review AI-generated changes with the same accountability as human-written changes.
* Identify the extra governance surfaces created by agents, Skills, MCP servers, hooks, and prompts.
* Recognise unsafe AI usage patterns before they become incidents.

## Rationale

AI-assisted development has two failure modes Organization needs to avoid simultaneously.

The first is **rejection**. If governance is too heavy or too theatrical, teams will either avoid AI tooling entirely or work around it informally. Organization loses the acceleration without gaining safety.

The second is **dilution**. If AI tools bypass normal gates - because they "feel fast", because reviewers trust the model, because permission modes are too permissive - the engineering bar drops invisibly. Reviewers approve more code than they understand. Tests are written by the same model that wrote the code they cover. Security scans run on output nobody fully read. Drift accumulates faster than humans can catch.

The principle threads between these failures by:

* Keeping accountability with humans, where it has always been.
* Treating AI as a powerful, governed development tool, not a peer engineer.
* Encoding controls in the *agent* (permission modes, hooks, registries) rather than in policy alone.
* Demanding the same observability and audit posture for AI-driven work as for human-driven work.

The AI strategy and AI policy decisions implement this principle as concrete controls. The principle generalises those controls into a stable expectation.

## Implications

* **A named human approves every AI-driven change.** Approval is meaningful: the reviewer has read and understood the change.
* **AI-generated code passes the standard CI gates.** Tests, linting, security scans, observability templates - all apply.
* **Claude Code runs with explicit settings.** Permission modes, hook scripts, allowlists, and CLAUDE.md fragments are configured per project.
* **MCP servers, Skills, and subagents are registered.** Capabilities outside the default set are added by request and reviewed.
* **Data classification rules are clear.** What can be sent to which model, in which mode, is a policy decision with an ADR.
* **Audit trails are real.** Tool usage, approvals, exceptions, incidents.
* **Exceptions to the default agent are recorded.** Codex, Gemini, or other agents may be used when justified, by ADR.
* **Incidents involving AI are handled like any other incident.** Same retrospective process, same lessons-learned discipline.

## Review Checklist

Before accepting AI-generated work, the accountable human should be able to answer yes to these questions:

* Do I understand the change well enough to explain it without mentioning the AI tool?
* Did the change pass the same tests, scans, and review expectations as human-written work?
* Are secrets, customer data, and internal-only context handled according to policy?
* Are the AI tools, MCP servers, Skills, and subagents used in the session approved for this repository?
* Did the agent stay inside the expected permission mode and command scope?
* Is there enough audit trail to reconstruct what happened if this change causes an incident?
* Have I checked that generated tests are testing behaviour, not simply mirroring generated implementation?

If the answer to any of these is unclear, the work is still draft input. The right response is not to ban the tool; it is to finish the engineering review.

## What This Means for Teams

For service teams:

* Read AI-generated changes as carefully as you would read a colleague's PR. Approval is a load-bearing act.
* Use Claude Code with the standard settings and CLAUDE.md fragments.
* Treat suspicious behaviour - hallucinated APIs, secrets pasted into prompts, unexpected tool use - as an incident, not a quirk.
* Add tests; do not let the model both write and test the same change without human eyes.

For platform and AI Engineering Enablement roles:

* Maintain the default agent settings, permission modes, hooks, Skills, MCP allowlists, and CLAUDE.md fragments.
* Run the six-month review on AI tooling.
* Track adoption, usage patterns, exceptions, and incidents.

For security and compliance roles:

* Classify data ahead of AI usage; do not leave classification to the moment of the prompt.
* Define what counts as a reportable AI incident.
* Audit the audit trails periodically.

For tech leads:

* Watch for "AI made me do it" patterns in PR reviews. The model proposes; the human disposes.
* Block changes that bypass the AI controls; route them through the exception process.

## Anti-Patterns

* **Approval without reading.** Reviewers rubber-stamping AI PRs because "it's just AI".
* **YOLO mode in production repos.** Permission modes that grant the agent broad write access without hooks or approvals.
* **AI-written tests for AI-written code.** No independent human verification of either side.
* **Tool sprawl.** MCP servers, subagents, and Skills proliferating without registration or review.
* **Secrets in prompts.** Pasting `.env` content or credentials into an AI session.
* **Bypass via personal accounts.** Engineers using personal AI accounts on company code to "avoid the rules".
* **Shadow agents.** Use of non-default AI tools without an exception ADR.
* **Audit blackout.** No record of which AI did what, in which repository, with which permissions.

## Examples

Aligned with the principle:

* A developer uses Claude Code to refactor a service. The change goes through CI, security scans, code review, and is approved by a named human.
* MCP servers and Skills used by the team are listed in the registry with owners.
* A data classification rule prevents production customer data being sent to a model.
* A six-month AI tooling review evaluates incidents, satisfaction, and effectiveness, with outcomes recorded as an ADR.

Out of alignment with the principle:

* A PR approved with a single "looks fine - generated by Claude" comment.
* Claude Code running with no settings file, no hooks, and no CLAUDE.md.
* A Skill written by one engineer being used across the org with no registration or ownership.
* AI agents wired into production deployment paths without explicit approval gates.

## Discussion Prompts

Use these prompts in onboarding or team retrospectives:

* What would make us confident that an AI-generated change was understood by a human?
* Which AI controls are currently encoded, and which still depend on memory or policy text?
* Where could AI speed tempt us to skip evidence, review, or ownership?

## Related Principles

* [[governance-as-code]] - AI controls are themselves encoded as settings, hooks, and registries.
* [[capabilities-follow-ownership]] - Skills, MCP servers, and subagents are capabilities with owners.
* [[tooling-explicit-and-reversible]] - the AI tooling default is dated and reviewed.
* [[production-ready]] - AI-driven changes still need to meet readiness.
* [[observable-by-default]] - AI-driven changes still need to be observable.
* [[markdown-records-as-canonical]] - AI tooling decisions and exceptions live as ADRs.

## Scope and Revisiting

This principle applies to all use of AI assistants - code, configuration, infrastructure, documentation, automation - in Organization's engineering work. It applies to Claude Code as the default agent, and to any other agent used by exception.

It does not apply to:

* Non-engineering uses of AI (for example, marketing or content) that have their own governance regime.
* Personal experimentation outside any Organization repository or system.

The principle should be revisited if:

* Agent capabilities change shape significantly (for example, autonomous multi-step deployments that need a different governance model).
* The default agent choice changes after a review cycle.
* Incident patterns reveal that current controls are insufficient.
* Regulation explicitly governs AI in software development in ways that require additional or different controls.

## Authoritative References

* Organization AI Decisions Log, AI Coding Policy: Human Accountability with Executable Controls ([[ai-policy]]).
* Organization AI Decisions Log, AI Engineering Standards: Governance-as-Code for Modernization ([[ai-engineering-standards]]).
* Organization AI Decisions Log, AI Developer Tooling: Claude Code as the Default Agent Platform for 2026 ([[ai-tooling]]).
* Anthropic, [Claude Code Documentation](https://docs.anthropic.com/claude/docs/claude-code).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
