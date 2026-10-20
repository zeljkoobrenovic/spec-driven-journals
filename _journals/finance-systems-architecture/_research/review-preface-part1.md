# Review log: preface and Part I (2026-10-18)

Scope: where-finance-architecture-goes-wrong, meet-northmere, part-1-intro, ch. 01–12. Each edited chapter's spec.md carries a Changelog line. Build clean; render check OK on all 15 pages (0 failed mermaid, 0 unresolved links).

## Changes by chapter

- **where-finance-architecture-goes-wrong**:
  - Added the canonical figures: Wayfare payout engine about €1.3M out from Fusion; Tablekin mapping error about $41M, caught on WD7.
  - The One-ERP Dream and Vendor Gravity now state the 8 Dec 2027 outcome (accounting hub; Central Finance rejected).
  - Added `[[case-uber-payments]]` to The Shadow Ledger, Point-to-Point Spaghetti and The Brand Exception, and `[[sap-s4hana]]` to The One-ERP Dream.
  - Replaced "leverage".
- **meet-northmere**:
  - The Wayfare rail ticket is now merchant of record but agent (€6.72 at ticket issue).
  - The €420 chargeback now has its ledger dates and split, with a note that ch. 21 follows an earlier, separate chargeback.
  - The Keystone summary stays at the 2027 baseline and points to `[[multiple-erps]]` for the December decision.
  - Lisbon dates were already correct.
- **part-1-intro**: The CFO's "one question" became "three questions", to match ch. 01.
- **01 chief-architect-role**:
  - Added a forward note on the five proposed standards: they became STD-FIN-01..05, mandatory from 1 Apr 2027; STD-FIN-01 and -02 are enforced from 1 Jul 2027 and STD-FIN-06 followed in Q3 2027.
  - Spelled out GL on first use.
- **02 capability-mapping**:
  - "About a dozen" workbooks became 14.
  - Spelling fixes.
- **03 application-portfolio**:
  - The canonical-events link now credits loosely-coupled-domains as owner.
  - Added a forward note on the wave 3 hub decision.
- **04 finance-landscape**:
  - Added the Adaptive Planning overlap to layer 5.
  - Fixed caption spacing.
- **05 accounting-for-architects**:
  - The Lisbon settlement and top-up entries are now dated 16 Mar (bank credit), with batch 1047 booked 14 Mar.
  - The €420 outcome is now the lost case: €357 recovered, €63 contra.
  - Wayfare rail is now agent, with €6.72 recognized at ticket issue.
  - Corrected the event count.
- **06 finance-processes**:
  - The Wayfare rail trace is now agent/net: €6.72 at issue, €77.28 operator payable.
  - Expanded ICFR at first use.
  - Spelling fixes.
- **07 finance-data-architecture**:
  - Partner bank details authored in Northmere Pay are now the target state. In 2027 SFP authors them, and authority moves by 30 Jun 2028.
  - Noted that Northmere runs no MDG in 2027.
  - Spelling fixes.
- **08 controls-and-auditability**:
  - The five control requirements are now the clauses of STD-FIN-05.
  - Added the STD-FIN-01..06 dates and STD-FIN-06 references.
  - Expanded acronyms on first use.
- **09 integration-architecture**:
  - Added the event v1 approval and registry dates.
  - Named the idempotent-posting standard STD-FIN-02, enforced from 1 Jul 2027.
  - Corrected the MuleSoft retirement wording.
  - Expanded acronyms on first use.
  - Hedged an unsourced claim about a 2026 SAP product rename.
- **10 global-scale**:
  - The entity split is now 55 SAP company codes, 12 Fusion entities in 3 primary ledgers and 4 Workday companies.
  - Recomputed the royalty FX example on the canonical March rates.
  - The multi-GAAP wording now follows ch. 15 and ch. 17.
  - The Pillar Two remark now reflects the Dutch ultimate parent.
- **11 build-versus-buy**:
  - SFP cost of owning is now $18.5M ($4.1M finance operations).
  - Corrected the cost-gap sentence to $3.2M.
  - Expanded CUEC.
- **12 modernization-patterns**:
  - Replaced the SAP News `?p=` links with canonical URLs (item 18).
  - The custom-code triage now starts from ch. 15's baseline of 1,240 objects not executed.

## Open issues for other parts or the author

1. **Ch. 28 company-code count.** Ch. 28 (lines ~37, ~290) says "52 SAP company codes"; the canonical figure is 55 (55 + 12 + 4 = 71). The ledger's [global-scale] line (52 / 5 Fusion ledgers / 7 Workday companies / Wayfare "local GAAP primary") is the outlier and needs an [editor] correction.
2. **Ch. 34 standard IDs.** Ch. 34 still uses STD-01..06; it should use STD-FIN (item 13).
3. **Tablekin ERP decision date.** ADR-0006 (ch. 34) dates "Workday Financials as governed second tier" to Feb 2027, while ch. 16 records the conditional decision in June 2027.
4. **Spelling convention.** The book mixes British and American spelling ("programme" ~134 times, "licence", "judgement", "cancelled"), including in the ledger name "Program Keystone". This needs one book-wide decision.
5. **Missing files.** config.yaml lists `introduction/index.md` and `part-5-intro/index.md`, but neither file exists.
6. **Ch. 01 length.** Ch. 01 is about 8,500 words, above the 7,500 limit; it was not trimmed.
