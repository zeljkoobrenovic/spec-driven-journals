# Editorial review — Part I (chapters 01–04)

Reviewer pass, 2026-10-22. Word counts are prose words before `## Sources and Evidence`, with table pipes removed. All four pages were under 8,500 words, so nothing was trimmed. Format checks passed on every page: complete front matter, the callouts in order with exact labels, exactly three KEY POINTS, two or three failure patterns with exact names, `<br>`, failure handling, the Chief Architect's view, Questions to ask, Sources and Evidence, and a hand-off to the next page in config order. "Across Markets" is not required in Part I. Each page has its own market section instead.

External spot-checks (WebFetch, 22 Oct 2026):

- **Auto Trader FY26 results PDF:** ARPR £2,995, 13,942 forecourts, levers +£117 / −£48, 155M partner calls a month, 220+ partners. Verified.
- **CDK FY2021 10-K:** "nearly 15,000 retail locations in North America" (used in ch03); 15,025 DMS customer sites and $1,313.9M subscription revenue (used in ch02). Verified. The two figures measure different things, so both pages are correct.
- **Car-Pass FAQ:** €11.10, free with fewer than four readings. Verified.
- **Ayvens FY2025:** net used-car sales result per unit of €1,075. Verified.
- CarMax, Carvana and AutoNation figures match the VERIFIED lines in `brief-dealer-workflows-economics`.

## 01 vehicle-data-ecosystem — 7,374 → 7,473 words

- Added a **register** definition to the definitions list, which expands RDW, DIV, KBA, DVLA, DVSA (with MOT), DMV and NMVTIS on first use.
- Expanded AAMVA, DPPA, CRM and B2B on first use. Replaced "OEM" with "manufacturer" (three places).
- Added a Wikipedia citation for CDK's 2022 Brookfield take-private. The FY2021 10-K that was cited cannot support a 2022 event.
- Changed "behaviour" to "behavior" and "DMS-centred" to "DMS-centered".
- Checked against the ledger: ecosystem-map line (21 contracts, 6 with no cache-retention clause), 99% of withdrawals within 10 minutes, Merelstad, Axleby Insight, segment shares. All agree.

## 02 dealer-and-data-economics — 7,539 → 7,581 words

- Dated the Brandsma month table to 2026, with a note that he added Sales Admin in January 2027 (consistency issue 26).
- **Month-end outage example corrected.** It said "failed lookups", but the outage hit the register's *transaction* channel. It now refers to failed register calls. It also says Axleby Trade bills a transaction only on register confirmation, per the ledger.
- Expanded SMMT. Changed "cancelling" to "canceling". Added blank lines between the three mermaid blocks and their captions.
- Arithmetic re-checked and correct: front-end gross €2,093, holding cost €8.8 a day, the €566 / €1,065 / €885 Brandsma totals, revenue per rooftop matching the editor line, €0.04 per lookup, and the Rijnstaal batch matching `scale-and-cost`.

## 03 vehicle-capability-map — 7,206 → 7,227 words

- **Fixed "Harrowgate Capital's board".** It is Axleby's board, on which Harrowgate holds the majority.
- **Aligned latency assumptions with the owning chapters.**
  - Identity resolution: changed from p95 ≤ 50 ms to under 80 ms, per `vehicle-identity`.
  - Licence check: changed from p99 ≤ 10 ms to p99 under 2 ms in process, per `data-licensing-and-governance`.
- Changed the ambiguous "documents" in the class-by-scope table to "import and export documents".
- Expanded VIN, B2B and DPIA.
- All v1 counts were recounted from the table and match the ledger: 13/21/5 by class, 6/20/8/5 by condition, 18/6/14/1 by scope, 18 market-flagged, the 9 + 8 + 1 shared split, and 8 added.

## 04 vehicle-bounded-contexts — 7,447 → 7,451 words

- **RDW row count:** changed 16,874,711 to 16,870,710, to match ch01 and ch02 (same query date).
- **Aligned latency assumptions** with `vehicle-identity` (p95 under 80 ms) and `data-licensing-and-governance` (p99 under 2 ms in process).
- Changed the Evans book year from 2004 to 2003, to match ch03.
- Expanded DDD and B2B. Added blank lines between the mermaid blocks and their captions.
- Contested rows match consistency issues 24, 25 and 31.
- Checked against the owning chapters: the Octavia figures (`inventory-and-vehicle-dossier`), the Margin-Scheme Error (`deals-and-sales-documents`), the Three Copies review (`registers-and-official-data`), the 68% de-listing audit (`market-data`), the July 2027 tenancy decision, Runway/Baseline and the Gatekeeper 30-second rule. All agree.

## Build and render

- One build run failed with a transient OSError in `docs/private-techuity/assets/images`, caused by a parallel build. The rerun passed: `[built] vehicle-data-dealer-saas-architecture`.
- The rerun warned that `glossary` and `bibliography` posts are missing (config lists them; outside Part I).
- `render_check.py` printed OK for all four pages, with no unresolved links and no failed mermaid diagrams.

## Open issues for the author or other parts

1. **"programme" vs American spelling.** "One Dossier programme" appears in about 25 pages and in the ledger. I left it as the programme's proper name. The final editor should decide book-wide.
2. **"licence" (noun).** The book uses "licence" everywhere, including the canonical pattern names (Licence Blindness, Licence Breach). The style guide asks for American spelling, which would be "license". I left it because it is a book-wide convention.
3. **Latency assumptions in other chapters.** `vehicle-identity` (80 ms) and `data-licensing-and-governance` (2 ms) are now the reference values. Other chapters quoting identity or licence-check latency should match them.
4. **Exact RDW row count.** Only Part I quotes an exact count (16,870,710). Consistency issue 14 uses 16.87M.
