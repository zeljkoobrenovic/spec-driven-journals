---
status: accepted
revised: 2026-11-07
---

# Spec: Monolith, Modular Monolith, Microservices, Composable: What the Evidence Says

## Intent

Give a reader new to commerce architecture a plain-language map of the four internal architecture styles (monolith, modular monolith, microservices, composable) and an honest reading of the famous examples behind them, so that they can judge a rebuild proposal instead of being carried by its vocabulary. The chapter's position is that a style is a choice about deployment units and boundaries, that the documented splits (Amazon 2001, Zalando 2015) and the documented refusal to split (Shopify 2019–2024) describe companies with thousands of engineers and carry dated costs, and that a merchant's own code should be split into exactly as many pieces as it has teams that must release independently. After reading, Noor Visser can answer a board member's "are we behind?" with evidence rather than reassurance.

## Audience

Newcomers to commerce architecture. The engineer or engineering lead who has just inherited a merchant's platform and is being pitched a composable or microservices rebuild benefits most; the product manager or executive who must judge that pitch benefits next. The chapter assumes the reader knows roughly what an API, a database and a queue are, and defines deployment unit, boundary, data ownership, system of record, eventual consistency, monolith, modular monolith, microservices, composable, MACH, strangler migration, PIM, OMS, WMS, PSP and iPaaS where they first appear.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The four styles are defined by deployment unit, data ownership and boundary enforcement, in a table and a diagram, before any company example.
- [x] Each company account (Amazon, Zalando, Shopify, Segment, Prime Video, MACH) carries its publication year, its evidence age, what it shows and what it does not show; no inferred internals are presented as fact.
- [x] The two-sided Shopify record is reported honestly: the 2019 componentization intent and the 2024 Packwerk retrospective's findings (removed privacy checks, runtime blind spots, boundaries not matching runtime, "discussed removing Packwerk").
- [x] The costs of microservices (distribution, eventual consistency, operational complexity) are tied to three concrete promises in Eva's order in a requirements table, and the people cost is quantified from public sources (Netflix, Uber, Segment, Zalando).
- [x] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage, and the "What to Take Away" section has the three tiers.
- [x] The Kestrel & Pine thread agrees with the ledger: the February 2027 review's composable rebuild option (about €3.2M, 18 months) versus stay-and-surround (about €1.33M; Waypoint €1.1M), 14 in technology, 9 engineers, the Black Friday figures; The Giant's Boots is named as the pattern.
- [x] Two mermaid diagrams with captions; "When it goes wrong" with detection and recovery; eight Questions to ask; a hand-off to [[multi-tenancy-and-isolation]]; article at or under 6,500 words including tables.

## Non-goals

- The platform landscape and what each vendor sells — [[commerce-platform-landscape]]; the composable movement as a case — [[case-composable-movement]].
- Shopify, Amazon and Zalando as full cases — [[case-shopify]], [[case-amazon]], [[case-zalando]]; this chapter uses only the architecture-style evidence.
- Integration styles, events, idempotency and reconciliation in depth — [[integration-styles]], [[events-consistency-and-reconciliation]].
- Build, buy or assemble decision criteria and TCO — [[build-buy-or-assemble]]; replatforming mechanics — [[replatforming-and-migration]].
- Team design in depth — [[organizing-commerce-engineering]]; multi-tenancy, which the next chapter owns.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Shopify's component and package counts after 2024, and whether the modular-monolith program continued, are undocumented; a reviewer should check whether a newer first-party retrospective has appeared.
- The primary text of the 2006 Vogels interview could not be fetched; the chapter relies on the 2007 High Scalability digest and AWS's 2006 relay. If the primary becomes fetchable, quote it directly.
- The MACH Alliance's principles page may change again; the chapter dates the three-principle formulation to November 2026.

## Decision log

- **2026-11-07** — Treated composable as a style alongside the three internal styles, but framed it explicitly as a buying style whose distribution costs land on the merchant's integration layer, rather than leaving it to the landscape chapter; this is what makes The Giant's Boots apply to composable as well as to a microservices rebuild.
- **2026-11-07** — Reported Shopify through the 2024 Packwerk retrospective rather than the 2019 announcement, so that the modular monolith appears as a seven-year learning rather than a slogan; rejected the alternative of presenting Shopify simply as "the modular monolith that worked".
- **2026-11-07** — Set the Kestrel & Pine scene as a board question after the February 2027 platform review (ledger addition by `build-buy-or-assemble`) rather than inventing a second rebuild proposal, so that the €3.2M rebuild figure and W4 stay canonical.
- **2026-11-07** — Expressed the chapter's rule as "one deployment unit per team that must release independently" and added three disciplines (ownership first, cheap boundary gate, split only on measured evidence), each anchored in a public source, instead of a generic "start with a monolith".

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the cast, Waypoint W4, the Black Friday figures and the February 2027 review's cost figures.
  - [[boundaries-and-systems-of-record]] — the ownership-first argument the chapter leans on.
  - `_research/brief-platform-engineering-scale.md` (Part 1), `_research/brief-shopify.md` (Part 2), `_research/brief-cases-amazon-zalando.md` (A1, A7, B1, B4), `_research/brief-platform-landscape.md` (Part 3) — the dated company evidence.
- **External**
  - Shopify Engineering, *Deconstructing the Monolith* (2019), *Under Deconstruction* (2020), *A Packwerk Retrospective* (2024), *How Shopify Reduced Storefront Response Times with a Rewrite* (2020) — the modular-monolith record.
  - Henning Jacobs, *One Decade in Zalando Tech* (2020); Zalando Engineering posts of 2015, 2020, 2023 and 2025 — the microservices split and the later discipline.
  - High Scalability, *Amazon Architecture* (2007); AWS News Blog (2006); the Dynamo paper (2007) — Amazon's move to services.
  - Martin Fowler, *Microservice Trade-Offs* and *MonolithFirst* (2015); Lewis and Fowler, *Microservices* (2014) — the costs and the boundary warning.
  - Uber Engineering (2020), Segment (2018), InfoQ on Prime Video (2023), Netflix (2016) — the people and operations costs and the consolidations.
  - MACH Alliance documents (2020, 2023, 2025, 2026) and commercetools documentation (accessed 2026-11) — composable as a style and its stated costs.
  - Melvin Conway (1968); Team Topologies key concepts (accessed 2026-11) — team-sized modularity.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: applied the item 13 ruling (consultancy composable pitch, agency headless pitch, suite as a costed option), expanded MACH, ERP, WMS, PIM, iPaaS, AWS on first use, defined idempotent handling, corrected two Zalando and Shopify quotations against the sources, fixed the incidents row (Price Drift and Double Refund under W5), nine engineers in the key points, American spelling. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
