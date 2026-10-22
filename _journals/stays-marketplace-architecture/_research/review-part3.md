# Review log — Part III (INVENTORY)

Reviewer pass, 21 Oct 2026. Word counts are `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`. Pre-edit copies were kept outside the repo (the files are untracked in git).

Build: no errors. Render check (`part-3 rates-and-availability-model availability-engine inventory-integrity dynamic-pricing promotions-and-loyalty`): all six pages print OK, 16 mermaid diagrams, none failed, no unresolved links, no XJ entries.

## part-3-intro (1,053 → 1,062)

- Search volume: "about 1,400 availability lookups per reservation" became "about 1,400 shopping requests per gross reservation, each fanning out to about ten Pricegrid reads" (the `[editor]` line).
- Format, failure-pattern names, chapter list and hand-off were already correct. The intro runs above the 500–800 target. It was not trimmed because it was not in the trim list.

## 11 rates-and-availability-model (9,306 → 8,490)

- Trimmed the "In Practice" survey, which restated the vocabulary sections. Also condensed the failure modes, the scene recap of the €12 rate, the horizon and short-stay bullets, the Chief Architect metrics and the worked-example sizing paragraph. Removed one question (10 → 9).
- Fixed a logic error. The text said materialization is "why Tally absorbs 650 million ARI messages a day". Those messages come from partners, so it now says materialization multiplies write load on top of them.
- Removed an unsourced claim that Airbnb's host pages "have been reported" to contradict its help center.
- Removed the "100 room types" cap. WebFetch of the Booking.com rate-plan and roomrate pages confirmed only 200 rate plans and 400 roomrates. Added "as of 2026" to the caps and horizons.
- Flagged the 2021/2019 Expedia post as old.
- Boutique-hotel sentence now matches the converging-two-marketplaces routing rule (another engine, not eight listings).
- Removed an unused source (Rapid "About the Shopping API"). Set timetoread to 35 min.
- Spot-checks: Booking.com rate-plan definition, the 1–200 percentage format and the 200/400 caps were verified. The Agoda DragonflyDB post returned 403, so its figures stay as cited.

## 12 availability-engine (8,939 → 8,683, light trim)

- Search volumes now follow the ledger: "about ten Pricegrid reads" and "21,000 Pricegrid reads a second". The Black Friday figure became "Pricegrid reads peaked at 96,000/s", and "lookups" became "shopping requests" in the Chief Architect's view.
- "Buys a third of its traffic on metasearch" became "more than a third … through paid search and metasearch", because the ledger's 38% covers both.
- "Roomstead's 41,000 mapped bedbank properties" contradicted the Brightwell ledger line (41,000 in the file, 32,200 matched and 8,410 new). It now refers to the June 2027 Brightwell Beds agreement.
- Removed an unsourced "reportedly SmartTTL" claim. Flagged the Agoda 2020, Expedia 2021 and Booking.com KDD 2019 evidence as old or possibly superseded.
- Condensed the Agoda, Expedia and Airbnb evidence paragraphs and removed a duplicate failure mode ("Age dashboards…").
- Spot-checks: Airbnb total-price release (21 April 2025) and arXiv 2601.06873 (Airbnb, January 2026) were verified. The page's "10,000 updates/s" and IVF details are not in the abstract and were kept as cited.
- Checked the worked-example fan-out arithmetic: 133 × 4 = 532 cells. The dates and weekdays are correct.

## 13 inventory-integrity (9,923 → 8,491)

