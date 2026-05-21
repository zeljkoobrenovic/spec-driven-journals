---
id: "ORG-PRIN-GOVERNANCE-AS-CODE"
status: draft:gray
title: "Practice Principle: Governance as Code"
date: 2026-05-16
author: Organization Tech Strategy
permalink: governance-as-code
timetoread: 12 min
excerpt: "Encode engineering standards, policies, and review rules as executable artifacts: CI checks, pre-commit hooks, IaC guardrails, Claude Code settings, CLAUDE.md fragments, Skills, MCP allowlists, and pull-request templates. Governance documented only in policy decks fails silently and gets discovered during incidents. Governance encoded in the platform fails loudly and gets fixed in pull requests. The principle is not 'no human review'; it is 'standards that can be enforced should be'."
tags: practices, governance, ci, hooks, claude-code, policy, automation
logo: "assets/images/governance-as-code/logo.jpeg"
logo_credit: "Inspired by Organization's AI engineering standards and policy-as-code thinking"
icon: "assets/icons/governance-as-code.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization expresses engineering standards, policies, and review rules as **executable artifacts** wherever feasible: CI gates, hooks, infrastructure-as-code guardrails, Claude Code settings, CLAUDE.md fragments, Skills, MCP allowlists, repository configurations, and templates. The default is "encode the rule"; written policy is a complement, not a substitute. Human review remains essential for judgement; executable governance handles the well-defined, repeatable parts.

## Statement

For every engineering standard, Organization asks:

1. **Can this be checked automatically?** If yes, encode it.
2. **Can the default behaviour satisfy it?** If yes, ship the default that way.
3. **Does it need human judgement?** Keep it as a written standard and review check.

The result is governance that lives partly in code, partly in templates, partly in CLAUDE.md and AI configuration, and partly in written policy. The written part exists; it just stops being the only line of defence.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Encode what can be encoded. | Encode everything. |
| Defaults satisfy most rules. | Defaults replace standards. |
| Written policy still matters. | Written policy is the primary mechanism. |
| Human review handles judgement. | Human review is bypassed. |
| AI configuration is part of governance. | AI replaces governance. |

The principle expects a layered model: defaults, executable checks, written standards, human review. Each layer catches what the others cannot.

## How to Apply This Principle

Use this principle to:

* Decide which standards should be defaults, checks, guardrails, review prompts, or written policy.
* Explain why encoded governance reduces drift without replacing judgement.
* Recognise noisy or ownerless checks as governance failures.
* Treat AI settings, hooks, Skills, and MCP allowlists as part of the governance surface.

## Rationale

Standards written only as policy documents fail in predictable ways:

* People forget them between writing and applying them.
* New joiners do not know they exist.
* Reviewers miss them because the rule is not surfaced at review time.
* Drift accumulates silently between incidents.
* Compliance becomes annual rather than continuous.

Encoded governance fixes most of these:

* The check runs every time, not only when remembered.
* The default already complies, so most code is correct by construction.
* Reviewers see violations as failed builds, not as policy memos.
* Drift is detected when it happens.

Organization's AI strategy makes this particularly powerful. Claude Code settings, hooks, CLAUDE.md fragments, Skills, MCP allowlists, and pull-request templates are all places where governance can be encoded. The AI engineering standards decision is built explicitly around this idea: governance-as-code for modernization.

## Implications

* **Standards are paired with checks.** A written standard without an enforcement story is incomplete.
* **Golden paths embody standards.** Templates, base images, and project scaffolds satisfy standards by default.
* **CI runs the gate, not the auditor.** Continuous, deterministic checks beat periodic audits.
* **Hooks catch local issues early.** Pre-commit and pre-push hooks reduce CI churn.
* **IaC guardrails enforce cloud policies.** AWS Organisations SCPs, Terraform policy modules, and CI scans cover infrastructure rules.
* **Claude Code is part of the governance surface.** Permission modes, hook scripts, Skills, MCP allowlists, and CLAUDE.md fragments enforce policy at AI authoring time.
* **Pull-request templates make rules visible at the moment of review.**
* **Written standards are kept current and small.** They are reference material, not the only enforcement.

## Encoding Ladder

Not every rule belongs in the same layer. Use this ladder when deciding how to govern a standard:

