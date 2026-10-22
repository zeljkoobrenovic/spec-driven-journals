# Review log — Part X (part-10-intro, 48–51)

Reviewer pass, 21 Oct 2026. Word counts are measured before `## Sources and Evidence`. No page needed trimming: all case studies are within the 5,000–7,000 range plus a small margin, and none is above 8,500.

## part-10-intro (1,192 → 1,195 words)

- "Why the business cares" said Expedia lowered guidance "because" Vrbo recovered slowly. It now says "citing", since the release names the Vrbo drag together with the B2C acceleration rate.
- Figures checked against chapters 48–51: the 3% guardrail, the May 2024 guidance cut, 3.9M of 4.4M Booking.com properties, $12.2B held by Airbnb, Expedia's 2.4M Vrbo homes and 1.2M hotels, and Booking.com's 70% merchant share and ~1,000 parallel experiments. All agree.
- Remaining: the intro is above the 500–800 target for part intros (about 900 words of prose plus tables). It was left as is because it carries the evidence-kinds table that the cases rely on.

## 48-case-booking-com (7,201 → 7,215)

- Expanded CNCF and KDD on first use, in the timeline.
- Spot-checked:
  - AGCM release of 22 Apr 2026: date and quotes confirmed. The URL path says "2024" but the release is from 2026.
  - Reservations API: 30-minute email fallback, 24-hour extension and repeated return until acknowledged, all confirmed.
  - Not reachable: booking.ai (403), the Preferred Partner page (403) and Medium (403). These claims rest on the brief's VERIFIED tags.
- Corvane facts checked against the ledger and found consistent: the Switchyard ±60% band, the 10-minute delivery fallback, 70% agency, Ranking Policy v1, 435,000 / 61,000 / 1.15M, and the Keystone exit at end of 2029.
- For the author: the CNMC appeal, the German damages cases and the Italian investigation are still open as of Oct 2026. Revisit them before publication.

## 49-case-airbnb (6,975 → 6,996)

- Corvane comparison row on boutique hotels: it said "decide early whether hotel rooms enter Almanac…", which contradicted the ledger's cross-type routing rule (the pilot runs on the hotel-type engine). The row now states Corvane's decision.
- Expanded PSP on first use.
- Spot-checked:
  - Q2 2026 shareholder letter (PDF text extracted): $12.2B funds held; "thousands of" boutique hotels in more than 20 destinations; a single-digit share of nights; hotel nights growing about three times as fast as homes; AI assistant at nearly 45%; over 5.5M hosts; host-only fee migration this year. All confirmed.
  - Reserve Now, Pay Later worldwide: 17 Feb 2026, flexible or moderate policies, over 70% adoption in Q4 2025. Confirmed.
  - Payment-orchestration post: Medium returned 403, so it was not re-verified (brief VERIFIED).

## 50-case-expedia-vrbo (7,085 → 7,089)

- **Fixed a One Stay mismatch.** The page gave v2 totals of "22 shared engines, 6 shared contracts, 21 brand-specific". The canonical figures (ch. 43, ledger) are **23/6/20 over 49**, and the page now uses them.
- The Vrbo calendar "must be called on page load" now reads "should be called on page load", which is the source's own wording.
- Changed "Programme" to "Program".
- Changed timetoread from 30 to 31.
- Spot-checked:
  - Q1 2024 release: the quote, 4% lodging and 12% hotel growth, and 2 May 2024. Confirmed.
  - Rapid Vrbo calendar: "Caching is not supported", 3-year horizon. Confirmed.
  - Rapid Vrbo integration guide: the `merchant_of_record` wording, no same-day bookings, the package ban. Confirmed. The 4-hour cancellation wording was truncated in the fetch.
  - FY2025 10-K: "shared platform infrastructure…" and 3.6M / 2.4M / 1.2M. Confirmed.
- "About 34% of Nookaway gross bookings made January–March" was a new local fact. It is now recorded in the ledger as an `[editor-review]` line.

## 51-case-agoda-trip-com (7,144 → 7,162)

- The page said "Booking.com's equivalent treats the end date as exclusive". The brief supports this only for B.XML's `to` date, so the sentence is narrowed to that.
- The Agoda Supply API link (developer.agoda.com/…/ota_hotelavailnotifrq) now redirects to agoda.com. This is flagged in the citation. **For the author:** find a live source or an archived copy.
- Expanded OTA and TTL on first use.
- Changed timetoread from 33 to 31.
- Spot-checked:
  - Trip.com FY2025 20-F (fetched in full): guaranteed-allotment and on-request models, revenue "when the reservation becomes non-cancelable", hotel matching at "billions of queries per day", RMB 26.1B at 42%, and 1.7M listings. Confirmed.
  - Agoda posts via the Medium RSS feed: the Price Cache (19 Aug 2026; three-hour warm-up; 10- and 3-point thresholds; 40 pods in about two minutes) and BAPI (20 Oct 2026; 2019 line-by-line port; MRs quadrupled; 64% / 1.08 vs 3.02 h; 34%; 91% vs 69%; 29%). Confirmed.
- Corvane facts checked against the ledger and chapters 07, 21 and 38: Brightwell 41,000 / 8,410 / June 2027; Pricegrid 180-day / 1–7-night / 1–4-adult tier at 94% → 71%; the 30-minute natural-key guard; Frankfurt standby; Nookaway warm standby by end of 2028. All agree.

## Cross-book consistency (issues on other pages, not edited)

1. **toolkit** (line ~698) says One Stay v2 is "22 shared engines, 6 shared contracts and 21 brand-specific". It must be **23/6/20** (ch. 43, ledger).
2. **05-property-and-listing-model** cites Booking Holdings' corporate site as "about 4.7 million properties and more than 33 million listings". Ch. 48 and the other chapters use the 10-K's 4.4M properties. These are not contradictory (different sources), but ch. 05 should say why its figure differs from the 10-K's.
3. All other case facts are stated identically in Parts I–IX (grep for Booking.com, Airbnb, Expedia/Vrbo, Agoda, Trip.com). This covers the 3.9M / 4.4M property counts, the 70% merchant share, the €413.24M CNMC fine, the 30-minute fallback, the 3-hour iCal interval, the 15.5% fee, the RNPL dates, the Vrbo re-platforming quote, Agoda's 300k / 1.5M figures and the ~1,000 experiments.

## Build and render check

- Build: no errors.
- `render_check.py part-10 case-booking-com case-airbnb case-expedia-vrbo case-agoda-trip-com`: all OK. 0 failed mermaid, 0 unresolved links, no XJ entries.
