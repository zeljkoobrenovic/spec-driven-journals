# Review log — Part IV (A): part-4 intro and chapters 16–20

Editorial pass, 2026-10-22. Prose words are counted up to `## Sources and Evidence`, with pipes stripped. No page was over 8,500 words, so nothing was trimmed.

| Page | Before | After |
| --- | --- | --- |
| part-4-intro | 1,171 | 1,183 |
| 16-vehicle-acquisition | 7,566 | 7,574 |
| 17-inventory-and-vehicle-dossier | 8,054 | 8,147 |
| 18-used-car-pricing | 7,557 | 7,557 |
| 19-merchandising | 7,590 | 7,628 |
| 20-listing-syndication | 8,088 | 8,094 |

Format checks passed on all six pages: front matter, callouts in order, `<br>`, Across Markets, failure handling, Chief Architect's view, Questions, Sources, hand-off to the next page in config order, consecutive figure captions, and valid `[[…]]` links (including the sibling links `media-pipeline` and `connectivity-and-channel-managers`). Every timetoread is within about a minute of 230 words per minute.

## Changes per page

- **part-4-intro**
  - The Zombie Golf summary no longer says the sold status "never reached Lotwise". It now says the DMS sold row was never matched in Lotwise, and that the deletes queued after the car was marked sold by hand, as the ledger records.
- **16-vehicle-acquisition** (item 28)
  - The appraisal date is now Saturday 11 Sept 2027, at 61,240 km (was 61,090). This is updated in the record table, Figure 3 and the text.
  - Offer v2 is now valid to 61,740 km.
  - The handover reading is now 61,302 km (was 61,155), described as "62 km over" the appraisal and three days after it.
  - American spelling: programme→program, tyres→tires.
- **17-inventory-and-vehicle-dossier** (items 24, 31, 32)
  - Lifecycle diagram: Reserved→Sold now happens on "conditions met and invoiced". A lapse or a cancellation before the invoice returns the car to Ready. Sold→Ready needs a credit note.
  - The Reserved guard now includes a signed sale contract.
  - The Sold guard is now: deal conditions met (payment or financing confirmed) and the invoice issued, or delivery where the dealer marks the car sold on delivery.
  - The Delivered guard no longer says "payment confirmed".
  - Figure 1 caption updated; "Sold requires a signed deal" reworded.
  - Tenant vs legal entity: a stock item now belongs to a tenant (the contracting organization) and is owned by one legal entity within it (item 31b).
  - The ownership table names the DMS's accounting stock unit, which the DMS owns (item 31a).
  - "A deal signed in the DMS" now reads "a sale posted in the DMS".
  - The Velto entity row now says that Velto Nederland B.V. is one of five Dutch legal entities and that the name is illustrative (item 32).
  - The Zombie Golf summary was corrected.
  - American spelling: programme→program, centres→centers.
- **18-used-car-pricing**
  - neighbour→neighbor.
  - All figures were checked against the ledger: Thursday run, Q1 review, vel-core v7 pilot, Octavia floor. The arithmetic checks.
  - No other changes.
- **19-merchandising** (item 28)
  - The Golf Variant mileage is now 61,302 km in three places.
  - "Appraised two days earlier" now reads "three days earlier, on Saturday 11 September".
  - Step 1 now shows the 09:15 handover, the 09:31 stock item and the 09:38 price, and links to journey-inventory-to-portal.
  - "Online 42 minutes after stock-in" now reads "51 minutes after its stock item was created, 42 after the draft opened".
  - The 118,000 Q1 stock-ins are now described as a sample with complete timelines. The full quarter is about 475,000 stock-ins (1.9M a year), so the old wording conflicted with that.
  - programme→program, tyres→tires.
- **20-listing-syndication**
  - Publish rules no longer treat "advertised" as a dossier state, which agrees with chapter 17's track model.
  - programme→program.
- **Specs:** a changelog line was added to all six.
- **Ledger:** one `[editor-review]` line was appended. It records the Golf Variant readings and times, the 118,000 sample, and the Sold rule.

## Evidence spot-checks (WebFetch)

- **AutoNation 10-K for 2025:** "guaranteed trade-in offer honored for 7 days or 500 miles at any of our locations" and "One Price used vehicle centralized pricing and appraisal strategy" are both confirmed (chapters 16, 17 and 18).
- **Bundeskartellamt mobile.de/Carwow clearance:** the press release is dated 8 October 2026, which matches the chapter's "October 2026". Both quoted findings are confirmed (chapter 20).

## Open issues for other pages or the author

1. **journey-inventory-to-portal** says the Golf Variant's offer v2 was "valid until Monday or 61,740 km". vehicle-acquisition, which owns offers, uses the 7-day default: issued Saturday 11 Sept, valid to Saturday 18 Sept, or 500 km. The journey reviewer should change "until Monday" to "for seven days", or give a reason for the shorter validity.
2. **Ledger line `vehicle-acquisition`** still carries 61,090 / 61,590 / 61,155 km. The `[editor-review]` line supersedes it.
3. **Ledger line `merchandising`** still says "61,155 km" and "live 42 minutes after stock-in". The `[editor-review]` line supersedes it.
4. **part-4-intro** has 1,183 words, above the 500–800 target for part intros. It was not trimmed because the brief only asks for trims above 8,500. The author may want to shorten the chapter list.
5. **deals-and-sales-documents vs item 24:** item 24 says a car becomes Sold on "conditions met (payment/financing confirmed)". The deals chapter's table says Sold comes on "invoice issued, or delivery (per dealer setting)". Chapter 17 now states both, so nothing contradicts. A final editor may want one wording book-wide.
