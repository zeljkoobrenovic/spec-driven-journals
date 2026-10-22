# Review log: Part IV (DISCOVERY)

Editorial pass of 21 Oct 2026. Word counts are measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`.

| Page | Before | After |
| --- | --- | --- |
| part-4 | 1,054 | 1,054 |
| stays-search-architecture | 9,006 | 8,492 |
| destinations-and-maps | 9,330 | 8,497 |
| stays-ranking | 9,225 | 8,500 |
| personalization-and-recommendations | 8,927 | 8,885 |
| property-page-and-room-selection | 9,501 | 8,474 |

Render check: all six pages print `OK` (0 failed mermaid, no unresolved links, no XJ entries). The build ran with no errors.

## part-4 (part-4-intro)

- Renamed Visibility Plus to **Front Row** (see the rename note below).
- Fixed a stray comma ("abandoned Lisbon search, is the case").
- Remaining: the intro has about 985 words of prose, above the style guide's 500–800 for part intros. It was not trimmed, because the chapter summaries carry the part's argument.

## stays-search-architecture (16)

- Waypoint approval changed from May to **June 2027** (consistency item 10). The target-design trace now says that Waypoint's first release was planned for Q1 2028 and the full design for late 2028.
- The Nookaway "Lisbon" rectangle now matches the ledger and ch. 17: drawn in 2014 and stretched in 2019 to reach Cascais, which pulled in Almada, Seixal and Barreiro. The table had said it "misses Cascais".
- The look-to-book paragraph now uses the editor wording (consistency item 6): 1,400 **shopping requests** per gross reservation, each making about ten Pricegrid reads, giving 21,000/s on average and 64,000/s at peak.
- Airbnb's 2022 Categories is flagged as possibly superseded.
- Trimmed duplicated failure modes, the Chief Architect item 4, the latency and look-to-book sources, and the landing, multi-room and Expedia/Vrbo paragraphs. The timetoread is now 34 min.

## destinations-and-maps (17)

- The worked example's retrieval count changed from 1,240 to **about 2,600**, so it agrees with ch. 16, which owns that stage and traces 2,600 → top 600 → 571 quotes. The target design is now "planned to be live for Nookaway by late 2028", not "was live".
- Trimmed the Expedia Geography API detail, the S2/H3 documentation, the Google pricing list, the OSM/PMTiles paragraph, place names, landing pages, the failure-mode list (merged into six bullets) and one question. Added a [[demand-channels]] link for landing-page SEO. The timetoread is now 34 min.

## stays-ranking (18)

- **Rename: Visibility Plus → Front Row**, applied in index.md and spec.md (consistency item 2). I did not use "Spotlight Partner" because LISTED's Tradeyard already has a "Spotlight" product (monetization-models, ranking). Front Row does not appear in BOOKED or LISTED and is not, to my knowledge, a real OTA programme name. Added the ledger's tier uplifts (+2/+4/+6 pp) and the ~38,000 participants.
- Removed the duplicated map-ranking detail (ch. 17 owns it), the Expedia 2013 dataset paragraph, the duplicate Juggler and Booking.com 2019 latency material, and the AWS feature-platform sentence. Removed two sources that are no longer cited.
- Compressed the failure modes into warning signs. Trimmed the long-term considerations, ranking council and judgement paragraphs and one question. The timetoread is now 34 min.
- Verified: AGCM PS13115 is dated 22 April 2026 (the URL path says 2024/4, but the release is 2026) and covers Preferred Partner and Preferred Plus. The quoted concerns match.
- Note for the author: the ledger's organizing-stays-engineering line lists "Ranking Policy v1 (Sept)" among the board escalations. The chapter has forum approval in June and the experiment in September. These are compatible (a September escalation of the revenue loss), but the chapter does not mention it. The 2022 "Circle boost" (×1.10) is in the archaeology table, but Policy v1 never says what happened to it. promotions-and-loyalty may want to settle that.

## personalization-and-recommendations (19)

- The fee-revenue estimate now uses the realized take rate of about 14.4% (€1.3M, linking [[stays-marketplace-economics]]) instead of "a combined 16% take".
- Light trim of the lead and "documented record" paragraphs. All Novak timeline figures match the ledger: €165 → €145 on the evening of 12 Feb, an 03:00 job, a push at 08:05 on 13 Feb, €1,428.00 before the cut, a 5% holdout and 7.4M saved searches.

## property-page-and-room-selection (20)

- The hand-off now goes to **[[part-5]]**. It had gone to checkout-orchestration, but this is the last chapter of the part.
- The Hotel Miradouro catalog now matches the ledger: 37 rate plans form **168 products**, not 64. The eligible-offers count was adjusted to 97 so the funnel still reaches 20 rows.
- **Lisbon tourist tax (consistency item 4):** I re-fetched Airbnb help article 2290 and it confirms €4.00 per person per night, maximum 7 nights. It states no child exemption, and lisboa.pt returned 403. The scene and the source note now present the under-13 exemption as Corvane's unverified working assumption, which agrees with the Part VI `[editor-review]` line and taxes-on-stays.
- Named **Levy** (first release Q4 2027) as the tax engine. Flagged Airbnb's 300,000-listings cleaning-fee claim as not verified. Flagged the 2021 accessibility review as possibly superseded.
- Trimmed the fragment-ownership sources, the enforcement/Airbnb paragraphs, strikethrough, normalization/occupancy, reviews, generated summaries, accessibility, performance, failure modes and one question. Removed three sources that are no longer cited (InfoQ 2018, Expedia reviews 2023, Morning Paper). The timetoread is now 34 min.

## Ledger

- Appended one `[editor-review]` line covering the Front Row rename, Waypoint in June 2027, the 2,600-candidate trace and Miradouro's 168 products.

## Open issues for other pages

- **Pages still using "Visibility Plus"** need to be changed to "Front Row" by their owners: `posts/meet-corvane/index.md`, `posts/10-extranets-and-host-tools/index.md`, `posts/15-promotions-and-loyalty/index.md`, `posts/39-marketplace-intelligence/index.md`, `posts/48-case-booking-com/index.md`, `posts/51-case-agoda-trip-com/index.md` and `posts/glossary/index.md` (entry "Visibility Plus / Ranking Policy v1"). The ledger's original [stays-ranking] line still uses the old name; the `[editor-review]` line overrides it. Consistency item 2 can be closed once these pages are done.
- Any page that cites a Lisbon tourist-tax child exemption as fact should hedge it, as ch. 20 and taxes-on-stays now do.
