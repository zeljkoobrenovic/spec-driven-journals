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
