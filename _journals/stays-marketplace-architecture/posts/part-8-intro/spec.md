---
status: accepted
revised: 2026-10-22
---

# Spec: Part VIII — PLATFORM: The Distributed System Underneath

## Intent

Orient the reader to Part VIII: the platform beneath both marketplaces (events, scale and reliability, metrics, experimentation, machine learning and demand channels), the judgement every chapter reaches in its own terms (share the machinery, keep the meaning per marketplace), where hotels and homes load the platform differently, and which question each of the six chapters answers. Frame the part through Corvane's 2027 platform decisions: Gauge, Kiln, Experimentation Standard v1, the event backbone, Lantern and Gangway, and the Black Friday degradation.

Productscape domains: framing for the event, reliability, data, experimentation, ML and channel domains (the part intro covers no bricks of its own; chapters 37–42 cover them).

## Audience

Chief architects, platform and data engineering leads, ML platform owners and distribution engineering leads of accommodation and hosted-stays marketplaces deciding which Part VIII chapter to read for the decision in front of them.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS THIS PART ADDRESSES callout using exact pattern names, linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument: the platform is where a group can share the most and where sharing goes wrong most quietly; share the machinery, keep the semantics.
- [ ] A short paragraph names where hotels and homes differ (look-to-book and search cost, ARI firehose and cancellations vs one-unit interference, hosts as natural persons, payout seasonality) and notes convergence.
- [ ] One diagram (illustrated) with a Figure caption: channels, offer and reservation contracts, event backbone, Gauge, experimentation, Kiln and journey objectives.
- [ ] Corvane (labeled fictional) uses only figures from chapters 37–42: €412,000 and 2,870 reservations in the shadow run, 40 minutes in D2 with the hit rate falling from 94% to 71%, 51.0 million bookings, the badge's vanished and shrunken wins, €38,400 absorbed after Tideline, 41% one-engine dependence, 1,400 shopping requests per booking, 435,000 alternative accommodations.
- [ ] Each chapter paragraph names the real platforms the chapter cites (Agoda, Booking.com, Airbnb, Expedia/Vrbo) without new claims.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, with what it decides, its Corvane case and when to read it.
- [ ] Names [[part-9]] and hands off to [[event-driven-stays]]; 500–900 words of body.

## Non-goals

Teaching any chapter's content: event contracts and the outbox ([[event-driven-stays]]), journey objectives and degradation ([[global-scale-and-reliability]]), governed metrics and partner insight ([[marketplace-intelligence]]), delayed outcomes and interference ([[stays-experimentation]]), the feature platform and model governance ([[stays-ml-platform]]) and channel architecture ([[demand-channels]]). No new external facts; the chapters carry the sources.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-21: Modeled on this book's Part I and Part VII intros: one paragraph per chapter, the Corvane thread compressed to one paragraph listing the 2027 platform decisions in date order.
- 2026-10-21: The first key point is the "share the machinery, not the meaning" judgement, because every chapter's Hotels and Homes section reaches it (ARI streams, degradation contents, supply metrics, experiment defaults, models and channel strategy stay per brand).
- 2026-10-21: Failure patterns chosen by how many chapters name them: Built for Sunny Days (38, 41, 42), The Unwatched Model (39, 40, 41) and Phantom Availability (37, 38, 41, 42). Ledgerless Money was left out because only chapter 37 carries it.
- 2026-10-21: The diagram shows the data loop (contracts → events → metrics → experiments and models → back to the offer) with journey objectives guarding it, at eight nodes; Fathom, Pricegrid and Waypoint are left to the chapters.

## Sources

Internal: [[event-driven-stays]], [[global-scale-and-reliability]], [[marketplace-intelligence]], [[stays-experimentation]], [[stays-ml-platform]], [[demand-channels]] (callouts, leads, Corvane worked examples, Hotels and Homes sections and Chief Architect's views), [[where-stay-platforms-go-wrong]], [[meet-corvane]]; `_research/scenario-ledger.md`; `_research/style-guide.md`.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: €412,000 cause aligned with chapter 37 (lost, read-back and duplicate events); 1,400 worded as shopping requests per gross reservation; 41% dependence worded as last external click. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 964 → 956 prose words; outline unchanged; argument sentence made a direct bold claim, Roomstead named as the OTA in the Hotels and homes paragraph, global-scale chapter paragraph split for readability; spec unchanged. *(AI-mediated session)*
