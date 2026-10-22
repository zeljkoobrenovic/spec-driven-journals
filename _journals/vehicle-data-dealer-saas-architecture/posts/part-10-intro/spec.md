---
status: accepted
revised: 2026-10-22
---

# Spec: Part X — PRACTICE: How Others Built It

## Intent

Orient the reader to Part X: four publicly documented companies as architecture cases, the stricter evidence rules the cases follow (documented fact with source and publication year, the author's marked reading, `INFERENCE, NOT DOCUMENTED` callouts, "read October 2026" for undated pages, vendor case studies as vendor numbers), and a contrast of the four positions, problems and evidence bases.

Productscape bricks: none directly; the VWE case explains the public-source model, mapped in [[domain-coverage]].

## Audience

Chief architects and engineering leaders who want the book's patterns tested against real companies, and who read vendor and investor material critically.

## Success criteria

- [ ] Opens with the standard callouts, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names.
- [ ] Explains the case-study evidence rules consistently with each case's "How to Read This Case" section.
- [ ] Contrasts the four cases in a table (position, hardest problem, best evidence, where the evidence stops) that agrees with each case's own "Where the Public Evidence Stops" table.
- [ ] Every company fact in the intro appears, with its date, in the case it summarizes.
- [ ] One line per case in config order, linking each case.
- [ ] Hands off to [[case-cox-automotive]]; the last chapter of Part IX hands off here.
- [ ] Body after the callouts stays short (about 500–800 words; the whole page about 900–1,050, in line with BOOKED and LISTED part introductions).

## Non-goals

New company facts not in the cases; reference-architecture inference; Axleby comparisons (each case owns its own).

## Modalities

Article only for now.

## Open questions

- `evolving-the-vehicle-platform`, the last chapter of Part IX, was not yet written on 2026-10-22; its closing paragraph should hand off to [[part-10]].

## Decision log

- 2026-10-22: A comparison table replaces the diagram, because the four cases differ in evidence more than in flow.
- 2026-10-22: Failure patterns: The Acquisition Archipelago, DMS Hostage and Borrowed Uptime, each documented by at least two cases.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, and the callouts, leads, "How to Read This Case" and "Where the Public Evidence Stops" sections of [[case-cox-automotive]], [[case-cdk-global]], [[case-auto-trader-uk]] and [[case-vwe]]. No external factual claims beyond those cases.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: format, links and claims checked against the four cases; reading time corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 0 mermaid diagrams to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
