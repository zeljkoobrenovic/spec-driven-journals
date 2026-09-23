# Editorial review: Turn “We Expect Growth” Into a Design Decision

Reassessed 15 September 2026 from the complete current article, summary and comic text where present, the previous review where present, revision log and Git changes. See the [collection review](../REVIEW.md).

## Current assessment

The article now develops a genuine design choice from the preceding assessment and organization findings. Buying a supplier capability, extracting a country boundary and replacing the platform have distinct costs, times and consequences. The treatment of bought products, configurable rules and organizational boundaries prevents “architecture” from becoming shorthand for rewriting software. The correction to the rare-failure rule is particularly important: consequence as well as frequency now matters.

The preferred option is understandable, but its cost comparison and fallback need more precise boundaries. Keep the current structure; another split would not solve these local problems.

## Active recommendations

1. **Medium impact — compare costs on the same basis.** The supplier route costs €60,000 to establish plus €40,000 annually, while the internal boundary has €140,000 of additional spending and separately funded staff. Calling the latter “an extra €80,000” compares setup expenditure alone. Calling the fallback a “€60,000” choice likewise omits its recurring obligation. Label the €80,000 as the upfront difference, show the relevant first-year and ongoing costs, and state how internal maintenance is funded. The €160,000 remaining cash headroom is useful, but it is not an estimate of the fallback's full cost.

2. **Medium impact — make the failure state genuinely reviewable.** If unexplained invoice differences persist, a “safe intermediate state” cannot simply assume that the extracted country capability is safe. State what remains live and validated. For example: “If the extracted path has not passed invoice replay, existing billing remains authoritative. The board can fund the supplier route using the unspent reserve, with migration and subscription costs shown separately.” Distinguish money already spent from the incremental fallback commitment, and show whether its four-to-five-month lead time still fits the launch window when invoked at month four.

3. **Medium impact — correct the summary's description of the options.** “Three options meet the requirement within €300,000” conflicts with the €1.3 million replacement option presented immediately afterwards. A useful sentence is: “Two options could fit the €300,000 additional-spend limit; the full replacement provides a comparison that exceeds both the immediate budget and the target for first benefits.” Keep this explicit across formats.

4. **Medium impact — preserve the distinction between changed timing and available cash.** A longer holding period may make later benefits relevant, but it does not itself make the replacement affordable. Likewise, slower growth does not establish that earlier spending “was not wasted.” Reassess the remaining costs and benefits under each changed condition rather than reassuring the reader about the original choice. The collection's financing chapters already provide the needed vocabulary.

5. **Low impact — specify specialist weeks and reduce table repetition.** “Six weeks of two specialists and the new engineer” can mean elapsed weeks or combined effort, while later passages use six protected specialist-weeks. Define the unit once. The successive overview, built-product and bought-product tables are helpful for different readers, but a few repeated explanations of the same five priorities can be cut. These are clarity and pacing edits, not reasons to rebuild the outline.

## Verification and formats

The €300,000 envelope less €140,000 additional spending leaves €160,000. The separate payback illustration is consistent when benefits start after the first year: €200,000 spent initially and €100,000 annual net savings thereafter recover the initial amount after approximately three years from the start. A €1 million valuation illustration at 10× €100,000 is arithmetic, not proof of an additional realizable return; retain that qualification and avoid adding it to a cash-flow valuation of the same benefits.

The main text, summary and comic all now treat design as a response to requirements. The summary's budget sentence is a confirmed mismatch. The risk section correctly rejects “rare” as sufficient reason to ignore a severe outcome.

## In-depth review round 1 — implemented 22 September 2026

All eleven findings (GID-001 … GID-011) were assessed against the current files and accepted. Dispositions:

