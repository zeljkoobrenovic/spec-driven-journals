# Review log — Part II (SUPPLY), editorial pass 2026-10-21

Words = text before `## Sources and Evidence`. Build passes. Render check: all 7 pages print OK (no mermaid failures, no unresolved links, no XJ links).

## part-2 (part-2-intro) — 1,049 → 1,041 (whole file)
- Tightened two KEY POINTS bullets and two lead sentences.
- Brightwell's 41,000 "new" **hotels** changed to "properties" (ledger).
- The chapter-05 summary now says that Waypoint ([[destinations-and-maps]]) enriches the place registry (issue 9 / map v2).
- Remaining: still above the 500–800 guide for part intros. The author may want to cut further.

## 05 property-and-listing-model — 8,799 → 8,492
- Place registry and Waypoint are now two components (Waypoint, June 2027, Jonas Weber, first release Q1 2028, writes geo enrichment to registry records, never the reverse). Changed in the decision item, the architecture table's "Must not" cell and the Location section.
- The registry is described as the design of map v1's "property and unit identity" shared contract; map v2 ([[converging-two-marketplaces]]) keeps it.
- The boutique-hotel pilot now follows the cross-type routing rule (hotel-type engine behind the Nookaway storefront). Multi-unit listings is shown as Rafael's first proposal.
- The Vrbo quote is corrected to the guide's wording: "not applicable to Vrbo".
- "licence" → "license". "Mistakes I see most often" → "The common mistakes" (no first-hand claim).
- Trims: the IN THIS CHAPTER callout, KEY POINT 3, two repeated failure-mode bullets, the scene, the Chief Architect's points and the hand-off. timetoread → 37 min.
- Removed the `[[glossary]]` link, which resolved to RECONCILED's glossary (XJ) because BOOKED has no glossary page yet.
- WebFetch confirmed: Booking.com rate plans (200 max), the Rapid Vrbo guide, the Airbnb Q2 2026 letter.

## 06 partner-onboarding — 8,610 → 8,499
- Added a "## From Onboarding to Content" hand-off heading, linking [[content-and-media]].
- Supply-party recommendation: map v1 already listed party onboarding as a shared engine, and v2 keeps it (links to [[stays-capability-map]] and [[converging-two-marketplaces]]).
- Spanish removals dated February–April 2026, per the [editor] line.
- Acronyms expanded on first use (OTA, PMS, VCC, ARI, EMI, PSP, STR, CRM, GDPR; DAC7 glossed). licence → license; programme → program.
- The Airbnb 2909 citation is narrowed to the non-EU/UK/AU version (updated 5 Feb 2026). Fixed a logic slip in the metrics paragraph.
- Cut repeated Booking.com status text, the skip_rtc_rto passage, duplicate sentences and Question 10. timetoread → 37 min.
- WebFetch confirmed: Airbnb 2909; Booking.com statuses and the 12:00 batch; the CGPJ note on judgment 620/2026.

## 07 content-and-media — 8,233 → 8,332
- Content sharing aligned with map v2 (issue 5):
  - The media pipeline and translation were already shared engines in v1, and the hash index is part of the media pipeline.
  - Policy rendering comes from Clause and the display policy service.
  - Concord's matching engine becomes a group engine from 2028, still run by Roomstead supply; the bedbank workflow stays with Roomstead.
  - The Hotels and Homes table, its judgement and the Chief Architect's view are updated, with a [[converging-two-marketplaces]] link.
- Booking.com deprecation corrected: only `OTA_HotelInvNotif` for Home providers (Dec 2024, sunset 31 Dec 2026), not `OTA_HotelDescriptiveInfo`. Corrected in the text and in Sources.
- OTA and STR expanded. Added "may be out of date" flags on the 2021–2022 Airbnb sources. The spec's open question on One Stay scope is marked answered.
- WebFetch confirmed: Booking.com Photo API, the RMA codes, the Airbnb 2021 Winter Release.

## 08 connectivity-and-channel-managers — 9,210 → 8,461 (required trim)
- Trimmed the lead and the scene. Condensed the hold, ordering, full-sync, delivery and rate-limit text, the bedbank and certification sections (dropped a duplicate AlpineBits row), the deprecation text, the neutrality text, the failure modes and the Chief Architect's view. Questions went from 10 to 9.
- All €12 Miradouro figures, the Switchyard redesign facts, the neutrality rule and the volumes are kept and match the ledger.
- King's Day queue dated 26 April 2027. "architecture advice forum" → "architecture forum".
- Booking.com reservation retrieval wording corrected to the docs ("once per twenty seconds"; returned until acknowledged). Added a second citation.
- Added a missing blank line after a table, which had swallowed the next paragraph. OTA and GDS expanded. "leverage" removed. timetoread → 37 min.
- WebFetch confirmed: the €5/€50,000 price bounds, the 30-minute email fallback (extendable to 24 h), 20-second polling.
- Not re-verified (403): the Agoda "1.5M price updates/min" Medium post and the SynXis–TPG July 2025 sale. Both are kept as dated, cited reports.

## 09 calendar-sync — 8,070 → 8,090
- Added a "## From Calendars to Workspaces" hand-off heading, linking [[extranets-and-host-tools]].
- OTA, PMS, CRS and ARI expanded on first use; duplicate expansions removed. "centre" → "center".
- Hedges added:
  - the earlier "every 2 hours" iCal claim is now marked as reported and unverified;
  - the 2020 Airbnb Community thread is flagged as anecdotal;
  - the list of 34 Airbnb software partners is marked "may differ".
- timetoread → 35 min.
- Seville, conflict and Calendar Sync v2 figures all match the ledger.
- WebFetch confirmed: Airbnb help article 99 (3-hour refresh), RFC 5545 DTEND/UID, the Booking.com overbooking FAQ.

## 10 extranets-and-host-tools — 8,639 → 8,494
- Miradouro's 14 Sept 2027 closure: "Superior Twin" → "Twin" (not a Miradouro room type). An [editor-review] ledger line was added.
- Courier named as the group notification platform, and Gauge as the metric layer behind partner analytics. programme → program (the real "Preferred Partner Programme" title is kept).
- Light trims across 17 passages. timetoread → 37 min.
- WebFetch confirmed: AGCM PS13115 (22 April 2026), the Booking.com 30-minute acknowledgement, Expedia's top-20 sort clicks (2024 data), the Airbnb co-host permissions (article 1534).

## Open issues for other parts / author
- **`[[glossary]]`** in introduction, toolkit and domain-coverage resolves to RECONCILED's glossary (XJ) until BOOKED's glossary page exists.
- **Superior Twin:** the ledger's extranets-and-host-tools line still says "Superior Twin". The [editor-review] line supersedes it.
- **Spelling, book-wide:** "One Stay programme" (about 23 uses) vs "program" (about 10), and "cancelled" vs "canceled", each need one decision.
- **Visibility Plus** (issue 2): chapter 10 links it to [[stays-ranking]] and must change if the program is renamed.
- **Rate Insights** (9% acceptance in 2026) appears in chapters 10, 39 and 44 but not in the ledger; it is worth adding.
