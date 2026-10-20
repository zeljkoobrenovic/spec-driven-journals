---
status: accepted
revised: 2026-10-20
---

# Spec: From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved

## Intent

Give the book a dated, sourced industry timeline and teach the reader to read a marketplace group's architecture as the **sediment** of its corporate history. The chapter divides the industry into five waves (print columns, online pioneers, portfolio building, consolidation, take-privates and break-ups), gives the public record for each, and shows what each wave left in the systems: pioneer monoliths, country copies, acquired national stacks, inherited parent technology, shared enabling platforms, partially converged product platforms and carve-out residue. It owns the terms *industry timeline* and *portfolio model*. The central argument is that capital strategy sets platform topology and changes faster than platforms do, so separability belongs in every group platform. After reading, an architect can ask of any system "which strategy deposited this, and does it still hold?" and can design shared platforms that survive a change of owner.

## Audience

Chief and enterprise architects of marketplace groups, technology leaders integrating acquisitions or preparing carve-outs, and engineering directors who inherit landscapes they did not design.

## Success criteria

- [x] A reference timeline table of dated events from 1977 to 2026, each with a source and year; no unverified company internals.
- [x] Each wave (print, pioneers, Schibsted, eBay, Naspers/OLX, verticals, consolidation, take-privates) has documented examples and a "what it left in the systems" reading, with inferences labeled.
- [x] Owns and defines portfolio model, copy-paste market entry, convergence, take-private, carve-out and TSA, and introduces "architectural sediment".
- [x] Veldmark worked example: the fictional history mapped to the waves, using ledger numbers (Yardstick, four category trees, three search engines, acquisitions, private-equity owner, Common Ground) and a separability rule per shared capability.
- [x] Trade-off tables for growth strategies and for platform topology versus capital strategy; a vertical-differences table.
- [x] Three mermaid diagrams; Chief Architect's view; questions to ask; Sources and Evidence grouped by kind.

## Non-goals

- Marketplace models and the endpoint ladder ([[marketplace-taxonomy]]).
- Liquidity economics and why leadership is local ([[liquidity-and-network-effects]]); stated briefly only.
- The full Adevinta, OLX, eBay Classifieds and AVIV stories ([[case-adevinta]], [[case-olx]], [[case-ebay-classifieds]], [[case-aviv]]).
- Payment, shipping and buyer-protection design ([[transactions-and-payments]]).
- The method for consolidating platforms and designing multi-country platforms ([[platform-consolidation]], [[multi-country-platforms]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Schibsted "Blocket platform" and copy-paste rollout are reported only through secondary sources (Nieman Lab 2012, not retrieved); a primary Schibsted source would let the chapter state it as fact.
- Whether Adevinta's leboncoin–Kleinanzeigen "unified global platform" was delivered is not public; the chapter says so.
- mobile.de ownership after the 2025 dual-track process is unclear (Bundeskartellamt names "Oak Germany Buyer GmbH" in October 2026); re-check before publication.
- AVIV's integrated platform: scope and extent are not public.
- Founding dates for craigslist, Rightmove and Auto Trader rest on Wikipedia (secondary); primary confirmation would strengthen the timeline.

## Decision log

- **2026-10-19** — Organized the chapter by waves rather than by company, so companies appear as evidence for architectural questions, consistent with the book's company-neutral stance.
- **2026-10-19** — Introduced "architectural sediment" and a sediment register as the chapter's practical tool, linking history to decisions rather than narrating it.
- **2026-10-19** — Wrote Veldmark's fictional history (newspaper origin of Tradeyard, copy-paste Belgium and Portugal, acquired Poland, Motorvane's single vertical platform) to mirror the waves; appended the new canonical facts to the scenario ledger.
- **2026-10-19** — Treated the transactional pivot only as a thread through the consolidation wave and handed it to [[transactions-and-payments]].

## Sources

- **Internal**
  - [[meet-veldmark]], [[marketplace-taxonomy]], [[liquidity-and-network-effects]], [[business-capabilities]], [[case-adevinta]], [[vertical-requirements]].
  - Research briefs: adevinta, olx, ebay-classifieds, real-estate-portals, automotive, monetization-economics.
- **External**
  - Adevinta annual reports 2019 and 2023, strategic report 2025, press releases 2021–2024, tech blog 2023–2024.
  - eBay 8-K (2004) and releases (2008, 2015); eCG brand pages (snapshots); Marktplaats Technology (2015); Berlin Tech Blog (2019, 2025).
  - OLX Tech (2018, 2023, 2026), OLX Group releases (2020, 2026), Naspers (2022), News24 (2023), Wamda (2020).
  - Rightmove and Autotrader results (2026); Immowelt (2015); KKR (2025); Online Marketplaces (2021, 2025, 2026); Scout24 (2025); AutoScout24 (2025); Vinted (2022, 2026).
  - CMA decision (2021); Bundeskartellamt (2026); NYU Stern on Seamans and Zhu (2013); Parker (2010); Wikipedia entries for founding dates.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: timeline checked against the six case pages; eight countries; AVIV CEO quote corrected (no "unified"); mobile.de and Marktplaats 2004 dates separated; OLX Autos revenue dated; Central Asian sales as agreements; separability decision record dated March 2027. *(AI-mediated session)*
- **2026-10-19** — Editor: reconciled with multi-country-platforms (copies folded back into one codebase 2016–2018, origin of the country branches). *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,848 → 7,837 words; excerpt and first KEY POINT now name the chapter's own five waves (no separate "land-grab" wave); lead names what the chapter builds on and which chapters use it; "What Wave 1 left in the systems" made a subheading like Waves 2 and 3; teaser first sentences replaced with each paragraph's point. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
