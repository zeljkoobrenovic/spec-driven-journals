# BOOKED — Cross-chapter consistency issues

Open items for the review pass. Resolve by editing chapters and adding `[editor]` lines to the ledger.

1. **Place registry vs Waypoint.** `property-and-listing-model` introduces a group "place registry" (decided 12 May 2027); `destinations-and-maps` introduces "Waypoint", the group place service (approved June 2027). Decide whether they are one component or two (registry of properties/units vs geographic place graph) and align names and dates.
2. **Visibility Plus** (stays-ranking) reuses a programme name LISTED uses for Tradeyard. Consider renaming.
3. **Length overruns** (>8,500 words incl. tables): 06, 10, 12, 14, 15, 28 (and check 05, 07, 11, 17, 18 at the limit). Trim in review.
4. **Lisbon tourist tax** €4 / 7-night cap verified only via an undated Airbnb help page; the under-13 exemption is unverified. `taxes-on-stays` should verify it against an official Lisbon source; `property-page-and-room-selection` and the ledger must match.
5. **Content sharing scope.** `content-and-media` recommends sharing five content services, beyond One Stay's ledger scope; `converging-two-marketplaces` must adopt or contradict it.
6. **Search volumes.** The 1,400 figure means shopping requests per reservation (see the `[editor]` line); check chapters 2, 16 and 38 use that wording.
7. **RESOLVED (Gauge rename, 21 Oct).** "Plumbline" used twice. `refunds-and-reconciliation` names Plumbline the reconciliation service; `marketplace-intelligence` names Plumbline the group metric layer (July 2027). Rename one (suggest keeping Plumbline for reconciliation, renaming the metric layer) and fix the ledger with an `[editor]` line.
8. **Experimentation sharing date.** `stays-capability-map` marks experimentation brand-specific until 2028; `stays-experimentation` adopts a group Experimentation Standard v1 on 14 Sept 2027 (Flipside retired Q2 2028). Align chapter 03 (and the 16/6/26 split if it changes).
9. **Resolved by `converging-two-marketplaces` (Dec 2027 map v2: 49 = 23/6/20):** place registry vs Waypoint (two components; Waypoint writes to the registry); content-and-media's five services adopted; experimentation and ML move to shared. Remaining work: `stays-capability-map` should present 16/6/26 as **v1 (March 2027)** and point to v2 in ch. 43; check ch. 40 and 41 agree.
10. **Waypoint date:** `stays-search-architecture` says May 2027; ledger/`destinations-and-maps` say June 2027 (approval). Align to June.
11. **Plumbline** (see 7) also appears in `evolving-the-platform` as the metric layer.
12. **Final pass (after all reviews):** replace "programme(s)" with "program(s)" and "cancelled/cancelling/cancellation(s) stay" → American "canceled/canceling" (keep "cancellation", which is American too) book-wide (posts/*/index.md and spec.md; style guide requires American spelling), except inside quoted titles or proper names of real organizations; do the same in the ledger.
13. **Unverified:** Airbnb $67M chargeback figure in `travel-fraud` — hedge or source in the final pass.
14. **Final pass:** grep for leftover "Watchpost" (removed in Part IX review; replaced by per-brand booking risk score models on Warden).
15. **Final pass:** search cost is ~46% (€44M), €0.0007 per request (per stays-marketplace-economics; `[editor-review]` line). Grep for leftover "€39M"/"€0.0006".
16. **Final pass:** Lisbon child exemption is unverified (lisboa.pt 403). Hedge "children under 13 exempt" as a Corvane assumption wherever stated as fact (`property-page-and-room-selection`, `toolkit`, `meet-corvane`, ledger example 10 via an `[editor]` line). Keep the total €1,271.20.
17. **Check:** `taxes-on-stays` cites a $332M Booking.com Italian tax settlement; the FY2025 10-K text shows a $337M accrual. Verify or reword to "about $0.3 billion" with the 10-K citation.
18. **FIXED (toolkit line 698).** toolkit says map v2 = 22/6/21; canonical is 23/6/20 (49 capabilities). Grep all pages.
19. **Author check:** chapter 05 cites 4.7M Booking.com properties (corporate site) vs 4.4M in the 10-K — explain or align. Agoda Supply API citation needs a live source. Booking.com CNMC, German and Italian cases are open — revisit before publication.
20. **DONE except glossary (sent to reference reviewer).** rename "Visibility Plus" → "Front Row" (Part IV review renamed it in stays-ranking) in every remaining page, the glossary row files (regenerate), and add an `[editor]` ledger line.

## Final pass (21 Oct 2026, editor)

- 12 DONE: 189 + 18 replacements of programme/cancelled/cancelling to American spelling outside URLs, real quotes and Sources; real names kept (Booking.com "Preferred Partner Programme", Agoda/Booking.com quoted documentation, phishing-message quotes, the code identifier `ReservationCancelled`).
- 13 VERIFIED: Airbnb FY2025 10-K: "total chargeback expense was $67 million" (fetched from SEC EDGAR).
- 16 DONE: Lisbon under-13 exemption hedged as the age rule Corvane applies in identity-accounts-and-access and meet-corvane; `[editor]` ledger line added (ch. 20, 21, 29 and the toolkit already hedge it).
- 17 VERIFIED: Booking Holdings FY2025 10-K: November 2024 settlement with the Italian tax authority, "paid $332 million" (STR Law); the $337M figure is a broader 2024 accrual for Italian indirect tax matters. Chapter 29 is correct.
- 19 OPEN for the author (see final report).
