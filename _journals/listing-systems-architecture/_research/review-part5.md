# Review log — Part V (TRUST)

Editorial review pass, 19 Oct 2026. Pages: part-5-intro, 24-trust-and-safety-architecture, 25-fraud-prevention, 26-identity-and-verification, 27-marketplace-regulation. Render check: all five OK (12 mermaid diagrams, no unresolved or cross-journal links).

## part-5-intro (`part-5`)
- No article changes needed. Format, ledger facts (bike timings, Barcelona ring, decision dates), links and hand-off to [[trust-and-safety-architecture]] all check out. The DSA 6% fine ceiling (Art. 52) was verified against the Official Journal text.
- Spec: decision-log line about the superseded Safe Deal figures updated; Changelog entry added.

## 24-trust-and-safety-architecture
- Consistency issue 20: Ingrid "had joined three weeks earlier" changed to "five weeks earlier" (she started 1 Feb 2027).
- Consistency issue 4: the DSA Art. 16, 17, 20 (six months; "qualified staff… not solely on the basis of automated means") and 24(5) wording was checked against the Official Journal text (32022R2065). The two unofficial-mirror links and the Sources entry now point to the official ELI.
- The Transparency Database demotion value is now `DECISION_VISIBILITY_CONTENT_DEMOTED`, not `CONTENT_DEMOTED`. It was verified against the API docs and now matches ch. 27.
- Spot-checked: Transparency Database figures (4.42B statements, 375 platforms, 41% fully automated, 180 days), OLX Jan 2026 post.
- Open: the spec's open question about the unofficial DSA wording is now resolved and can be removed by the author. The Ofcom July 2026 report and the Clubic link were not re-fetched.

## 25-fraud-prevention
- Consistency issue 16: added that none of the 26 Barcelona accounts had proved more than an e-mail address, with a link to [[identity-and-verification]].
- Checked: the ring timeline and weekdays (Thu 1 Jul, Fri 9 Jul, Mon 12 Jul, Tue 13 Jul 2027), the €1,130 average, and the friction-threshold table arithmetic (all four rows reconcile).
- Spot-checked: UK Finance 2026 report (175,809 cases, £118.1m, 71%, £671, 78%, seller-verification ask), OLX (30%, 80% precision, published 28 Jan 2026), Mercari (13M passkeys, quote).
- Open (author): the Airbnb evidence still comes via InfoQ 2018 (see spec).

## 26-identity-and-verification
- Consistency issue 19: "a group operating in seven countries" changed to "eight countries".
- "Two months later, in June 2027" changed to "Three months later": the account review was in mid-March 2027.
- Checked: DSA Art. 30(1)(b) and 30(3) wording, and that implementing regulation 2025/848 applies from 24 Dec 2026 (Official Journal text). The ledger's identity baseline and Barcelona L4 rule numbers match.
- No [[part-6]] reference was found or needed here; the chapter correctly hands off to [[marketplace-regulation]].

## 27-marketplace-regulation
- Consistency issues 1 and 17: Safe Deal 2026 changed from 4.1M / €310M to 11.6M transactions / about €1.02B GMV. The DAC7 seller estimates (1.3M sellers, ~21,000 above the test) were left as they are in the ledger.
- Consistency issue 16 and hand-off rule: the closing paragraph now hands off to [[part-6]] (the next page in config order), still mentioning [[messaging-and-leads]].
- "Country Fork… cost seven times as much" changed to "eight times as much, once per country".
- Spot-checked: Transparency Database API vocabulary (`DECISION_VISIBILITY_CONTENT_DEMOTED`, `SOURCE_TYPE_OTHER_NOTIFICATION`, batches of 100); P2B repeal proposal (19 Nov 2025, page updated 2 Jul 2026); implementing regulation 2024/2835 (first full cycle 2026, two months, five years); EPBD Art. 20(4) "property search portal websites" (Official Journal text).

## Issues for other parts
- 01-marketplace-taxonomy (Sources) and 12-sellers-and-accounts (body and Sources) still cite DSA Art. 30 through the unofficial eu-digital-services-act.com mirror. The Art. 30 wording they quote matches the Official Journal, so the links can be switched to https://eur-lex.europa.eu/eli/reg/2022/2065/oj.
