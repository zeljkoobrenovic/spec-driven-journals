# Review log — Part VIII (JOURNEYS)

Editorial pass, 2026-10-22. Scope: part-8-intro (new), 40–43. Word counts are prose words to "Sources and Evidence" (tables counted, pipes stripped). No page was over 8,500, so nothing was trimmed.

## part-8-intro (new, permalink `part-8`)
- Written to the part-intro format (Part VI model): callouts, 3 key points, failure patterns (Zombie Listing, Sticky Error, Leaky Lead), `<br>`, lead on what only the journey view shows (hops, identifiers as idempotency keys, evidence at the ends, recovery), one diagram, a paragraph per journey, hand-off to [[journey-inventory-to-portal]]. Body after the callouts: 535 words; file total about 1,100 words (Part VI intro is 1,075).
- spec.md written.

## 40 journey-inventory-to-portal — 7,479 → 7,479
- WHY THE BUSINESS CARES: generic dealer "he" made neutral.
- Checked: Golf Variant timeline matches item 28 (appraised Sat 11 Sept at 61,240 km = 61,302 − 62; stocked Tue 14 Sept at 61,302 km); Zombie Golf (Feb 2027, Breda, 4 portals/4 days, 37 leads, 9 test drives); €8.8/day holding cost (`dealer-and-data-economics`); 7,200 rooftops, 1.9M stock-ins, 1.4M ops/day, 61 channels; ledger line for the 20 Sept portal outage and the 12 Oct Eindhoven re-key.
- Spot-checked: Emerce 28 Nov 2025 (AutoScout24 took over AutoTrack and Gaspedaal.nl) — confirmed.

## 41 journey-data-correction — 7,374 → 7,377
- Failure-pattern callout: colons replaced by the house em dash.
- Item 17 already followed: median gate described as insufficient, per-chain check (94% of 3,050) as the one that fired.
- Checked against ledger: 2,870 / 6,140 / 412 / 96 / 1,180; 13 May load, 19/21/24 May dates; Volvo XC60 readings; 1,870 + 3,980 + 290; 74/29/212/286; 271/64; CC-2027-0012; 210 XML-only clients.
- Spot-checked: RDW *Tellerstand corrigeren* (business corrects the last reading; older ones by RDW within 10 working days) — confirmed.

## 42 journey-lead-to-dms — 7,451 → 7,504
- Item 27: replaced "three large used-car sites with about 410 cars (240 still booked on 15 Sept)" with the [editor] ledger version: about 1,100 cars, including Velto's central used-car stock, moved to hub Noord-Brabant but stayed advertised under the three old rooftop codes — a hub-sized stock, hence ~160 leads a day. Scene sentence and "Why nobody noticed" aligned.
- Checked: 6 Sept / 3 Sept / 15 Sept timeline, v14/v15, source split 690/280/60/310/120, 188 + 1,272, 96, 37 sales, €6,854, Hitch read-back 25 Oct 2027, DriveDesk Outage 9–21 Nov 2027 with ~11,800/~22,200 split, Pitwall live September 2027.
- Spot-checked: Pied Piper 2025 (4,023 dealerships, 19% no personal reply in 24 h) — confirmed.

## 43 journey-sale-to-registration — 8,214 → 8,225
- Failure-pattern callout: colons replaced by the house em dash.
- Item 25: the DMS paragraph said the registration "starts from" the DMS sold signal, contradicting the next section (DMS sales still started by a dealer click in 2027); reworded so the signal supplies the key whichever trigger starts the act.
- Items 24 and 26 already followed (signing reserves, invoice/conditions make Sold, payment release rule; Brandsma added Sales Admin January 2027).
- Month-End Outage agrees with ledger and `reliability-and-dependencies`: 14:20–20:00, slow to ~15:05, banner ~15:20, 3,100 queued (1,610/1,240/180/70), 214 doubles (131/83), 41 ambiguous on 30 June, redesign 14 June.
- Spot-checked: RDW *Voertuig op naam van een klant zetten* (authorization valid 3 months, DigiD; card within 5 working days) — confirmed.
- Hand-off: ends with [[part-9]] and [[build-buy-or-partner]] — correct.

## Cross-journey consistency
- Brandsma: Leeuwarden, one rooftop, ~55 cars, no DMS, Sales Admin since Jan 2027 — consistent across 40, 42, 43.
- Velto: 46 rooftops, 7 legal entities, DriveDesk; Zombie Golf at Breda — consistent across 40, 42, 43.
- Withdrawal p99 6 h 20 min (June) → 14 min (September 2027) — 40 and 43 agree; priority lane "summer 2027" in both.
- Golf Variant appears only in 40; Month-End Outage told in 43 and referenced consistently.

## Other pages
- 39 privacy-and-retention: closing sentence reworded so it hands off cleanly to [[part-8]] (it already linked part-8, awkwardly as "starting with [[part-8]]"); spec changelog appended.

## Checks
- Build: passes (one transient OSError in another journal from a parallel build; rerun clean).
- Render check: part-8, 40–43 and privacy-and-retention all OK, no mermaid failures, no unresolved links.

## Open items for the author / other reviewers
- timetoread on 43 (33 min) is slightly low for 8,225 words (~36 min); left as is.
- Sources sections in 41–43 use bold group labels while 40 uses `###` headings; harmless, could be harmonized in a final pass.
- Item 33 (`vehicle.fact.disputed` in the `events-webhooks-and-sync` catalog) is still for the Part VI reviewer.
