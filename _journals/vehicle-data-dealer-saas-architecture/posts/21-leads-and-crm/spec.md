---
status: accepted
revised: 2026-10-22
---

# Spec: Every Enquiry Counts: Lead Capture, Routing and CRM

## Intent

Show how a dealer SaaS platform should capture, normalize, deduplicate, match, route and deliver leads from portals, dealer websites, ADF/XML e-mail and phone calls, into its own inbox or into CRMs and DMS products it does not control, and how outcomes flow back to portals and to attribution. The chapter defines the lead as a buyer's interest in a car at a rooftop, separate from its interactions and from the prospect; compares the public lead contracts of mobile.de, Marktplaats/2dehands, Auto Trader, ADF 1.0 and STAR's 2025 Sales Lead API; and turns them into the Switchboard reference architecture: durable intake, a canonical lead event, three-level deduplication, routing rules as validated configuration against the tenant directory, delivery with read-back, a lead lifecycle, consent as data and attribution. The reader should leave able to design a lead pipeline in which a routing change fails loudly instead of silently and every enquiry can be accounted for from arrival to outcome.

Owns: **lead**, **lead routing**, **ADF/XML**, **lead attribution**. Productscape brick: `dweb` (Dealer Website and Lead Capture: lead inbox, lead API, lead store, portal lead adapter). **[ADDED]**: CRM integration (in-house inbox versus external CRM).

## Audience

Chief architects, product directors and integration leads of dealer software vendors, portals and dealer groups who run or buy lead handling across several portals and CRMs. They know webhooks, queues and idempotency; they need the automotive lead contracts, the group-routing problem, the consent rules per market and the delivery and attribution design.

## Success criteria

- [x] Defines enquiry event, lead, interaction and prospect, and separates the four owned terms clearly; places the prospect per dealer legal entity, never across tenants.
- [x] Explains ADF 1.0 from the specification (minimum lead, id chain, resend, e-mail transport, interpretation drift) with a short example, and positions STAR's 2025 Sales Lead API.
- [x] Compares portal lead contracts (mobile.de, Marktplaats/2dehands, Auto Trader, US ADF) on delivery semantics, routing data and status write-back, with dated sources.
- [x] Presents Switchboard with a stage diagram, a responsibility table, three-level deduplication, a requirements table, routing order and validation, a routing decision diagram and a lifecycle state diagram.
- [x] Covers delivery modes (inbox, external CRM, both), delivery with read-back through Hitch, outcome write-back, attribution and consent per market (GDPR Art. 6(1)(b), ePrivacy Art. 13, UWG § 7, PECR reg. 22, TCPA).
- [x] Uses response-time evidence (HBR 2011, Pied Piper 2025, mobile.de 2026) with its age stated, and an Axleby latency budget labeled as assumption or illustration.
- [x] Introduces the Lost Leads of Velto without retelling the journey, and works an attribution example at Autobedrijf Brandsma with labeled illustrative figures.
- [x] Covers duplicates, out-of-order events, incomplete records, leads for sold cars, closed targets, silent acceptance, CRM outage and conflicting status; includes trade-offs, Across Markets, the Chief Architect's view and questions.

## Non-goals

- The hop-by-hop journey of one lead, lead acknowledgement and dead-letter review ([[journey-lead-to-dms]]).
- DMS adapter mechanics, the xref map and command receipts ([[dms-integration]]).
- Tenant hierarchy, restructuring and isolation ([[tenancy-and-dealer-groups]]); configuration inheritance ([[onboarding-and-configuration]]).
- Conversations, safety checks and lead delivery from the portal's side (LISTED's [[messaging-and-leads]]).
- Lawful basis and retention analysis per market ([[privacy-and-retention]]); deals, financing and quotes ([[deals-and-sales-documents]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The STAR Sales Lead API schema and its relation to ADF were not read; the chapter uses only the June 2025 announcement.
- No independent European lead-response study was found; no verified CRM market shares exist for Europe or the US.
- Whether the EU existing-customer exception (ePrivacy Art. 13(2)) covers an enquiry without a sale depends on national law; the chapter flags it rather than resolving it.
- Public lead contracts for AutoScout24 and US portals were not found; the chapter does not describe them.

## Decision log

- **2026-10-22** — Opened with Velto's hub reorganization and the routing request, and introduced the Lost Leads of Velto only to pose the design question, because [[journey-lead-to-dms]] owns the full incident.
- **2026-10-22** — Made cross-source deduplication a link, not a merge, because dealers pay portals per lead and attribution needs every touch.
- **2026-10-22** — Placed routing rules in Baseline and validation against the tenant directory in Switchboard, consistent with [[onboarding-and-configuration]] and [[tenancy-and-dealer-groups]]; delivery to DMS-vendor CRMs through Hitch, consistent with [[dms-integration]].
- **2026-10-22** — Verified the consent rules directly against the ePrivacy Directive, UWG § 7, PECR regulation 22 and 47 CFR 64.1200, since the research briefs did not cover marketing follow-up law.

## Sources

- **Internal**
  - [[listing-syndication]] — adverts that produce leads; the Zombie Golf.
  - [[dms-integration]] — Hitch, receipts and the DriveDesk Outage.
  - [[tenancy-and-dealer-groups]], [[onboarding-and-configuration]] — tenant directory and Baseline.
  - [[observability-and-data-operations]] — the lead-flow monitor.
  - `_research/brief-syndication-leads.md`, `_research/brief-dms-integration.md`, `_research/brief-connected-data-privacy-regulation.md`, `_research/scenario-ledger.md`.
- **External**
  - ADF 1.0 (2000); Kelley Blue Book ADF usage guide (2014); STAR Sales Lead API announcement (2025).
  - mobile.de Lead API (2026) and summer 2026 update; Marktplaats LMS documentation and Lead Delivery Webhook v3.2.0; Auto Trader developer documentation.
  - GDPR; Directive 2002/58/EC; UWG § 7; PECR 2003 regulation 22; 47 CFR 64.1200.
  - HBR (2011); Pied Piper via Auto Remarketing (2025); Auto Trader FY26 results (2026); Car Dealer Magazine (2025).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Lost Leads of Velto aligned to the editor ledger line (hub-sized stock under three old rooftop codes, deactivated brand-cluster queue); acronyms expanded; unverifiable mobile.de pilot figures hedged. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
