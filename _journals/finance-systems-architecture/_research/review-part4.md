# Review log — Part IV (part-4-intro, ch. 34–43), 2026-10-18

Format checks were scripted for every page: front matter, callout order and labels, three KEY POINTS, failure-pattern names, `<br>`, mermaid fences and captions, valid `[[links]]`, and hand-offs in config order. All pages passed. Every ch. 34–42 hand-off points to the next chapter; ch. 43 now points to Part V. Render check: 11/11 OK.

All chapters (except ch. 42) got an American-spelling pass. Lowercase "programme" became "program"; the proper name *Program Keystone* is unchanged. Also fixed: catalogue → catalog, licence → license, theatre → theater, labelled → labeled.

## part-4-intro
- The ch. 43 learning-path bullet now matches ch. 43's three KEY POINTS: stressors and residues, portability, and the shift from reviewing to providing.

## 34 architecture-governance
- Standard IDs renamed from STD-0x to STD-FIN-0x in the article and the spec (item 13).
- Catalog column renamed "In force". All standards are dated 1 Apr 2027; STD-FIN-01/-02 are enforced from 1 Jul 2027 (schema registry); the STD-FIN-04 ATC gate from June 2027; STD-FIN-05 has SFP controls from 1 Jul 2027.
- Per-standard waiver counts changed to 1/2/4/2/2/0 (total 11) so they reconcile with ch. 35's 14 at the end of Q3. Added a sentence linking the two figures.
- In ADR-0007, Ingrid's advice now reflects the move of bank-details authority from SFP to Northmere Pay (item 8).
- The ch. 1 standards are now described as "five proposed … a sixth followed in Q3 2027".
- The resolved open question in the spec is marked as resolved.
- The editor note about a Feb 2027 Tablekin decision does not apply to this article: ch. 34's body has no such date. The Feb 2027 date for ADR-0006 appears only in the ledger's [architecture-governance] line, and the fix landed in ch. 36.

## 35 principles-standards-reference
- States that STD-FIN-01/-02 were declared on 1 Apr and enforced from 1 Jul 2027. Added a link to governance.

## 36 target-and-transition-states
- Plateau 1 now names STD-FIN-01..06.
- Product funding now starts from 2028, matching ch. 41 (it said 2030).
- The Tablekin ledger decision is now dated to the June 2027 recommendation.
- Added cross-references to ch. 38's benefit and budget breakdowns.

## 37 vendor-portfolio-strategy
- "Leverage" (buzzword) changed to "negotiating power".
- Noted the 8 Dec 2027 accounting-hub outcome.

## 38 finance-transformation
- **Item 11.** The benefits register is now $22M + $9M (= $31M retired systems), $38M effort and $26M PSP/bank, mapped explicitly to ch. 36. The $310M budget is also tied to the $54M/$171M/$85M tranches.
- **Item 21.** The cut-over calendar now follows ch. 12's blackout rules, which leave early May and early November. Also corrected the criterion "never at year-end".
- Partner bank-details authority is now presented as the target state (item 8).
- The decisions table records the 8 Dec 2027 convergence decision; it was "pending".
- Corrected the S/4HANA Private Edition change cadence (feature packs every 6 months, a release every 2 years). It said "upgrades every year".
- Birmingham: no figure is quoted (item 12 OK).

## 39 technical-debt-and-fitness
- Standards are referenced as STD-FIN-01..06.
- The SFP cut-over is now 2 Aug 2027 (item 24).

## 40 resilience-and-security
- The Q4 2027 control-totals rule is now a clause of STD-FIN-03, not an extra standard. That keeps the six-standard catalog intact.

## 41 organizing-for-architecture
- Payout ownership clarified: the Head of Partner Settlement owns the rules, and Ingrid owns the process and the platform that executes payouts. The RACI payments cell is annotated and an explanatory sentence added.
- Six standards; August 2027 cut-over.

## 42 ai-in-finance
- **Item 18.** Replaced the Gartner `gcom.pdo.aws` staging host with the www.gartner.com newsroom path and added CFOtech as a secondary report.
- The "errors are visible and reversible" quotation could not be verified, so it is now paraphrased with verified wording. The run-reconstruction quote was verified via CFOtech.
- The agent control card is now named STD-FIN-06.

## 43 long-term-evolution
- **Item 16.** The separability criterion is tied to the 8 Dec 2027 accounting-hub decision; until now it said "whichever route it took". Noted that the decision lists a plausible Wayfare sale as a reversal condition.
- 2031 figures reconciled:
  - ~150 apps against the 158 planned after wave 3 (ch. 36).
  - Wayfare closing on S/4HANA from FY2029; Fusion retired in 2030.
  - $88M against $95M explained by the deferred effort benefit (ch. 38).
- Changed "five" to "six" mandatory standards.
- Added a bridge paragraph to [[part-5]] and [[case-uber-payments]] before the toolkit paragraph.
- Spec non-goal updated.

## Open issues for other parts / the author
- **Item 24 vs the calendar rule.** The editor's new 2 Aug 2027 SFP cut-over falls in Stayloft's July–August peak, which ch. 12 blocks and ch. 38 now repeats. Consider another date (e.g. early May or early November 2027) or an explicit exception.
- **Ch. 12/33 calendar.** "Early May" cut-overs (e.g. 1 May 2029) fall inside the April close's WD−2..WD9 month-end blackout as ch. 12 defines it. Check the wording in ch. 12 and ch. 33.
- **Ledger lines.** The [architecture-governance] ledger line still says STD-01..06, with ADR-0006 dated Feb 2027. The [finance-transformation] ledger line still has the old benefit split and a December–January cut-over rule. A superseding [editor] line was appended; the originals were not rewritten.
- **timetoread.** Front-matter values (30–34 min) sit between prose-only and all-words estimates at 230 wpm, so they were left unchanged.
