---
status: accepted
revised: 2026-10-22
---

# Spec: When the Register Is Down: Reliability With External Dependencies

## Intent

Show how a vehicle data and dealer SaaS platform stays useful when the registers, data suppliers, portals and DMS vendors it depends on fail. The chapter turns Borrowed Uptime into design rules: a dependency map with criticality per (journey, dependency) pair; journey SLOs with three outcomes (good, degraded, bad) that count upstream failures and attribute them; a dependency budget that limits synchronous dependencies on critical paths; and a catalog of named degraded modes (labeled copy, partial answer, honest queue, local system of record, fail fast). It covers timeouts and deadline propagation, one retry point with jitter and a budget, success/failure/ambiguous outcome classes for writes with legal effect, read-before-retry, circuit breakers driven by a shared health state and a session monitor, bulkheads per supplier, push-fed mirrors, supplier SLAs versus measured reality, communication from the health state, and game days. The reader should leave able to review a journey's dependency chain and require a budget line and an exercised degraded mode for every synchronous external call.

Owns: **journey SLO** (vehicle), **degraded mode**, **dependency budget**. Productscape bricks: `rdwc` (register session monitor), `rdwt` (transaction retry queue); stressor `rdwoutage`.

## Audience

Chief architects, platform and SRE leads, and integration leads of vehicle-data companies and dealer-software vendors. They know timeouts, retries and circuit breakers in general; they need the domain-specific split between information and transaction dependencies, the register and DMS failure behavior, and a way to govern dependencies at group scale.

## Success criteria

- [ ] Opens with the Month-End Register Outage (31 March 2027, 5 h 40 min, 3,100 queued, 214 double submissions) told as a timeline whose cause is the missing ambiguous-outcome class, consistent with the ledger.
- [ ] Defines journey SLO, dependency budget and degraded mode, with a criticality-tier table and a degraded-mode catalog including what each must never be used for.
- [ ] Includes a dependency map diagram, a dependency table, a requirements table (consistency, latency, freshness, availability) and a worked dependency-budget calculation with labeled assumptions.
- [ ] Shows read-before-retry in a sequence diagram and dependency health states in a state diagram; covers timeouts, deadlines, one retry point, jitter, retry budgets, breakers, session and quota monitors, planned-maintenance calendars and bulkheads, each with a dated source.
- [ ] Retells the DriveDesk Outage from the dependency side without contradicting [[dms-integration]] (dates, 1,900 rooftops, 2,140 tickets, ~3,900 expired commands) and uses the 2024 CDK filings with inferences labeled.
- [ ] Failure table covers ambiguous writes, duplicates, retry storms, recovery surges, stale queued work, restores, quota exhaustion and a misleading monitor.
- [ ] Across Markets table compares NL/BE, DE, UK and US register write channels, outage behavior, read paths, published limits and DMS concentration, with sources.
- [ ] Chief Architect's view, 6–10 questions, hand-off to [[scale-and-cost]]; article under 8,000 words.

## Non-goals

- Register transaction model, prerequisites, proof documents and fees ([[registration-and-trade-services]]); the full sale journey ([[journey-sale-to-registration]]).
- DMS adapter design, field ownership and reconciliation mechanics ([[dms-integration]]).
- Telemetry plumbing, synthetic probes, support console and severity scale ([[observability-and-data-operations]]).
- Workload shapes, lanes and cost per lookup ([[scale-and-cost]]); ransomware defense of the platform ([[vehicle-platform-security]]).
- Delete propagation and desired-state sync ([[listing-syndication]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No public availability commitment was found for RDW, DVLA or DVSA channels; the chapter says so rather than inferring one.
- Belgian registration channel behavior during outages (DIV, WebDIV) could not be verified from a primary source.
- Whether the Dutch transaction channel supports a client-reference query is not public; the chapter describes read-before-retry generically.
- US state DMV partner-program outage rules beyond California's BPA program were not studied.

## Decision log

- **2026-10-22** — Counted upstream-caused failures in journey SLIs and attributed them, instead of excluding them as the platform brief's implication suggested, because exclusion hides Borrowed Uptime where it lives.
- **2026-10-22** — Added a third SLI outcome ("degraded") with its own cap, so a journey permanently running in degraded mode (the DriveDesk lead inbox) is visible.
- **2026-10-22** — Made the 214 double submissions the consequence of a missing "Slow" state and ambiguous-outcome class, and placed the fix (read before retry, per-vehicle hold, paced drain) here while leaving the transaction design to [[registration-and-trade-services]].
- **2026-10-22** — Rejected a runtime second-provider fallback as a default recommendation, citing Amazon's dormant-fallback argument; recommended push-fed labeled copies instead.

## Sources

- **Internal**
  - [[where-vehicle-platforms-go-wrong]] — Borrowed Uptime, DMS Hostage, Provenance Amnesia.
  - [[dms-integration]] — Hitch, DriveDesk Outage timeline and numbers.
  - [[registration-and-trade-services]] — Month-End Register Outage detail (14:20–20:00, two slow windows), probe before retry, June 2027 redesign.
  - [[registers-and-official-data]] — register mirror from daily snapshots, purchase gate, Three Copies review.
  - [[observability-and-data-operations]] — flow records, probes, incident communication.
  - [[scale-and-cost]] — upstream budget broker and lanes.
  - [[dealer-and-data-economics]] — journey requirements and targets.
  - [[case-cdk-global]] — the 2024 outage as a company case.
- **External**
  - AWS Builders' Library (2019) on timeouts, retries and avoiding fallback; Brooker (2015) on jitter; Google SRE book (2016); Fowler (2014); Nygard, *Release It!* (2018); AWS Well-Architected REL12-BP05.
  - AutoScout24 Tech Blog (2024) on SLOs for critical user interactions.
  - RDW informatiemap (2026) and maintenance page; DVSA MOT history API documentation; DVLA VES; GOV.UK; KBA GKS brochure (2024); California DMV BPA; §39 StVG.
  - AutoNation, Sonic and Lithia SEC filings (2024); CyberScoop and TechTarget (2024); CISA ransomware guide (2023); OWASP API10:2023.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: AutoNation per-share figure checked against the 15 July 2024 Form 8-K and cited with its filing date (consistency item 10); Month-End outage times confirmed against the ledger. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