| Finding | Disposition |
| --- | --- |
| GID-001 reversal rule contradicts the economics | **Fixed.** Losing the third country is now a *reassessment* trigger. The three signals are split into a numbered list, each tied to the one response it justifies (switch / defer / reassess), and the reassessment compares remaining spend, delivery risk, specialist time and expected years of use — showing that A wins before any spend, while after €80,000 finishing B costs €60,000 against €100,000 to start A. Summary realigned. |
| GID-002 fallback proved cash, not people | **Fixed.** A new "Who does the work" step sources A's eight engineer-weeks (six from the billing engineer freed when the extraction stops, supplier implementation team for configuration, two protected specialist-weeks), and "What if that protection fails" forces an explicit choice — defer the launch or separately fund incident cover — when the trigger was itself lost specialist time. |
| GID-003 invoice date substituted for the payment milestone | **Fixed.** A new paragraph separates commit / go-live / invoice / payment, states the fictional payment terms (invoiced in the month service starts, thirty-day terms) and fixes the milestone as first *payments* by month twelve. Table row, record items 2–5 and the fallback timing now label invoice dates and add the month to cash; the fallback margin is recomputed from "two to three months" to **one to two months**, and C is noted as landing its first payment after month twelve. |
| GID-004 summary changed material conditions | **Fixed.** A's month four-to-five range restored; C described as several times over budget with its first invoice about month twelve (benchmark, not candidate); the three triggers now distinguish switching, deferring and reassessing. |
| GID-005 financial terminology beyond the audience | **Fixed.** EBITDA is explained rather than merely expanded (including that it is not cash), with interest, taxes, depreciation and amortization each glossed. Enterprise value, net debt, present value, discounting, holding period, margin, buyout, funding round and corporate parent now carry plain-English glosses; the €1 million sensitivity is walked through step by step, and the summary carries its own definitions. |
| GID-006 technical terms and unintroduced cast | **Fixed.** Larkspur introduced as a fictional scheduling-software company; Alex, Priya, Sam and Ines named with their roles, and CEO/CFO/CTO spelled out in the decision record. "Coupled", regression, replay, reconciliation, sandbox, notice period and margin glossed; option B described first in plain terms. Summary and comic carry their own replay and specialist-week definitions. |
| GID-007 comic omitted the worked decision | **Fixed.** Panel 3 regenerated as a priced A/B/C comparison (€100,000 first year / month 4–5; €140,000 once / month 8; €1.3 million crossed out) and panel 6 as the signed decision record (€140,000 of €300,000, paying customers by month 12, the priced fallback, the month-4 replay trigger). Captions and transcripts rewritten to match. |
| GID-008 visual logic overstated the mapping | **Fixed.** Figure 1 regenerated: right-hand boxes are now explicit question cards ("Which responsibilities can be separated, and can the data move?"), with no "independent services" and no API labels. Panel 3's modular/microservices-versus-monolithic binary is gone, replaced by the actual supplier/component/core alternatives. |
| GID-009 missing label transcripts and jargon | **Fixed.** Alt text for Figure 1 and panels 1, 2, 3, 4 and 6 now reproduces the embedded labels and their meaning, glossing market share and "acquisition costs" (spend to win each customer). Regenerated artwork carries no unexplained background jargon and uses large high-contrast lettering. |
| GID-010 dense reconciliation interrupted the argument | **Fixed.** The setup paragraph is split into money / people / clock-and-basis, with the cross-chapter bookkeeping moved into a labelled note. Funding, capacity, authority and evidence are separate labelled steps; the fallback is seven short steps; the stress test is three labelled scenarios. |
| GID-011 annotations distorted their sources | **Fixed.** Fowler is described as reporting almost all successful cases he had heard of, explicitly tentative; fitness functions defined as repeatable checks of desired properties with the country-rules example. Real option and discounted cash flow glossed; NYU Stern identified. |

### Verification performed

