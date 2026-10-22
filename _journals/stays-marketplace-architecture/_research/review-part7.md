# Review log — Part VII (TRUST)

Editorial pass, 2026-10-21. Scope: part-7-intro, 31–36. Word counts are the prose before `## Sources and Evidence`. No page was over 9,000 words, so I trimmed nothing.

| Page | Words before → after | Changes |
| --- | --- | --- |
| part-7-intro | 1,058 → 1,058 | None. Above the style guide's 500–800 range, but every part intro in the book is 1,030–1,190 words, so I left it to match the others. |
| 31 stays-trust-and-safety | 8,371 → 8,371 | American spelling: neighborhood, neighbors, behavior, honored, honor, honoring. Timetoread changed from 34 to 36 min. |
| 32 travel-fraud | 8,469 → 8,469 | Timetoread changed from 35 to 37 min. The phishing-wave figures match the ledger: 230/4,100/310/€212,000/€684, 1,260 contacts, 37 domains, 148/82, 86%, January 2028 26/610/640/3. Partner Shield, Autumn Cities, €46M Circle credit and the 16,000 takeovers also match. |
| 33 identity-accounts-and-access | 8,340 → 8,346 | "Airbnb's 2025 annual report" changed to "annual report for fiscal 2025". Timetoread changed from 33 to 36 min. Corvane ID (June 2027, rollout Q1 2028/2028/2029, Burrow purge October 2027, ~31,000 held) and the Miradouro 11→1 migration (February 2028) match the ledger. |
| 34 reviews-and-reputation | 8,395 → 8,395 | Timetoread changed from 33 to 37 min. The ring, Hearth, Vouch (18 May 2027; Nookaway live November 2027) and June 2027 Roomstead audit figures match. €14,300 = 1,940 × €46 × 16%. |
| 35 protection-and-incidents | 8,348 → 8,348 | "fulfil" changed to "fulfill". Timetoread changed from 33 to 36 min. The Dubrovnik items, dates and weekdays, the 70-minute response, the €2,550 net and the 21 Sept 2027 decisions match the ledger. |
| 36 stays-regulation | 7,872 → 7,876 | American spelling: licence(s) → license(s), "programme eligibility" → "program eligibility". "Licences API" is kept because it is Booking.com's product name. Replaced the unverified "Article 3(12)" pin-cite with a reference to the Regulation's activity-data definition. Timetoread changed from 37 to 34 min. |

## Consistency checks

- **Spanish purge.** All pages give 9 Feb–24 Apr 2026, before the Supreme Court ruling announced 21 May 2026 (judgment 620/2026), so they match the `[editor]` line. Chapter 36 states that regional numbers still apply and that the annulment is real. The reconstruction (1,240/870/1,510, 9 analysts for 7 weeks) and the Ordinance replay (3,180/2,480/1,240) agree with the ledger, toolkit, meet-corvane and where-stay-platforms-go-wrong.
- **Platform dates.** Warden 17 Aug 2027 (Q4 2027 / Q1 2028), Vouch 18 May 2027, Ordinance 17 Mar 2027 (ES/PT May 2027, gateway Sept 2027) and Corvane ID June 2027 are consistent across Part VII, toolkit, meet-corvane and ch. 43. Turia Homes figures sum correctly (€48,540; €31,640 avoided; 16 days).

## External claims spot-checked

- **BOE consolidated RD 1312/2024** (updated 18 Jul 2026): Art. 10 and the other registry articles are annulled. The text cites Supreme Court judgments of 19 May, 21 May and 1 June 2026, so ch. 36 is accurate.
- **Airbnb identity-graph post:** 7B nodes, 11B edges, 4–8 hops, JanusGraph/DynamoDB/OpenSearch. The page carries no date; its image paths suggest May 2026.
- **Airbnb July 4 post** (24 June 2026): more than 20,000 redirected in 2025.
- **EC AI Omnibus:** in force 27 Jul 2026; Annex III applies from 2 Dec 2027.
- **Booking.com DSA page:** "well above 45 million" for H1 2026.
- **Airbnb Q3 2025 shareholder letter:** "removed over 550,000 listings" since the 2023 hosting quality system.

Press-based claims are already hedged as press reports or secondary sources: Airbnb's ~65,000 Spanish removals, the Paris 90-night cap (Houst), the CNMC fine suspension (Hosteltur), the ABC7 camera ban and the Krebs-relayed 85 million figure.

## Build and render

The build passes. render_check returns OK for all 7 pages: no failed mermaid, no unresolved links, no XJ problems.

## Open issues for the author

- "One Stay programme" (22 uses) and "One Stay program" (9 uses) are mixed across the book. The ledger uses "programme", so I left it, but the book should pick one spelling (American "program" per the style guide).
- All part intros exceed the 500–800 word guide. Either the guide or the intros should change.
- Not verified: Airbnb's $67M 2025 chargeback expense (ch. 32) and the STR Regulation article numbering for the definition of activity data (EUR-Lex did not render).
