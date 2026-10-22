# Review log — Part VI (MONEY)

Editorial pass, 21 Oct 2026. Scope: part-6-intro, 26–30. Word counts measured up to `## Sources and Evidence`.

| Page | Before | After |
| --- | --- | --- |
| part-6-intro | 1,062 (902 prose without front matter and mermaid; in line with other part intros) | unchanged |
| 26 merchant-and-agency-models | 8,796 | 8,805 |
| 27 stay-payments | 8,918 | 8,913 |
| 28 payouts-and-settlement | 8,649 | 8,649 |
| 29 taxes-on-stays | 8,437 | 8,475 |
| 30 refunds-and-reconciliation | 9,434 | **8,491** |

## Checks that passed on every page

- Front matter, callout order and labels, exactly three KEY POINTS, two or three failure patterns with exact names, `<br>`, Hotels and Homes section with table (26–30), Chief Architect's view, Questions to ask, Sources and Evidence.
- Hand-offs follow config order: part-6 → 26 → 27 → 28 → 29 → 30 → part-7 (30 hands off to `[[part-7]]` and `[[stays-trust-and-safety]]`).
- Nookaway fees (12% guest + 4% host) and payout 48 h after scheduled check-in are used consistently; no stale 3%/14%/15% or 24-hour figures. The 17% host-only fee is not used in Part VI (no conflict).
- Novak (€1,085 / €130.20 / €56 / €1,271.20; host payable €1,041.60; payout 4 Aug; fee VAT split), Carmen (€130 fee, €374.40, €244.40 on 15 Feb), Bauers (€1,360, €1,523.20 refund, €420 guarantee), Prinsenkade (€32,130 / €78,948 / €1,600 / €45,218), King's Day, €1.8M gap breakdown and outcome, DAC7, Levy, Payment Plans v1 and Semana Santa figures all agree with the ledger. Arithmetic re-checked.
- Plumbline = reconciliation service only (part-6, 30). Gauge does not appear in Part VI.
- Mermaid fences and figure numbering correct; render check OK for all six pages, no unresolved links, no XJ problems.

## Changes per page

**part-6-intro** — no changes needed.

**26 merchant-and-agency-models**
- Float table: the Nookaway row was labelled "about €3.0 billion including fees" but computed on GBV before guest fees (€2.98B × 60/365 = €490M); relabelled as stays value before guest fees.
- American spelling: licence → license (×27), programme → program, instalments → installments.

**27 stay-payments**
- Hotel Miradouro VCC example used a generic "82% of the price" (€369, €492). Chapter 26 and the ledger give Miradouro a 15% commission with VCCs loaded net of commission, so the example now loads €382.50 (and €510 after an added night). Recorded as an `[editor-review]` ledger line.
- American spelling (license).

**28 payouts-and-settlement**
- No factual changes; all figures match the ledger. American spelling: ageing → aging, licence → license, fulfil → fulfill, programme → program. Not trimmed (8,649, inside the light-trim band; no clear repetition worth cutting without touching the argument).

**29 taxes-on-stays**
- Lisbon tourist tax: official municipal pages (lisboa.pt, cm-lisboa / informacoeseservicos.lisboa.pt) returned HTTP 403; visitlisboa returned 404. Airbnb help article 2290 (fetched 21 Oct 2026) confirms "4.00 € per person per night, up to a maximum of 7 nights" but says nothing about a child exemption. The table row now says "as of October 2026" and notes the exemption age is not stated; the caveat paragraph now marks the under-13 exemption as an assumption of Corvane's illustrative rule. Scene sentence points to the caveat. `[editor-review]` ledger line added so other chapters (20 property-page, meet-corvane, any Novak mention) can align.
- American spelling (program).

**30 refunds-and-reconciliation**
- Trimmed 9,434 → 8,491: removed the "Refund funding" and "Unclaimed funds" definitions (both covered by their own sections), condensed the intro, the three Airbnb/PSP evidence paragraphs, the chargeback provisioning bullet, the currency lead-in, safeguarding, adjustment, unclaimed-funds and close prose, merged two overlapping failure modes ("totals" and "only against the bank"), shortened What to watch, dropped one question (refund vs dispute, already covered by rule 3 and a failure mode). Corvane worked example, evidence, tables and hotels-vs-homes comparison kept.
- Fixed: the €0.14M FX row was described as "four years" of un-revalued payables; cards date from the 2024 launch to Q1 2027, so "three years".
- Fixed a missing blank line that merged the concepts list with the following paragraph; replaced the "One clarification prevents most design arguments" opener, which chapter 28 also uses.
- Expanded ATC on first use. American spelling (aging ×6, program ×6, license). Timetoread 36 → 37.

## Spot-checked external claims

- Airbnb Reserve Now, Pay Later worldwide (newsroom, 17 Feb 2026): confirmed date, flexible/moderate eligibility, "over 70 percent adoption" in Q4 2025 (27).
- Airbnb help article 2290: Lisbon €4/person/night, max 7 nights; no child-exemption age (29).
- Booking Holdings FY2025 10-K: ViDA risk sentence confirmed (29). The fetched text shows a "$337 million accrual in 2024 related to the settlement of certain Italian indirect tax matters"; the **$332 million November 2024 settlement of a 21% short-term-rental withholding claim** cited in chapter 29 could not be located in the fetched portions of the filing. **Author to check** the figure and its description against Note 16 / the income-tax note before publication.

## Open issues for the author or other parts

1. **Lisbon tourist tax, official source.** Verify the child-exemption age (under 13?) and the €4 rate's effective date against the Lisbon municipal regulation (Regulamento Geral de Taxas / taxa municipal turística), which blocks automated access. Chapter 20 (`property-page-and-room-selection`, line ~48) and the ledger's worked example 10 state the under-13 exemption as fact; they should carry an "as of 2026" date and the same hedge (other reviewers' scope).
2. **Booking.com Italian settlement figure** in chapter 29 ($332M vs the $337M accrual seen in the 10-K): verify.
3. The ledger's generic "82% of the guest price" VCC net (stay-payments line) now applies only to properties without a stated commission; any other chapter that uses 82% for Miradouro should switch to 85%. A grep found no other use.
4. Chapter 26's ViDA wording ("from between July 2028 and January 2030") and chapter 29's (Art. 28a applies from 1 July 2028, member states may apply it at the latest from 1 January 2030) are consistent; neither was re-verified against EUR-Lex in this pass.
5. "cancelled" (British double-l) is used book-wide, including in the ledger; left as the book's convention.
