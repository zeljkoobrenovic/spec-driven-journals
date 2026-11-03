---
status: accepted
revised: 2026-10-28
---

# Spec: Caching and Context Budgets

## Intent

Show that prompt layout, cache keys, invalidation rules and context budgets are architectural decisions that control most of an agent's cost and part of its latency, and that every cache above the model trades correctness for cost. The reader should leave able to design a stable prefix layout, decide which caches are safe for which data, set and enforce per-step context budgets, choose when to compact, and move deadline-tolerant work onto batch tiers, without letting any cached value decide an action.

## Audience

Architects, principal engineers and platform leads who run or review agent platforms and are accountable for their cost, latency and correctness. They know caching in general; they need the agent-specific mechanics (exact-prefix provider caches, silent misses, compaction as a cache event) and the rules that keep caches from serving wrong answers.

## Success criteria

- [ ] Reader can explain how provider prompt caches work (exact prefix, invalidation order, TTL, silent misses) and why a broken prefix can cost more than no caching, with pricing given only as a dated snapshot.
- [ ] Reader can design a layered prompt layout (stable → volatile) and name what breaks prefix stability (timestamps, unsorted serialization, per-call tool filtering, model or speed changes).
- [ ] Reader can state the cache-key rule and apply it to response, tool-result, semantic and plan caches, including the rule that no cached value is the basis of an executed action.
- [ ] Reader can set a per-step context budget split by source, explain why it is set by evaluation rather than the window, and where the runtime enforces it.
- [ ] Reader can choose a compaction policy that accounts for cache rebuilds and pins commitments.
- [ ] Reader can decide which workloads belong on batch tiers and what resumability and deadline fallbacks they need.
- [ ] The Ostrell worked example (Keelson prefix layout; 11% → 76% cache-read share) is consistent with the scenario ledger, and figures are labeled as illustration or assumption.
- [ ] The chapter has a failure-scenario table, a trade-off table, a requirements table, the Across Domains section and at least two mermaid diagrams.

## Non-goals

- How to select and order context content, and compaction mechanics in depth — [[context-engineering]].
- Freshness SLOs and provenance envelopes in general — [[provenance-and-freshness]].
- Run budgets, cost per successful task and model cascades — [[agent-cost-and-model-routing]].
- Latency budgets, rate-limit ceilings and capacity planning — [[agent-latency-and-throughput]].
- Version manifests and release mechanics — [[versioning-agent-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public production writeup reports an agent's cache hit rate with cost before and after a layout change; revisit if one appears.
- Whether Anthropic's 1-hour TTL refreshes on hit, and Gemini's cache isolation scope, were not stated on the pages consulted.
- Provider cache sharing scope has changed since the 2025 timing audit; re-check before the next edition.

## Decision log

- **2026-10-28** — Framed the chapter around one rule for caches above the model (the key must carry everything the result depends on; TTL below the freshness SLO) rather than a catalogue of cache products.
- **2026-10-28** — Kept every price, multiplier and TTL in one dated snapshot table and used ratios in the body, because pricing is volatile (prices are scheduled to rise at one provider).
- **2026-10-28** — Used an Ostrell shadow trial (2.3% wrong would-be hits) to show semantic-cache risk instead of asserting it; rejected semantic caching for contract-dependent answers.
- **2026-10-28** — Treated compaction *timing* as this chapter's concern (cache rebuild cost) and left compaction content to [[context-engineering]].

## Sources

- **Internal**
  - [[context-engineering]], [[provenance-and-freshness]], [[agent-cost-and-model-routing]], [[agent-latency-and-throughput]], [[versioning-agent-systems]].
  - Research briefs `brief-performance-economics-evolution.md` (§1.1–1.3, 1.7) and `brief-context-memory-state.md` (Parts 2–3); digests `digest-platform-and-coding.md`, `digest-customer-facing.md`, `digest-back-office.md`.
- **Interview design examples**
  - `ai-coding-cli/interview.json` (steps `context`, `compaction`, `inference`; tenant policies), `agentic-platform-foundations/interview.json` (step `capacity`), `agentic-legal-platform/interview.json` (step `citation-gate`), `agentic-hr-platform/interview.json` (step `grounding`).
- **External**
  - Anthropic, OpenAI and Google prompt-caching, batch and pricing documentation (accessed 2026-10).
  - Gu et al., "Auditing Prompt Caching in Language Model APIs", ICML 2025.
  - Schroeder et al., "vCache", ICLR 2026; Zhang et al., "Agentic Plan Caching", NeurIPS 2025.
  - Manus, "Context Engineering for AI Agents", 2025; vLLM prefix caching design docs; MCP 2026-07-28 changelog.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Answerdesk budget table aligned to context-engineering (14 tools ≈ 3,000 tokens, not 5,400; slot ceilings exceed the 24,000 hard limit by design); quadratic-input arithmetic and Gemini price rises reduced to links to agent-cost-and-model-routing; corrected the OpenAI `allowed_tools` quote and the Gemini increase wording (several models, input and output); "turn" to "exchange"/"call" where ruling 19 applies. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
