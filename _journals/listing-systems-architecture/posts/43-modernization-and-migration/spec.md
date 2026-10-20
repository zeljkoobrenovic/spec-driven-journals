---
status: accepted
revised: 2026-10-20
---

# Spec: Changing the Engine in Flight: Modernizing a Live Marketplace

## Intent

Show architects how to retire a marketplace monolith while it keeps serving buyers, sellers, partners and search engines. The chapter owns three terms — **migration stage gate**, **relevance parity** and **URL migration** — and argues that migration happens by slice behind seams (edge, BFF, events, branch by abstraction), that parity means equal outcomes rather than identical features or results, and that every slice passes measured gates with a rehearsed rollback and an explicitly decided point of no return. The Veldmark thread is the Yardstick exit plan, consistent with the ledger milestones (insertion Q2 2028, search Q4 2028, decommissioning end of 2029) and with Yardstick Relay in [[event-driven-listings]].

## Audience

Chief and principal architects, engineering directors and platform leads who own or inherit a legacy listing platform and must plan its replacement under traffic, SEO and revenue constraints. They know the strangler fig by name; they need the marketplace-specific mechanics and gate criteria.

## Success criteria

- [ ] Reader can choose between rewrite, re-platform and incremental re-architecture, with the Scout24 contrast.
- [ ] Reader can name the four seams of a listing site and the transitional components (relay, Legacy Mimic writer) with their end dates.
- [ ] Reader can define five stage gates with numeric exit criteria and rollback per gate.
- [ ] Reader can design a search migration with layered relevance parity (analyzers, replay, shadow, non-inferiority experiment) and explain why identical results are the wrong target.
- [ ] Reader can apply Google's site-move guidance and the "do not change URLs because the platform changed" rule.
- [ ] Documented, dated evidence (Marktplaats 2015, Kleinanzeigen 2019 and 2025, Vinted 2023–2024, AutoScout24 2016, Scout24 2019, Subito 2023, Kleinanzeigen rebrand 2023, Adevinta 2026) is used without inventing internals.
- [ ] Veldmark numbers match the ledger and neighbouring chapters (Relay, CloudFront routes, OpenSearch order with Portugal first, Tally shadow billing, Veldmark ID 2028).
- [ ] Includes trade-off and vertical tables, failure modes, Chief Architect's view, questions and sources.

## Non-goals

- Event contract design, outbox and CDC mechanics — [[event-driven-listings]].
- Search engine choice and index design — [[search-architecture]].
- URL service, redirect registry and landing pages — [[web-and-seo-architecture]].
- Account and identity migration design — [[identity-and-verification]].
- Post-acquisition consolidation sequence — [[platform-consolidation]]; team design — [[organizing-marketplace-engineering]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Veldmark should lift the remaining 2029 slices to AWS rather than rebuild them if wave 5 slips (contingency not yet decided).
- No classifieds company has published a complete URL-migration post-mortem with traffic data; revisit if one appears.
- The Kleinanzeigen 2025 post does not name the new platform; do not attribute it to an Adevinta group platform.

## Decision log

- **2026-10-19** — Defined relevance parity as non-inferiority on contacts per search session, with overlap reported but not gated.
- **2026-10-19** — Kept accounts out of Yardstick Exit and inside the Veldmark ID slice, to avoid migrating accounts twice.
- **2026-10-19** — Added the Amsterdam colocation end date (31 December 2029) as the reason the decommissioning date is hard.
- **2026-10-19** — Ordered waves read paths first, insertion second, search third, messaging and Safe Deal last, because the last depend on accounts.

## Sources

- **Internal**
  - [[event-driven-listings]], [[search-architecture]], [[web-and-seo-architecture]], [[publication-pipeline]], [[products-and-entitlements]], [[saved-searches-and-alerts]], [[case-adevinta]].
  - `_research/brief-platform-data-ml.md` Part 1; `_research/brief-ebay-classifieds.md` Parts 3.1, 5.1, 5.2; `_research/scenario-ledger.md`.
- **External**
  - Fowler, *Strangler Fig Application* (2024) and *Branch By Abstraction* (2014); Cartwright, Horn and Lewis, *Patterns of Legacy Displacement* (2024).
  - Google Search Central, *Site moves with URL changes* (updated 2026).
  - Marktplaats (2015), Berlin Tech Blog (2019, 2025), Vinted (2023, 2024), InfoQ (2016), Computerwoche (2019), Adevinta (2023, 2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: American spelling; figure caption spacing; Vinted Vespa figures re-verified. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,419 → 5,467 prose words; lead now ties the chapter to Part VIII (after consolidation and organization) and names what depends on it; Vinted and URL paragraphs reordered point-first; no headings renamed; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Excerpt lists all five stage gates, starting with contract, to match the body and glossary. *(AI-mediated session)*
- **2026-10-20** — Term alignment with the glossary: "projection" → "read model", "copy register" → "consumer registry", "filter compiler" → "query compiler", where they occur on this page. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 2: kept attempt 1: prints the words 'START' and 'END' beside the start and end dots (otherwise correct); Figure 3: kept attempt 4: 'CDC' arrow dashed instead of solid; 'Yardstick PHP monolith'–'Yardstick MySQL' line has an arrowhead; MySQL box icon is a dolphin resembling the MySQL logo. *(AI-mediated session)*
