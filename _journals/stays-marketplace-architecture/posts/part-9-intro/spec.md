---
status: accepted
revised: 2026-10-22
---

# Spec: Part IX — LEADERSHIP: The Chief Architect's Agenda

## Intent

Orient the reader to Part IX: the decisions that belong to the group rather than to any one domain (convergence, organization and governance, modernizing a live monolith, AI across the stay, and evolving the platform over a decade), the judgement the chapters share (the Chief Architect's main product is a small set of governed records), where hotels and homes still differ at this level, and which question each of the five chapters answers. Frame the part through Corvane's late-2027 decisions: the AI use-case register and Frontdoor v2, One Stay Org Design v1, the register's first annual review, the Keystone Exit Plan and the five fitness functions.

Productscape domains: framing for the group-level architecture, organization, modernization, AI and evolution concerns (the part intro covers no bricks of its own; chapters 43–47 cover them).

## Audience

Group chief architects, CTOs, VPs of engineering and architecture-forum members of travel groups that run an accommodation marketplace, a hosted-stays marketplace or both, deciding which Part IX chapter to read for the decision in front of them.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS THIS PART ADDRESSES callout using exact pattern names, linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument: the Chief Architect's main product is a small set of governed records (register, ownership catalog, migration plan, AI register, fitness functions), not one-off decisions.
- [ ] A short paragraph names where hotels and homes still differ (room-type inventory vs one calendar per home, PMS copies vs host apps, 18- vs 41-day median booking windows) and acknowledges convergence.
- [ ] One governance-loop figure with a Figure caption: board question → convergence register → org design, Keystone Exit Plan and AI register → fitness functions → back to the register (plus one slogans-to-records figure).
- [ ] Corvane (labeled fictional) uses only figures from chapters 43–47: €145 million; 16/6/26 → 23/6/20; about 1,750 engineers in 190 teams; 5.6 million future reservations and 31,400 differences; 23 AI uses, 8 without an owner; nine stressors; five fitness functions.
- [ ] Naming is consistent with the chapters: the group metric layer is Gauge; Plumbline (the reconciliation service) is not named here.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, with what it decides, its Corvane case and when to read it.
- [ ] Names [[part-10]] and hands off to [[converging-two-marketplaces]]; 500–900 words of body after the callouts.

## Non-goals

Teaching any chapter's content: the convergence register and routing rule ([[converging-two-marketplaces]]), team topology, decision classes and supplier on-call ([[organizing-stays-engineering]]), parallel runs and in-flight reservation migration ([[modernizing-a-live-marketplace]]), tool contracts, booking authority and AI governance ([[ai-in-travel-stays]]), and stressor analysis and fitness functions ([[evolving-the-platform]]). No new external facts; the chapters carry the sources.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-21: Modeled on this book's Part VII and Part VIII intros: one paragraph per chapter, the Corvane thread compressed to one paragraph listing the late-2027 decisions in date order.
- 2026-10-21: The first key point restates chapter 43's sharing rule because every later chapter applies it; the second (contracts outlast engines) joins chapters 45, 46 and 47; the third (records, not slogans) is the part's argument.
- 2026-10-21: Failure patterns chosen by how many chapters name them: The Hotel-Shaped Home (43, 47), Lost at the Front Desk (44, 45) and The Unwatched Model (44, 46). Built for Sunny Days and City-by-City Firefighting were left out because only chapter 47 carries them.
- 2026-10-21: The diagram shows the governance loop (register → owners, migration and AI controls → fitness functions → register) at seven nodes; Stayline, Kiln and Frontdoor are left to the chapters.

## Sources

Internal: [[converging-two-marketplaces]], [[organizing-stays-engineering]], [[modernizing-a-live-marketplace]], [[ai-in-travel-stays]], [[evolving-the-platform]] (callouts, leads, Corvane scenes and worked examples, Hotels and Homes sections and Chief Architect's views), [[where-stay-platforms-go-wrong]], [[meet-corvane]]; `_research/scenario-ledger.md`; `_research/style-guide.md`.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 914 → 881 prose words; lead paragraphs merged (the part-scope sentence restated IN THIS PART); Figure 1 caption no longer repeats the lead; spec criterion updated from mermaid diagram to the two figures the visual pass added. *(AI-mediated session)*
