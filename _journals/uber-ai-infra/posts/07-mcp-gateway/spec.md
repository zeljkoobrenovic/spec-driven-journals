---
status: accepted
revised: 2026-10-20
---

# Spec: The MCP Gateway: Every Internal Service One Tool Call Away

## Intent

Explain how Uber exposed thousands of internal services and vendor tools to agents through one MCP Gateway, and why it was fast: tools are generated from the Thrift and Protobuf contracts in the IDL registry, and the team that ran Uber's API gateway built it. Walk through the documented control plane (registry, AutoCrawler, MCPFx, disabled by default, owner-approved descriptions) and data plane (proxy, protocol translation, per-tool authorization with the caller's identity, token exchange, redaction). Then explain the context-cost problem and the CLI projection (Code Mode) that answered it. Translate the pattern for companies without a contract registry.

## Audience

Platform, API-gateway and security leads, staff engineers and CTOs deciding how agents should reach internal systems and vendor tools.

## Success criteria

- [x] Reader can trace a tool from IDL to agent call through the documented control and data planes.
- [x] Reader can explain why generated tools start disabled and how description changes are governed.
- [x] Reader can map tool poisoning, rug pulls, confused deputy and token passthrough to specific mitigations in Uber's design.
- [x] Reader can explain Omni MCP, Response Projection and Code Mode, and why the CLI became the default for coding agents.
- [x] Reader can cite Uber's figures with sources and dates without merging them (800+/5,000+ vs 1,000+).
- [x] Reader can name the four pre-AI foundations that made the gateway fast and what a company without them must do first.
- [x] Reader can choose a path for ≈50, ≈500 and ≈5,000 engineers.

## Non-goals

- The IDL registry's history and Edge Gateway internals — owned by [[contracts-and-context-propagation]].
- Skills built on the gateway and the CLI rewrite of the skills repository — owned by [[skills-monorepo]].
- The context graph and Cortana — owned by [[context-graph]].
- Harness-side configuration — owned by [[aifx-harness-layer]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Does the episode's April 2025 date refer to the gateway or to the wider early-2025 agent platform?
- How are write tools approved at call time, and what share of tools is enabled?
- How do the three context mechanisms split the reported token savings?

## Decision log

- **2026-10-20** — Built the "What Uber built" section on the October 2026 Uber post rather than the episode, per the ledger's reconciliation rule; the episode supplies origin, team and motivation.
- **2026-10-20** — Framed MCP vs CLI as "the protocol governs; the CLI is the interface" instead of taking a side, because Uber keeps both.
- **2026-10-20** — Added a risk-to-mitigation table using Invariant Labs (April 2025) and the MCP security best practices as the threat sources, labeling one mitigation as not stated.

## Sources

- **Internal**
  - [[contracts-and-context-propagation]], [[build-what-does-not-exist]] — the IDL registry, Edge Gateway, uOwn, Cadence.
  - [[aifx-harness-layer]], [[skills-monorepo]], [[model-gateway]] — neighbours.
- **External**
  - The October 2026 Pragmatic Engineer episode and show notes.
  - Uber Blog: Designing MCP Gateway (October 2026), Software Factory (August 2026), agent identity (May 2026); AAIF write-up (May 2026); Pragmatic Engineer (March 2026); Port summary of the AI Engineer 2026 talk.
  - Invariant Labs (2025); MCP specification security best practices and versioning; Anthropic, code execution with MCP (2025); Thoughtworks Radar Vol. 34; Stripe Minions (2026); Spotify Honk Part 2 (2025); Kong documentation.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: removed a misattributed episode claim (the permissions remark concerns the context graph, not the MCP Gateway), labeled the weeks-versus-years line as judgement, linked the 2016 Tech Stack post, Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 3 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
