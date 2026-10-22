---
status: accepted
revised: 2026-10-22
---

# Spec: Volumes, Peaks and Paid Lookups: Scalability and Operating Cost

## Intent

Show where a vehicle data and dealer SaaS platform has to scale, and what it costs to serve a lookup, a rooftop, a publish and a report. The chapter argues that load arrives in a few nameable **workload shapes** that need their own lanes and upstream budgets. It also argues that the cost of a data call is mostly **paid upstream data**, so license-aware caching, fetch coalescing and per-call-path costing move the unit cost more than compute tuning. After reading, an architect can take an average cost per lookup apart, find the loss-making tail, and design the broker, cost meter and attribution that keep it visible.

Productscape bricks covered: all (the chapter is cross-cutting: cost and capacity of every brick), with emphasis on vidn (specification build data), vapi (data API traffic and batch), bill (metering), advf (syndication operations) and occm (dealer stock).

## Audience

Chief architects, platform and SRE leads, data-product leads and the finance or FinOps partners who work with them in vehicle-data companies and dealer-software vendors. They know cloud cost basics. They need the vehicle-specific part: paid upstreams, license-limited caching, no-hit rules, shared register quotas and bundled reports.

## Success criteria

- [ ] Names and quantifies the workload shapes (interactive, batch burst, nightly, Monday edits, month-end registration, consumer spikes, market ingestion) with ledger volumes and labeled assumptions.
- [ ] Decomposes the €0.031 lookup by call path and by component, with arithmetic that adds up, and shows the miss/no-hit tail.
- [ ] Gives a worked example (the Saturday Batch) with revenue versus cost.
- [ ] Presents an architecture (lanes, upstream budget broker, license-aware cache, cost meter) with at least two diagrams and a requirements table.
- [ ] Covers duplicates, concurrent misses, incomplete records, retry storms, meter gaps, outages and cold caches, and runaway clients.
- [ ] Includes trade-off tables for data purchase/caching/pricing and for capacity strategies, with a conditional recommendation.
- [ ] Has an evidenced "Across Markets" table (NL/BE, DE, UK, US).
- [ ] Labels every non-ledger volume, latency and cost as an assumption.

## Non-goals

- Metering pipeline design, rating, credits and invoices: [[billing-and-metering]].
- License register and purpose checks: [[data-licensing-and-governance]].
- Degraded modes, SLOs and dependency budgets: [[reliability-and-dependencies]].
- Telemetry and support tooling: [[observability-and-data-operations]].
- Specification resolution itself: [[specification-and-equipment]].
- Dealer and data business economics in general: [[dealer-and-data-economics]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No vehicle-data provider's per-call price or caching clause is public; all upstream figures are Axleby illustrations or assumptions.
- The ledger's "350,000 nightly restock valuations" sits oddly with 19 million valuations a year; the chapter avoids annualizing it.
- UK plate-change peaks (March, September) are stated as industry practice; no official source was fetched.

## Decision log

- **2026-10-22** — Defined "the €0.031 lookup" as a fully loaded blended average and built the chapter on its decomposition, rather than as a pure compute cost, because the point is that compute is a tenth of the cost.
- **2026-10-22** — Chose an insurer batch (Rijnstaal) as the opening incident instead of a dealer peak, because it shows workload shape, upstream cost and flat pricing failing together.
- **2026-10-22** — Made the build-data license retention clause (30 days) the root cause, so the fix is a procurement and Charter decision, not only a cache change.
- **2026-10-22** — Kept the batch surcharge out of Lotwise (dealers stay in the interactive lane and plan) to respect the per-rooftop pricing model.

## Sources

- **Internal**
  - [[meet-axleby]], [[dealer-and-data-economics]], [[specification-and-equipment]], [[billing-and-metering]], [[data-licensing-and-governance]], [[reliability-and-dependencies]], [[listing-syndication]], [[observability-and-data-operations]].
  - `_research/brief-platform-apis-operations.md` (Parts 1.6, 4.2–4.4, 5, 7), `_research/brief-saas-tenancy-billing.md` (1.4, 1.5, 7.1–7.2).
- **External**
  - FinOps Foundation: Unit Economics, Allocation, FOCUS.
  - Microsoft Learn: tenant consumption measurement (2024), noisy neighbor (2025).
  - AWS Builders' Library: fairness (2020), caching (2019); S3 Intelligent-Tiering.
  - DVSA MOT history API limits; DVLA VES; RDW open data; NHTSA vPIC; OWASP API4:2023; OpenTelemetry metrics guidance; AutoScout24 Karpenter (2024).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: arithmetic and ledger figures checked; Odolo price marked VAT-inclusive; timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
