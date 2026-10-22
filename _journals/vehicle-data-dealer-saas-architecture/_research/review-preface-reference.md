# Editorial Review — Preface and Reference Pages

Reviewer pass, 22 October 2026. Pages: `introduction`, `where-vehicle-platforms-go-wrong`, `meet-axleby`, `part-1-intro`, `domain-coverage`, `toolkit`. Callout rules follow the BOOKED counterparts (preface and reference pages use "IN THIS SECTION"; `introduction` and `where-…-go-wrong` carry no failure-pattern callout; `meet-…`, `domain-coverage` and `toolkit` carry "FAILURE PATTERNS THIS SECTION ADDRESSES"; `domain-coverage` and `toolkit` carry no WHY callouts).

Word counts: whole file with `sed 's/|/ /g' | wc -w` (before → after); prose to Sources in brackets after.

| Page | Before | After | To Sources (after) | timetoread |
| --- | --- | --- | --- | --- |
| introduction | 5,276 | 5,428 | 5,224 | 22 → 23 min |
| where-vehicle-platforms-go-wrong | 6,771 | 6,948 | 6,621 | 30 (unchanged) |
| meet-axleby | 5,548 | 6,447 | 6,250 | 24 → 27 min |
| part-1-intro | 1,145 | 1,145 | 1,145 | 5 (unchanged) |
| domain-coverage | 5,890 | 5,957 | 5,763 | 30 → 25 min |
| toolkit | 8,437 | 8,469 | 8,134 | 40 → 35 min |

No page is over 8,500; no trimming needed.

## introduction

- Callout label "IN THIS PAGE" → "IN THIS SECTION" (BOOKED).
- Part table checked against every chapter's KEY POINTS: Part I now names the capability map and boundaries (ch. 3–4); Part III adds evidence-with-method (market, condition, battery, connected data, ch. 11, 13–15); Part VI adds aggregation-is-not-anonymization and the free check (ch. 33–34). Other rows matched.
- Fitness functions: "a few … identity match precision … valuation error" → twelve, named as in `evolving-the-vehicle-platform` (identity merge precision, segment valuation bias, register outcome certainty …).
- Routing table: added three rows that had no entry (enumeration and leaked keys → `vehicle-platform-security`; erasure / owner scoring → `privacy-and-retention`; AI agents → `ai-in-dealer-workflows`). Existing rows verified against chapter scope.
- `journey-lead-to-dms` bullet: outcome write-back to portals is off by default per channel; reworded.
- Issue 23: "authorised information providers" → book term "authorized information provider", linked to `registers-and-official-data`, not RDW's title.
- Issue 5: Carfax now part of Mobility Global Inc. (trading from 1 July 2026), not S&P Global Mobility.
- Spot-checked: Auto Trader FY25 results quotes ("part of our core advertising proposition", "no longer be monetised per transaction") verified in the PDF; Data Act Art. 50 and Battery Regulation Art. 77 dates consistent with chapters.

## where-vehicle-platforms-go-wrong

- Callout label → "IN THIS SECTION".
- Built a pattern → chapter map from every chapter's and part intro's FAILURE PATTERNS callout and reconciled each "Where this book helps" line:
  - Cloned Identity: dropped `registers-and-official-data` (does not claim it); added `vehicle-bounded-contexts`, `inventory-and-vehicle-dossier`, `journey-inventory-to-portal`.
  - Spec Guesswork: added `case-auto-trader-uk`. Provenance Amnesia: added `condition-and-damage`, `ev-battery-health`. Sticky Error: added `valuation-engine`, `merchandising`.
  - Zombie Listing: added `dms-integration`, `b2b-trade-and-remarketing`. Feed Roulette: added `journey-inventory-to-portal`. DMS Hostage: added `deals-and-sales-documents`.
  - Unmetered Call: "`vehicle-data-apis` meters at the gateway" contradicted `billing-and-metering` (the service that knows the outcome meters); replaced with the shared outcome vocabulary; added `registration-and-trade-services`.
  - Licence Blindness: added `build-buy-or-partner`. Acquisition Archipelago: added `organizing-engineering`.
  - Customization Creep: removed `organizing-engineering` (does not claim it); added `used-car-pricing`, `deals-and-sales-documents`.
- Customization Creep Axleby paragraph said "the ledger records no incident"; replaced with the Hartley migration (14 code paths → 9/3/1/1) and Velto's 23 special requests (none became code).
- Sticky Error: "API clients held copies nobody had recorded" → 19 external clients, 2,310 lookups, found by manual impact analysis to 3 June (ledger, `events-webhooks-and-sync`, `journey-data-correction`).
- Spot-checked: AutoNation 15 July 2024 8-K, about $1.50 per share before recoveries (issue 10) — verified; European Parliament 31 May 2018 odometer figures — verified.

## meet-axleby