- Removed the ```` ``` ```` code-block wrappers around all three mermaid fences, which broke the house format.
- Trimmed in these places:
  - Merged the window-policy trade-off table into one paragraph (the concurrency trade-off table remains).
  - Condensed the Booking.com, Expedia and Hotelbeds evidence that repeated chapter 12.
  - Shortened the four window controls, the Seville and King's Day narration, the Connect data-boundary paragraph and the Chief Architect items 2, 3 and 5.
  - Removed a failure mode that restated earlier sections, and one question (10 → 9).
- Removed the "Guestline/IDeaS integration guide (search excerpt)" citation (unverifiable) and the Agoda "reportedly" relocation claim.
- Dated the Airbnb host-fee schedule "as of 2026" and flagged Riasi (2018) as old.
- Ledger check: King's Day (14 sellable, 23 sold, Roomstead 9 = 6 + 3, €2,150 / €1,600, €400 cap), Seville, 2026 baselines and hold times all agree. Timetoread 37 → 35.

## 14 dynamic-pricing (9,044 → 8,499)

- Fixed a contradiction with the ledger and chapter 11. The text said Duarte Silva "sets prices … from a spreadsheet". Miradouro's Flexible rate is set daily by its RMS through the PMS, so the paragraph now uses spreadsheet pricing as the small-hotel case and Miradouro as the RMS case.
- "Price-setting models are tier-1 systems" clashed with Kiln's consequence tiers (where tier 1 = operational). It now reads "run like critical production systems", and Smart Rate is registered as third-party facing when Kiln's tiers arrive in July 2027.
- Trimmed in these places:
  - The Airbnb, PriceLabs and Expedia/Agoda insight paragraphs.
  - The €12 recap (now a link).
  - The Productscape reference-model sentence.
  - Three failure-table rows that repeated earlier text (merged into one).
  - The coordination, strikethrough and governance paragraphs.
  - One question (10 → 9).
- Spot-checks: *Gibson v. Cendyn* (9th Cir., filed 15 Aug 2025, "undoubtedly violate Section 1") and the Agoda Partner Portal release (17 Aug 2026; YCS rename, comp-set benchmark, 90-day suggestions) were both verified.
- Ledger check: Smart Rate figures, Lisbon 16,800 (34/22/44), the strike arithmetic (1,260 × €190 × 17% ≈ €40,700), the summer-2026 RevPAN, guardrail v3, the Novak €145 / €120 / €176 figures and Rate Insights at 9% all agree.

## 15 promotions-and-loyalty (8,695 → 8,563, light trim)

- Renamed "Visibility Plus" to **Front Row** to match `stays-ranking`, which has been renamed (consistency item 2).
- "Architecture advice forum" became "architecture forum".
- The Black Friday sentence wrongly attributed the hit-rate fall to audiences. The cause was sale dates outside the 180-day hot tier, so the sentence was rewritten and links to global-scale-and-reliability.
- Removed an unused source (Agoda Diamond tier) and an unsourced "reportedly, the commission base" claim.
- Changed "cancelled" to "canceled" (American spelling) and shortened the Booking.com Promotions API paragraph and the opening scope paragraph.
- Spot-check: AGCM PS13115 is dated 22 April 2026 and the quotes match.
- Ledger check: the Autumn Cities figures (8,450 / €346,450 / 3,870 / 54% / €161,300 / 31,600 / €1.30M / ~2,700 / ≈€480), the Circle tiers, 238,000 properties, €46M and the weekdays all agree.

## Open issues for other parts or the author

1. **Front Row rename is incomplete.** These pages still say "Visibility Plus": 10-extranets-and-host-tools, 39-marketplace-intelligence, 48-case-booking-com, 51-case-agoda-trip-com, meet-corvane and glossary. The ledger's `[stays-ranking]` line has no `[editor]` rename line yet. The Part IV reviewer, or whoever made the rename, should add one.
2. **Novak price provenance.** The personalization ledger line says the Alfama host cut the price by hand from €165 to €145 on 12 Feb. Dynamic-pricing says the listing was on Smart Rate (minimum €120). The two are compatible (a host override under the precedence rule), but neither chapter says so.
3. **The part-3 intro runs to about 1,060 words** against the 500–800 target for part intros.
4. Chapter 12 cites Airbnb's arXiv 2601.06873 for "~10,000 listing updates/s" and the IVF index choice. These are not in the abstract, so a reviewer with the full PDF should confirm them.
