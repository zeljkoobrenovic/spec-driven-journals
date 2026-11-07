# Review log — Part VIII (TRUST)

Editorial pass, 2026-11-07. Fresh start (the previous reviewer made no edits).

## part-8-intro (1,694 → 1,739 words)
- WHY IT MATTERS rewritten to two sentences; corrected "fees for payments that were all declined" (about 260 cards were live) to "fees for declined authorizations".
- Eva's price corrected: she paid full price, so the prior-price rule did not apply; now "had to include VAT and sit in a price history that any later reduction is measured against" (same fix in chapter 36).
- Defined the button wording, the two 14-day clocks, ERP, hosted fields and MFA; "nine of the thirteen systems".
- Ownership map attributed to Part I's system-of-record map and Part VI's integration inventory (was "Parts V and VI").
- timetoread 5 → 8 min.
- Note for the author: every part intro is 1,300–1,950 words against INTRO-BRIEF's 500–900; not trimmed, for consistency with the other parts.

## commerce-security (6,494 → 6,529 words)
- WHY IT MATTERS shortened and corrected (declined authorizations, two weeks of raised declines).
- Expanded OWASP, acquirer, 3-D Secure, dunning, CDN, ERP, WMS, iPaaS.
- Failure pattern "thirty-four hand-built connectors" → iPaaS flows, agency scripts and vendor connectors (ledger: 14/9/11).
- Spot-checked: PCI SSC 26 March 2025 post (6.4.3 and 11.6.1 removed from SAQ A, eligibility criterion added, quote verified).
- timetoread 24 → 28 min.

## privacy-and-customer-data (6,499 → 6,553 words)
- Expanded PSP, WMS, ERP, POS, iPaaS, OMS, CDP, ePrivacy, EDPB, IAPP.
- "all 41 apps" in May 2027 → "every installed app" (6 apps were removed in April 2027; 34 by July).
- "five days to spare" → six (deadline 10 June, reply 4 June).
- PIM removed from the processor row (it holds no customer data).
- Sephora 2022 flagged as more than three years old.
- Hand-off sentence reworded ("discovered only months before it applies").
- Spot-checked: Shopify compliance webhooks (10 days, 48 hours, 30 days; verified).
- timetoread 26 → 28 min.

## commerce-regulation (6,514 → 6,673 words)
- **ESPR newsletter month settled as June 2026** (ledger line by this chapter wins; consistent with "weeks before" the 19 July 2026 date). Heading "The end-of-season decision (July 2026)" → "The newsletter (June 2026)"; scale-stage cell "(July 2026)" → "(June 2026)"; `[editor-review]` line appended to the ledger.
- Consistency item 5: Belgian e-invoicing hedged in the scene, the calendar row (fines apply to Belgian businesses) and the take-aways (German mandate does not bind a Dutch issuer; Belgian one unsettled).
- Item 11: WHY IT MATTERS rewritten to two sentences; the Black Friday "was €199" case is now explicitly hypothetical (the 2026 Price Drift ended 14 October, more than 30 days before Black Friday).
- Expanded SKU, EDI, Peppol, ERP, OMS, PIM, WMS, ViDA, PPWR, WCAG, PSD2, XRechnung, FTC, GTIN.
- Spot-checked: Rijksoverheid 11 September 2026 (Dutch e-invoicing 1 July 2030, reporting 1 July 2031) and Regulation (EU) 2026/1744 (8 July 2026; Annex III 2 December 2027, Annex I 2 August 2028); both verified.
- timetoread 25 → 29 min.

## Open issues for other parts or the author
- **Ownerless integrations: 13 vs 5.** The integration-styles ledger line says 13 of 34 had no named owner; the organizing-commerce-engineering line says 5. Chapters 34 and 35 (and where-commerce-platforms-go-wrong) use 13. The Part VI/X reviewers should rule and record it in consistency-issues.md.
- The ledger's commerce-regulation line says a Dutch issuer "is not bound by the Belgian … mandates", which goes further than item 5; the chapter now hedges, and the line should be read with the editor-review line.
- Chapter 36's Sources lists the Sephora settlement, which the chapter body no longer cites (harmless; consider removing).
- Build clean; render check OK for all four pages.
