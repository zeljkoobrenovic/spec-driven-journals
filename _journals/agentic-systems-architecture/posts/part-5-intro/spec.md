---
status: accepted
revised: 2026-10-28
---

# Spec: Part V — TOOLS: Tools and Execution Boundaries

## Intent

Orient the reader to Part V: how a model's output becomes a call, a command or an effect in someone else's system, and what code decides at each step. State the part's argument as one line of reasoning across four widening boundaries (one tool's contract, many tools behind one broker, model-written code inside a sandbox, external effects as action objects with receipts), with one rule throughout: the model proposes; code validates, authorizes, contains and records. Frame it through the Ostrell events the chapters use (the 1,000-call credit review and the June 2027 credit tool, Toolyard's inventory and the Tracker Update, Forge's red team and the Silent Fallback, the Promised Credit).

## Audience

Chief architects, principal engineers, platform and security leads who design tool surfaces, tool platforms, execution environments and the action path for agentic systems.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the argument as one chain across the four chapters, not a list of summaries.
- [ ] Lists the questions the reader will be able to answer.
- [ ] Says once that Ostrell is fictional; Ostrell numbers match the chapters (1,000 calls, 31 wrong-account, 6 false-success replies, 7 June 2027; 212 tools, 31 hours; 118 workstations, 9 days; €2,310, 38%).
- [ ] Hands over from Part IV (what the agent knows) and to [[part-6]] (intent that survives crashes, deploys and approval waits).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: one `[[permalink]]` per chapter in config order, saying what it decides and naming its Ostrell case, then hands off to [[tool-contracts]].
- [ ] 500–900 words.

## Non-goals

Teaching tool contract design, MCP, isolation technologies or action-object mechanics (the chapters own them); idempotency and unknown outcomes ([[retries-idempotency-and-concurrency]]); the Across Domains comparison; new citations or external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on this book's part-3 introduction and the vehicle book's part-2 introduction: callouts, a short lead, one diagram, one paragraph per chapter.
- 2026-10-28: Failure patterns: The Fire-and-Forget Action (the one the style guide assigns to Part V), plus Ambient Authority and The Lethal Trifecta, which three of the four chapters address through brokered credentials, run-scoped tokens, trifecta classification and default-deny egress. Autonomy by Default and The Rubber Stamp are left to the chapters and Part VII.
- 2026-10-28: The argument is framed as four boundaries of widening reach (one tool, many tools, executed code, external effects), so the diagram shows the chain rather than components.

## Sources

`PLAN.md`, `config.yaml`, `_research/style-guide.md`, and [[tool-contracts]], [[tool-ecosystems-and-mcp]], [[sandboxes-and-execution-environments]] and [[side-effects-and-external-actions]]. No external sources.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: approval wait wording aligned to the 4-hour approval expiry; lead and questions trimmed to the 900-word target. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
