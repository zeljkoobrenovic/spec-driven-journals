# Review log — Part II (part-2-intro, ch. 13–23)

Editorial pass 2026-10-18. Ledger: appended two [editor] lines (item 24 SFP cut-over 2 Aug 2027; item 14 canonical €1.74 split).

## part-2-intro (permalink `part-2`)

- No changes. Format (IN THIS PART, failure patterns with exact names, `<br>`), ~750 words of prose, Figure 1 caption, all links valid, hand-off to [[custom-finance-platforms]] and [[part-3]] checked.
- Note: the intro frames the Q4 2027 decision as open ("must recommend whether Central Finance or an accounting-hub pattern"), which is fine because Part II is set before the decision.

## 13 custom-finance-platforms

- Item 20: added an italic forward note after the merchant-subledger recommendation. It says the FI-CA recommendation was superseded on 8 Dec 2027 by the accounting-hub decision (group engine generalized from SFP's subledger engine; FI-CA keeps merchant invoicing). It links [[multiple-erps]] and [[incremental-modernization]].
- Item 8: the boundary table now words Northmere Pay's sole authority over bank/KYC attributes as the target state (SFP authors until mid-2028). In the classification table, bank-detail authority now moves from SFP to Northmere Pay by 30 June 2028.
- Traveler-funds row: "reconciles to FI-CA open items after 2029" became "the group core's merchant open items" so it stays true under the hub decision.
- Partner-app example: "paid €510 on 22 April" became 26 April (the canonical settlement date).
- Defined KYC on first use.
- Item 4: FI-CA statements (learning.sap.com quote, batch-oriented summarizing subledger) agree with brief-sap.md and ch. 15. No Central Finance mechanics are claimed.
- Lisbon dates (batch 1047, 14/16 Mar, 22/26 Apr) were already correct.
- Spec: resolved the open question and added a Changelog entry.

## 14 designing-financial-ledgers

- Item 24: the migration now has shadow posting through the June and July 2027 closes and cut-over on Monday 2 August 2027. The rationale is the second-month-of-quarter rule, with a link to [[modernization-patterns]]. The legacy summarizer stops after Sunday 1 August. The example rule's `effective_from` is now 2027-08-02.
- Lisbon rule table: `PaymentSettled` (14 Mar) now debits "Cash in transit – Adyen" and no longer debits Bank – safeguarding, because the bank credit lands on 16 Mar. The bank-to-ledger match moves it. The "cash is €88.26" check still holds.
- Added a parenthetical forward note to "The 2029 question": the Dec 2027 decision chose the hub and generalized this engine into the group accounting engine ([[multiple-erps]]).
- [[case-uber-payments]] sentence: reworded to match ch. 44 (deterministic identifiers give exactly-once order processing; every order's entries sum to zero). The earlier wording "zero-sum check run before every money order is written" was not supported by ch. 44. It now reads naturally.
- Defined OLTP on first use.
- Item 4: the FI-CA and Central Finance statements are hedged and consistent with brief-sap.md and ch. 15.
- Spec: added a Changelog entry.

## Remaining issues for the author / other parts

- **Toolkit (`posts/toolkit/index.md:464`)** still says "eleven merchant rule families at the 1 September 2027 cut-over". It should say 2 August 2027.
- **Calendar tension with item 24.** The ledger [modernization-patterns] blackout includes "July–August peak", and [finance-transformation] excludes "Stayloft's July–August peak". Both conflict with an August cut-over. The ledger blackout WD−2 to WD9 also covers 2 Aug, which is WD1 of the July close. The canonical decision (2 Aug) was applied as instructed, but the author should either:
  - narrow the peak exclusion so it does not cover ledger-internal subledger cut-overs, or
  - pick another second-month date.
- Ch. 14 is about 11,000 words, above the 8,500 platform-chapter ceiling. It was not trimmed (out of scope for surgical edits).

## 15 — sap-s4hana

- Added a forward note to the FI-CA section: the May 2027 recommendation to move the merchant subledger into FI-CA was superseded by the December 2027 decision (links to [[multiple-erps]] and [[incremental-modernization]]).
- Added a parenthetical to the Chief Architect's view recording the 8 December 2027 accounting-hub decision and the rejection of Central Finance. The June 2027 narrative is unchanged.
- Item 18: replaced three SAP News short links (`news.sap.com/?p=231556`, `?p=233946`, `/africa/?p=140253`) with the canonical article URLs found with WebFetch, and corrected the titles in Sources.
- Removed the meta phrase "(a figure for this chapter)" after Sven's team of 26, which matches the ledger.
- Changed to American spelling: programme→program (but kept "Program Keystone"), catalogue→catalog.
- Changed timetoread from 38 to 40 min.
- Remaining: none.

## 16 — workday

- Item 18: the q4cdn PDF did not render as text. Replaced it with the Workday newsroom release of 11 Feb 2025, in both the body and Sources. Corrected the quote to Workday's verbatim wording ("manage their entire fleet of AI agents – from Workday and third-parties alike – in one place").
- Item 7: Data Cloud for finance data is already hedged ("targeted for 2027R1", recheck). Item 2: the Adaptive Planning renewal is already Q2 2028. No change needed for either.
- Changed to American spelling: licence→license, programme(s)→program(s).
- Changed timetoread from 38 to 41 min.
- Remaining: none in this chapter.

## 17 — oracle-fusion

- Added a parenthetical after Dana's "leaning" recording the 8 December 2027 decision: Wayfare goes to S/4HANA from FY2029 through the group hub, and Oracle Accounting Hub is not adopted.
- Checked the Wayfare rail ticket: merchant of record but agent, net €6.72 recognized at ticket issue. The dates (3 Mar issue, 5 Mar payout of €82.49, 12 Apr supplier run) match the ledger. No change.
- Item 12: Birmingham £20M against £144.4M checked with WebFetch against The Register (24 Sept 2026). Kept as written.
- Checked the cohort B update dates (5/19 Mar, 4/18 Jun, 3/17 Sep, 3/17 Dec 2027). All are Fridays.
- Changed to American spelling: centred, analysed, analysable, favour, towards, catalogue.
- Changed timetoread from 40 to 37 min.
- Remaining: none.

## Checks

- No SFP cut-over date, Lisbon date or €1.74 split appears in these three chapters.
- Item 6: no vendor corporate-status statements in these chapters.
- Hand-offs are correct: workday, oracle-fusion, blackline.
- Build is clean. Render check: OK for sap-s4hana, workday and oracle-fusion (3 mermaid diagrams each, 0 failed, 0 unresolved).

## Ledger-internal conflicts for the author (not edited)

- Company and ledger counts: the [global-scale] line says 52 SAP company codes, 5 Fusion primary ledgers and 7 Workday companies. The [sap-s4hana], [oracle-fusion] and [workday] lines, and chapters 15–17, say 55 company codes, 3 primary ledgers and 4 Tablekin entities. Chapter 10 (global-scale) should be checked against them.
- Workday ADR date: [architecture-governance] lists ADR-0006 "Workday Financials as governed second-tier ERP (Feb 2027)". [workday] and chapter 16 place that recommendation in June 2027, with a conditional decision and a Q1 2028 review.

## 18 — BlackLine (`blackline`)

- Batch 1047 / dates / €1,380.52 already correct (item 1 previously fixed); batch arithmetic verified (1,997.30 − 180 − 420 − 16.78 = 1,380.52).
- Leg 1 now states the canonical €1.74 split: €1.64 on the line = interchange €1.20 + scheme €0.21 + €0.23 of markup; €0.10 = rest of the €0.33 markup, batch-level processing fee (item 14).
- Named the merchant account `NMPay_Stayloft_EEA` for batch 1047.
- Added one sentence saying the −€420 chargeback in batch 1047 is the earlier January-stay dispute, not the June 2027 chargeback in payments-fundamentals.
- SOC 1: added hedge that the modules, data centers and AI features in scope are not public and are to be confirmed against the report (item 7).
- American spelling: program (×4), analyzed, defense, license, Center.
- Corporate status wording (listed; SAP bid rejected; Strategic Committee, March 2026) checked, consistent with item 6. Hand-off → onestream correct.
- Remaining for author: "Journals Risk Analyser" kept as the product name (not verified).

## 19 — OneStream (`onestream`)

- "dozens of functional currencies" → "nineteen" (ledger: 19 functional currencies).
- Item 18: the `/1384528/Content/.../Dimensions.html` URL was checked with WebFetch. It resolves and lists the dimensions, while the `/docs/...` variant of that page needs a login, so the link stays as it is. The Consolidation Dimension `/docs/` URL also resolves.
- Checked with no change needed: renewal 31 Dec 2027 with notice by 30 Sep, reconciliation module dropped at renewal (item 2); Hg take-private completed 1 Apr 2026 (item 6); SOC 1 scope hedged (item 7); worked-example arithmetic (CTA 270, group 16,200 / 5,300 / 10,900, NCI 216); flash WD3 / final WD7 / lock WD9; hand-off → payments-fundamentals.

## 23 — Satellite platforms (`satellite-platforms`)

- FIS URL: dropped `:443`. The canonical URL was checked with WebFetch and the product name matches.
- SAP Help Ariba link: the 2016 S/4HANA 1610 page still resolves and supports the cXML claim. Current help.sap.com pages render with JavaScript and could not be checked, so the link stays, now dated in the text and in Sources, with a note that Ariba Network is now part of SAP Business Network.
- Hand-off now names [[part-3]] (the next item in config order) before [[transaction-to-report]].
- First-use expansions: EBICS spelled out; "B2B" → "business-to-business".
- Checked with no change needed: vendor status (Coupa, Thoma Bravo 2023; Zuora source present); Vertex standard and the 9 + 4 + 5 Wayfare markets; e-invoicing dates hedged "as of October 2026".
- Remaining for author: "catalogue" (the reconciliation catalogue) kept to match the rest of the book; switch to American "catalog" book-wide if wanted.

## Build and render check

Build has no errors. Render check: blackline OK (mermaid 4), onestream OK (4), satellite-platforms OK (4); 0 pages with problems.

## Issues outside these chapters

- The scenario-ledger line [modernization-patterns] and the [finance-transformation] cut-over windows rule out July–August (the Stayloft peak). That conflicts with the canonical 2 Aug 2027 SFP cut-over (item 24). Raise this with the author.
- The book mixes "programme" and "program": 53 vs 122 occurrences outside the proper name "Program Keystone". Other parts may need the same American-spelling sweep.

## Ch. 20 — payments-fundamentals

- Fee table: PSP markup €0.33 now stated as €0.23 line-level + €0.10 processing fee charged at batch level (item 14).
- Added one paragraph after the fee table: €1.64 on the settlement line (net €598.36) + €0.10 batch fee; canonical net €598.26; link to [[adyen]].
- Figure 3 sequence label corrected (was "598.26 net and 1.74 fee for this line"; now line net 598.36 after 1.64 commission plus 0.10 batch fee).
- Hand-off sentence now refers to the €598.36 line and the batch fee behind the €598.26 net.
- Expanded NPCI on first use; American spelling "license" (3 places).
- Verified: Lisbon dates (14/16 Mar, 22/26 Apr), €420 June chargeback dates/amounts, PSD3/PSR "not in force" hedged as of October 2026, [[case-uber-payments]] sentence reads naturally, hand-off to adyen/stripe, Figures 1–5, timetoread 30 (prose ≈ 30 min).

## Ch. 21 — adyen

- €1.74 table: scheme fees 0.30 → 0.21, markup 0.14 → 0.23; processing fee row labelled as the rest of the €0.33 markup (item 14).
- Added sentence: Adyen margin €0.33 = €0.23 line + €0.10 batch; adapter attributes the €0.10, so canonical PSPFeeCharged €1.74 and PaymentSettled €598.26.
- Batch 1047 ledger table: scheme fees expense 1.20 → 1.11, markup 0.72 → 0.81 (total still 16.28).
- Hedged the 2017 European banking license date ("which Adyen reports"); Euronext listing already hedged as secondary-source.
- Exit test bullet dated to the ledger (first test November 2027, new-card traffic) instead of implying an existing yearly practice in March 2027.
- Verified: the earlier €420 chargeback (stay 30 Jan–2 Feb, debited 14 Mar in batch 1047) is kept distinct from the June 2027 dispute; dates 14/15/16 Mar; €1,380.52 arithmetic; hand-off to stripe; Figures 1–3.

## Ch. 22 — stripe

- Hedged the current API version (`2026-09-30.endive`, "as of October 2026; confirm before pinning") in text and in Sources (item 7).
- Expanded ASC 606 / IFRS 15 on first use.
- Verified item 15: Wayfare rail ticket is agent, €6.72 margin recognized at ticket issue, €77.28 owed to operator. Tablekin dates (Thu 1 Apr, available Mon 5 Apr, payout 6 Apr) and amounts match the ledger; hand-off to satellite-platforms.

## Remaining issues for the author

- Ch. 22 says Stripe Tax keeps a dated exception "until 2029" (shared tax service); ch. 34's waiver W-2027-011 expires 31 Mar 2028. Consistent only if the waiver is renewed — consider saying "a waiver renewed until the shared tax service is live".
- Ch. 06 (line ~421) says "€598.26 credited to the bank 16 Mar"; the bank credit is the €1,380.52 batch. A simplification, outside this scope.
- Scenario ledger's [adyen] line still shows the old €0.30/€0.14 split; the parent's [editor] line supersedes it.

## Open issues for the author / other parts

- **SFP cut-over date:** per the coordinator's later editor correction, ch. 14 now says cut-over Mon 1 Nov 2027 with shadow posting through the Aug, Sep and Oct 2027 closes (rule `effective_from` 2027-11-01; results table relabelled Nov–Dec 2027). This supersedes the 2 Aug date in the ch. 14 entries above. Note: 1 Nov is WD1 of the October close, inside the WD−2..WD9 close blackout in the ledger [modernization-patterns] line — the author may want to note the start-of-month exception.
- **toolkit/index.md ~line 464** still says "the 1 September 2027 cut-over" — should be 1 November 2027.
- **ch. 06 ~line 421** says "€598.26 credited to the bank 16 Mar"; the bank credit was the €1,380.52 batch.
- **Stripe Tax exception:** ch. 22 keeps it to 2029; ch. 34 waiver W-2027-011 expires 31 Mar 2028.
- **Entity counts:** ledger [global-scale] (52 SAP company codes, 5 Fusion primary ledgers, 7 Workday companies) vs ch. 15–17 and their ledger lines (55, 3, 4) — check ch. 10.
- **Workday ADR date:** ledger [architecture-governance] ADR-0006 Feb 2027 vs ch. 16 / [workday] June 2027 conditional decision.
- **Spelling:** ~53 "programme" remain book-wide (outside "Program Keystone"); "catalogue" vs "catalog" inconsistent.
- **Length:** ch. 14 ~11,000 words, above the 8,500-word platform-chapter ceiling; not trimmed.