- Callout labels → "IN THIS SECTION" / "FAILURE PATTERNS THIS SECTION ADDRESSES".
- New section "The Group Platforms the Chapters Introduce" (modeled on BOOKED's meet-corvane): Hitch, Inlet, provenance envelope v1, Retrace, Pulse v2, Gauge and Lotwise Inspect, Mandate and Signalyard, Lotwise Dossier/Dossier service, rebuilt Appraise, Relay 2, sale-right register and Handback, Runway and Baseline, tenant directory, Axleby ID/Gatekeeper, Meterline, Charter, Folio/JSON API v2, event backbone, Horizon, Pitwall, Tidemark — each with owner/status and chapter, from the ledger.
- Cast: added Sanne Koster (CISO); partners: Merelstad Auto Finance, Kavelstad, Lintvelt Leads B.V., Meridal Import B.V.
- Timeline: added June (register redesign), October (v2 lookups), November (DriveDesk Outage) and December 2027 milestones.
- Lotwise business model aligned with the `[editor]` revenue-per-rooftop line (≈€1,110/month; subscriptions about half). Resolution: the editor line wins over the brand table's "per-report fees charged through Axleby Data".
- Prices: `[editor]` Odolo prices are VAT-inclusive; header no longer says all prices exclude VAT.
- Programme: issue 20 (v2 lookups October 2027, webhooks Q3 2028); retirement milestones (contract freeze 1 Jan 2028, facade Q2 2028, colocation exit 30 June 2029, stock writer flip 2028) from `modernizing-the-platform`.
- Lost Leads row aligned with the `[editor]` hub-sized-stock line.
- Added a sentence naming chapter-local incidents (Margin-Scheme Error, Saturday Batch, Twice-Sold Returns, Two Certificates).

## part-1-intro

- Checked against chapters 1–4 and the ledger (9 of 39 duplicated capabilities, 29/11/4 entity census, €1,110 per rooftop, 58 vs 51 days, €0.46, 16 March board, 3 June table). No change needed. Body ≈1,050 words, above the 500–800 guide; left as is (not over the trim threshold).

## domain-coverage

- Callouts aligned with BOOKED: "IN THIS SECTION", WHY ARCHITECTS SHOULD CARE removed, failure-pattern label → "THIS SECTION".
- "Chapters still in writing … placed by their contract" removed; placements spot-verified against finished chapters (NAP adapter in `vehicle-history`, consumer documents in `consumer-vehicle-checks`, plates and materials and export declarations in `registration-and-trade-services`, detection vendor in `build-buy-or-partner`, etc.).
- Empty Axleby cells filled (battery-health service, Merelstad referral, Axleby Trade webshop / Axleby Trade); `fenr` row adds JSON API v2 `/v2/lookup-jobs` and the v2 map merge into D1.
- Added-domains table names each Axleby system (Inlet, envelope v1, Mandate/Signalyard, Switchboard, Hitch, Runway/Baseline, event backbone, Pitwall).
- Stressors: the page said the book adds the digest's seven proposed stressors; `evolving-the-vehicle-platform` actually runs sixteen (model's seven + S6, S8, S10–S16). Rewrote the added-stressor table to the chapter's numbering and residues; the two digest proposals not in that table (second register, file-exchange breach) are noted with their covering chapters. "fourteen stressor rows" → sixteen.

## toolkit

- Tool 2 Sold rule aligned with issues 24 and 31(f) (signing/deposit/hold → Reserved; Sold on conditions met and invoice, or delivery).
- Tool 9 DriveDesk field ownership aligned with issue 31(a) (accounting stock unit vs stock item).
- Closing fitness-function list aligned with `evolving-the-vehicle-platform`.
- Verified against owning chapters: Tool 3 envelope example (`provenance-and-data-quality`), Tool 4 Kilometra contract v2 and per-chain gate (issue 17), Tool 5 replay (week 5, +5.8%, €0.3M), Tool 8 Brandsma Corolla (`registration-and-trade-services`), Tool 9 5-day expiry, Tool 10 €16 / €130 assumptions, Tool 11 Rijnstaal 400 calls/s, Tool 12 `damage-partner-nl`, Tool 13 e-Niro €5.22, Tool 16 vetoes and event backbone record.

## Build and render check

- Build: no errors; warns that `posts/glossary/index.md` is missing.
- Render check: `meet-axleby`, `part-1`, `where-vehicle-platforms-go-wrong` OK. `introduction`, `domain-coverage`, `toolkit` report only `XJ:../finance-systems-architecture/glossary.html` — `[[glossary]]` resolves to RECONCILED because this book's glossary does not exist yet. Kept per WRITER-BRIEF's explicit exception; they resolve in-journal once the glossary is written.

## Open issues for the author or other reviewers

1. **Glossary page missing** (`posts/glossary/`): until it exists, every `[[glossary]]` link in the book points to RECONCILED's glossary.
2. `provenance-and-data-quality` envelope example: version 2 of the reading shows `value_as_delivered: 41220, unit km`; if version 2 is the corrected redelivery, the delivered unit should presumably be `mi`. The toolkit mirrors the chapter; fix both together if changed.
3. `vehicle-data-apis` does not list The Sticky Error, though it carries the `data_correction` credit; optional.
4. `meet-axleby` spec's success criteria may still reference "eleven incidents" only; the page now also names chapter-local incidents and the platform table (spec changelog updated, criteria not rewritten).
5. Ledger brand table still says Lotwise's per-report fees are "charged through Axleby Data"; the `[editor]` revenue line contradicts it. Consider an `[editor]` clarification.
