---
status: accepted
revised: 2026-10-22
---

# Spec: Seeing the Platform: Observability, Data Quality Operations and Support

## Intent

Show how a vehicle data and dealer SaaS platform knows that it, and the data inside it, is healthy per tenant and per channel. The chapter argues that this domain's costly failures return success at every hop (an adapter's 200, a CRM queue that accepts and discards, a supplier batch that loads cleanly with wrong units), so service monitoring must be complemented by **business-flow monitors** measured against confirmed external outcomes, by **data monitors** (freshness, volume, distribution, linkage) with blocking gates on paid-output sources, and by tenant- and channel-aware telemetry at controlled cardinality. It defines **publish lag** with evidence levels per channel, makes "Unknown" an explicit flow state, and presents the **support console** as flow monitors plus audit trails filtered to one tenant and object.

Productscape bricks covered: `dosr` (dossier timeline as an observability and support source), `advf` (channel delivery status). Also addresses digest gaps 6 (observability and SRE) and 7 (data quality operations).

## Audience

Chief architects, heads of platform and SRE, integration leads and data-platform leads at vehicle-data companies and dealer-software vendors who already run standard monitoring and need to design detection for silent flow and data failures across many external integrations and thousands of tenants.

## Success criteria

- [ ] Reader can distinguish service, flow and data health and name the signals and detection times for each.
- [ ] Reader can define publish lag, its four evidence levels, and why withdrawal lag gets its own target.
- [ ] Reader can design a flow record with an explicit Unknown/ambiguous state for syndication, leads and register transactions.
- [ ] Reader can apply a tenant-tagging standard that keeps metrics low-cardinality and keeps personal data and tenant context out of telemetry and third-party calls.
- [ ] Reader can specify data contracts and a blocking batch gate, and explain why the first median gate would not have caught the Odometer Correction and the per-workshop-chain check would.
- [ ] Reader can specify a support console's views and its access and audit rules.
- [ ] Chapter includes the Axleby publish-lag worked example with ledger-consistent numbers, a requirements table, a trade-off table, the Across Markets table, two mermaid diagrams, failure handling and Questions to ask.

## Non-goals

- Retries, circuit breakers, degraded modes and journey SLO definitions (`reliability-and-dependencies`).
- Syndication design and the desired-state Relay rebuild (`listing-syndication`).
- The provenance model and correction propagation (`provenance-and-data-quality`, `journey-data-correction`).
- Valuation drift monitoring internals (`valuation-engine`).
- Security monitoring and threat detection (`vehicle-platform-security`); retention schedules (`privacy-and-retention`).
- Observability cost economics in depth (`scale-and-cost`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public source describes how any dealer-software vendor or portal measures end-to-end publish lag; the evidence levels are a labeled reference design. Revisit if a portal or vendor publishes one.
- Belgian rules on employee monitoring (collective agreements) were not verified; the Across Markets table covers NL and DE works-council law only.
- Whether portal partner terms permit read-back sampling varies by portal and was not verified per portal.

## Decision log

- **2026-10-22** — Framed the chapter around "success at every hop" failures (Zombie Golf, Lost Leads of Velto, Odometer Correction) rather than a generic observability survey, because standard monitoring is assumed knowledge for the audience.
- **2026-10-22** — Made publish lag evidence-based (confirmed, accepted, file delivered, read-back) instead of adapter-response-based; rejected canary adverts on live portals as usually against portal terms.
- **2026-10-22** — Chose tenant ids on traces, logs and flow events with only tier and market on metrics, after computing the 5.27-million-series cardinality of a rooftop-labeled publish metric.
- **2026-10-22** — Included employee-monitoring law (NL WOR art. 27(1)(l), DE BetrVG §87(1) no. 6, US Safeguards Rule logging) in Across Markets, because it changes product defaults for per-salesperson metrics and support-console audit.

## Sources

- **Internal**
  - [[reliability-and-dependencies]], [[listing-syndication]], [[provenance-and-data-quality]], [[journey-data-correction]], [[journey-lead-to-dms]], [[tenancy-and-dealer-groups]], [[inventory-and-vehicle-dossier]], [[events-webhooks-and-sync]], [[data-licensing-and-governance]], [[privacy-and-retention]], [[vehicle-platform-security]].
  - `_research/brief-platform-apis-operations.md` (Parts 3, 4.4, 7, 8); `_research/scenario-ledger.md`; `_research/productscape-digest.md` gaps 6 and 7.
- **External**
  - Google SRE book, *Monitoring Distributed Systems* (2016) — golden signals, symptoms vs causes, black-box monitoring.
  - AutoScout24, *SLOs for Critical User Interactions* (2024) — journey-level SLO practice in an automotive marketplace.
  - Auto Trader UK Connect documentation (n.d.) and Auto Trader Engineering (2026) — per-message notifications; quarantine of failed events.
  - OpenTelemetry docs and CNCF project page — span links, baggage leakage, cardinality, graduation date.
  - GDPR Art. 33; 16 CFR 314.4; BetrVG §87; WOR art. 27 — notification and monitoring rules by market.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Odometer Correction gate aligned with consistency item 17 (median gate as the insufficient first version, per-workshop-chain check as the fix); RabbitMQ named for the 2027 Lotwise Classic path; timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
