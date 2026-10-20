---
status: accepted
revised: 2026-10-20
---

# Spec: A Timeline of Uber's Developer Platform, 2014–2026

## Intent

Be the book's canonical record of dates. Every system named in the book gets a dated, sourced entry with an evidence label, organized in six eras from the two-service architecture of 2014 to the October 2026 episode. Where the episode and Uber's written record disagree (Jaeger, DevPods, service counts, agent PR share, context-graph size and more), the page reconciles them once, following the fact ledger, so chapters can cite it instead of re-arguing. The page also makes the thesis's time claim concrete by showing the lag from each foundation to its AI-era interface.

## Audience

Readers who want to check the book's "decade and a year" claim, and chapter writers and reviewers who need one place for canonical dates and the handling of disputed figures.

## Success criteria

- [x] Six era tables; every entry has a date, an event, an evidence label and a linked source.
- [x] Evidence labels (POD, SN, HOST, DOC yyyy, IND yyyy, PRESS yyyy) are defined before the first table.
- [x] A mermaid diagram of the eras and a mermaid diagram of foundation→AI lags, each with a captioned point.
- [x] A lag table from foundation date to AI-interface date.
- [x] A disputed-dates table covering at least Jaeger, DevPods, "two services", service counts, Model Gateway and MCP Gateway start, agent PR share, context-graph and MCP sizes, token cost and spend policy, each matching the ledger's reconciliation table.
- [x] A section on what the record does not date.
- [x] Exactly one KEY POINTS block; `IN THIS PAGE, YOU WILL:` label; no BUILT ON line.

## Non-goals

- Explaining how any system works; the chapters own that.
- The thesis argument; [[the-harness-is-the-easy-part]] owns it.
- A full system inventory with descriptions; [[system-catalog]] owns it.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- uOwn, the design-doc hub, AIFX, Capri and Code Inbox have no documented start dates; update if Uber publishes them.
- Whether the June 2026 per-tool spend cap was replaced by the August shared tier is not stated anywhere.
- When Uber's review platform moved from Phabricator "diffs" to "PRs" is unknown.

## Decision log

- **2026-10-20** — Started the timeline in 2014, because the two-service architecture and the program/platform split are dated 2014 in Uber's own sources; retitled from PLAN's "2015–2026" to "2014–2026" in the review pass so the title matches the entries (permalink unchanged).
- **2026-10-20** — Used flowcharts rather than mermaid's `timeline` syntax, which needs colons the style guide forbids outside quotes.
- **2026-10-20** — Industry events (ChatGPT, MCP, Agent Skills, DORA 2025) included sparingly as IND entries to show what Uber was reacting to, not as a second timeline.
- **2026-10-20** — Press reports labeled PRESS and kept separate from Uber's written record.

## Sources

- **Internal**
  - [[the-harness-is-the-easy-part]] — the thesis the dates support.
  - The fact ledger's cross-source reconciliation table (`_research/fact-ledger.md`).
- **External**
  - *The Pragmatic Engineer*, "Uber's AI infra, from the inside" (2026).
  - Uber engineering blog posts 2016–2026, NSDI '26 failover paper, and 2026 talks, as listed on the page.
  - Anthropic, "Introducing the Model Context Protocol" (2024) — MCP release date.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: retitled to 2014–2026; corrected the lag claim in KEY POINTS (four to ten years, since Slate precedes its agent use by four); fixed the Model Gateway reconciliation note (the date slip is not corrected in the episode). *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
