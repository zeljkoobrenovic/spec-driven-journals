# Review log — Part VI (DISTRIBUTION)

Editorial review pass, 2026-10-22. Word counts are prose words before `## Sources and Evidence` (table pipes stripped). No page was over 8,500 words, so nothing was trimmed.

## part-6-intro (`part-6`)

- No changes. Callouts, failure patterns, Figure 1, chapter list and hand-off to `vehicle-data-apis` checked.
- Words: 1,075 → 1,075. This is above the style guide's 500–800 range for part intros, but under the trim threshold. **For the author:** consider tightening.

## 31-vehicle-data-apis

- Item 20: the October 2027 milestone is now named "v2 public lookup contract and developer portal", and v2 webhooks are dated Q3 2028, in the scene and in the hand-off.
- Expanded acronyms on first use: VIN, SKU, BEV, SLA, MOT, NMVTIS, VRN, StVG (Road Traffic Act).
- American spelling: modeling, signaling.
- timetoread 33 → 34.
- Spot-checked: DVSA rate limits (500,000/day, burst 10, 15/s, 24-hour restriction) are verified. The Autotrader Connect 404→200 breaking change is verified: sandbox Friday 11 September, listed under the 30 November 2026 heading. The 30-day notice is verified.
- Words: 7,797 → 7,848.

## 32-events-webhooks-and-sync

- Item 25: the sold-audit row for Axleby Trade now says that from June 2027 a sale at a Lotwise Sales Admin rooftop creates the registration transaction, held as Draft until the payment release rule is met. A sale entered in a DMS still needs a dealer click. The row links to `journey-sale-to-registration`.
- Item 33: `vehicle.fact.disputed` added to the catalog row for vehicle facts, linking to `journey-data-correction`.
- Item 20: the builds-on paragraph names both milestones: lookups since October 2027, webhooks from Q3 2028. The Q1–Q4 2028 sequencing already matched the ledger.
- Expanded acronyms: DMS, CDC, CRM, ADF, DVSA, DVLA, MOT, NMVTIS, STAR. RCI is now attributed to Reynolds and Reynolds.
- timetoread 33 → 34.
- Spot-checked: the CloudEvents CNCF graduation (25 Jan 2024, Event Grid and Eventarc) is verified. The Standard Webhooks steering committee includes Zapier, Twilio, Svix and Kong (verified; it also lists Lob, Mux, ngrok and Supabase). The Autotrader retry schedule (10 s / 30 s / 30 min) was not found in the first part of the docs page I could read. It stays as the brief states it. **For the author:** it is not re-verified.
- Words: 7,772 → 7,872.

## 33-data-products-and-insights

- **Format fix:** all four mermaid blocks were wrapped in ``` code fences, which would have broken rendering of the diagrams and captions. The fences are removed. The quotes around the stateDiagram transition labels are also removed, because they would render as literal quote marks.
- Item 22: added the pre-2027 retention. Monthly scores were kept indefinitely, and the August 2027 erasure request found 14 scores back to 2024. The text links `privacy-and-retention`. The 90-day expiry remains the post-redesign rule.
- Item 21: checked. The 2027 design is match-in on the client's own customers only, with aggregates for everyone else. The pre-2027 territory lists appear only as the history the DPIA ended. This chapter is consistent with the ledger's `data-products-and-insights` line and the `[editor]` Horizon line.
- Expanded acronyms: VIN, APK (italicized), CRM, DMS, KBA, DfT, DVLA, DVSA, MOT, DPPA, StVG.
- American spelling: "anonymized" outside quotations.
- Spot-checked: the VWE change-of-ownership lead generator page (1–2 months, "hotness" per plate, dealer matches to its own customer file) is verified.
- Words: 7,180 → 7,241.

## 34-consumer-vehicle-checks

- Odolo prices are now stated as VAT-inclusive consumer prices, per the `[editor]` line.
- Added "as of 2026" to the HPI, autoDNA and Car-Pass prices.
- Expanded acronyms: MOT, SLO, DVLA, NMVTIS. DPPA is now expanded at its first use.
- American spelling: fulfillment.
- Spot-checked: the Car-Pass price of €11.10 incl. VAT, free under four readings and mandatory for private buyers, is verified. Crit'Air at €3.85 with the only official site (page verified 1 Jan 2026) is verified.
- Words: 7,168 → 7,198.

## Checks run

- Cross-links: every `[[…]]` on the five pages is a valid permalink. There are no hard-coded book `.html` links except the failure-patterns header.
- Hand-offs follow config order: part-6 → vehicle-data-apis → events-webhooks-and-sync → data-products-and-insights → consumer-vehicle-checks → part-7 / reliability-and-dependencies.
- Build: passes. A transient OSError from a parallel build was cleared by a rerun.
- Render check: all five pages OK (mermaid 1/3/3/4/2, 0 failed, 0 unresolved).

## Open issues for other parts or the author

- **Item 22, `privacy-and-retention`:** it still says "Axleby Insight trade-in signal" / "trade-in-signal scores" and does not use the name **Horizon**. That chapter's reviewer should rename these.
- **Ledger wording:** the `events-webhooks-and-sync` ledger line lists "manual Axleby Trade click" among the sold-audit mechanisms. Per item 25, that now applies to DMS-originated sales only. The chapter is aligned, but the ledger line is unchanged (append-only).
- **Part VI intro length:** 1,075 words against a guide of 500–800.
