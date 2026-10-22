# Editorial Review — Part X (PRACTICE)

Reviewer pass, 22 October 2026. Scope: `part-10-intro`, `50-case-cox-automotive`, `51-case-cdk-global`, `52-case-auto-trader-uk`, `53-case-vwe`. Case studies have no "Across Markets" section, as briefed. Word counts are prose words before `## Sources and Evidence` (table pipes removed). No page was over 8,500 words, so nothing was trimmed.

## Word counts

| Page | Before | After | Reading time |
| --- | --- | --- | --- |
| part-10-intro | 980 | 980 | 5 → 4 min |
| case-cox-automotive | 7,565 | 7,637 | 29 → 33 min |
| case-cdk-global | 7,155 | 7,169 | 32 → 31 min |
| case-auto-trader-uk | 7,540 | 7,634 | 31 → 33 min |
| case-vwe | 7,304 | 7,336 | 30 → 32 min |

## part-10-intro

- Callouts, table, chapter list and hand-off to `case-cox-automotive` are correct. Claims (15,000 dealerships; VWE moves from 2022 to 2026) match the cases.
- Reading time corrected to 4 min. At 980 words the intro is above the 500–800 target. I left it, because the comparison table carries the evidence rules.

## case-cox-automotive

- **Item 18 (Bridge Federation):** I fetched https://www.coxautoinc.com/bridge/federation/ myself on 22 Oct 2026. The page offers OIDC federation to "Dealerships and Lender Partners with their own Identity Provider", and users must already be Bridge users. I replaced the "could not be fetched" sentence with the quoted evidence and the same URL and access date as `identity-access-and-entitlements`. I also added the source entry and updated the comparison and evidence-gap tables.
- The opening said "the largest group … by most measures". It now attributes that claim to Cox's own October 2026 boilerplate ("the world's largest automotive services and technology provider"). I verified the boilerplate in the 8 Oct 2026 VinSolutions/Fullpath PDF, together with "One less system to log into", 29,000+ employees and 2.3 billion interactions.
- Checked item 1 (incadea owned 2015–2018, then sold to Volaris; it is never called a current Cox product) and item 7 (no Autorola claim on this page).
- The Axleby figures agree with the ledger: One Dossier €38M for 2027–2029, about 300 engineers, DriveDesk on 1,900 rooftops, the 12-day outage in November 2027, Pulse at 2.3M adverts a day with a 61% match rate, the EV Overvaluation at 9.5% for 14 weeks, and Showroomly acquired in 2023.

## case-cdk-global

- **Item 10:** I fetched AutoNation's 15 July 2024 8-K. It says EPS "will be negatively impacted by approximately $1.50 per share" before potential recoveries. The table row now quotes that figure and names the filing.
- **Item 2:** no "2018 consent" appears. The 2015 agreements, the Authenticom litigation and the settlements are described correctly.
- The CEO succession (5 Oct 2026, announced 27 Aug 2026) was sourced only to Wikipedia. I verified it by web search and added CBT News (2026) as the source.
- The Axleby figures agree with the ledger: 640 API clients, 210 that use only XML, the sunset on 31 Dec 2029, the Zombie Golf (4 portals, 4 days), the Lost Leads (1,460) and Velto's 46 rooftops.

## case-auto-trader-uk

- **Item 4:** the Deal Builder protest is dated November 2025 throughout.
- **Item 12:** the page claimed that no source publishes Auto Trader's valuation error. That is wrong: the valuation brief and `valuation-engine` cite the help-center accuracy figures (99/97/95% at 1/3/6 months). I added those figures, with the caveat that they are measured against Auto Trader's own later valuation and not sale prices, and adjusted the evidence-gap table, the comparison row, the Axleby row and the Chief Architect's view to match. I added the help article to Sources. The page returned 403 to WebFetch, so the entry says the figures came from the brief.
- I verified the FY2026 results PDF: ARPR £2,995, 13,942 forecourts, 220+ partners, 155m calls a month, Deal Builder at 6.7k retailers, 175k vehicles and 137k deals, the response wording ("pausing auto-rollout …") and "11x" its nearest competitor. The stock-lever outlook now gives the unit: the lever cut ARPR by £48 in FY2026, and the outlook is minus £30–40.
- I replaced "Leverage over dealer workflow" with "Power over dealer workflow" to remove a buzzword.

## case-vwe

- **Mermaid:** all four diagrams were wrapped in triple-backtick code fences around the `---begin mermaid---` lines, so they would have rendered as code. I removed the backtick fences, and the render check now draws 4 mermaid diagrams.
- **Item 6:** the page already says that the public developer documentation is XML only (Interdata, XMLmode). I fetched the English "Vehicle characteristics" page on 22 Oct 2026. It does say "registration plate API" with data "via JSON" and a demo environment. The page's "public-record discrepancy" paragraph is therefore accurate, and I kept it. The canonical line in item 6 still holds for the API documentation.
- **Productscape:** the page states plainly that the model was the author's research map, built by inference. Its one Productscape detail (a cached register and a retry queue) is labeled as the author's assumption. No bricks are presented as VWE internals.
- **Axleby distinct:** the dedicated comparison table and the "not a disguised VWE" paragraph are clear. The paragraph called Axleby Data "an authorized provider of the Dutch register". It now describes a contractual data-supply and transaction-provider relationship, uses *authorized information provider* as a book term and links `registers-and-official-data` (items 13 and 23).
- **Item 14:** the UK row said "DVLA vehicle data … through public APIs". It now names the DVSA MOT history API, with its bulk files and daily changes, and says DVLA's vehicle enquiry API has been closed to new registrations as of October 2026.
- **Main Capital deal:** a web search on 22 Oct 2026 found no closing or ACM decision, which matches the page's "not confirmed".
- The carVertical source label now reads "read Oct 2026" instead of "2026", to match the n.d. source entry.
- The Axleby figures agree with the ledger: Month-End Register Outage (31 Mar 2027, 5 h 40 min, 3,100 queued, 214 duplicates), No-Hit Credit (€186,000, 41 clients), €214M revenue, 1,150 staff and 12,400 customers.

## Checks run

- Spot-checks by WebFetch or search: Cox Bridge ID and Bridge Federation pages, the Cox/VinSolutions October 2026 release, AutoNation's 8-K of 15 July 2024, the CDK CEO succession, Auto Trader's FY2026 results, VWE's Vehicle characteristics page and the Main Capital closing status.
- Cross-links: every `[[…]]` resolves to a valid permalink, or to the allowed LISTED sibling `multi-country-platforms`.
- Hand-offs follow config order: intro → Cox → CDK → Auto Trader → VWE → `domain-coverage`.
- Build: a transient OSError came from a parallel build in another journal's assets. A rerun built `vehicle-data-dealer-saas-architecture` cleanly.
- Render check: all 5 pages print `OK` (Cox 4 mermaid diagrams, CDK 4, Auto Trader 3, VWE 4).

## Open issues for the author or other parts

- The build warns that `posts/glossary/index.md` and `posts/bibliography/index.md` are listed in config but missing (Reference part).
- `case-auto-trader-uk` cites the help-center accuracy article from the brief because the page refuses automated access. Verify it by hand if possible.
- In VWE's comparison table, "Eleven fictional incidents" matches the eleven recurring worked examples in the ledger. Change the count if the ledger grows.
