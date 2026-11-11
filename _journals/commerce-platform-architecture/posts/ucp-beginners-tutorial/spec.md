---
status: accepted
revised: 2026-11-09
---

# Spec: Universal Commerce Protocol: A Beginner's Tutorial

## Intent

Teach a newcomer how Universal Commerce Protocol (UCP) connects a shopping application to a merchant, using a hypothetical purchase from the fictional Kestrel & Pine. Explain each concept before introducing protocol fields, external references or examples. Follow discovery, capability agreement, checkout, payment, completion and order updates, including human handoff and uncertain outcomes. Publish as an appendix rather than expanding the existing AI chapter.

## Audience

Engineers, product managers and architects who understand an API but have not implemented agentic commerce. No earlier chapter is required. Readers should be able to follow a message exchange and judge what a first integration must prove.

## Success criteria

- [x] Explain UCP's purpose, participants, profiles, services, capabilities, extensions and transports in plain language.
- [x] Distinguish UCP from ACP, MCP and AP2 without implying ACP only covers payments or that every UCP integration requires AP2.
- [x] Walk through one coherent fictional jacket purchase, with annotated message excerpts and amounts that agree throughout.
- [x] Separate a checkout session from a completed order and payment authorization from fulfillment; cover confirmation, escalation, retries and reconciliation.
- [x] Include an opening hero image and ten inspected explanatory illustrations with descriptive alt text and captions, covering the participants, each purchase step and recovery.
- [x] Date the technical reference, cite primary sources, and clearly label illustrative excerpts and omitted authentication details.
- [x] Provide a practical learning exercise, implementation boundaries and the book's three takeaway tiers.
- [x] Add the appendix to navigation, link it from the AI chapter, build the journal, and verify rendering, examples and local links.

## Non-goals

- A production-ready payment server, a live purchase, or a claim that an example merchant or consumer program supports UCP.
- A forecast of protocol adoption or a survey of vendor marketing.
- Changing Kestrel & Pine's established 2027 decision to prepare its data and APIs without launching a shopping agent.

## Modalities

Article only, with illustrated message walkthroughs.

## Open questions

None that block the tutorial. Protocol and sample revisions must be checked again before a later edition.

## Decision log

- **2026-11-09** — Use the published 2026-08-25 UCP documentation and record the inspected source revision. Keep excerpts small and explicitly incomplete; a runnable production-looking mock would hide the authentication and payment integration work.
- **2026-11-09** — Use a hypothetical lab purchase of one €199 jacket, separate from Eva's canonical €235 storefront order. This teaches the protocol without changing the scenario ledger.
- **2026-11-09** — Place the tutorial in a new Appendix section before Reference, preserving the numbered chapter sequence and existing permalinks.

## Sources

- [UCP specification](https://ucp.dev/2026-08-25/specification/overview/) and its checkout, fulfillment, payment, identity and order specifications — protocol behavior and message formats, checked 2026-11-09.
- [UCP source revision](https://github.com/Universal-Commerce-Protocol/ucp/tree/7dd79ea2ff0bc8bc394ac5b17ababa91284fa581) — inspected schemas and documentation snapshot.
- [UCP samples](https://github.com/Universal-Commerce-Protocol/samples) — optional local learning exercise.
- [ACP specification](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol) — comparison and overlapping scope.
- [[ai-and-agentic-commerce]] and the journal's scenario ledger — conceptual context and fictional merchant facts.

## Changelog

- **2026-11-09** — Added an opening hero illustration of shopper approval, the UCP connection and the merchant's order, matching the journal's visual style.
- **2026-11-09** — Illustrated every step: added Figures 3, 4, 5, 8 and 9 for Steps 2, 3, 4, 6 and 7 (Gemini, matched to the existing palette); Steps 1 and 5 already had Figures 2 and 7. Figures renumbered 1–10. *(AI-mediated session)*
- **2026-11-09** — Status `accepted`; completed the illustrated tutorial, checked message excerpts against the dated specification, and verified the built appendix and entry links. Added its sources to the bibliography while preserving reference identifiers.
- **2026-11-09** — Initial spec, status `draft`; requested illustrated beginner's appendix tutorial.
