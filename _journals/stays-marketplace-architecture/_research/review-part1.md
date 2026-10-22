# Review log — Part I (editorial pass, 21 Oct 2026)

Scope: part-1-intro, 01-two-stay-marketplaces, 02-stays-marketplace-economics, 03-stays-capability-map, 04-stays-bounded-contexts.
Word counts measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`.

| Page | Before | After |
| --- | --- | --- |
| part-1-intro | 1,033 | ~1,050 (not trimmed; above the 500–800 guide, flagged below) |
| 01-two-stay-marketplaces | 9,203 | 8,498 |
| 02-stays-marketplace-economics | 10,150 | 8,499 |
| 03-stays-capability-map | 9,869 | 8,495 |
| 04-stays-bounded-contexts | 10,432 | 8,500 |

Build: clean (only the known missing `bibliography`). Render check: all five pages OK, no failed mermaid, no unresolved links, no XJ entries.

## All pages

- American spelling: programme(s) → program(s) (incl. "One Stay program"), licence → license, fulfil → fulfill, behaviour, honour, centre, labelling, neighbourhoods. "Cancelled" left as is (book-wide usage).

## part-1-intro

- "a thousand searches" → "about a thousand shopping requests"; "1,400:1 look-to-book" → "1,400 shopping requests per reservation" (editor ledger line).
- 48-capability map named as capability map v1 (March 2027); both the map and the context map pointed to their December 2027 revisions in [[converging-two-marketplaces]].

## 01-two-stay-marketplaces

- Trimmed: chapter-ownership boilerplate, history waves (Wave 1–6 condensed, no dates or sources lost), the layered-architecture list (merged supply engines and connectivity edges), duplicated Request-to-Book explanation, one failure mode folded into the Chief Architect's view, questions 10 → 8.
- Spot-checked: Expedia FY2023 10-K (Hotels.com front end 2022, Vrbo 2023, "one unified front-end stack in 2023") — matches; Booking Holdings FY2025 10-K (merchant 70% of gross bookings vs 63%, 4.4M / 3.9M / 500k properties, ~36% alternative-accommodation room nights) — matches; Airbnb Help Center 1857 (15.5% host-only; split 3% host, 14.1–16.5% guest) — matches (the page itself gives no start date; the October 2025 date comes from the 10-K as cited).
- Fixed a "programr" typo introduced by the spelling pass (David Clouse, programmer).

## 02-stays-marketplace-economics

- Search-volume wording aligned with the `[editor]` line: the 1,400 is "shopping requests"; each makes about ten "Pricegrid reads"; per-second figures are "availability lookups (Pricegrid reads)". Figure 3 node relabeled; the Hotels-and-Homes table no longer uses "1,400:1".
- Removed "Corvane's own Nookaway fees changed in 2026 as well": the 21 Oct 2026 `[editor]` fee change is an editorial correction, not an in-world event.
- Trimmed: Booking.com seasonality and Expedia revenue-mix repeats (already in ch01), program examples, marketing commentary, the AI-disintermediation aside, Nookaway look-to-book bullets, three duplicated failure modes, a trade-off row, three side-by-side rows that repeated the opening table, the Watch list, questions 10 → 8.
- Latency evidence (2019) now flagged "seven years old and may be superseded".
- Request-to-book share stated as 32% (= 100% − 68% instant book, ledger).

## 03-stays-capability-map

- The 16/6/26 split is now explicitly **capability map v1 (23 March 2027)**; added a paragraph on **v2 (14 Dec 2027: 49 = 23/6/20)** with the moves from the ledger and a pointer to [[converging-two-marketplaces]] as the decision of record. Figure 4 caption says v1. The experimentation cell links to the September 2027 Experimentation Standard (consistency item 8/9). The hand-off says "the v1 map".
- Corrected Expedia: Hotels.com moved to the Brand Expedia front end in 2022, Vrbo in 2023 (was "both in 2023").
- Trimmed: scene-setting, model descriptions, the duplicated "Where the Two Maps Differ" table (now one paragraph), two failure modes, the Chief Architect's view (now records map versioning), questions 9 → 7.

## 04-stays-bounded-contexts

- Checked Context Map v1 (5 May 2027) against capability map v2: change and cancellation policy row now says it was superseded in July 2027 by Clause (one group engine); decision table gains the July Clause row; new paragraph records the December review (Clause, Vouch as a shared engine in the trust platform, place registry and Waypoint as two contexts with Waypoint writing to the registry, experimentation/ML shared engines on the capability map but platforms on the context map). Data and metrics target names Gauge (July 2027).
- Fixed a contradiction: subdomain rule 3 cited inventory as "core for one, supporting for the other", but the table marks inventory core for both; the example is now offer composition.
- Removed an unsourced claim that Booking.com and Expedia "described replacing" monoliths (kept Airbnb Monorail and Agoda, both sourced).
- In Practice condensed (Airbnb, Agoda, Expedia + Booking.com) with every source kept; the Airbnb warehouse rule now refers to ch03 instead of repeating it. Dropped Agoda's "64% faster review" detail.
- Trimmed: intro, concepts list, scene findings (merged into a paragraph), two night-table rows, merged ledger/tax subdomain rows, two relationship rows, ACL text, second trade-off table (kept the payment-arrangement default as prose), two Hotels/Homes rows, two failure modes, questions 10 → 8.

## Open issues for the author / other parts

1. **"programme" vs "program" book-wide.** Part I now uses "program"; at least ten other chapters (e.g. 43-converging-two-marketplaces, meet-corvane, toolkit) still use "One Stay programme". The ledger also uses "programme". Pick one book-wide (style guide says American).
2. **"cancelled/cancelling"** is British-leaning; left as is because it is book-wide and also acceptable in US usage.
3. **part-1-intro** is ~1,050 words against the 500–800 part-intro guide; not trimmed in this pass.
4. Chapters 01–04 still overlap on Expedia's re-platforming and Booking.com's homes counts; each now cites them briefly, but a later pass could keep the full treatment only in ch01.
5. Airbnb help article 1857 does not state the October 2025 transition date; ch01 and ch02 rely on the 10-K for it.