| Layer | Use when | Example |
| --- | --- | --- |
| **Default** | The desired behaviour can be generated or scaffolded. | New services start with structured logging enabled. |
| **Local check** | The issue can be caught before CI. | Pre-commit hook blocks committed secrets. |
| **CI gate** | The rule is deterministic and important enough to block merge. | Dependency scan fails on critical vulnerabilities. |
| **Platform guardrail** | The rule must hold even if a repository bypasses checks. | AWS SCP prevents public S3 buckets. |
| **Review prompt** | The rule needs human judgement. | PR template asks whether an ADR is needed. |
| **Written policy** | The rule needs explanation, exceptions, or legal framing. | AI data-classification policy. |

Good governance chooses the lowest layer that reliably works. Over-encoding judgement creates friction; under-encoding deterministic rules creates drift.

## What This Means for Teams

For service teams:

* Use the templates. They satisfy most standards out of the box.
* When a check fails, treat it as feedback, not as paperwork. The standard exists for a reason; the check surfaces it.
* If you find yourself bypassing a check repeatedly, raise the standard for review.

For platform and AI Engineering Enablement roles:

* Own the encoded surface: templates, CI checks, hooks, IaC modules, Claude Code defaults, Skills, MCP allowlists.
* Keep the written standards small, current, and linked to the executable artifacts that enforce them.
* Provide a clear path for teams to propose changes.

For security, data, and compliance roles:

* Express policy in the encoded layer where possible.
* Distinguish "must be enforced" from "must be reviewed" from "must be advised".
* Avoid pure-text policy where an executable expression is feasible.

For tech leads:

* Treat encoded governance as a load-bearing part of the platform.
* Push back on proposals to weaken checks without changing the underlying standard.

## Anti-Patterns

* **PDF policy.** Standards live only in documents that no engineer reads at review time.
* **Manual audits.** Quarterly compliance sweeps that catch problems months after they were introduced.
* **Bypass culture.** Skipped checks (`--no-verify`, "approve and merge") become routine because the checks were too noisy or too wrong.
* **Encode everything.** Excessive automation that catches no real risk and creates significant friction.
* **Encoded but unowned.** A CI check that fails for years with no one fixing the underlying issue or the check itself.
* **AI bypass.** Claude Code used in modes that disable the encoded governance, "just for this change".
* **Policy without defaults.** Standards exist but no template satisfies them, so every project must implement them from scratch.

## Examples

Aligned with the principle:

* The default container base image is Ubuntu with security defaults; teams inherit compliance without writing it.
* A CI check blocks secrets committed in the repository.
* A Claude Code hook prevents writing to specific paths or running certain commands without explicit approval.
* A CLAUDE.md fragment encodes Organization's coding conventions and pull-request rules; Claude Code applies them when generating changes.
* A pull-request template lists the readiness items, with links to the encoded checks.

Out of alignment with the principle:

* A 60-page policy PDF that nobody opens.
* A CI gate that has been disabled for six months because it kept "false-positiving".
* Claude Code used in YOLO mode, with no settings, no hooks, no CLAUDE.md, because "we need to move fast".
* Standards that require teams to implement boilerplate to comply, with no template to lean on.

## Discussion Prompts

Use these prompts when reviewing standards:

* Which standard are we relying on people to remember that could be encoded?
* Which encoded check is noisy, unowned, or no longer aligned with the standard?
* Which governance rule needs human judgement rather than automation?

## Related Principles

* [[standardize-before-diverging]] - encoded defaults are the visible expression of standards.
* [[production-ready]] - readiness items are partly encoded.
* [[observable-by-default]] - observability is enforced through templates and CI.
* [[ai-output-must-be-governed]] - AI output flows through the encoded governance layer.
* [[capabilities-follow-ownership]] - encoded governance artifacts are themselves capabilities with owners.

## Scope and Revisiting

This principle applies to Organization's engineering standards, security policies, infrastructure rules, AI configuration, and any policy that produces repeatable, machine-checkable expectations.

It does not apply to:

* Standards that require human judgement (for example, architectural quality, design taste).
* Personnel, legal, and commercial policies outside engineering.
* One-off compliance exercises.

The principle should be revisited if:

* The encoded surface becomes too rigid to evolve standards safely.
* Bypass rates rise in ways that suggest the checks are wrong rather than the code.
* A new class of standards emerges that does not fit the executable model.

## Authoritative References

* Organization AI Decisions Log, AI Engineering Standards: Governance-as-Code for Modernization ([[ai-engineering-standards]]).
* Organization AI Decisions Log, AI Coding Policy: Human Accountability with Executable Controls ([[ai-policy]]).
* AWS, [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).
* Open Policy Agent, [Policy as Code](https://www.openpolicyagent.org/).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
