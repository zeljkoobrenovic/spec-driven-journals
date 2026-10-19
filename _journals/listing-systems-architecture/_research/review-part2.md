# Review log — Part II (editorial pass, 19 Oct 2026)

Scope: part-2-intro, 07-listing-aggregate, 08-categories-and-taxonomies, 09-attribute-schemas, 10-media-pipeline, 11-location-and-geo, 12-sellers-and-accounts. Build clean; render check OK on all seven pages (no failed mermaid, no unresolved links, no XJ entries).

Primary-text verification: the DSA (32022R2065: Arts 17, 20, 30) and Directive (EU) 2019/2161 (PID Art. 6a, CRD Art. 6a(1)(b), UCPD Art. 7(6)) were fetched from the EU Publications Office and match the chapters' quotations and summaries.

## part-2-intro
- No changes. Callouts, chapter table, hand-off to [[listing-aggregate]] and Veldmark decisions agree with the ledger.

## 07-listing-aggregate
- Rotterdam bike reservation 16:32 → **14:02** (consistency-issues 9; index and spec decision log).
- Bike photo count five → **six** (media-pipeline ledger line owns the photo facts).
- Lead: "several hundred buyers" → the canonical 214 digest recipients.
- Erasure row: "Mon 6 Sep 2027" → "Sep 2027 (request Mon 6 Sep)" (response sent 15 Sep per listing-data-management).
- Sold-to-gone target for search 30 s → **10 s p95**, matching the publication-pipeline SLA card and search-architecture.
- timetoread 32 → 37 (house measure: words before Sources, tables included, ~230 wpm).
- Spot-checked: Auto Trader FY26 (Deal Builder pause, listening sessions, "request a reservation") — verified; DSA Arts 17/20 and PID Art. 6a — verified.

## 08-categories-and-taxonomies
- No changes needed. Bike figures (380k NL across all bike leaves, 410k reclassified, 46/50/4%, 96.8% audit) agree with the ledger and the editor line on 380k vs 214k.
- Spot-checked: Mercari 2024 (3B+ items, ~USD 1M / 1.9 years, ~10 candidates, kNN "performed satisfactorily"), Google vehicle-listing changelog (Oct 2023 / Jun 2025 / Sep 2025), ESCO v1.2.1 counts — all verified.

## 09-attribute-schemas
- Acronyms expanded on first use: DMS, NHTSA.
- timetoread 35 → 39.
- Frame-size baseline already 23% (consistency-issues 22 resolved before this pass).
- Spot-checked: Service-Public DPE (2.3 → 1.9 on 1 Jan 2026; fines €3,000/€15,000; G/F/E rental dates), Vinted 2023 facets figures, ESCO — verified. Note for author: Service-Public now also lists a further electricity factor cut 1.9 → 1.7 from 2027; the chapter could mention it in a later revision.
- Open (author): Etsy figure still rests on a secondary summary (flagged in text).

## 10-media-pipeline
- AI Act Art. 50 date (2 Aug 2026) hedged: "under the regulation as adopted in 2024 (check for later amendments to its timeline)" — the source is an unofficial reproduction and timeline amendments were proposed in 2025.
- Removed odd scene phrase ("Two weeks after the summer").
- timetoread 30 → 32.
- Spot-checked: Autotrader FY26 Co-Driver (1.9M descriptions, 700k re-orders), Google Merchant 500 × 500 minimum enforced from 31 Jan 2027 — verified.
- Open (author): OLX duplicate-detection posts and the YAMS ">3 PB" figure remain search-summary only (already flagged in text).

## 11-location-and-geo
- "four marketplaces in seven countries" → "four brands in **eight** countries" (consistency-issues 19/23).
- Cross-border example: Motorvane markets completed (DE, NL, PL, AT); dropped "Belgian listings" (Motorvane is not in Belgium).
- "seven copies of a typical Veldmark listing" → "seven copies of Femke's bike listing alone" (the listing-data-management fact).
- "The REM Productscape domain model" → "The real-estate Productscape domain model" (undefined acronym).
- timetoread 31 → 36.

## 12-sellers-and-accounts
- Ruhrblick KYB: no longer says contract-signature check is "still the only check" in 2027; now aligned with identity-and-verification's June 2027 re-check pilot and 90-day re-checks.
- Contract named: Motorvane **Pro 150** (150 slots, €1,450/month), per consistency-issues 12.
- Golf leads: "23 leads" → "23 raw leads (19 after deduplicating…)" (consistency-issues 11).
- Bundeskartellamt: restated as reported — clearance on 8 Oct 2026 *noted* multi-homing and dealer data export; main stated reasons were Carwow's new-car focus and AutoScout24. The earlier text overstated it as a finding that these "constrain mobile.de's market power".
- DSA Art. 30 citation moved from an unofficial mirror to EUR-Lex (text verified); added Directive (EU) 2019/2161 as the source for CRD Art. 6a and UCPD Art. 7(6); the spec's open question on that wording marked resolved.
- "Veldmark ID approved for June 2027" → "due for approval in June 2027" (scene is set in May).
- Closing hand-off now goes to [[part-3]] (last chapter of the part), then [[listing-ingestion]].
- Spot-checked: Rightmove 16,385 agency branches and ARPA definition, Autotrader 13,942 forecourts / £2,995 ARPR, CarGurus paying-dealer definition and 34,409 — verified.

## Issues for other pages / the author
- Ledger: the listing-aggregate line still says the bike was reserved at 16:32; the editor line (14:02) overrides it. Rewriting another chapter's ledger line is not allowed, so it is left in place.
- Ledger: listing-data-management's line says "seven copies" but lists eight places (SoR, sold page, media, Snowflake, T&S case, Safe Deal records, digest archive, e-mail provider logs). That chapter's owner should reconcile the count.
- Editor line on frame-size coverage gives 71% "after enrichment and the required-attribute date of 1 March 2028", but normalization-and-enrichment and ch. 09 say 71% was reached by end of September 2027. Suggest the editor line say "by end of September 2027".
