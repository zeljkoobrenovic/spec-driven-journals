---
status: accepted
revised: 2026-10-20
---

# Spec: Map What the Marketplace Does Before What Runs It

## Intent

Give the reader a working method for describing a listing marketplace by its business capabilities, independently of systems, teams and org charts, and for using that description to decide what a multi-brand group should share, split or keep local. The chapter must define capability, value stream, product and system precisely; offer a reusable three-level marketplace capability map (ten level-1 areas); cross-map it to four value streams (list-to-sell, search-to-contact, lead-to-deal, pro onboarding); and teach heat-mapping on three separate scores (differentiation, maturity, duplication). The central claim: duplication alone proves nothing, and most good answers come from splitting a capability at level 3 into shared machinery and local content.

## Audience

Chief and enterprise architects of marketplace groups, platform and product leaders preparing a consolidation or platform program, and integration leads after an acquisition. They should leave able to draft a group capability map in weeks, run a scored heat map with evidence, and defend the verdicts in front of brand CTOs and a CFO.

## Success criteria

- [ ] Capability, value stream, product, system and process are distinguished in a table, with marketplace examples and owners.
- [ ] A three-level map is given: ten level-1 areas matching the PLAN, level-2 capabilities for each, and level-3 examples that show the machinery/content split.
- [ ] Four value streams are defined with stages and outcome metrics, and at least one is cross-mapped to capabilities with a Veldmark example using ledger timings (Rotterdam city bike).
- [ ] Heat-mapping uses three separately scored dimensions, a maturity scale with evidence rules, and a verdict table that includes "keep separate on purpose".
- [ ] The Veldmark worked example finds five overlaps that agree with the ledger's "four of everything", plus the Poland commercial overlap and the Keybridge deliberate duplicate, and shows how the map changed Common Ground's sequence.
- [ ] Documented public examples are dated and sourced (Adevinta 2023/2024/2025, Rightmove 2025 results, Autotrader FY26, Vinted 2026); no company internals are invented.
- [ ] Includes a trade-off table of mapping approaches, a vertical-differences table, failure modes, the Chief Architect's view and questions to ask.

## Non-goals

- Software decomposition, context maps and aggregates — owned by [[bounded-contexts]].
- The business-model taxonomy (classifieds, lead-gen, transactional) — owned by [[marketplace-taxonomy]].
- Liquidity metric definitions — owned by [[liquidity-and-network-effects]].
- The full shared-versus-specific vertical analysis — owned by [[vertical-requirements]].
- Consolidation sequencing after acquisitions — owned by [[platform-consolidation]]; team design — owned by [[organizing-marketplace-engineering]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The TOGAF capability definition is now paraphrased, not quoted (the guide is behind a login and could not be re-read, 2026-10-19).
- The OMG value-stream sentence is quoted as Wikipedia quotes the OMG BAWG *Business Architecture Overview* (2012); a primary BIZBOK or OMG source would be stronger.
- Should the toolkit's capability-map template reproduce all 54 level-2 capabilities, or only the level-1 frame?

## Decision log

- **2026-10-19** — Made level 3 the place where verdicts are decided ("share the machinery, keep the content") rather than treating level 2 heat-map colors as final, because duplicated-and-differentiating cells otherwise lead nowhere.
- **2026-10-19** — Defined the five Veldmark overlaps as the ledger's "four of everything" (identity, T&S, search, product catalog, data) so the chapter confirms, then refines, what the board already knew; added the Poland dealer clash as a commercial overlap and Keybridge as a deliberate duplicate to show what platform-only maps miss.
- **2026-10-19** — Used the Productscape reference models' shared 88-capability skeleton as evidence that one map serves all verticals, labeled as the author's generic models, not company fact.
- **2026-10-19** — Rejected an org-first or systems-inventory-first mapping method as the recommended approach; both are presented in the trade-off table.

## Sources

- **Internal**
  - [[meet-veldmark]] — Veldmark brands, Common Ground and cast.
  - [[marketplace-taxonomy]], [[liquidity-and-network-effects]] — business models and liquidity metrics this chapter builds on.
  - [[bounded-contexts]] — the next chapter, which turns the map into a decomposition.
  - `_research/productscape-digest.md` — reference capability models, value streams and review lessons.
  - `_research/brief-monetization-economics.md`, `_research/brief-adevinta.md`, `_research/brief-platform-data-ml.md`.
- **External**
  - The Open Group, *TOGAF Series Guide: Business Capabilities, Version 2* (2022) — capability concept.
  - Lewis and Fowler, "Microservices" (2014); Conway, "How Do Committees Invent?" (1968) — capability-aligned services and Conway's law.
  - DDD Crew, Core Domain Charts — separating differentiation from complexity.
  - Adevinta Annual Report 2023 and Tech Blog (2024); Rightmove 2025 results; Autotrader FY26 results; Vinted Engineering (2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: TOGAF definition paraphrased, OMG value-stream quote verified via its Wikipedia citation, Strategic Report 2025 dated 2026 and linked, toolkit link added. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 6 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,921 → 5,853 prose words; lead rewritten to place the chapter in Part I (builds on industry-evolution, taxonomy and liquidity; feeds bounded-contexts, vertical-requirements, platform-consolidation); internal "digest" references replaced with first-person reference-model wording; question and teaser first sentences turned into claims; no headings renamed, no spec criteria changed. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
