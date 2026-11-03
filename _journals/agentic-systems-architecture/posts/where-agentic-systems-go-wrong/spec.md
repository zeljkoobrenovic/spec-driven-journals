---
status: accepted
revised: 2026-10-28
---

# Spec: Where Agentic Systems Go Wrong: Sixteen Failure Patterns

## Intent

Give the book one shared vocabulary for how agentic systems fail, before the reader meets Ostrell or any chapter. The page names the sixteen failure patterns of the style guide, with their exact names, and for each gives an illustrative design-review quote (labeled as invented), warning signs, the mechanism, the cost, the documented public evidence that the chapters already cite (or a plain statement that none exists), the fictional Ostrell incident that shows it with the chapter that tells it, and the chapters that address it, strongest first. It ends by showing how the patterns compound in pairs and chains, so that readers look for the second pattern before funding a fix for the first. Every chapter's FAILURE PATTERNS callout links here.

## Audience

Software architects, principal engineers and technical leaders reading the book, and the people who sit with them in design, incident and autonomy reviews. They know distributed systems and security well; they need a compact map of where agent-specific designs break and where in the book each break is repaired.

## Success criteria

- [x] All sixteen patterns appear with the exact names, warning signs and parts from `_research/style-guide.md`, in one summary table (pattern, warning sign, part) and one section each.
- [x] Every pattern section has an illustrative quote labeled as illustrative, warning-sign bullets, mechanism, cost, documented examples, an Ostrell incident labeled fictional with its chapter, and an "Addressed in" list of `[[…]]` links ordered by strength.
- [x] Documented examples use only sources the chapters cite, with the same dates and links; patterns with no public incident (Amnesiac Execution, The Fire-and-Forget Action, The Different Second Answer, The Lost Handoff, The Agent Committee, The Token Bonfire, The Agent-Shaped Hammer) say so plainly.
- [x] Ostrell numbers match `_research/scenario-ledger.md` (Double Credit, Half-Posted Accrual, Weekend Fan-out, Lost Handoff, Poisoned Ticket, Stale Price Book, Fixture Purge, Alias Drift, Rubber Stamp, and the chapter additions used).
- [x] A section on how patterns compound covers at least Lethal Trifecta + Ambient Authority and Different Second Answer + Fire-and-Forget Action, with one mermaid diagram and caption.
- [x] Preface callouts ("IN THIS SECTION, YOU WILL"), exactly three KEY POINTS, a grouped `## Sources and Evidence` section and the fictional disclaimer.
- [x] 6,000–9,000 words; the build resolves every `[[…]]` link and the diagram renders.

## Non-goals

- Teaching the remedies: each pattern links to the chapters that own them ([[autonomy-and-consequence]], [[retries-idempotency-and-concurrency]], [[agent-threat-model]], [[human-oversight-and-bounded-autonomy]], [[versioning-agent-systems]] and the rest).
- Introducing Ostrell, its agents and its cast — [[meet-ostrell]].
- Telling the incidents in full — the chapters named in each Ostrell paragraph.
- New external research: the page adds no source the chapters do not already cite.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger gives two detection dates for the Fixture Purge ([[partial-failure-and-compensation]] vs [[domain-coding-agents]]); this page avoids the date and links the coding chapter.
- Several patterns have no public incident as of October 2026. A later edition should re-check incident databases and postmortems for duplicated agent side effects, lost handoffs and runaway agent spend.
- An illustration pass may replace Figure 1 with a generated image; keep the caption.

## Decision log

- **2026-10-28** — Grouped the sixteen patterns under the parts that address them rather than in invented families, so the summary table, the section order and the book's structure agree.
- **2026-10-28** — Kept non-LLM cases (Michigan's unemployment system, Robodebt, the Dutch childcare-benefits classifier, CrowdStrike) only where the chapters use them, and labeled each as non-agent, because they document the mechanism where agent incidents do not yet exist.
- **2026-10-28** — Made the "compounding" section about pairs (one pattern creates the bad action, the other hides or amplifies it), because every expensive Ostrell incident and the GitHub MCP case needed two patterns.
- **2026-10-28** — Kept "Addressed in" lists as bare link lists ordered by strength to stay within the word budget; each chapter's own FAILURE PATTERNS callout gives the chapter-specific reason.

## Sources

- **Internal**
  - `_research/style-guide.md` — the sixteen pattern names, warning signs and parts.
  - `_research/scenario-ledger.md` — every Ostrell number.
  - `PLAN.md` — the preface contract.
  - The FAILURE PATTERNS callouts and `## Sources and Evidence` sections of chapters 01–44, from which every documented example and citation is copied.
- **Interview sources**
  - None used directly; the linked chapters cite them.
- **Key external sources** (all cited in chapters)
  - Willison, "The lethal trifecta for AI agents", 2025; Invariant Labs, GitHub MCP, 2025; NVD, CVE-2025-32711 (EchoLeak), 2025.
  - Yao et al., τ-bench, 2024; Cemri et al., MAST, 2025; Anthropic, multi-agent research system, 2025.
  - The Register (Replit, 2025); Tom's Hardware via Yahoo (Terraform, 2026); Euronews and NeuralTrust (PocketOS, 2026).
  - Anthropic, "A postmortem of three recent issues", 2025; Parasuraman & Manzey, 2010.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
