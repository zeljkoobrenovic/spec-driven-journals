---
status: accepted
revised: 2026-10-28
---

# Spec: A Reference Architecture for Agentic Systems

## Intent

Give the reader the map of the whole book: the components an agentic system needs, what each owns and must never do, how they connect, which plane each belongs to, and which chapter develops each in depth. The chapter must make three ideas stick. First, the agent-specific part of the architecture is narrow, and every added component is justified by a failure it contains. Second, there is exactly one path from model output to the world (runtime records, policy enforcement point decides, tool broker executes with brokered credentials, evidence log records intent and receipt), and it has to be made true with mechanical checks, not just drawn. Third, the control plane publishes versioned artifacts that a statically stable data plane caches and enforces, but autonomy grants fail closed. This is the hub chapter; it introduces components and links out instead of teaching them.

## Audience

Architects, principal engineers and platform leads who are about to build or adopt a shared agent platform, or who must review agents built by several teams. They know control and data planes from infrastructure, and API gateways, workflow engines and audit logs. They need the agent-specific responsibilities and prohibitions, and a way to check that a design actually enforces them.

## Success criteria

- [ ] Reader can name every component of the reference architecture, its Keelson name, what it owns, what it must never do and the chapter that owns it, from one responsibilities table that agrees with the chapters already written (Toolyard, Bulkhead, Runtime, context assembler, Wake, Sounding, Agent Registry).
- [ ] Reader can state the one-path rule and show how a conformance check (egress, secrets, pinning, tiers) and a daily "side effect without policy decision" query make it true.
- [ ] Reader can place each component in the control plane or the data plane, explain why Toolyard and Bulkhead are each split across both, and use the static-stability table to say what keeps running and what degrades when each component fails.
- [ ] Reader can follow one €180 Answerdesk credit through every data-plane component (sequence diagram) and map the nine 2027 Ostrell incidents to the components where their fixes landed, with ledger numbers.
- [ ] Reader has a dated comparison of published decompositions (Anthropic, CoALA, Lu et al., AWS AgentCore, the interview designs), with what each leaves out and an explicit statement that no study compares architectures by incident rate.
- [ ] Reader has a failure-scenario table for the platform itself, a build/adopt trade-off table, the thin-versus-thick platform line, and an Across Domains table that identifies domain-added deterministic components.
- [ ] Reader will not mistake a managed service list for an architecture, or a drawn single path for an enforced one.

## Non-goals

- The model gateway in depth ([[models-and-the-model-gateway]]); the runtime's loop and lifecycle ([[agent-runtime]]); enterprise integration patterns ([[agents-in-the-enterprise]]); interaction modes ([[agent-interaction-design]]).
- Policy as code, guardrails and the evidence log in depth ([[policy-enforcement-and-audit]]).
- The broker, registry and MCP in depth ([[tool-ecosystems-and-mcp]]); durable execution ([[durable-agent-execution]]); task state ([[task-state-and-checkpoints]]); versioning and manifests ([[versioning-agent-systems]]); ownership and operating model ([[owning-agentic-systems]]).
- Retelling any incident in full; each row links to its owning chapter.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[owning-agentic-systems]] (not yet written) should confirm the platform-versus-product ownership line stated here (platform owns cross-agent exploitable components; product teams own domain semantics, datasets and, with risk owners, tiers).
- [[policy-enforcement-and-audit]] (not yet written) should confirm the daily Logbook query for side effects without a Bulkhead decision.
- The AWS AgentCore service list is volatile; re-check it at the next revision.

## Decision log

- **2026-10-28** — Organized the chapter around a responsibilities-and-prohibitions table rather than a layer-by-layer tour, because prohibitions are what keep controls in the right component, and a table links cleanly to the owning chapters.
- **2026-10-28** — Adopted the separation of authorization (Bulkhead) from execution (Toolyard) and rejected the interview designs' identity broker that also executes (consistency ruling 15), citing OWASP LLM06.
- **2026-10-28** — Applied static stability to availability but fail-closed to autonomy, to reconcile AWS's static-stability guidance with the 60-second demotion requirement set in [[evidence-for-autonomy]].
- **2026-10-28** — Used the nine canonical incidents as the worked example's map instead of inventing a new one, so the hub agrees with every chapter that tells an incident in full.

## Sources

- **Internal**
  - [[what-makes-a-system-agentic]], [[autonomy-and-consequence]] — harness, agent loop, autonomy tiers.
  - [[tool-ecosystems-and-mcp]], [[task-state-and-checkpoints]], [[durable-agent-execution]], [[context-engineering]], [[agent-observability]], [[evidence-for-autonomy]], [[versioning-agent-systems]] — component responsibilities and requirement values the table must agree with.
  - Interview designs (design examples): `agentic-platform-foundations` (final architecture, no-bypass invariant), `agentic-finance-platform`, `agentic-support-platform` (step `live-loop`), `agentic-healthcare-platform`, `agentic-public-benefits-platform` (step `rules`).
- **External**
  - Anthropic, *Building effective agents* (2024) — augmented LLM; start with APIs directly.
  - Sumers et al., *CoALA* (TMLR 2024); Lu et al., reference architecture preprint (2023/2024) — research decompositions.
  - AWS, AgentCore overview (accessed 2026-10); AWS control/data plane whitepaper; Furr, *Static stability* (2019).
  - OWASP LLM06 Excessive Agency (2025); Sculley et al., NIPS 2015.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned the idempotency key (agent id + run id + action object id), the Bulkhead latency assumption (p99 ≤ 5 ms) and Tidemark trust levels with their owning chapters; added the on-output PEP to Bulkhead's row; trimmed an unverified Furr quote; pointed the independent Toolyard limit check to autonomy-and-consequence. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
