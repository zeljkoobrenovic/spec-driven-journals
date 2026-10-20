---
status: accepted
revised: 2026-10-20
---

# Spec: Skills as a Product: The Agent Skills Monorepo

## Intent

Show why a company-wide skills repository is a platform, not a folder: once thousands of engineers depend on agent skills daily, skills need one place to live, one quality gate, distribution into every harness, one tool layer, and a loop that improves them after release. Use Uber's skills monorepo, as described in the October 2026 episode and the August 2026 Uber blog, as the worked case, and the CLI rewrite as the concrete proof that the single repository pays off. Name the **skill quality loop** and be honest that Uber's back half of it (trace-driven patches, evals) was still in flight.

## Audience

Platform and developer-experience leads and staff engineers deciding who owns agent skills, how they ship and how quality is judged; engineering leaders sizing the effort for 50, 500 or 5,000 engineers.

## Success criteria

- [x] Reader can describe Uber's skills platform (core and team skills, one gate, AIFX portability, MCP Gateway tool access, auto-installed marketplace, personas) with each claim attributed.
- [x] Reader can explain why the CLI rewrite shows the value of one repository, with Uber's published token figures.
- [x] Reader can name the stages of the skill quality loop and which ones Uber has built versus in flight.
- [x] Usage numbers are given per source and date (talk 2,500 / 20K+; blog 3,600+ / 30K+; episode ~30,000), not merged.
- [x] The monorepo layout is labeled podcast-only; the quality gate's contents are labeled inference.
- [x] "If you are not Uber" gives specific steps by company size and says what not to copy (auto-install without a gate).
- [x] At least two mermaid diagrams, one trade-off table, failure modes, record gaps, questions, sources.

## Non-goals

- AIFX internals, personas and settings sync ([[aifx-harness-layer]]).
- MCP Gateway design and the CLI projection itself ([[mcp-gateway]]).
- Token-spend policy ([[token-spend-governance]]).
- Maintenance skills run by Fox and Shepherd campaigns ([[shepherd-and-fox]]).
- The engineer's context-engineering role ([[the-engineer-as-context-builder]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What does Uber's single quality gate check? (Not public.)
- Have trace-driven skill improvement patches shipped, and who reviews them?
- Does Uber measure outcomes per skill, or only executions?

## Decision log

- **2026-10-20** — Built the chapter around one worked example (the CLI rewrite) rather than a feature list, because it is the only documented event that shows why one repository matters.
- **2026-10-20** — Explained the Agent Skills format's progressive disclosure and description-based activation, because they explain why an auto-installed catalog needs a gate; rejected a longer format tutorial (the audience knows the basics).
- **2026-10-20** — Kept three usage snapshots in a table rather than one headline number, per the ledger's reconciliation rule.

## Sources

- **Internal**
  - [[aifx-harness-layer]], [[mcp-gateway]], [[model-gateway]], [[monorepos-and-one-build]], [[devpods]], [[shepherd-and-fox]], [[context-graph]], [[token-spend-governance]].
- **External**
  - Pragmatic Engineer, *Uber's AI infra, from the inside* (14 Oct 2026) — primary account.
  - Uber blog, *Running a Software Factory Efficiently at Uber Scale* (27 Aug 2026) — skills counts, Continuous Skill Optimization, MCP schema token costs.
  - AI Engineer World's Fair 2026 talk, *Agentic SDLC at Uber* — earlier counts, marketplace, lint and review.
  - AAIF write-up of MCP Dev Summit talk (14 May 2026) — skills registry roadmap.
  - Anthropic, *Equipping agents for the real world with Agent Skills* (16 Oct 2025); agentskills.io; Claude Code cost docs; AGENTS.md; Thoughtworks Radar Vol. 34; Spotify Honk Part 2.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: paraphrased most episode quotes in What Uber Built (quote budget), shortened the persona bullet (owned by AIFX), trimmed the token-arithmetic paragraph and an unsupported savings claim, linked the AI Engineer talk, standard problem heading. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
