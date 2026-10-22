---
status: accepted
revised: 2026-10-22
---

# Spec: One Dossier, One Account: Integrating an Acquired Product Portfolio

## Intent

Show a Chief Architect how to turn a portfolio of acquired vehicle data and dealer software products into one platform without stopping any of them. The chapter argues for a small shared kernel first (who the customer and person are, which car, what was used, whether it was allowed), sequenced by dependency and by customer-visible milestones, with each element moving through link, migrate and retire. It closes Axleby's One Dossier Year 1 at the December 2027 board checkpoint, presents **capability map v2** relative to v1 of [[vehicle-capability-map]], and introduces an **acquisition integration contract** so the next acquisition joins a platform rather than starting a program. It owns the terms **portfolio integration** and **capability map v2**.

Productscape bricks covered (as integration targets, not as features): `iden`, `bill`, `dgov`, `vidn`, `dosr`, plus the `acquisitions` stressor of the digest's residuality model.

## Audience

Chief and group architects, CTOs and platform leads of groups built by acquisition; product directors who must give up capabilities to shared services; deal teams who need the integration cost of a target.

## Success criteria

- [ ] Reader can name the five integration depths and say when each is right, using a trade-off table.
- [ ] Reader can state the kernel (who, which car, what used, whether allowed) and the dependency order among identity, tenant directory, vehicle key, meter, license check and events, with a diagram.
- [ ] Reader can distinguish link, migrate and retire, and the three mappings (people, customers, vehicles) with their evidence rules, including why a shared VAT number must not merge customers.
- [ ] The Axleby example uses ledger numbers (Velto 58 records and 19 invoices, census counts, AVK backfill 97.2%, login counts) and an integration scorecard by product.
- [ ] Capability map v2 is defined relative to v1 (39 → 40 capabilities) with canonical counts recorded in the ledger.
- [ ] Public evidence is dated and labeled: Cox layers (2018–2026), CDK/Keyloop separation (2021), Mobility Global transition services (2026), VWE XRAY and ATC (2026), Auto Trader's Autorama reporting (2026); inferences marked.
- [ ] Failure handling covers duplicates, wrong merges, dual-running conflicts, incomplete records, partial migration failures and kernel outages.
- [ ] A requirements table gives consistency, latency, freshness and availability per kernel interaction.

## Non-goals

- Building each kernel element: [[identity-access-and-entitlements]], [[tenancy-and-dealer-groups]], [[vehicle-identity]], [[billing-and-metering]], [[data-licensing-and-governance]], [[events-webhooks-and-sync]].
- Strangler mechanics, parallel runs and API client sunset: [[modernizing-the-platform]].
- Whether to build, buy or partner each capability: [[build-buy-or-partner]].
- Team design: [[organizing-engineering]].
- The full Cox, CDK, Auto Trader and VWE histories: Part X cases.
- No "Across Markets" section (Part IX); market variation appears through the map's market flags.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should the integration contract appear as a template in [[toolkit]]?
- Whether Showroomly is eventually replatformed onto Lotwise is left open to 2029, with the flip condition stated.

## Decision log

- **2026-10-22** — Framed the kernel as four questions rather than as a list of systems, so the rule survives renaming and future acquisitions.
- **2026-10-22** — Defined v2 by changes and counts against v1 (added A13 and F7, merged D2 into D1, moved A9 to shared, drew level 3 for A1, A8 and F2, added tier and adoption columns) rather than reprinting all 40 rows.
- **2026-10-22** — Used the customer census's 14 wrong merges as the central failure, because it ties portfolio integration to The Tenant Blur and the Cross-Tenant Lead.
- **2026-10-22** — Included two separations (CDK/Keyloop, Mobility Global) as evidence that kernels must stay separable; rejected treating Cox as the only model.

## Sources

- **Internal**
  - [[vehicle-capability-map]] — capability map v1 and its counts.
  - [[identity-access-and-entitlements]], [[tenancy-and-dealer-groups]], [[onboarding-and-configuration]] — Velto and Hartley migrations, tenant directory, Runway and Baseline.
  - [[vehicle-identity]], [[inventory-and-vehicle-dossier]] — AVK backfill and dossier.
  - [[billing-and-metering]], [[events-webhooks-and-sync]] — Meterline shadow run and event backbone.
  - [[case-cox-automotive]], [[case-cdk-global]], [[case-auto-trader-uk]], [[case-vwe]] — public cases.
- **External**
  - Cox Automotive Bridge ID page and 2026 Fullpath release; Apollo GraphQL customer story; Amazon 2018 release.
  - CDK Global Form 10-K FY2021; Keyloop 2021 release.
  - Mobility Global Information Statement (2026) — transition services and duplicated IT.
  - VWE XRAY release (2026); Journal de l'Automobile on ATC (2026).
  - Auto Trader FY2026 results.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: tier counts made explicit (E2 not offered carries no tier, item 29); red-capability count corrected to seven of eight; sold-audit wording aligned with events-webhooks-and-sync; American spelling. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: customer census counts three billing systems (Connect XML invoice run, Lotwise Classic, Showroomly), consistency item 34. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
