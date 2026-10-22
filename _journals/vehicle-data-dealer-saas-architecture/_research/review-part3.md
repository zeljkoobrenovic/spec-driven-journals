# Editorial Review — Part III (VALUE)

Reviewer pass, 2026-10-22. Pages: `part-3-intro`, `11-market-data`, `12-valuation-engine`, `13-condition-and-damage`, `14-ev-battery-health`, `15-connected-vehicle-data`.

Word counts are prose words before `## Sources and Evidence` (pipes stripped). No page was over 8,500, so nothing was trimmed.

| Page | Before | After |
| --- | --- | --- |
| part-3-intro | 1,028 | 1,028 |
| market-data | 7,479 | 7,512 |
| valuation-engine | 8,199 | 8,230 |
| condition-and-damage | 8,029 | 8,029 |
| ev-battery-health | 7,645 | 7,661 |
| connected-vehicle-data | 7,432 | 7,460 |

Build: no errors. Render check: all six pages `OK` (mermaid rendered, no unresolved links).

## part-3-intro

- No edits. Callouts, figure, chapter list and hand-off (to `market-data`) checked against the chapters and the ledger (EV Overvaluation 9.5%/14 weeks, Fleetmoor no-sale rate 18% → 41%, Pulse 61%, de-listing audit 68%).
- Note for the author: at 1,028 words it is above the 500–800 target for part intros. It is under the trim threshold, so I left it.

## market-data

- Flagged the Cox January 2022 days' supply definition as more than three years old.
- Flagged the Auto Trader July 2023 Retail Price Index method ("circa 800,000 daily pricing observations") as more than three years old. Checked by WebFetch: the figures (800,000 observations, used-EV −19.1%, supply +174%, published 5 July 2023) are accurate.
- The segment minimum-evidence rule (30 on offer, 10 sales) is an Axleby ledger fact, so I removed the `*(assumption)*` label and stated it as Axleby's rule.
- Checked by WebFetch: the Bundeskartellamt release (8 October 2026) and its quotes on multi-homing and data export are accurate.
- Ledger figures checked: Pulse breakdown, de-listing audit, BEV segment table (33.8 vs 31.0 days; ×1.6 and ×1.47), Q4 2027 match and coverage, the 30-day delay and ≥5 rooftops / ≥20 cars rule, and the Belgian purge rehearsal (31 hours).

## valuation-engine

- **Consistency item 30:** rewrote the AI Act paragraph. The high-risk dates now follow Regulation (EU) 2026/1744 (Digital Omnibus on AI, OJ 24 July 2026): **2 December 2027** for Annex III and **2 August 2028** for Article 6(1). The paragraph notes that Article 4 was narrowed, links [[ai-in-dealer-workflows]] and adds the regulation to Sources. The Publications Office record confirms that the act exists, amends 2024/1689 and was published on 24 July 2026. I took the dates from `ai-in-dealer-workflows`, which fetched the text. Also resolved the open question in the spec.
- **Item 11:** this page already agrees with it (UK used EVs −22.7% vs petrol −3.8% / diesel −2.2%; Hertz $245M). Checked the Hertz 8-K by WebFetch: about 20,000 EVs and about $245 million of incremental net depreciation.
- **Item 12:** this page already agrees with it (Auto Trader's 99/97/95% is measured against its own later valuation).
- Corrected the scope of a cross-cloud failure. It was "trade-in offers at 7,200 rooftops"; it now says "the roughly 4,800 Lotwise rooftops that use Appraise", per the `vehicle-acquisition` ledger line.
- Flagged two older sources: the Auto Trader June 2023 ML "c.500,000 observations" and the Cox January 2022 stability quote.
- Expanded VRM.
- EV Overvaluation figures checked against the `valuation-engine` ledger line (window, MdAPE 6.1 → 6.6%, 8% alert, +13.1% peak in week 12, 400-sale minimum, 610 cars, €1.1M, replay week 5 and €0.3M) and the `[editor]` valuation-counts line (19M issued vs 350,000 nightly stock signals).

## condition-and-damage

- Corrected timetoread from 31 to 35 min.
- Changed "analyst's translation" to "author's translation" (2 places).
- Changed the Sources group headings from bold to italic, to match the house style.
- Checked by WebFetch: the SRA article on BPM valuation-report checks (17 July 2026; independent recognized appraiser; within one month before the RDW inspection; exaggerated damage) is accurate.
- Ledger figures checked: Fleetmoor Q1 and Q4 2027, the claim mix (39/24/21/16, so the "61%" sum is correct), recon variance (+€310 → +€95), the Inspect pilot date (14 June 2027) and the Handback prototype (October 2027, about 200 returns). The Peugeot 308 table arithmetic (€260 / €1,930 / €1,290) and the image-volume estimates are correct.

## ev-battery-health

- Updated the status of the Article 77(9) implementing act. The text no longer stops at "could not confirm". It now says that as of October 2026 only a draft was found, and cites EUROBAT's 27 May 2026 feedback on the draft implementing act (fetched and read). Adoption is still unconfirmed from an official source.
- Corrected timetoread from 31 to 33 min, and aligned the Sources headings.
- The Two Certificates figures, the 6,700-PDF verification, the €107-per-point slope (91% → −€320, 87% → −€750), the 3,400 tests and the Q4 2027 61% all agree with the ledger.
- Checked by WebFetch: Car-Pass SoH linking is accurate.

## connected-vehicle-data

- Expanded acronyms on first use: FRAND, GNSS, TDDDG, PECR and ICO.
- Renamed the heading "Trade-offs" to "Trade-Offs".
- Corrected timetoread from 34 to 32 min, and aligned the Sources headings.
- Checked by WebFetch: the FTC GM/OnStar final order (14 January 2026; "misleading enrollment process"; five-year ban on disclosure to consumer reporting agencies; affirmative express consent) and Car-Pass's 345.5 million readings in 2025 are accurate.
- Pilot figures (11,600 / 9,400 / 7,950 / 830 / 620; 5.8%; 6.9%; 1,020 and 97.8%; 21,000 promoted; 1,140 dual-route; 640 sold / 23 streaming / about 140 readings) agree with the ledger, and the derived shares are correct.
- The hand-off goes to `part-4` and then `vehicle-acquisition`, which is correct.

## Open issues for other pages or the author

1. **`ai-in-dealer-workflows`, line ~320:** the sentence "This updates the timetable given in [[valuation-engine]], which was written before the Omnibus text was final" is now stale. Valuation-engine uses the 2026/1744 dates. The Part VIII/IX reviewer should drop or reword that clause.
2. **Forum naming:** market-data and valuation-engine say Ines took her question to "the One Dossier architecture board in March 2027". The ledger dates the first One Dossier architecture forum to 22 April 2027 and the architecture board's v1 to 3 June 2027. This is harmless, but the final editor may want "the One Dossier programme review" or a date-neutral wording.
3. **Article 77(9) implementing act:** if the act is adopted before publication, update ev-battery-health (Definitions and Chief Architect's View) and its spec.
4. **part-3-intro length:** 1,028 words against the 500–800 target for intros. Left for the author to decide.