- Arithmetic recomputed: €300,000 − €140,000 = €160,000; €220,000 after the €80,000 stop; A's first year €100,000 leaving €120,000; finishing B €60,000; the €80,000 upfront premium; A cumulative €140,000 / €180,000; 6 + 10 = 16 and 6 + 2 = 8 engineer-weeks; payback ≈ 3 years; 10 × €100,000 = €1 million; €900,000 + €240,000 + €160,000 = €1.3 million.
- `python3 _wiring/build.py` clean; all eight cross-links resolve (no literal `[[…]]` in output); regenerated images byte-identical between source and `docs/`.
- Manuscript exported and `validate_manuscript.py` prints `[valid]` (46 files, 1084 internal links, 128 images).
- Rendered `docs/private-techuity/growth-into-design.html` via `file://` in Playwright at 1280×1200 and 375×812: no broken images, all three tabs present. Figure 1 and comic panel 3 captured at their 327 px mobile render width — amounts, dates and question text readable, closing the previous round's mobile-legibility gap for the regenerated images.

### Not resolved

- Panels 1, 2, 4 and 5 and both remaining figures were **not** regenerated; their stale or faint embedded labels are compensated in alt text and captions only. Panel 2 still shows faint "MARKET SHARE" / "ACQUISITION COSTS" board notes and a partly obscured third label that could not be transcribed from the artwork; the alt text explains the two legible ones.
- Mobile legibility was verified only for the two regenerated images and Figure 1; the un-regenerated panels were not re-checked at 375 px.
- The summary now runs to about 800 words against the spec's original 300–500-word target. The standalone-comprehension requirements of GID-004/005/006 could not be met inside that cap; the spec was amended to record the trade-off explicitly rather than leave the contract silently broken.

## Changes since the previous review

| Previous recommendation | Current disposition |
| --- | --- |
| Complete a choice among three designs | **Partially resolved:** the decision, dependencies and fallback exist; comparable costs and the fallback state need repair. |
| Correct the rare-failure rule | **Resolved:** likelihood, impact and unacceptable consequences are considered together. |
| Remove universal claims about investor-driven design | **Resolved in the main argument:** the specific growth requirement now does the work. |
| Separate built and bought product explanations | **Resolved:** their distinct implications are visible. |
| Clarify the assessment/design boundary | **Resolved:** this chapter chooses a response to an already identified constraint. |
| Reduce unsupported “most” claims and density | **Largely resolved; low-impact pacing remains.** |

The summary budget claim and incomplete recurring-cost comparison are new findings. Preserve the option-specific reasoning and the corrected risk treatment.

## In-depth review round 2 — implemented 22 September 2026

Nine findings (GID-001, 005, 006, 007, 009, 010, 012, 013, 014). All nine were supported by the current files and **all nine fixed**; none disagreed with, none blocked.

