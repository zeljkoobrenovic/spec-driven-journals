# Editorial Review — Part II (VEHICLE)

Reviewer pass, 2026-10-22. Scope: `part-2-intro`, `05-vehicle-identity`, `06-registers-and-official-data`, `07-specification-and-equipment`, `08-vehicle-history`, `09-ingestion-and-entity-resolution`, `10-provenance-and-data-quality`.

Word counts are prose words before `## Sources and Evidence`, with `|` replaced by spaces. No page was over 8,500 words, so nothing was trimmed.

Every page passed these checks: front matter, the callout order and labels (exactly three KEY POINTS, 2–3 failure patterns with exact names linking `where-vehicle-platforms-go-wrong.html`), the `<br>`, an Across Markets table, failure handling, the Chief Architect's view, Questions to ask, Sources and Evidence, a hand-off to the next page in config order, mermaid fences and quoted labels, consecutive figure captions, and valid `[[…]]` permalinks (the `entity-resolution` link resolves only to LISTED).

## Spot-checked external claims (WebFetch, 2026-10-22)

- RDW paid business access: €0.18 per lookup on the web; €580 plus €0.07 per lookup over XML; per plate only; includes stolen and export status. Verified (pages 06 and 09).
- DVSA MOT API: 500,000 requests a day, 15 a second on average, burst of 10, key restricted for 24 hours after exceeding the quota. Verified (pages 06 and 09).
- RDW, 28 July 2026: the share of illogical German-import readings that arise at import fell from 92% to 60%. Verified (page 08).
- auto.dev OEM Build Data: $0.10 per call on Growth, $0.08 on Scale, with a match confidence score. Verified (page 07).
- HPI guarantee of up to £30,000. Verified (page 08).
- BBC/RAC cloning figures (10,460 in 2024; 7,377 in 2020): BBC was not reachable. The claim is now attributed as "as reported by BBC News" (page 05).

## Per page

### part-2-intro — 1,109 → 1,109
- No change. Note for the author: the page is above the 500–800 target for part intros, but it is well under the trim threshold.

### 05-vehicle-identity — 7,384 → 7,396
- Changed "colour" to "color" (4 places).
- Harmonized the RDW row count to "about 16.87 million". Pages 05 and 06 had given two different exact counts for the same date.
- The 118 retained-plate matches are now described as found by a later replay, not "during" the Odometer Correction (per the ledger and `journey-data-correction` CC-2027-0012).
- BBC/RAC figure attributed.

### 06-registers-and-official-data — 7,772 → 7,788
- Expanded DVLA and DVSA at first use (line 37), and the DPPA at its first use in the access-regime table.
- Harmonized the row count to about 16.87 million, in the text and in the sources.
- "From 2028" register-change webhooks is now "from Q3 2028" (consistency item 20).
- "programme" changed to "program"; "anonymised" changed to "anonymized".

### 07-specification-and-equipment — 7,349 → 7,352
- Aligned the Golf Variant timeline with consistency item 28: appraised Saturday 11 Sept 2027, stocked in Tuesday 14 Sept. The page had said "stocked in two days later".
- Row count changed to 16.87 million.

### 08-vehicle-history — 7,530 → 7,542
- The Q1 2027 audit now counts 9,800 *reports*, not cars, matching the ledger.
- Expanded APK, MOT, DVSA and OEM at first use.
- Removed "(OVI)" as the label for paid business register access. OVI is not that product, and the label was unverified.
- "artefact" changed to "artifact".

### 09-ingestion-and-entity-resolution — 8,325 → 8,458 (timetoread 35 → 37)
- **The main fix: the Dutch register feed now follows the snapshot model** (consistency item 14, owned by `registers-and-official-data`).
  - Before: the page described a register "change stream" with a median lag under 2 minutes and a 15-minute target.
  - Now: the ~95,000 events a day are Turnstile's mutation feed, derived from daily snapshots. Anchor applies them within an hour of the snapshot's publication *(assumption)*, and decision facts are asked live.
  - Updated to match: the source table, the volume cell, the per-source decision table, the requirements table, the outage row, the reconciliation paragraph and the market table.
  - Added an `[editor-review]` line to the ledger that supersedes the chapter's ledger wording.
- The golden record is now materialized *beside* Anchor as a projection (consistency item 31c).
- Changed "programme", "grey" and "anonymised" to American spelling.

### 10-provenance-and-data-quality — 7,423 → 7,431
- The register freshness SLO is now "within an hour of the daily snapshot's publication", to match page 09.
- The worked vehicle's UK→NL import date changed from June 2027 to March 2027. In June it would have postdated Rijnstaal's May calls on it.
- Expanded ODCS and GDPR at first use.

## Open issues for other pages or the author

- `04-vehicle-bounded-contexts` and other chapters were not checked for any "real-time register stream" wording. The ledger's `ingestion-and-entity-resolution` line still says "median lag under 2 minutes". The `[editor-review]` line now supersedes it, but the final editor may want to annotate the original line.
- `10-provenance-and-data-quality` cites `[[reliability-and-dependencies]]` for the JSON API v1 metadata block. `vehicle-data-apis` may be the better owner; the author should confirm.
- Kept as book terms: "licence" (the noun, as in the failure-pattern name) and "judgement" (an owned term).

## Build and render check

- Build: clean. One transient OSError from a parallel build in finance-systems-architecture passed on rerun.
- `render_check.py`: all 7 pages OK, 0 failed mermaid diagrams, 0 unresolved links.
