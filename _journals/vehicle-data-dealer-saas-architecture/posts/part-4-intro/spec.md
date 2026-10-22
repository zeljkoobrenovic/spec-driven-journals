---
status: accepted
revised: 2026-10-22
---

# Spec: Part IV — DEALER: The Used-Car Workflow

## Intent

Orient the reader to Part IV: each step of the used-car workflow is a recorded decision or a legal act on one stock item, and every boundary to a system the platform does not control (portals, CRMs, registers, DMS, auction partners) needs intent, a receipt and reconciliation. Frame the part through Velto Mobility Group and DriveDesk (the Zombie Golf, the Thursday run, the Lost Leads of Velto, the DriveDesk Outage) and each chapter's own case.

Productscape bricks: the union of the part's chapters (tapp, occm, dosr, advf, dweb, admn, finc, rdwt, impx, mats, bpmc, b2bt; DMS integration is a gap the book adds).

## Audience

Chief architects, dealer-SaaS product and engineering leaders, and integration leads.

## Success criteria

- [ ] Opens with the standard callouts, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names.
- [ ] States the argument (decisions and legal acts recorded with reasons; intent, receipt and reconciliation at every boundary) and the Velto thread.
- [ ] Axleby numbers match the ledger and chapters (7,200 rooftops, 4 portals for 4 days, 1,460 leads, 1,240 cars, 12-day DriveDesk outage, 214 double submissions, 17 cars sold twice, 23% of sampled purchases).
- [ ] One mermaid diagram with a Figure caption.
- [ ] A one-sentence summary per chapter (ten chapters) in config order, each linking the chapter and naming its case.
- [ ] Hands off to [[vehicle-acquisition]]; [[connected-vehicle-data]] hands off here.
- [ ] Body after the callouts stays short (about 500–800 words; the whole page about 900–1,050, in line with BOOKED and LISTED part introductions).

## Non-goals

Teaching appraisal, pricing, syndication, lead routing, VAT schemes, register transactions or DMS integration (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-22: One sentence per chapter instead of a paragraph, because the part has ten chapters and the intro must stay short.
- 2026-10-22: Failure patterns: The Zombie Listing, The Leaky Lead and DMS Hostage, the patterns unique to this part; Borrowed Uptime and The Confident Valuation are left to the chapters.
- 2026-10-22: The diagram follows one stock item and marks the arrows that leave the platform.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, Setting the Scene sections and closing paragraphs of the ten chapters from [[vehicle-acquisition]] to [[b2b-trade-and-remarketing]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: corrected the Zombie Golf summary (DMS sold row unmatched, then deletes stuck in Relay). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
