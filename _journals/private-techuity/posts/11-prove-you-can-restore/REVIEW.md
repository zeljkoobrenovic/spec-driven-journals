# Editorial review: Prove You Can Restore, Not Just That You Back Up

Reviewed 14 September 2026. Read the full article, summary and reader-facing comic text.

## Overall assessment

The argument is that security and recovery need evidence of business capability, not merely policies, successful backup jobs or monetized risk claims. The intended reader is a company leader deciding what to fund and who may accept the remaining exposure. The 6am scheduling dependency, eleven-hour restore and uncertain expected-loss example are excellent foundations.

The title promises a focused recovery lesson, while the article becomes a broad security-governance chapter. That breadth can work if the restore failure remains the organizing case. At present it disappears into risk, diligence, shared services and investor access without a completed recovery decision.

## Detailed feedback

- **Introduction and narrative:** Three definitions precede the strongest scene. Open with dispatchers unable to assign engineers, then introduce security, resilience and recovery as the capabilities that situation needs. “A company under no pressure to show earnings” is an unhelpful implied comparison, and a security case does not inherently require a stronger justification simply because an outside investor exists.
- **Authority and terminology:** The introduction says the leader must argue in terms an “investment committee” recognizes. That can be appropriate during a transaction, but the book has carefully distinguished the fund committee from the company board and executives. Name the actual company approval forum or specify that this is an investment-approval scenario. “Security Work Needs an Owner” could use “accountable leader” to avoid ambiguity with share ownership.
- **Examples and technical precision:** The missing credential and unavailable database version make restore failure concrete. However, eleven hours is never compared with an agreed maximum outage or acceptable data loss. Add those plain-language recovery objectives, then explain what a test must demonstrate: restored data, integrity, access, application dependencies and the customer workflow. The summary already says a technical restore may not establish business recovery; bring that useful distinction into the worked case.
- **Risk calculation:** Five percent of €4m is €200,000; two percent is €80,000; the difference is €120,000. The arithmetic is sound for the stated simplified scenario. The tail-risk warning and refusal to book this as EBITDA are especially valuable. The assumed probability improvement remains illustrative, not verified effectiveness of a real control; preserve that label.
- **Organization and pacing:** NIST's six functions provide orientation, but this chapter need not expand into an equal treatment of all of them. “Funding Pressure” and “Shared Support” overlap on access and continuing recovery responsibilities. Combine them or link to the engagement chapter.
- **Tone and conclusion:** The voice is responsible without treating checklists as worthless. The ending restates the proposal formula rather than showing how Larkspur remedies and retests its failure. No specific notification deadline is asserted, which appropriately avoids a false universal legal rule.
- **Other formats:** The summary's whole-service recovery explanation is stronger than the article's scenario. The comic retains the title's lesson, but its introduction repeats the investment-committee ambiguity.

## Recommended changes

- **High impact — Make the failed restore the chapter's spine.** Define Larkspur's service need, demonstrate the gap, select funded corrective work, repeat the test and record residual exposure. This turns the title into a complete leadership decision.
- **High impact — Identify the appropriate authority.** Replace the generic investment committee with the company decision-maker in this scenario. Clarify that documented acceptance cannot make an unmet mandatory obligation disappear; specialist interpretation still governs that question.
- **Medium impact — State recovery objectives in ordinary language.** “Dispatch must resume by [fictional agreed time], with no more than [agreed period] of lost updates.” Show how that requirement changes the restore test rather than adding an acronym-heavy checklist.
- **Medium impact — Keep quantified risk as a bounded inset.** Preserve the arithmetic and severe-loss warning, then return to the decision. Link shared-service and data-access detail to Part IV.
- **Low impact — Start with the scene and shorten the conclusion.** Retain the distinction between evidence of a backup and evidence of an operating service; it is the chapter's strongest line.

## Proposed structure

6am service dependency → failed restore against stated objectives → evidence and response roles → funded corrective option, with risk estimate as an inset → retest and residual-risk decision → implications for shared services and changing owners.
