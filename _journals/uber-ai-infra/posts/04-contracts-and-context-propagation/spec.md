---
status: accepted
revised: 2026-10-20
---

# Spec: The Hidden Foundations: Typed Contracts, Ownership Metadata and Trace Baggage

## Intent

Show which invisible pieces of Uber's pre-AI infrastructure turned out to be load-bearing for its AI systems, and why. Five foundations, each with what Uber documented, what the episode adds, and which AI-era system it later carried: the Thrift/Protobuf IDL registry (MCP Gateway), uOwn ownership data (Shepherd routing, context graph, tool enablement), Jaeger trace context and baggage (Slate routing), standardized language frameworks (Capri capture), and the Edge Gateway (tenancy injection, capture and replay, dependency metadata). The reader should leave knowing that coverage, not technology, made these foundations valuable, and in what order to build them.

## Audience

Engineering leaders, platform leads and staff+ engineers who own service infrastructure and want to know which properties of their estate decide whether agents can call, test and debug services.

## Success criteria

- [x] Each of the five foundations is defined in one clause and linked to the AI system it enables, with the evidence label for the link.
- [x] The baggage-routing mechanism is explained from the 2020 multitenancy and 2022 SLATE posts, with a sequence diagram, and the Jaeger date correction is applied.
- [x] uOwn is presented as podcast-only; the uOwn-to-AI links are labeled as inference.
- [x] The Shadower (2022) vs. Capri (2026) reversal on in-process capture is explained, with the inference labeled.
- [x] A trade-off table covers contract style, registry, test isolation, routing actor, frameworks, capture method and front door.
- [x] Comparisons are dated (Lyft 2022 via InfoQ, Signadot, W3C Baggage 2024, Spotify 2025), and guidance is given by company size.
- [x] Failure modes include baggage injection from untrusted clients and silent propagation drops.

## Non-goals

- The MCP Gateway's design — [[mcp-gateway]].
- Slate's agent workflows and evidence attached to PRs — [[slate]].
- Capri, MatchGuard and dimension tagging — [[capri]].
- The context graph's schema — [[context-graph]].
- Shepherd campaigns — [[shepherd-and-fox]].
- The city as a primitive and the build/open-source/buy lifecycle — [[build-what-does-not-exist]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Does any AI system read ownership from uOwn directly?
- How far has the Jaeger-to-OpenTelemetry migration gone, and what is propagation coverage today?
- How are the Edge Gateway's required/optional dependency tags computed?

## Decision log

- **2026-10-20** — Treated the five foundations as parallel sections with the same three questions (what the record shows, what it later carried, why it was cheap or expensive) rather than one narrative, so each maps cleanly to a later chapter.
- **2026-10-20** — Kept Slate and Capri mechanics to one paragraph each; this chapter owns the baggage and framework substrate, not the testing systems.
- **2026-10-20** — Recommended measuring coverage per foundation, because the chapter's main claim is that partial coverage gives agents an inconsistent world.

## Sources

- **Internal**
  - [[mcp-gateway]], [[slate]], [[capri]], [[context-graph]], [[shepherd-and-fox]] — the AI systems these foundations carry.
  - [[monorepos-and-one-build]], [[devpods]] — the neighbouring Part I foundations.
- **External**
  - Pragmatic Engineer podcast, "Uber's AI infra, from the inside" (Oct 2026).
  - Uber blogs: distributed tracing (2017), multitenancy (2020), Edge Gateway (2020), API gateway architecture (2021), Shadower (2022), SLATE (2022), BITS (2024), MCP Gateway (Oct 2026); NSDI '26 failover paper; uber-go/fx README.
  - InfoQ on Lyft staging overrides (2022); Signadot docs; W3C Baggage (2024).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: added the episode's service-mesh routing description and the documented Muttley sidecar name (with the open question of which component acts on overrides); removed process wording from the Lyft citation; Sources headings made consistent. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
