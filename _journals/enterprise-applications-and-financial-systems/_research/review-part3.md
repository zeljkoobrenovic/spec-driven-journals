# Review log — Part III (part-3-intro, ch. 24–33)

Editorial review pass, 2026-10-18. Every chapter: American spelling normalized (catalogue→catalog, licence→license, programme→program except the proper name "Program Keystone", labelled→labeled, analysed→analyzed). Structural check: callout labels and order, exactly 3 KEY POINTS, 2–3 failure patterns with exact names, mermaid captions numbered consecutively, all `[[…]]` permalinks valid. Build clean; render check OK for all 11 pages.

## part-3-intro
- Verified claims against ch. 24, 31 and the ledger: "three engineers, nine working days" for the September 2027 top-down dry run (ch. 31, ledger [traceability-and-reconciliation]); €14m 2026 average suspense; eleven hops (ch. 24). No content change needed.

## 24 transaction-to-report
- Joined a stray paragraph break in hop 5; "Authorise" → "Authorize" in Figure 1.
- Verified: Lisbon dates (batch 1047 booked 14 Mar, credit 16 Mar, payout 22/26 Apr), €1.74 = €1.64 settled-line commission + €0.10 batch Fee line, the earlier separate €420 chargeback in batch 1047 (stay 30 Jan–2 Feb), Wayfare agent at €6.72 recognized at ticket issue.
- Note: the OneStream `documentation.onestream.com/1384528/...Dimensions.html` link (flagged in item 18 for ch. 19) resolves with title "Dimensions"; the `/docs/` variant of that page returns a login page. Kept.

## 25 payments-to-ledger
- Reworded the [[case-uber-payments]] sentence to read naturally; added the Uber Finance Computation Platform blog post (2021) to Sources (the quote is from it, per ch. 44).
- Fixed "ageing,," double comma.
- Verified the June 2027 €420 chargeback (booked 2 Apr, stay 1–4 May, payout €357 on 7 May, received 13 Jun, lost 26 Jul, €357 recovered, €63 contra-revenue).

## 26 finance-data-flows
- Item 8: "partner bank details are authored only in Northmere Pay" reworded to SFP-authored in 2027, Northmere Pay sole author from mid-2028 (target), linking [[systems-of-record]].

## 27 systems-of-record
- Item 23: Figure 3 and text now say parallel run April 2028, first cohort with the May 2028 invoicing cycle, remaining cohorts through 2028 (end date 31 Dec 2028 unchanged).
- Item 8: wording already canonical (SFP 2027, transitional to Northmere Pay, end date 30 Jun 2028).
- Added heading "From Authority to the Number of Ledgers" for the closing hand-off.

## 28 multiple-erps
- Editor note: 52 → 55 SAP company codes (also in Figure 3 caption); 64 → 67 company codes after convergence in Figure 3; Wayfare "five primary ledgers" → three (ch. 17, ch. 10); Tablekin "seven companies" → four.
- Editor correction (supersedes item 24): SFP merchant subledger "went live on 1 November 2027".
- Tablekin recommendation cited as June 2027 (ch. 16).
- Item 17/22: decision text (route B, Wayfare on S/4HANA from FY2029, Fusion retired wave 3 2030) agrees with ch. 29 and ch. 33.

## 29 redundancy-and-coupling
- Overlap register row 10.1 said integration technologies "decision due Q4 2027", contradicting ch. 30's June 2027 design-authority decision. Row now records that decision (Contain MuleSoft; Kafka sole canonical-event backbone; Integration Suite the SAP boundary); the paragraph after the table was rewritten to match. Appended a line to the ledger noting this supersedes the earlier [redundancy-and-coupling] wording.
- Added heading "From Design Rules to Contracts" for the closing hand-off.
- Item 22: payout-engine collapse dates (parallel runs Feb–Mar 2029, cohorts Apr–Jul 2029) left as canonical.

## 30 loosely-coupled-domains
- Item 13: Chief Architect's view now names STD-FIN-01 (mandatory 1 Apr 2027, enforced with STD-FIN-02 from 1 Jul 2027 when the registry went live), linking [[principles-standards-reference]].

## 31 traceability-and-reconciliation
- "Closed means reconciled … extending the subledger-to-GL standard of 2026" → extends STD-FIN-03 (standards came into force in 2027).
- Verified the walkthrough figures (9 days/3 engineers top-down, 4 days bottom-up, 38/22 minutes in November) against the ledger and the part intro.

## 32 brands-entities-markets
- Closing hand-off said "Stayloft's legacy ledger moving to S/4HANA". It now says the merchant subledger moves from SFP to the group accounting engine that posts into S/4HANA, per the Dec 2027 decision. Added heading "From Onboarding to Migration".

## 33 incremental-modernization
- Items 17/22: the migration already follows the accounting-hub decision. The 2029 concurrency (CoA v2 and Wayfare from 1 Jan 2029; payout service absorbing Wayfare suppliers Apr–Jul 2029; UK+INTL cut-over 1 May 2029) is stated and handled (the payout service changes only one interface).
- Item 23: FI-CA merchant-invoicing timing aligned in three places plus the Gantt label.
- STD-05 → STD-FIN-05, linked to [[principles-standards-reference]].

## Remaining issues for the author or other parts
- Ledger [global-scale] still says 52/12/7 entities and five Fusion primary ledgers. Canonical (editor) is 55/12/4 with three primary ledgers; the line needs an [editor] annotation.
- Ledger [designing-financial-ledgers] still says cut-over 1 Sep 2027. Canonical is now 1 Nov 2027; ch. 14 must change to match.
- Ledger [architecture-governance] and ch. 34 still use STD-01..06 and ADR-0006 (Workday second tier, Feb 2027). That conflicts with STD-FIN IDs and with the June 2027 Tablekin recommendation (ch. 16/28).
- 1 Jan 2029 go-lives (CoA v2, Wayfare on S/4HANA) sit inside the ch. 12 January–February blackout. The book treats a fiscal-year-start chart switch as an exception, but never says so explicitly. Consider one sentence in ch. 12 or ch. 36.
- The ch. 29 payout cohorts (Apr–Jul 2029) include a quarter-end month (June) and the peak month (July). They are payout-run migrations, not ledger cut-overs, but a reader may see a clash with the ch. 12 rule.
- Spelling of "catalog/catalogue" and "license/licence" is still mixed in other parts. The ledger itself uses "catalogue".