| Finding | Disposition |
| --- | --- |
| GID-001 initial choice asserted without a usage horizon | **Fixed.** The reassessment is split into three dated moments. "Before any money is spent" now derives the answer from expected years of use and states the crossover explicitly: A cheaper over one subscription year, **level with B at two (€140,000 each)**, dearer from the third — so A is the better answer only under a one-to-two-year horizon, an earlier launch or tighter capacity. The holding period is now supplied (about four more years), which is what makes B's case work. |
| GID-005 summary swapped EBITDA for "annual earnings" | **Fixed.** The summary names EBITDA, explains it in plain words, states the two conditions the €1 million rests on (the saving continues every year; the multiple stays at ten), and identifies the result as estimated value of the **operating business** across lender and owner claims — not cash, not shareholder value. |
| GID-006 unexplained vocabulary; wrong capacity-month arithmetic | **Fixed.** "twelve of the eighteen capacity-months" — which read as 72 person-months — is now **"twelve months of the four-person team"**. "Deployment" replaced by releasing versions for customers to use (with *release* defined before *microservices*); "portable data" by data that can be moved out in usable form; "parallel running" by operating the old and new systems side by side; "migration" by moving customers and their data across. The summary gives Alex, Priya and Ines their roles and explains reconciliation in place. |
| GID-007 comic omitted the requirement and B's rationale | **Fixed.** The comic's standalone preamble now states the actual requirement (paying customers in a second country within twelve months, a third expected within two years). Panel 3's caption explains what B changes — the country rules are separated out so later countries are settings — and why it beats A despite costing more at first. Panel 6 no longer claims the record is "complete": the reversal is conditional on unexplained replay differences after the two-week window **and** on specialists actually being free, with deferral named as the alternative. |
| GID-009 alternatives described intended, not actual, artwork | **Fixed, with artwork regenerated.** Panel 4 was a solid cube beside a tangle; it is now genuinely one block divided into four compartments ("ONE PIECE, FOUR PARTS") beside four connected separate blocks ("FOUR SEPARATE PIECES"), both equally tidy. Panel 5's alt text now describes the four labelled cards that are actually drawn rather than one card turning four times. Panel 2's two financial labels are explained in the **visible caption**, not alt text alone. |
| GID-010 dense summary and reassessment paragraphs | **Fixed.** The 187-word option paragraph became a four-column table (option / additional cash / first invoice / what it leaves behind); the 232-word decision paragraph became a chosen-plan paragraph, a fallback paragraph and three trigger bullets. The article's reassessment is three labelled decision points. |
| GID-012 one-month supplier start asserted as a deadline | **Fixed.** Recomputed from a month-4.5 decision: a 1.5-month wait plus five-month setup reaches payment in month twelve exactly, and a two-month wait plus four-month setup reaches month 11.5. The text now names one month as the **planning condition** chosen to keep a month or two of slack, and roughly a month and a half as the true cutoff that leaves none. |
| GID-013 B described as costing nothing further | **Fixed.** The article says B adds **no further supplier subscription** and states that its upkeep consumes the billing engineer's already funded salary — an existing budget line, not an eliminated cost. Panel 3's caption carries the same correction for comic-only readers. Cumulative comparisons remain explicitly on the additional-cash basis. |
| GID-014 cash-timing sketch reversed its own lesson | **Fixed, artwork regenerated.** The card is now a labelled time sequence on a baseline: one bar **below** the line on the left ("PAY FIRST"), two shorter bars **above** it later ("SAVE LATER"), with a left-to-right "TIME" arrow. Direction now matches Figure 2 and the payback example. |

### Verification performed

- Arithmetic recomputed and passing: €300,000 − €140,000 = €160,000; €220,000 after the €80,000 stop; A's first year €100,000 leaving €120,000; finishing B €60,000; A cumulative €100,000 / €140,000 / €180,000 over one to three subscription years; 6 + 10 = 16 and 6 + 2 = 8 engineer-weeks; €900,000 + €240,000 + €160,000 = €1.3 million; payback ≈ 3 years; 10 × €100,000 = €1 million.
- Fallback timing recomputed across both setup durations and three supplier waits, which is what established that the one-month start is an allowance rather than an arithmetic limit.
- `python3 _wiring/build.py` clean; no unresolved `[[…]]` in the built page; all ten article/comic/summary assets byte-identical between source and `docs/`.
- Trial export to `/tmp` compared file-by-file against `manuscripts/owned/` before the real export, since another session had post 12 in flux; no unrelated chapter differed. Real export run and `validate_manuscript.py` prints `[valid]` (46 files, 1084 internal links, 128 images).
- Playwright render of the built page via `file://` at 1280×1200 and 375×812: three tabs present, no broken images. The summary's new comparison table renders 4×4 with no horizontal overflow at either width. Regenerated panels 4 and 5 inspected at their 327 px mobile render width — card headings, "PAY FIRST", "SAVE LATER" and both block labels legible.
- Both regenerated panels were visually inspected against their scripts before and after a second generation pass; the first pass drew a stray panel number and duplicated the "SAVE LATER" label, which the tightened prompts corrected.

