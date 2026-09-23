# Editorial review: Visma: Continuity of Manager Is Not Continuity of Money

Reassessed 15 September 2026 (dispositions for the 23 September in-depth review rounds appended below) from the complete current article, summary and comic text where present, the previous review where present, revision log and Git changes. See the [collection review](../REVIEW.md).

## Current assessment

The transaction map now supports the title, and the transition from repeated acquisitions to changing earnings definitions is much stronger. Narrowing shared services to a question raised by the case is an effective alternative to inventing an intervention story. The ESMA annotation also corrects a material earlier error. Preserve the distinction between a manager, its funds and the operating company, and the point that an earnings adjustment does not create cash.

Remaining recommendations concern two ownership shortcuts and a prescriptive statement about the “right” earnings measure. The exact reconciliation has now been independently checked against primary report copies. The current structure is coherent and does not need another split or title change.

## Active recommendations

1. **Medium impact — replace “no exit” in the opening.** The map itself records KKR's announced complete exit in 2017. Continued involvement by Hg is not an absence of exits by other shareholders or funds. Suggested rewrite: “Visma shows a continuing company and manager relationship through repeated investor entries and exits.” This is the distinction the chapter otherwise explains well. Hg's 2017 announcement also makes completion subject to regulatory approval; keep announced terms distinct from verified closing events. [Hg's 2017 announcement](https://hgcapital.com/insights/hg-leads-usd5-3bn-buyout-of-visma)

2. **Medium impact — do not assume one fund holds the majority.** The final authority check, summary and comic panel 6 ask “which fund now holds the majority.” A manager's aggregate majority can be held through several vehicles. Ask instead: “Which vehicles hold the interests, how are their rights exercised, and which horizons affect the plan?” This preserves the title's central distinction without assuming an ownership structure the map marks unknown.

3. **Medium impact — qualify “the right basis for comparing product lines.”** The budget example calls earnings before deal costs the right basis, after correctly explaining that usefulness depends on the question. An acquisition-heavy product line can also need recurring integration resources. Use “one basis for comparing operating performance, alongside the full cost of the strategy.” The callout similarly need not demand that purchase valuation and management budgeting use the identical metric; the definitions and reconciliation must be explicit.

4. **Low impact — remove editorial navigation language from the argument.** “This chapter is the book's home for that lesson” can become a simple link explaining what TeamSystem adds. The compact authority-and-budget check is a useful conclusion; keep it, with plural vehicles and the unresolved facts stated precisely.

## Verification and limits

The [ESMA guidelines' scope paragraphs 1–5](https://www.esma.europa.eu/sites/default/files/library/2015/10/2015-esma-1415en.pdf) support the revised annotation: issuer, securities and disclosure matter; private share ownership alone is not an exemption. This is not a determination of Visma's legal obligations. Hg's primary announcement supports the named Hg5/Hg7 investments, announced 41% position and planned KKR exit. Complete fund-level cash flows, company funding receipts and a measured shared-service intervention remain unestablished.

Independent text extraction from cached primary PDFs verifies the bridge: [2024 report, pp. 50/52](https://cdn.prod.website-files.com/69787181d8720ea08c1f22fe/69787181d8720ea08c1f460b_Visma-Annual-Report-2024.pdf), €892.646m EBITDA; [2025 report, p. 96](https://cdn.prod.website-files.com/69787181d8720ea08c1f22fe/69bb9fc407e856cb8d6f7726_Visma%20Annual%20Report%202025.pdf), €11.665m M&A adjustment and €904.311m adjusted EBITDA for the 2024 comparative. The sum checks exactly. Current CDN retrieval failed, but cached original reports resolved the transcription question; the [live financials page](https://www.visma.com/investors/financials) also shows the rounded €904m. This is a selected-page check, not an audit of either full report.


Comic panel 6 has revised dialogue but an unchanged image and no regeneration flag. Its visible speech needs **verification** against the new text; the metadata alone cannot establish agreement.

## In-depth review round 2 (23 September 2026): dispositions

Implemented from the run `.in-depth-reviews/20260923-151518.4RqrNT` (round-01 review). Images were inspected and left unchanged: panel 4 carries only the REVENUE, CASH FLOW and DEFINITIONS headings and panel 5's ledger (892.6 + 11.7 = 904.3, € million, 2024) carries no payment wording, so both problems lived in the captions.

| Finding | Disposition |
| --- | --- |
| VISMA-009 (medium) “was spent during 2024” | **Fixed.** Article and panel 5 caption now say the €11.665 million was recorded as an expense of 2024 and deducted; the 2025 report lists it under other operating expenses and gives no separate figure for when the cash was paid, so payment timing is not asserted. Summary add-back sentence aligned. |
| VISMA-002 (medium) opening usable before definitions; M&A unexpanded | **Fixed.** Key point 2 explains two profit calculations and the excluded deal costs before naming EBITDA; “reconciliation” and “adds back” removed from the callouts. “M&A” expanded as mergers and acquisitions in the summary and in panel 5. |
| VISMA-010 (medium) panel 4 definitions incomplete | **Fixed.** Caption and metadata quote organic growth (same businesses in both periods, constant exchange rates) and free cash flow (operating cash before tax, after investment in own software and other long-lived assets), with the Q4 report citation beside the caption. Matches the report's definitions page. |
| VISMA-006 (medium) repeated promises; three dense paragraphs | **Fixed.** Callouts rewritten to do different jobs; the platform decision now precedes the definitions block; the definitions paragraph split into ownership (shares, funds, vehicles) and management (manager, Hg, private equity); the map paragraph split at “What the map cannot show”; the add-back paragraph split into calculation, boundaries and the remaining exclusions. Longest remaining paragraphs (2023 announcement, report definitions) were not flagged and each do one job. |
| VISMA-011 (low) residual jargon | **Fixed.** Platform program described as rebuilding systems several products share; share-based compensation and initial public offering (IPO) explained; closing example now names a concrete ratio (engineers per million euros of revenue); summary gives equivalents for shared infrastructure and integration capacity, and explains buyout. Also added descriptors for NPS, NYC Retirement System, ICG/TPG and GIC from the terminology audit. |
| VISMA-012 (medium) earnings-based pricing stated as a rule | **Fixed.** Investor callout is now conditional (“when investors use a company's earnings to judge what its shares are worth…”) and states that a measure informs a negotiated price without setting it. Spec criterion added. |

Checks run: `python3 _wiring/build.py` (private-techuity built; docs change-set identical to the run baseline after restoring one unrelated teamsystem asset the build had copied); no unresolved `[[…]]` and every relative link in the built page resolves; summary prose 499 words by the exclusion rule used in round 1; panel JSON parses; 892.646 + 11.665 = 904.311 unchanged; Playwright screenshots at 1280 px and 390 px of the article, add-back section, TL;DR and comic panels 4–5 read correctly. Manuscript: exported to a scratch directory and only `visma.md` installed (heading kept as “# 31.”), with its two manifest entries updated; the validator still reports 11 pre-existing errors for other chapters whose sources are mid-edit (toolkit, glossary, bibliography, …), none for Visma. Still unverified: the three original Visma PDFs (local text extractions only).

## Changes since the previous review

| Previous recommendation | Current disposition |
| --- | --- |
| Correct ESMA's scope | **Resolved.** |
| Give the title an explicit transaction map | **Partially resolved:** the map works; opening and conclusion still oversimplify exits and majority ownership. |
| Connect ownership continuity with measure continuity | **Resolved:** the transition and budget application are clear. |
| Narrow or substantiate the operating-model claim | **Resolved through effective narrowing:** a documented model is not called a demonstrated cause. |
| Consolidate limitations and improve the comic's final action | **Partially resolved:** the final action is specific but assumes a single majority fund. |
| Broaden the title if no map can be sourced | **Superseded:** the partial documented map justifies retaining it. |

The report reconciliation is confirmed; the remaining ownership-language inconsistencies are separate issues.
