---
status: accepted
revised: 2026-10-22
---

# Spec: From Portal Enquiry to Dealer System: Routing a Lead End to End

## Intent

Walk one buyer's enquiry end to end: from a portal (webhook, cursor pull or ADF e-mail) through Switchboard's intake, normalization, matching, deduplication and routing, into the Lotwise inbox and a DriveDesk CRM queue through Hitch, and back as acknowledgement, first human response, portal status and attribution. The chapter adds what only the journey view shows: who owns each hop, which identifiers cross each boundary, the consistency and latency each hop needs, and what each hop must confirm before the next one starts. It tells the full **Lost Leads of Velto** (September 2027), including how the incident was discovered (a buyer's phone call on day 9), why each hop reported success, the recovery (deduplicated, marked redelivery from Switchboard's own store) and the changes by hop. The reader should leave able to define "delivered" for every target, design a dead-letter process that cannot lose a lead, and prove a lead journey works with metrics taken from outside it.

Owns: **lead acknowledgement** (the four-rung ladder A0 Accepted, A1 Delivered, A2 Acknowledged, A3 Answered) and **dead-letter review**. Productscape brick: `dweb` (sales lead, "follow-lead" journey step); the DMS side is a gap in the model.

## Audience

Chief architects, integration leads and product directors of dealer-software vendors and dealer groups who run lead delivery into CRMs and DMS products they do not control. They know idempotency, queues and read-after-write; they need the hop-by-hop contract, the acknowledgement model and a worked incident.

## Success criteria

- [x] Sequence diagram of the success path; a second sequence diagram of the failed path; a dead-letter flow diagram.
- [x] Hop table with owner, identifiers crossing, consistency and latency for nine hops; a timeline table replaying one lead on the old and the new path.
- [x] Defines lead acknowledgement as four rungs with evidence and lifecycle effect, and registers the highest provable rung per target.
- [x] Tells the Lost Leads of Velto from discovery to recovery with ledger numbers (46 rooftops, 9 hubs, 3 closed rooftops, 1,460 leads, 9 days) and labeled illustrations; consistent with [[leads-and-crm]], [[dms-integration]], [[tenancy-and-dealer-groups]] and [[observability-and-data-operations]].
- [x] Covers at least six failure cases (silent acceptance, closed rooftop, duplicate from two channels, lead for a sold car, CRM outage, consent missing, plus ambiguous timeout and out-of-order follow-up), each with detection and recovery.
- [x] Defines dead-letter review with reason codes, owners and rules.
- [x] Trade-off table, journey metrics table, "What Changes in Another Market", Chief Architect's view and questions.
- [x] Article at or under 8,000 words; every external claim dated and sourced.

## Non-goals

- The lead model, deduplication levels, routing-rule language, consent law per market and attribution rules ([[leads-and-crm]]).
- Hitch's adapters, xref map, command receipts in general and the full DriveDesk Outage ([[dms-integration]]).
- Tenant hierarchy and restructuring operations ([[tenancy-and-dealer-groups]]); Baseline configuration ([[onboarding-and-configuration]]).
- The lead-flow monitor's design and Pitwall ([[observability-and-data-operations]]); the event backbone ([[events-webhooks-and-sync]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No public source describes how any portal or CRM vendor implements lead delivery internally; the chapter's design is reference-architecture judgement.
- Velto's conversion and gross-profit figures for the late cohort are illustrative; no industry benchmark for lead-to-sale conversion in the Benelux was found.
- Whether a misrouted-and-deleted lead is a notifiable breach depends on the controller's risk assessment; the chapter records Velto's judgement, not a rule.

## Decision log

- **2026-10-22** — Told the incident as a walk of one lead through every hop rather than as a timeline, because the leads, DMS and tenancy chapters already explain each component and the journey view is what only this chapter can add.
- **2026-10-22** — Made the inactive target one DriveDesk queue (the former brand-cluster queue), matching the ledger's "an inactive DriveDesk CRM queue", and explained why closed rooftops kept receiving leads (stock still booked there, portal accounts, tracking numbers, website pages).
- **2026-10-22** — Set the Hitch cut-over for lead delivery on 25 October 2027, before the DriveDesk Outage, so that the outage's automatic fallback to the Lotwise inbox in [[reliability-and-dependencies]] and [[dms-integration]] is explained by the journey.
- **2026-10-22** — Kept Switchboard's 2027 stock-state source as the nightly export, consistent with the sold audit in [[events-webhooks-and-sync]].

## Sources

- **Internal**
  - [[leads-and-crm]], [[dms-integration]], [[tenancy-and-dealer-groups]], [[observability-and-data-operations]], [[onboarding-and-configuration]], [[events-webhooks-and-sync]], [[listing-syndication]].
  - `_research/brief-syndication-leads.md`, `_research/brief-dms-integration.md`, `_research/scenario-ledger.md`.
- **External**
  - mobile.de Lead API (2026) and summer 2026 update; Marktplaats LMS documentation (n.d.); ADF 1.0 (2000).
  - Sonic Automotive 8-K (2024); AutoNation 10-Q (2024); AutoScout24 tech blog on critical user interactions (2024); Pied Piper via Auto Remarketing (2025).
  - GDPR Articles 4(12) and 33; BetrVG § 87; PECR regulation 22.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Lost Leads volume aligned with the [editor] ledger line (hub-sized stock of about 1,100 cars under three old rooftop codes; consistency item 27). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
