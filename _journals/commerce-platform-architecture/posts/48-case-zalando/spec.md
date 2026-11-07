---
status: accepted
revised: 2026-11-07
---

# Spec: Case: Zalando, Microservices, Platform Strategy and the Return to Discipline

## Intent

Present Zalando as the fullest public record of a European retailer's architecture decisions and their corrections, using only its own dated posts and filings: the 2015 "Jimmy" and Radical Agility posts for the split made for team autonomy; the 2015 business-intelligence post and Nakadi for the cost of distributed data; the API Guild (2015), the guidelines (2016, active 2026) and the Tech Radar for API governance; the 2018, 2020, 2023 and 2025 posts for the return to discipline, with the 2025 event-to-API reversal worked in detail as the Black Friday Oversell told from a platform's side; the 2011–2026 partner program, Connected Retail, ZFS, ZEOS, SCAYLE and ABOUT YOU record for a retailer becoming a platform; and the 2023 assistant and 2026 identity broker for AI. After reading, a newcomer can say what team-sized modularity costs after the split, which platform pieces survived and why, what a written API standard should contain, when an event stream is the wrong source of current state, and where the public evidence stops.

## Audience

Readers new to commerce architecture. The integration engineer or architect who must write contracts with vendors and marketplaces benefits most (the guidelines table is written as a list of demands); the leader deciding how far to decentralize a growing team benefits from the discipline timeline; the product manager running a marketplace channel benefits from the platform-strategy timeline. Every term (monolith, microservices, autonomous team, internal platform-as-a-service, fragments, event, event bus, schema, API First, compatible extension, versioning, deprecation, sunset, tolerant reader, paved road, synchronous read API, partner program, seller of record, ship-from-store, logistics as a service, delegated access, token exchange) is explained in one plain clause on first use.

## Success criteria

- [x] Every company fact carries its year in the sentence and a source in Sources and Evidence; secondary or unfetched items (team sizes of three to seven, the 2019 leadership change, the "expanded too much" wording, the Connected Retail wind-down from trade press) are labeled as such.
- [x] Every statement about Zalando's internals beyond its own posts is inside a `> **INFERENCE, NOT DOCUMENTED:**` block; the chapter states that no source announces the end of Radical Agility or a 2019 reorganization.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The chapter contains the guidelines table (rule number, plain words, what to demand of a vendor), the discipline timeline table (year, what Zalando published, what narrowed), the open-source status table, the platform-strategy timeline, the lessons table, and three mermaid diagrams (fragments behind the router; the deprecation lifecycle; the 2025 before-and-after) with captions.
- [x] The 2025 Product Read API post is worked as the central example and tied to Kestrel & Pine's stock sync chain and the two-hour lag of 27 November 2026, with the 30-minute figure attributed to Zalando.
- [x] A "Where the evidence stops" section precedes "What to Take Away"; the three take-away tiers are present and honest; 6–10 questions to ask; the closing hands off to [[case-composable-movement]].
- [x] One short paragraph says what Kestrel & Pine takes from the case, tied to W1 and W5 and to the Deprecated Endpoint of February 2027.
- [x] No "Across Scale Stages" section (Part XI); length 4,500–6,000 words.

## Non-goals

- Architecture styles compared in general — [[commerce-architecture-styles]].
- The book's contract, versioning, webhook and deprecation rules — [[api-contracts-and-versioning]]; this chapter supplies the Zalando specimen only.
- Events, outbox, idempotency and reconciliation as techniques — [[events-consistency-and-reconciliation]]; the chapter uses the 2025 post as evidence, not as a tutorial.
- Marketplace selling mechanics and the Zalando partner API as a channel — [[marketplaces-and-channel-integration]].
- Team topologies and governance for a merchant — [[organizing-commerce-engineering]]; multi-brand and acquisition questions — [[commerce-scaling-stages]].
- Agentic commerce protocols and the merchant's readiness list — [[ai-and-agentic-commerce]].
- Any description of Zalando's current service inventory, order or pricing architecture, or ZEOS internals.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- McKinsey's 2018 interview with Eric Bowman timed out on 7 November 2026; it may contain a first-hand account of the 2018–2019 reorganization that would let the "return to discipline" framing cite a declared program rather than a sequence of posts.
- The reconciliation between "over 60" fulfillment merchants (December 2025) and "over 600" B2B partners (annual report) is the brief's reading; a reviewer with access to Zalando investor relations could confirm the scopes.
- The open-source status table will drift; re-check archive and last-change dates before any print edition.

## Decision log

- **2026-11-07** — Gave the 2025 event-to-API post its own section and diagram rather than one row in the discipline table, because it is the single Zalando document most useful to a merchant and maps directly onto Kestrel & Pine's stock sync chain; rejected treating it as a footnote to the Nakadi story.
- **2026-11-07** — Wrote the guidelines as a three-column table with a "what to demand of a vendor" column, because the chapter's reader is a merchant on the receiving end of APIs, not a platform publishing them; rejected quoting the rules as a list.
- **2026-11-07** — Framed the 2018–2026 changes as "narrowing a choice each time" and stated explicitly that Zalando never declared the end of Radical Agility, rejecting the commissioned framing of a 2019 "reorganization" that no source supports.
- **2026-11-07** — Included the open-source status table as evidence of what survived, because archive notices are dated primary statements and the pattern (pieces with outside users survived) is a transferable warning.

## Sources

- **Internal**
  - `_research/brief-cases-amazon-zalando.md` (Part B, Part C, key numbers, open questions) — every Zalando fact and its tag.
  - `_research/scenario-ledger.md` — the Zalando channel, the stock sync chain, the Black Friday figures, the Deprecated Endpoint, W1, W5, W7, W8, the team of fourteen.
  - [[case-amazon]] — the companion case; the chapter reads the two agent stories together.
  - [[api-contracts-and-versioning]], [[events-consistency-and-reconciliation]], [[commerce-architecture-styles]], [[organizing-commerce-engineering]], [[commerce-scaling-stages]], [[ai-and-agentic-commerce]] — owning chapters linked rather than re-taught.
- **External**
  - Zalando Engineering blog posts 2015–2026 (Radical Agility on AWS; On APIs and the API Guild; Data Integration in a World of Microservices; From Jimmy to Microservices; Four Lessons; Tech Radar; One Year Later; Third Generation Microservices; Principles over Frameworks; Tech Radar Update 2020; Sunrise; From Event-Driven to API; Agentic Identity Broker) — the architecture record.
  - Zalando RESTful API and Event Guidelines; Tech Radar; GitHub repositories (Skipper, Patroni, Nakadi, Zalenium, STUPS) — governance rules and project status.
  - Zalando corporate pages 2020–2025, FY2025 fact sheet and Annual Report 2025; ABOUT YOU press release 2025 — the platform strategy and figures.
  - InfoQ (2016, 2016, 2018), Diginomica (2016), ChannelX (2023), Retail Gazette (2023), FashionUnited (2026) — secondary accounts where primary pages were absent.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
