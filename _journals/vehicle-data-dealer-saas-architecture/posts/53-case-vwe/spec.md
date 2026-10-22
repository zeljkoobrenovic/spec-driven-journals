---
status: accepted
revised: 2026-10-22
---

# Spec: VWE: A Dutch Vehicle Data Company Becomes a Dealer Platform

## Intent

Read VWE Automotive's public, dated record as an architecture case: a Dutch register-access provider that grew into data products and a dealer workspace, and that is now buying, selling and changing owners. The case must show what a strong-register market does to a platform (the register as moat and dependency), what per-licensor XML schemas say about licensing and harmonization, and what acquisitions, a divestment and a pending majority sale ask of identity, billing and partner contracts. Because VWE publishes no architecture, the chapter is equally a lesson in how far an architect may reason from a product surface: every internal claim is a labeled inference, every gap is listed, and public-record discrepancies are reported, not resolved.

The book's research started from the author's own public-source Productscape model of VWE. The chapter says so once and never presents that model's bricks, modules, stores or KPIs as VWE's internals.

Productscape bricks touched (as research map, not as VWE structure): `rdwc`, `rdwt`, `vidn`, `vapi`, `dgov`, `bill`, `iden`, `occm`, `tapp`, `vhis`, `mins`, `cool`, `b2bt`, `bpmc`, `fnnk`; residuality stressors `rdwoutage`, `freedata`, `portalconsolidation`, `acquisitions`, `privacy`.

## Audience

Chief architects and engineering leaders of vehicle-data and dealer-software groups, especially in the Benelux; investors' technical advisers assessing a buy-and-build platform. They should leave able to judge a register-dependent platform from the outside and to name the spines a buy-and-build group must share.

## Success criteria

- [ ] Every VWE claim carries a dated public source; undated product pages are cited as "read October 2026".
- [ ] The Productscape model is disclosed as the author's research map and nothing from it is presented as VWE internals; all internal reasoning sits in `INFERENCE, NOT DOCUMENTED` callouts or is marked "my reading".
- [ ] Public-record discrepancies are stated: XML-only public API documentation versus a product page mentioning JSON; 10,000+ vs 11,000+ customers; 100+ vs 150+ channels; founding year; Main Capital closing unconfirmed as of 22 Oct 2026.
- [ ] A dated timeline, a "Where the Public Evidence Stops" table, a trade-off table and four mermaid diagrams.
- [ ] The contrast with Axleby is explicit: a table of differences and a statement that Axleby is not a disguised VWE; Axleby numbers match the ledger.
- [ ] A short comparison of what changes outside the Netherlands (BE, DE, UK, US).
- [ ] A Chief Architect's view with decision rules and 6–10 questions to ask.

## Non-goals

- Re-teaching the Dutch register model ([[registers-and-official-data]]), register transactions ([[registration-and-trade-services]]), billing ([[billing-and-metering]]) or licensing ([[data-licensing-and-governance]]).
- Any claim about VWE revenue, volumes, uptime, technology stack or incidents (none is public).
- Main Capital's reported CarCollect stake (not verified from a public, dated source in this session).
- Competitor analysis beyond what frames VWE's position.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Did the Main Capital transaction close, and did the ACM clear it? Update the timeline when a completion notice appears.
- Is the JSON plate API mentioned on the Vehicle characteristics page documented anywhere public?
- The weDAT release (13 Oct 2026) describes DAT Nederland as part of VWE; ownership share is not stated. Verify before strengthening the claim.
- "Voorraad Nederland" and Cargo International's contribution were not checked.

## Decision log

- **2026-10-22** — Structured on the BOOKED Booking.com case (timeline, evidence limits, trade-offs, failure modes, evidence stops, Chief Architect's view, pattern and fictional-company comparison) rather than the Part II–VII chapter shape, because Part X cases need visible evidence discipline.
- **2026-10-22** — Drew Figure 1 only from edges stated on public pages (sources → product surfaces) instead of reusing the research model's dependency graph, to avoid presenting the model as VWE's architecture.
- **2026-10-22** — Added an explicit VWE-versus-Axleby difference table because Axleby shares Dutch-market traits (register provider, XML legacy API, PE ownership since 2022) that could otherwise be read as a disguise.
- **2026-10-22** — Made divestment the sharpest lesson for Axleby, since One Dossier plans only for joining products.

## Sources

- **Internal**
  - [[registers-and-official-data]], [[registration-and-trade-services]], [[reliability-and-dependencies]] — register model and degradation.
  - [[vehicle-data-apis]], [[specification-and-equipment]], [[data-licensing-and-governance]] — API, harmonization, licensing.
  - [[billing-and-metering]], [[privacy-and-retention]], [[b2b-trade-and-remarketing]], [[one-platform-from-many-products]] — pricing, privacy, partner hand-offs, integration.
  - [[case-auto-trader-uk]] — API contrast; [[domain-coverage]] — the research model.
  - `_research/brief-case-autotrader-carfax-vwe.md` (Part 3–5), `_research/productscape-digest.md`, `_research/scenario-ledger.md`.
- **External**
  - VWE product pages (homepage, Over VWE, MijnVWE, Occasion Manager, Finnik Zakelijk, Schadeverleden, Marktinzicht, lead generator, API documentation, Vehicle characteristics), read October 2026.
  - VWE releases 2022 (NewPort, AVN), 2025 (Financial Lease Partner), 2026 (XRAY, Main Capital, weDAT).
  - Main Capital Partners and William Blair, 2026; ACM decision ACM/22/179803, 2022; Journal de l'Automobile on the ATC sale, 2026; AutoRAI on AutoScout24, 2025.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: unwrapped four mermaid blocks from code fences, aligned the authorized-information-provider wording (items 13/23) and the UK register row (item 14), reading time corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