### Not resolved

- Panels 1, 2, 3 and 6 and both article figures were **not** regenerated this round. Panel 2's faint "MARKET SHARE" / "ACQUISITION COSTS" board notes remain faint in the artwork; they are now explained in the visible caption as well as the alt text, which is the accessibility fix, not a redraw. Its partly obscured third label still cannot be transcribed and is not described as if it were readable.
- Panel 5's regenerated artwork letters the document stack "PROPOSAL" in mirrored text. Cosmetic, does not affect meaning, and the alt text describes it as a stack of paper marked "proposal"; left rather than spend another generation pass on it.
- The summary remains above the spec's original 300–500-word target (the spec records this exception); round 2 restructured it into a table and bullets rather than cutting the definitions the standalone-comprehension criterion requires.

## In-depth review round 3 — implemented 22 September 2026

Eight findings (GID-001, 005, 006, 007, 010, 012, 015, 016). All eight were checked against the current files, supported, and **fixed**; none disagreed with, none blocked. No artwork needed regeneration this round: every finding landed in prose, captions or alt text, and the review itself confirmed the drawn figures in panels 3 and 6 already match the article's amounts and dates.

| Finding | Disposition |
| --- | --- |
| GID-012 fallback margin overstated, cutoff self-contradictory | **Fixed.** Recomputed 4.5 + wait + setup + 1 against month 12 for waits of 1, 1.5, 2 and 2.5 months at four- and five-month setups. The sum is now shown once as its four terms. The one-month planning wait is given its **actual** margin (first cash month 10.5 or 11.5, so half a month to a month and a half of slack, not "one to two"). The cutoff is stated as setup-dependent rather than absolute: 1.5 months against a five-month setup, 2.5 months against a four-month setup, each landing on month twelve exactly — and the text notes that planning on the longer wait means betting on the shorter setup. The previous flat "beyond a month and a half the date is gone" contradiction is removed. |
| GID-001 third country presented as the deciding reason | **Fixed in all three formats.** The article's choice paragraph now leads with expected years of use as the reason that stands on its own (four-year horizon: A reaches €220,000 against B's €140,000, **no third country needed**), and names the third country as a separate, reinforcing reason that brings the advantage forward. Trigger 3 is reworded to match: losing the third country removes one of two reasons, not the main one, so it weakens the margin rather than reversing the answer. The summary and panel 3's caption carry the same distinction, separating third *year* from third *country*. |
| GID-005 summary expanded EBITDA without explaining it | **Fixed.** The summary now glosses each exclusion in plain words — the cost of borrowing money, income taxes, and two accounting charges that spread the cost of things bought earlier (a building, a server, purchased software) across the years they are used — and states explicitly that it is not cash available to spend, with the falling-bank-balance illustration. "What its lenders and its owners are owed" is replaced: lenders have first claim on a fixed amount, owners keep whatever remains, which is why operating-business value exceeds the value of the owners' shares. |
| GID-007 short formats kept only one switch trigger | **Fixed.** The summary bullet and panel 6's caption now carry **both** triggers — unexplained replay differences after the two-week window, *or* incidents eating the specialist time B depends on — and then state A's own conditions: two specialist-weeks to check the invoice data handed to the supplier, and a supplier schedule reaching customer payment inside twelve months; otherwise the launch is deferred. This matches the article, where switching is relief from B's six specialist-weeks but not from A's two. |
| GID-006 residual investment/software vocabulary | **Fixed by substitution at first meaningful use, not by another glossary.** "Stake" → ownership share (opening, holding period, longer-ownership-period test); "thesis" → the investor's investment/growth plan (overview table heading, decision record); "unit cost" → cost per customer; "acquisitions" → businesses the company buys, with separation spelled out as selling part of the business off; "infrastructure" → computing systems underneath / switch off computing systems nobody uses; "resilience" → the ability to withstand and recover from failures; "capacity management" → keeping enough computing resources available for demand; "hosting" glossed at the closing transition and in the summary as what the company pays for the computers and services that run its software; "service that borrowing" → pay the interest and repay the loans; "valuation premium" → guaranteed lift in business value. |
| GID-010 summary's financial illustration was one 193-word block | **Fixed.** Split into three labelled short paragraphs a reader can locate separately: **when the cash comes back** (the three-year simple payback), **then beware the bigger number** (the conditional €1 million and its terminology), and **do not add the two together** (double counting). Definitions were kept rather than cut to a word target, per the spec's standing exception. |
| GID-015 "three different events" then four listed | **Fixed.** Changed to "four different events"; signing, going live, invoicing and payment are all four defined in the sentences that follow. |
| GID-016 A claimed to carry "no regression risk" | **Fixed.** A is now described as avoiding B's *particular* regression risk — it never reaches into the fragile module to pull the country rules out — and that is explicitly called a lower risk, not an absent one, since connecting a new billing service still has to be proved not to disturb what already works. The sentence now links directly to A's own two specialist-weeks for checking the invoice data. |

