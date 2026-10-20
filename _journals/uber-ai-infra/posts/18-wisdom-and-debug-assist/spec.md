---
status: accepted
revised: 2026-10-20
---

# Spec: From Bug Report to Fix: Wisdom, DebugAssist and the Closed Loop

## Intent

Explain how Uber, by Medisetty's account, shortens the path from an employee's dogfooding bug report to a merged fix: Wisdom attaches telemetry, reproduction steps and expected versus observed behavior and routes the report; the DebugAssist managed agent proposes root cause, impact and an evidence timeline; an engineer accepts it and Minion writes the PR, attached to the Jira task; network-response replay by bug ID reproduces and confirms; corrections feed improvement. Separate this podcast account from the documented pieces (2016 dogfooding and bug reporter, 2016 mobile network record/replay, the September 2026 Debug Assist talk abstract) and argue that report quality, not agent cleverness, sets the loop's length.

## Audience

Mobile and platform engineering leaders, DevEx leads and staff engineers who own bug intake, triage and on-call, and who are deciding whether and how to put an RCA agent in front of a fixing agent.

## Success criteria

- [x] Reader can name what a context-rich report contains and why each element saves triage time.
- [x] Reader can describe the closed loop (report, route, RCA, human acceptance, Minion PR, replay, corrections) and which parts are podcast-only.
- [x] The talk abstract's figures (LangGraph, 11 MCP servers, ~30 minutes to PR, ~5,000 RCAs/month, 5% → 30% acceptance) are cited with date and the auto-PR versus hand-off difference is stated, not resolved by guesswork.
- [x] Reader understands the trade-off of gating fixes on an accepted root cause.
- [x] Comparisons with Meta SapFix/Sapienz (2018) and Google AI-powered patching (2024) are dated and specific.
- [x] Sized "If you are not Uber" guidance, starting with the report rather than the agent.
- [x] Failure modes include confident wrong RCAs, symptom fixes, routing loops, telemetry privacy and dogfooding bias.

## Non-goals

- Minion's architecture and entry points — owned by [[minion]].
- Managed maintenance loops (Fox) — owned by [[shepherd-and-fox]].
- Capture-replay for backend regression testing — owned by [[capri]].
- Productivity measurement of the loop — owned by [[feature-velocity]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Why does the episode's DebugAssist hand off to Minion while the talk's version opens PRs itself?
- How is Wisdom's routing done and how accurate is it?
- What telemetry is captured with employee reports, and how is it scrubbed and retained?
- How are corrections turned into improvements (evals, skill edits, fine-tuning)?

## Decision log

- **2026-10-20** — Opened with the on-screen "Cannot mock location" example to keep the chapter concrete and tie it to cities as a first-class dimension.
- **2026-10-20** — Treated the MCPCon Japan abstract as the main written source (it names Debug Assist) and stated its differences from the episode rather than merging them.
- **2026-10-20** — Positioned Genie (2024) as a retrieval-only predecessor to show the step from answering to investigating.
- **2026-10-20** — Made "fix the report before the agent" the core recommendation, over leading with agent tooling.

## Sources

- **Internal**
  - [[minion]], [[shepherd-and-fox]], [[mcp-gateway]], [[skills-monorepo]], [[build-what-does-not-exist]], [[contracts-and-context-propagation]], [[plans-as-source-of-truth]].
- **External**
  - Orosz and Medisetty, *Uber's AI infra, from the inside* (Pragmatic Engineer, 2026) — Wisdom and DebugAssist as described.
  - Dangi, *MCP-Powered Crash Investigation* (MCPCon Japan abstract, 2026) — Debug Assist figures.
  - Lozinski, *The Uber Engineering Tech Stack, Part I* (Uber, 2016) — dogfooding and the feedback reporter.
  - Uber, *Genie* (2024), *DragonCrawl* (2024), *Running a Software Factory Efficiently* (2026); At Scale *Octopus* abstract (2016).
  - Jia, Mao and Harman, *SapFix and Sapienz* (Meta, 2018); Keller and Nowakowski, *AI-powered patching* (Google, 2024).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: made the DebugAssist → Minion hand-off match the transcript everywhere (engineer judges the root cause right, hands it to Minion, PR attached to the Jira task holding the RCA) and dated the talk-abstract variant in KEY POINTS; shortened the DebugAssist quote to the transcript wording; cut an unsupported "good number" judgement and filler; Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
