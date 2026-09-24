# Editorial review: Is the Investor’s Adviser Helping, Assessing or Deciding?

Reassessed 15 September 2026 from the complete current article, summary and comic text where present, the previous review where present, revision log and Git changes. See the [collection review](../REVIEW.md).

## Current assessment

The coaching-to-assessment scene gives this chapter a distinctive purpose and justifies retaining it separately from sourcing and engagement design. The reporting relationship replaces the mistaken claim that only investor advisers have privileged access. Returning to the opening planning meeting gives the conclusion a satisfying practical payoff. Preserve the reciprocal expectations, limited confidentiality and distinction between influence and authority.

The main remaining problem is a new categorical claim about who may authorize an assessment. It turns a useful proposed working agreement into an unsupported general rule about rights.

## Active recommendations

1. **High impact — distinguish a newly agreed company assignment from existing investor rights.** “Only the company can authorize an assessment of its executive,” repeated in the summary and comic, is too broad. An investor can assess leadership for its own decisions, and an existing agreement may already authorize relevant access or use of information. For example, this [SEC-filed investors' rights agreement, section 3.2](https://www.sec.gov/Archives/edgar/data/1540171/000119312526147573/ck0001540171-ex4_2.htm) grants specified investors and representatives inspection and discussion rights for monitoring and investment decisions, subject to limits. It does not establish Larkspur's rights; it demonstrates why those rights must be checked. Suggested rewrite: “In Larkspur's agreed arrangement, a new company-sponsored assessment needs Inès or board approval. Morgan first checks the existing information and reporting obligations, then explains the new purpose, any additional access and the proposed use of coaching material.” Keep the separate rule that directing company work requires applicable authority. Do not imply a company veto over every investor opinion.

2. **Medium impact — separate oversight from instructions in the diagnostic table.** The combined “Formal oversight or interim leadership” row tells employees to hear an authorized instruction. Formal oversight can instead be review or escalation without day-to-day direction. Split the row or state: “Review finding for oversight; authorized instruction only for decisions explicitly delegated.” Otherwise the table reproduces the ambiguity it is designed to remove.

3. **Medium impact — finish the visual role change.** Panels 2 and 6 carry explicit regeneration markers. Panel 6's new coaching-to-assessment scene is central to the revision, so its old image cannot be treated as a completed fix. Check panel 3's surviving pricing-example label too. The text is substantially improved, but the current reading formats are only partially reconciled.

4. **Low impact — remove editorial scaffolding and simplify the confidentiality explanation.** “The table adds a diagnostic column” describes the revision rather than helping the reader. Say what to listen for directly. Explain reporting duties and agreed confidentiality in one connected paragraph without implying that every material concern automatically permits disclosure of a coaching conversation. The present structure needs no redesign.

## Verification and limits

The private P01 role brief can establish the supplied example's described responsibilities, not the effectiveness or universal authority of that role. No Larkspur engagement agreement or jurisdiction is supplied, so its legal boundaries cannot be verified. The active recommendation is to state scenario assumptions and existing rights precisely, not to prescribe a universal legal rule. The professional coaching code remains an explicitly adopted professional framework rather than a law binding every adviser.

## Changes since the previous review

| Previous recommendation | Current disposition |
| --- | --- |
| Make dual-role conflict central | **Partially resolved:** the scene is substantial; its approval rule overreaches. |
| Correct uniqueness claims in every format | **Resolved:** the actual reporting relationship replaces the consultant contrast. |
| Move engagement mechanics to their home | **Resolved:** this chapter now owns purpose, information use and role changes. |
| Make the assignment table diagnostic | **Partially resolved:** the added column helps, but oversight is conflated with operating direction. |
| Consolidate repeated comic scenes and clarify responsibility language | **Partially resolved:** revised text works; image updates remain pending. |

The scope of assessment authority is a new substantive concern, not a reason to abandon the effective dual-role example.

## In-depth review round 2 — dispositions (2026-09-22)

Seven findings were raised against the round-01 revision. Note that all sixteen article files
were reverted on disk to their pre-round-01 state partway through this pass; round-01's work was
recovered from `stash@{0}` (five files byte-identical to the round-02 inventory, `spec.md`
identical plus one in-progress edit) before these fixes were applied.

| Finding | Disposition |
| --- | --- |
| IA-004 — onboarding example overstates the evidence | **Fixed.** Now reports five sampled implementations averaging ~80 hours and the specialist needed in three of five; Morgan's scaling claim is labelled a hypothesis with its linear-growth assumption stated; Alex's 40% is an estimate; the measurement records data cleaning, product-related work **and** the remaining setup work instead of forcing a two-way split. |
| IA-009 — summary reinstated the company-veto reading | **Fixed.** The summary now separates the investor opinion Morgan may form from information already lawfully available under existing arrangements from the company-commissioned assessment or extra access that Ines or the board approves. |
| IA-001 — escalation condition and contractual parties | **Fixed.** "Only if unresolved" restored in the summary; "only Alex is party" replaced in both formats with Alex as the protected client; a sentence notes a private agreement cannot displace a legally required disclosure. |
| IA-002 — residual jargon | **Fixed.** Comic intro now defines board, existing rights, coaching and delivery capacity; "charter" became "written assignment"; onboarding is defined at first use; fund and coaching sponsor glossed; oversight explained in the summary. |
| IA-003 — dense paragraphs and long summary | **Fixed (paragraphs); partially addressed (length).** The ~200-word rights paragraph is four units and the coaching-fallback paragraph three. Summary prose went 597 → 514 words against a 300–500 target; the residue is the consent and existing-rights material this same review requires. Journal median is 506. |
| IA-010 — Alex's appearance changed in panel 2 | **Fixed in the artwork.** Panel 2 regenerated (three attempts); Alex is medium-brown-skinned with short dark curls as in panels 1/3/4/6, and the two detached reporting chains plus the dashed ADVICE arrow are retained. Inspected directly. |
| IA-011 — unreadable labels and missing text equivalents | **Fixed.** Summary figure and comic panels 3, 4 and 6 regenerated with enlarged labels and no decorative microtext; alt text and captions now carry the agreement dimensions and the paper/card labels. Verified at 360px and at the true 312px rendered width. |

Checks run: full build clean; all three modalities present; six local link targets exist; zero
unresolved `[[…]]`; published assets byte-identical to sources; panel sha256 provenance refreshed;
figures re-inspected as images, not prompts; Playwright at 1280×900 and 360×780 with no overflow.

Not done: the full manuscript exporter was not run, because a fresh export rewrites 22 chapters
belonging to other in-flight sessions. This chapter's `.md` and its manifest entries were spliced
instead; the nine remaining validator "rerun export" errors are pre-existing and belong to those
other sources. The private P01 role brief is still missing from its recorded path.

## In-depth review round 3 — dispositions (2026-09-22)

| Finding | Disposition |
| --- | --- |
| IA-001 — comic omits the basis for Alex's consent | **Fixed.** Panel 6's caption now says that Alex and Morgan agreed in writing, when the coaching began, that what Alex says is not reported to the firm and that a concern goes to Alex first and to Ines only if it remains unresolved. It ties Alex's consent to using those conversations in the assessment, says Ines's approval of the assessment does not release them, and states that no private agreement overrides a legally required disclosure. The scene itself is unchanged, so the artwork was not regenerated. The summary now has separate "Who approves the work?" and "Who releases the coaching?" paragraphs and carries the same legal-disclosure limit. |
| IA-003 — dense passages, summary length, Block annotation | **Fixed.** The authority key point now separates the principle from its four sources. The measurement passage is split after the three kinds of work, and "size them" / "sized" are replaced by "how much work each explanation accounts for" in the article and the panel 3 caption. The summary is down to **498** prose words (image and caption excluded), with no conditions removed. The Block annotation uses the wording the review proposed. |
| IA-002 — residual financial and internet terms | **Fixed in the text; tab label not changed.** "Return" is now "financial gain" in all three openings. "Revenue" is now "money coming in from sales", and "stake" is now "share of the company". "Senior officers" is now "senior executives" in the article, summary and comic, and "a quarter" is now "three months". The research annotation now defines private equity and corporate governance, and the cited title is unchanged. **Not changed:** the "TL;DR" tab label comes from `_MODALITIES` in `_wiring/build.py` and applies to every post in every journal. Changing it would rebuild every post page across the site, which is outside this article's scope. Note that CLAUDE.md documents this label as "Summary", so the code and the docs disagree. The author needs to decide site-wide. |
| IA-011 — small labels at phone width; panel 4 alt text | **Fixed in the artwork.** Figure 2 and comic panels 3 and 4 were regenerated with fewer, upright, larger labels. Figure 2 now has five labels: company, adviser, advice, decision, agreed access. Panel 3 has three upright cards: setup work, messy data, what we will measure. Panel 4 has a company capacity board and an other investments folder stack. All three were inspected at full size and at 312 px wide. The alt text for Figure 2 and panels 3 and 4 now matches the drawn labels word for word. Old images are archived under `_research/discarded-*-variants/`, and the prompt archives now hold the new prompts and hashes (panels 2 and 6 hashes, which were stale, were also refreshed). A separate narrow mobile variant was not added, because the regenerated images are readable at the mobile width. |

Unresolved: the private P01 role brief is still missing from its recorded path.
