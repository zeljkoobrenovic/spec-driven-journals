---
status: accepted
revised: 2026-10-22
---

# Spec: Data as a Product: Designing Vehicle Data APIs

## Intent

Show how a vehicle data provider should expose identity, registration, specification, history and valuation data to software vendors, lessors, insurers and portals. The chapter's argument: the unit of sale is a **category block** with its own price, license, freshness and outcome; a thin **response composer** assembles blocks from the internal contexts that own them and reports failures per block; one outcome vocabulary (hit, partial, no hit, failed, plus current, stale or unavailable) drives the response, the meter and the service level; and an **API contract registry** holds one canonical description from which both legacy XML and JSON are rendered, with dated per-client version pins, automated change classification and per-client usage evidence that decides deprecations. After reading, the reader can design the request and response shape, the error semantics, the versioning and deprecation policy and the migration path for a legacy XML interface.

The chapter owns **response composer**, **category block** and **API contract registry**.

Productscape bricks covered: `vapi` (Vehicle Data API Gateway: developer portal, API gateway, response composer, API contract registry), with its edges to `rdwc`, `vidn`, `valu`, `dgov` and `bill`.

## Audience

Chief architects, API platform leads and data-product managers at vehicle-data companies and at dealer-software groups that sell data by API. They know REST, OpenAPI and gateways; they need the vehicle-specific decisions (plate versus VIN keys, outcome-dependent pricing, license per block, freshness of register copies, slow-moving integrator clients) and a defensible policy for change and sunset.

## Success criteria

- [x] The reader can explain the four product shapes (lookup, report, batch, change feed) and why the lookup's block model makes the others cheap.
- [x] Category block, response composer and contract registry are defined, with the composer's boundary (assembly, not data or hit classes) stated and tied to the 7.4% disagreement in Axleby's April 2027 inventory.
- [x] A response example shows per-block outcome, freshness, sources, fact version and Charter's license block; an error-semantics table separates business answers (200) from transport failures and maps each to metering.
- [x] Versioning models (Google AIP, Stripe 2017 and 2024, Azure) are compared with dated sources; Axleby's choice (path major plus dated per-client pins, two breaking releases a year, 12-month field notice, Deprecation and Sunset headers) is justified; semantic, code-list and privacy changes are treated as breaking.
- [x] The portal, scenario-vehicle sandbox and an SLA definition for composed answers are covered.
- [x] An Axleby worked example (Fleetmoor's four-block return lookup, €5.22 at list) uses ledger prices and the No-Hit Credit rules; the Connect XML facade and sunset milestones are given.
- [x] Failure handling covers duplicate requests, duplicate vehicles, conflicting facts, incomplete records, upstream outages, retry storms, renderer drift, transform bugs and corrections.
- [x] Trade-off tables (product shape; legacy coexistence), a requirements table, three mermaid diagrams and an Across Markets table (NL/BE, DE, UK, US) are present.

## Non-goals

- Webhooks, event feeds and their delivery contract ([[events-webhooks-and-sync]]).
- License register and purpose-check internals; the chapter only consumes Charter's decision and license block ([[data-licensing-and-governance]]).
- Usage events, rating and no-hit definitions in depth ([[billing-and-metering]]).
- Batch-lane economics and the upstream budget broker ([[scale-and-cost]]); file enrichment products ([[data-products-and-insights]]).
- Credential types and API-client authorization ([[identity-access-and-entitlements]]); enumeration defense ([[vehicle-platform-security]]).
- The organizational side of migrating 210 XML clients ([[modernizing-the-platform]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The Autotrader Connect change from 404 to 200 for failed vehicle lookups had a sandbox date (11 September 2026) and a scheduled date of 30 November 2026; whether it shipped on that date should be rechecked.
- The IETF RateLimit header fields are still an Internet-Draft (-11, May 2026); revisit if they become an RFC or change shape.
- `events-webhooks-and-sync` places "the public gateway" in Q3 2028 alongside webhooks; this chapter puts the v2 lookup contract live in October 2027. The reading here is that Q3 2028 is the event and webhook gateway; reconcile if the reviewer reads it otherwise.
- No public source describes any provider's internal response composition or per-client field-usage telemetry; the design is reference architecture throughout.

## Decision log

- **2026-10-22** — Opened with an April 2027 two-stack inventory (57 XML response profiles, 7.4% field disagreement on 20,000 plates) instead of re-telling the No-Hit Credit, which [[billing-and-metering]] owns; the inventory shows the contract problem as well as the metering problem.
- **2026-10-22** — Chose two independent labels per block (outcome from the context, freshness from the composer) to align with [[vehicle-history]]'s hit classes, Meterline's outcomes and [[reliability-and-dependencies]]'s freshness labels.
- **2026-10-22** — Recommended a facade over the new composer for Connect XML rather than keeping the legacy back end or forcing migration, with the condition (210 clients, 33 months) under which it pays off.
- **2026-10-22** — Rejected GraphQL-style field selection for external clients because license, price and freshness are per block; stated as judgement.

## Sources

- **Internal**
  - [[meet-axleby]] — two API stacks, 640 clients, 210 XML-only, sunset 31 December 2029.
  - [[billing-and-metering]], [[data-licensing-and-governance]], [[scale-and-cost]], [[vehicle-history]], [[vehicle-identity]], [[specification-and-equipment]], [[reliability-and-dependencies]], [[events-webhooks-and-sync]], [[case-auto-trader-uk]], [[case-vwe]], [[case-cdk-global]].
  - `_research/brief-platform-apis-operations.md` Part 1, 4.3, 6.1; `_research/brief-saas-tenancy-billing.md` Parts 4 and 7; `_research/brief-case-autotrader-carfax-vwe.md` 1.4, 3.5; `_research/brief-identity-registers.md` 1.2.
- **External**
  - Autotrader Connect developer documentation (read October 2026); VWE API documentation page.
  - Stripe versioning posts (2017, 2024); Google AIP-180, 181, 185; Microsoft Azure REST guidelines.
  - RFC 9457, RFC 9745, RFC 8594; IETF RateLimit header draft -11; OpenAPI 3.1; JSON Schema 2020-12; STAR; NHTSA vPIC.
  - DVSA MOT history API rate limits; DVLA VES API description; RDW open data.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: named the v2 milestones (lookups October 2027, webhooks Q3 2028), expanded acronyms, American spelling, timetoread. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (defense). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