### Spec updated first

Three success criteria were tightened before the post was edited, per the spec-as-contract rule:

- The fallback-timing criterion now requires the calculation shown once with its actual margin, and forbids declaring the date lost at a wait the arithmetic still permits under the other setup length.
- The A-versus-B criterion now requires the two reasons to be kept separate: expected use beyond two subscription years favours B on its own; the third country is an independent, reinforcing reason. No format may present the third country as what makes B cheaper within the holding period.
- The short-format criterion now requires **both** switch triggers plus A's own staffing and schedule conditions in every short format.

`revised:` and the changelog were updated in `spec.md`.

### Verification performed

- Fallback timing recomputed programmatically for all eight wait × setup combinations; the article's stated figures (10.5, 11.5, 12.0 for the 1.5/5 case and 12.0 for the 2.5/4 case) match.
- Re-checked the unchanged arithmetic the edits touch: A cumulative €100,000 / €140,000 / €180,000 / €220,000 over one to four subscription years against B's flat €140,000 — which is what supports the new "four-year horizon without a third country" claim; €300,000 − €140,000 = €160,000; 10 × €100,000 = €1 million.
- `python3 _wiring/build.py` clean across all journals; no unresolved `[[…]]` in the built page; all three modality payloads in `docs/private-techuity/growth-into-design.html` contain the revised text.
- Export and validation re-run with the documented commands: `export_journal.py … --output manuscripts/owned` then `validate_manuscript.py manuscripts/owned --source _journals/private-techuity` → `[valid]` (46 files, 547 anchors, 1084 internal links, 128 images). Only `growth-into-design.md` and the manifest changed from this round's edits; no unrelated chapter churned.
- Playwright render of the built page via `file://` at 1280×900 and 390×844: all three tabs (Article / TL;DR / Comic) present, **zero JavaScript errors**, **zero horizontal page overflow** at either width on all three tabs. Tables scroll inside their own wrapper (`overflow-x: auto`), which is the template's existing behaviour. The revised fallback-timing passage and the split EBITDA paragraphs were screenshotted at 390 px and read cleanly.

### Not resolved

- No artwork was regenerated this round, so the carry-over items from round 2 stand unchanged: panel 2's faint "MARKET SHARE" / "ACQUISITION COSTS" board notes (explained in the visible caption rather than redrawn), its partly obscured third background label, and panel 5's mirrored "PROPOSAL" lettering. None of the round-3 findings asked for a redraw.
- The external real-options PDF (Damodaran) remains visually unverified end to end; the annotation's claim was checked against the paper's text, not a full 75-page visual review. Carried over from the review's own limitations.
- The summary stays above the spec's original 300–500-word target, and GID-010's fix added explanation rather than removing it. The spec records this exception explicitly.
