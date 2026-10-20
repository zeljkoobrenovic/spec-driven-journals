---
status: accepted
revised: 2026-10-20
---

# Spec: System Catalog: Every Uber System Named in This Book

## Intent

Give the book one index of every Uber system it names, so a reader who meets "Muttley", "MatchGuard" or "Glue" in a chapter can see in one row what the system does, when it appeared, how strong the public evidence for it is, what it depends on and which chapter explains it. The page also restates the book's thesis as a lookup: a second section groups the AI-era systems by the pre-AI foundation they reuse, so the "decade and a year" mapping can be checked system by system.

## Audience

Engineering leaders, platform leads and staff engineers reading the book out of order, and reviewers checking that the chapters agree on names, dates and evidence labels.

## Success criteria

- [x] One alphabetical table covering every Uber system named in the chapters, with columns for system, what it does, era, evidence label, dependency and chapter link.
- [x] Evidence labels use exactly three values (podcast only, documented (year), both) and follow the fact ledger's cross-source reconciliation (Jaeger and DevPod dates, context-graph sizes, the 15% Minion share, "fine-tuned" as podcast-only).
- [x] Alias rows for systems with several written names (GenAI Gateway, Michelangelo Gateway) point to the Model Gateway.
- [x] A grouping by foundation→AI dependency, with a mermaid diagram and a table, consistent with the dependency map in [[the-harness-is-the-easy-part]].
- [x] Systems with no AI-era successor are named, and the page says what the grouping does not claim.
- [x] Opens with `IN THIS PAGE, YOU WILL:` and a lead; no KEY POINTS, no BUILT ON.

## Non-goals

- Explaining how any system works; each chapter owns its system.
- The dates and their reconciliation; [[timeline]] owns them.
- Definitions of terms that are not system names; [[glossary]] owns them.
- Sources; the [[bibliography]] lists them, and each chapter's Sources and Evidence section cites them.
- Industry systems used for comparison (Stripe Minions, Spotify Honk, Google Rosie).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The design-doc hub's real name ("U-Plan" as heard) is unconfirmed; rename the row if Uber publishes it.
- Start dates for Capri, MatchGuard, Wisdom, Code Inbox and Shepherd are not public; update the era column if they appear.

## Decision log

- **2026-10-20** — Built the system list by scanning all chapters for Uber system names and checking each against the chapter that discusses it, not from the PLAN alone; the catalog has 74 rows, including earlier GenAI tools and documented components (AutoCrawler, Omni MCP, MCPFx, Muttley) that the episode does not name.
- **2026-10-20** — "Both" is reserved for systems in the episode and in a dated written source; documented systems the episode does not discuss are "documented", so the evidence column tells a reader where the account comes from.
- **2026-10-20** — Owning chapter follows PLAN's "Owns" lists; systems mentioned only in passing link to the page that discusses them (often [[timeline]]).
- **2026-10-20** — Kept internals out: the dependency column records only reuse the chapters source; where none is described it says so.

## Sources

- **Internal**
  - Every chapter's body and Sources and Evidence section; [[the-harness-is-the-easy-part]] for the dependency map; [[timeline]] for dates.
  - The fact ledger (`_research/fact-ledger.md`), including its cross-source reconciliation table.
- **External**
  - As cited in the chapters and listed in the [[bibliography]].

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Hero image and icon generated. *(AI-mediated session)*
