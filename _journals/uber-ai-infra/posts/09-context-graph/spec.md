---
status: accepted
revised: 2026-10-20
---

# Spec: The Context Graph and Cortana: Grounding Agents in the Company

## Intent

Explain how Uber cut the turns agents spend getting grounded: Cortana (December 2025) exposed the cost in its traces, and the context graph joined metadata from Uber's siloed systems (people, services, PRs, design docs, features, on-call events, config changes, incidents, tables and queries) into a live graph agents query first, in Cypher. Make the chapter's two owned terms concrete — **grounding turns** and **context graph** — and make the thesis concrete: the graph is a join over a decade of pre-AI metadata (uOwn, code review, design docs, incident tooling, data catalog), so the hard part is shared identifiers, not the graph store.

## Audience

Platform leads, staff engineers and data/metadata owners deciding whether to build a context layer for agents, and what to start with at 50, 500 or 5,000 engineers.

## Success criteria

- [x] Reader can explain grounding turns and why they drive cost via Uber's cost equation.
- [x] Reader can describe what Uber's graph holds and how agents navigate it, with each claim attributed.
- [x] The size discrepancy is shown per source (episode 100+/130+; blog 86/117, 24M nodes, 80M edges, 30+ systems; talk ~40M entries, 150 types).
- [x] The cash-trips example is worked step by step, and the blog's 38 s versus 20 min 9 s example is cited as one example, not an evaluation.
- [x] Permission handling is attributed (episode) with the agent-identity post as a related public mechanism, and the aggregation risk is labeled inference.
- [x] Databook (2020 blog) is presented as a documented precedent, with the caveat that the episode does not name it.
- [x] Size-banded guidance, trade-off table, failure modes, record gaps, questions, sources, two or more diagrams.

## Non-goals

- MCP Gateway mechanics and tool permissions ([[mcp-gateway]]).
- The design-doc hub itself ([[plans-as-source-of-truth]]).
- uOwn and Jaeger as systems ([[build-what-does-not-exist]], [[contracts-and-context-propagation]]).
- Context engineering as an engineer's skill ([[the-engineer-as-context-builder]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- How is the graph ingested and kept fresh, and which store runs it?
- How are node- and edge-level permissions enforced?
- Do managed agents such as Minion use the graph by default yet?
- Why do the type counts differ between the August blog and the October episode?

## Decision log

- **2026-10-20** — Led with the trace finding (grounding turns) rather than the graph's schema, because the measurable problem is what transfers to other companies.
- **2026-10-20** — Compared five grounding approaches (agentic search, RAG, catalog, graph, federated query) instead of graph databases, because the store is the commodity part.
- **2026-10-20** — Marked the IDL/Jaeger feed into the graph as inferred, since only the show notes' one-line remark supports it.

## Sources

- **Internal**
  - [[skills-monorepo]], [[mcp-gateway]], [[model-gateway]], [[plans-as-source-of-truth]], [[build-what-does-not-exist]], [[contracts-and-context-propagation]], [[token-spend-governance]], [[the-engineer-as-context-builder]].
- **External**
  - Pragmatic Engineer, *Uber's AI infra, from the inside* (14 Oct 2026) — primary account and show notes.
  - Uber blog, *Running a Software Factory Efficiently at Uber Scale* (27 Aug 2026) — graph size, sources, grounded-versus-ungrounded example.
  - AI Engineer World's Fair 2026 talk — Cortana usage, alternative size figures.
  - Uber blog, *Solving the Identity Crisis for AI Agents* (21 May 2026); *Turning Metadata Into Insights with Databook* (10 Nov 2020); *Genie* (10 Oct 2024).
  - Thoughtworks Radar *Context graph* (Apr 2026); Backstage catalog docs; Anthropic *Effective context engineering* (29 Sep 2025).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: paraphrased the cash-trips and other quotes (quote budget), removed an undefined "city-and-service catalog" from BUILT ON, made the schema-sprawl failure mode conditional on the type-count gap being growth, linked the AI Engineer talk, Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
