# Editorial Review — Part IV (B): chapters 21–25

Reviewer pass, 2026-10-22. Length is prose words before Sources (`awk … | sed 's/|/ /g' | wc -w`). No page was over 8,500 words, so nothing was trimmed. All five pages already had the full callout set (exactly 3 KEY POINTS, 3 failure patterns with exact names), Across Markets, failure handling, Chief Architect's view, Questions, Sources and the correct hand-off (21→22→23→24→25→`part-5`/`tenancy-and-dealer-groups`). Every cross-link resolves to a valid permalink. Mermaid fences and captions were correct.

## Web spot checks (October 2026)

- Slaughter and May on FCA PS26/3 (30 Mar 2026; 6 Apr 2007–1 Nov 2024; £9.1bn; 12.1M agreements): verified (ch. 22).
- Belastingdienst 2026 BPM table (€2,727 + €181/g for 100–139; €14,538 + €594/g above 155; diesel €114.83/g above 69 g/km for cars over 70 g/km): verified (ch. 23).
- VNA: 1,371,900 lease vehicles at end of 2025, including 256,600 vans: verified (ch. 25).
- AutoNation 10-Q Q2 2024: DMS restored 29 June, ancillary systems and integrations by end of July, estimated 5% gross-profit decline: verified (ch. 24).
- Sonic 8-K July 2024 names its CRM among affected systems: verified (ch. 21). "Workaround solutions" is not in the 8-K. Chapter 24 cites the 8-K and the 10-Q together, so the quote is attributed to the pair.
- NADA Data 2025: the PDF text contains 21.9% in the used-vehicle sources section: plausibly verified (ch. 25).
- mobile.de summer 2026 newsroom page: HTTP 403. The call-assistant pilot figures are now hedged as not re-checked (ch. 21).

## 21 leads-and-crm — 7,605 → 7,712 words

- Lost Leads of Velto aligned to item 27 and the `[editor]` ledger line. The three closed rooftop codes carried a hub-sized stock (about 1,100 cars plus central stock), and their cars stayed advertised under the old codes. Their leads fell through to older rooftop rules pointing at a deactivated brand-cluster queue, at about 160 leads a day.
- The simulation sentence now matches this mechanism.
- Acronyms expanded: GDPR, FCC, PECR.
- The mobile.de pilot claim is hedged. "Dutch" was dropped from the pilot because it cannot be verified.

## 22 deals-and-sales-documents — 7,675 → 7,765 words

- Items 24 and 31(f) applied:
  - Sold now requires the deal's conditions (payment or financing) to be met, and then the invoice or delivery.
  - "Advertised" is treated as a track, not a stock state. Reserve sets the advertising track to withdrawn in the same transaction (dossier ledger).
- Item 25: in the worked example, the sold event starts *tenaamstellen* automatically for Sales Admin rooftops from June 2027. The Polo's *vrijwaren* is submitted at hand-over, which is consistent with ch. 23.
- Fixed a missing period in the CarMax sentence.
- Acronyms expanded: ERP, SEC, FTC, AO, eIDAS.
- American spelling: "canceled".

## 23 registration-and-trade-services — 7,420 → 7,525 words

- Item 25: the opening now says the sold event starts registration automatically for Sales Admin rooftops from June 2027, held as a draft until the balance is covered. DMS-originated sales still start with a dealer click. Worked example step 3 says the same.
- Items 13/23: "authorized information provider" is used as a book term, linked to `registers-and-official-data`, and not presented as an RDW title.
- Item 19: already correct (live register query for *wachten op keuren*).
- "400-car batch" changed to Velto's ~380 quarter-end registrations (journey ledger).
- VED rates marked "as of 2026".

## 24 dms-integration — 7,666 → 7,768 words

- Item 31(a): added a paragraph that separates the DMS's accounting stock unit from the dossier's stock item, linked by Hitch's xref, with a link to `vehicle-bounded-contexts`.
- Item 27: Lost Leads wording aligned.
- "Five different match keys" changed to "A different match key per DMS family".
- Acronyms expanded: GDPR, SRE.

## 25 b2b-trade-and-remarketing — 7,441 → 7,468 words

- Dated inline links added for the NADA, CarMax, VNA, OPENLANE, Hertz and Ayvens figures. These were previously cited only in Sources.
- Acronyms expanded: NADA, VNA, NMVTIS, NAAA. "OEM" changed to "manufacturer".
- American spelling: neighbors, curbed, canceled.
- The Month-End outage link now points to its owner, `registration-and-trade-services`.

## Open issues for other reviewers or the author

- **`inventory-and-vehicle-dossier`:** its state table still needs the item 24/31(f) alignment (Reserved → Sold on conditions met plus invoice or delivery, not on "contract signed"). This belongs to the Part IV-A reviewer.
- **`events-webhooks-and-sync`:** must also state the item 25 rule (automatic registration start for Sales Admin rooftops from June 2027, dealer click for DMS sales). This belongs to the Part VI reviewer.
- **Ch. 21:** the mobile.de summer 2026 figures (19-dealer call-assistant pilot, 91% out of hours, "45 percent" AI-written replies) could not be re-fetched (403). The author should verify them in a browser.
- **Ch. 21:** the Lead Manager quotes in the Chief Architect's view rest on the same unreachable page.
- **Ch. 22:** the Belgian equivalent of *suppletie* is left unnamed. NL B2B e-invoicing is still marked *(re-verify)*.
