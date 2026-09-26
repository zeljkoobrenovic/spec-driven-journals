# Editorial review: Can the Software and the Team Deliver What Was Promised?

Reassessed 15 September 2026 from the complete current article, summary and comic text where present, the previous review where present, revision log and Git changes. See the [collection review](../REVIEW.md).

## Current assessment

The revised assessment now has a job: determine whether Larkspur can invoice in another country within twelve months. It records a working core as a strength, identifies a shared billing constraint, costs a transition and hands a specific finding to the following chapters. This is much more useful to a technology leader than a maturity checklist. The placement before the organization and design chapters also improves the argument.

The principal remaining issue is an inference about waiting time. The metrics are now defined correctly, but their difference does not establish the cause claimed. Preserve the finding table, strengths and distinction between transition spending and later benefits.

## Active recommendations

1. **Medium impact — do not infer that all time outside the DORA measure is waiting.** In “Does the team deliver safely and predictably?”, commit-to-production time below two days is compared with roughly three weeks from request to delivery. Work before a commit can include implementation as well as queues and approvals. [DORA's current definition](https://dora.dev/guides/dora-metrics/) starts at a version-control commit. Suggested rewrite: “Most elapsed time falls outside commit-to-production. A trace of one recent country change is needed to distinguish approvals, specialist queues and implementation.” The following chapter supplies that trace; use it as the evidence for the waiting diagnosis. Correct the corresponding shortcut in the summary and linked organization chapter.

2. **Medium impact — qualify the new investor callout.** “Investment plans fix the destination and date before anyone has looked at the systems” turns this example into a claim about all investment planning. “An honest assessment is the only way” also excludes other relevant evidence. Prefer: “If the investment plan assumes a country launch before the systems have been assessed, the assessment tests whether the date and budget are credible.” This matches the conditional framing already restored elsewhere.

3. **Medium impact — finish the comic's assessment scene in the artwork.** Panel 4 now describes a plan-specific assessment rather than prescribing modular services. That is an effective correction in the text. The embedded regeneration marker means the current image is not evidence that the visual message has changed. Confirm that the regenerated scene preserves the stable core and identifies the constraint, rather than silently reinstating an architectural prescription.

4. **Low impact — reduce repeated explanation after the finding.** The transition table and final assessment already establish that a working system can still fail a new plan. A shorter conclusion could name the handoff directly: “The next question is why a small country change waits on these people; only then should Larkspur choose a replacement or a new boundary.” This is a pacing preference, not a request for another outline or more assessment frameworks.

## Verification and formats

DORA currently uses five software delivery performance metrics; the previous five-metric finding was correct and should remain. Its change lead time is commit-to-production, not request-to-delivery. The proposed transition sums correctly to €1.3 million: €900,000 staffing, €240,000 parallel running and €160,000 migration. The new “spending before benefit offsets” label avoids presenting that total as net cost. First invoicing around month 12 and retirement later in the transition are now distinguishable. The numbers are scenario assumptions, not external estimates.

The summary is a usable standalone assessment but inherits the waiting inference. Comic text has improved; artwork remains outside this textual verification.

## Changes since the previous review

| Previous recommendation | Current disposition |
| --- | --- |
| Produce a finding owned by this chapter | **Resolved:** the completed finding table supplies a clear handoff. |
| Replace universal claims about ordinary ownership | **Partially resolved:** the main argument improves; the later callout reintroduces a universal claim. |
| Distinguish DORA lead time from end-to-end delivery | **Partially resolved:** definitions are correct, but the causal inference between measures is not. |
| Clarify transition timing and cost | **Resolved:** parallel running, migration, first benefit and later retirement are separated. |
| Relocate broad standards and avoid “fewer projects” as a diagnosis | **Resolved:** the chapter is more selective and evidence-driven. |
| Align the comic with assessment rather than a prescribed design | **Partially resolved:** dialogue is revised; panel 4 still requires visual verification after regeneration. |

No substantial restructuring remains necessary. The new sequence is a material improvement.
