---
status: accepted
revised: 2026-09-23
---

# Spec: Is the Investor’s Adviser Helping, Assessing or Deciding?

## Intent

Explain how a company leader establishes an investor’s technology adviser’s assignment and reporting relationship, separates the adviser’s influence from decision authority, and handles a change of role (coaching that becomes assessment, or advice that becomes interim delivery) before sharing sensitive information. “Investor’s technology adviser” is the general term; the supplied Technology Principal role is this book’s example and is kept explicitly fund-specific. Sourcing help and engagement mechanics belong to the two following chapters.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Follow `useful-engagement` and lead into `tech-operating-partner`; do not describe this chapter as the start of Part IV.
- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Keep the artwork consistent with the argument, not only with the captions. No figure or comic background may place the adviser inside the company’s reporting chain; show the adviser reporting to the investment firm and the company leadership reporting to its own board. Figure labels use plain words drawn from the article’s own definitions rather than management shorthand, and every label carried in an image is large enough to read at phone width.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a set of comic pages — each image one page of three stacked strips with the dialogue, labels and questions lettered in the artwork — generated from the `comic-page` blocks in `comics.md`, with consistent fictional characters, a caption and a transcript per page.
- Keep each recurring character’s appearance identical across every panel, matching the journal cast sheet: Alex is a medium-brown-skinned man with short dark curly hair and a blue rolled-sleeve shirt. A regenerated panel that changes a character’s skin tone, hair or clothing is rejected and generated again.
- Where an image carries a label that does more than decorate — the agreement’s dimensions, a document’s subject, the three role cards — give the same distinction in adjacent reader-facing text, so a text-only reading loses nothing. Drop decorative microtext rather than shrink a meaningful label to fit.
- Explain the board, the investor’s existing information rights, coaching and delivery capacity inside the comic itself, so it reads without another chapter. Use “written assignment” rather than “charter”, define onboarding where it is first used, and gloss fund and coaching sponsor where they appear.
- Make the dual-role conflict the central worked case: what the CTO can ask before sharing sensitive information, what the adviser must explain, who can authorize a changed assignment (distinguishing the investor’s existing information rights from a newly agreed company-sponsored assessment) and how employees are informed; promise no confidentiality beyond agreed obligations.
- Give the fictional coaching agreement one explicit information-sharing rule, and keep the permission to reuse coaching material separate from the company’s approval to commission an assessment. State what Morgan does when reuse is not permitted: ask Alex to consent, assess from independently obtained evidence, or leave the assessment to someone else. Carry the distinction into the summary and the comic: each short format states that the consent requirement comes from the written coaching agreement, that it governs reuse in the investor’s assessment, and that the agreement does not override a legally required disclosure.
- State the escalation condition identically in every format: a concern goes to Alex first, and to Ines only if it remains unresolved. Describe Alex’s consent as required because the coaching agreement protects what he said, not because he is the only party to it, and do not present the private agreement as overriding an applicable legal disclosure requirement.
- In the summary, distinguish the investor opinion Morgan may form from information already lawfully available under the existing arrangements from the new company-commissioned assessment or additional access that Ines or the board must approve.
- Keep the onboarding example inside the diligence chapter’s evidence: five sampled implementations averaging about eighty hours each, the same specialist needed in three of the five. Present Morgan’s scaling concern as a hypothesis with its linear-growth assumption stated, keep Alex’s 40% an unverified estimate, and name a measurement that records data cleaning, product-related work and other setup work without forcing the remaining hours into a single category.
- State the adviser’s distinguishing feature as the reporting relationship to the investment firm, not privileged access; avoid uniqueness or universal-ownership contrasts across all formats.
- Use the assignment table as a diagnostic: what employees should hear (assessment finding, recommendation, authorized instruction); ask “Who is authorized to decide?” rather than “who owns”.
- End with the agreed purpose and authority of the opening planning meeting; link engagement mechanics (availability, resources, continuing service, handover) to the engagement chapter rather than repeating them.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Explain the title question and its implications for a concrete company decision.
- Distinguish sourced observations, the manuscript's analysis, and explicitly fictional examples.
- Include a meaningful trade-off or counterargument and identify the evidence that would change the judgment.
- Link related chapters and cite substantive external factual claims close to the text.
- Keep the TL;DR and the comic page scripts consistent with the full article; inspect every generated page against its script.

## Non-goals

Universal prescriptions, invented evidence, promises of investment performance, or disclosure of confidential inputs. The chapter is not a legal or tax opinion.

## Modalities

- Full Article: index.md, the substantive argument.
- TL;DR: summary.md, the practical implications in concise prose.
- Comic: comics.md, eight illustrated pages of three strips each, with alt text, visible captions and per-strip transcripts rendered from the page blocks that are also the artwork scripts.

## Open questions

Evidence gaps and chapter-specific next research are tracked in the separate editorial backlog. The book uses the author’s accepted working title; evidence and role questions remain open.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- 2026-09-12: Use an explanatory essay rather than the repository's ADR template. Preserve per-post folders and stable permalinks. User explicitly requested varied chapter structures.

## Sources

The supplied book brief establishes scope. Public citations appear in the article and bibliography. Private provenance is recorded separately in _research/input-reading.md and is excluded from the site configuration.

## Changelog

- 2026-09-23 (comic pages): The six single-scene panels replaced by eight comic pages of three strips each, so the separate reporting lines, the four questions and the shareholder agreement's grants and limits, the three jobs and what employees hear, the four sources of authority, the coaching-to-assessment case with its five questions, the one-sentence coaching rule, the three honest routes and the two permissions, the authorization and the written note to managers, the diligence dispute and its agreed measurement, and the four planning-meeting statements are drawn into the artwork rather than carried by captions. Page images live under `assets/images/13-investors-adviser/`; captions and transcripts are rendered from the page blocks; the previous panel comic is archived under `_research/comic-pages-pilot/`. No fact, rule or decision changed; permalink unchanged.
- 2026-09-22 (in-depth review, round 3): Comic panel 6 now establishes the written coaching agreement, attaches Alex’s consent to reuse in the assessment, restates the only-if-unresolved escalation and notes the legal-disclosure limit; the summary gives company approval and coaching consent separate paragraphs with the same limit, trimmed to 498 words. Plainer wording for return, revenue, stake and senior officers; private equity and corporate governance glossed in the research annotation; the authority key point and the measurement passage split; the Block annotation recast. Figure 2 and comic panels 3 and 4 regenerated with fewer, larger labels readable at a 312px phone width, with alt text matching the drawn labels. Permalink and id unchanged.
- 2026-09-22 (in-depth review, round 2): Correct the onboarding example to the diligence chapter's actual evidence (five sampled implementations averaging about eighty hours, the same specialist in three of them), label Morgan's scaling concern a hypothesis with its linear-growth assumption explicit, keep Alex's 40% an estimate, and widen the resolving measurement to include the remaining setup work. Restore the “only if unresolved” escalation condition in the summary and describe Alex's consent as the protected client's rather than the sole party's, noting that a private agreement cannot displace a legally required disclosure. Separate the investor opinion formed under existing rights from a company-commissioned assessment in the summary. Define board, existing rights, coaching and delivery capacity inside the comic; replace “charter” with “written assignment”; define onboarding at first use; gloss fund and coaching sponsor; explain formal oversight in the summary. Split the rights and coaching-fallback paragraphs; summary prose trimmed 597 to 514 words. Comic panel 2 regenerated to restore Alex's established appearance while keeping the two separate reporting chains; summary figure and comic panels 3, 4 and 6 regenerated with phone-legible labels, with the meaningful labels mirrored in alt text and captions. Permalink and id unchanged.
- 2026-09-22 (in-depth review): Give the fictional coaching agreement one explicit information-sharing rule and separate permission to reuse coaching material from the company’s approval to commission an assessment, with the fallback stated when reuse is not permitted; split the long confidentiality, authorization and closing-agreement passages into shorter units; introduce investor, shareholder, board, information rights, venture and growth investor, deal team, partner, onboarding, board paper, escalation, legal privilege and trade secret in plain language at first use, and expand chief executive officer and artificial intelligence; state the onboarding disagreement and its resolving measurement in ordinary words rather than by reference to the diligence chapter; introduce Alex’s and Ines’s roles in the summary and Ines’s in the comic; qualify the private-equity research annotation as an association the study reports plus an authorial inference. Comic panel 2 regenerated so its background chart no longer places the adviser under the executive team, and figure 1 regenerated with plain scope labels. Permalink and id unchanged.
- 2026-09-21 (Part IV order): Move the adviser chapter immediately before the technology operating partner chapter, in source folder `13-investors-adviser`. Update the opening recap and closing bridge; preserve its article, summary, comic and artwork.
- 2026-09-15: Editorial revision per review: the claim that only the company can authorize an assessment replaced across article, summary and comic by the distinction between the investor’s existing information and discussion rights (filed example cited) and a newly agreed company-sponsored assessment; formal oversight separated from interim leadership in the assignment table; confidentiality explained in one paragraph tied to the agreed obligations; authority definition now refers to decide-who-decides; comic panel 3 flagged for regeneration (pricing-example prop); panel images inspected against dialogue (2, 3 and 6 mismatch, 1, 4 and 5 agree); summary trimmed back within the 500-word limit; timetoread 12 min; permalink and id unchanged.
- 2026-09-14: Editorial revision per review: uniqueness claim replaced by the reporting-relationship framing, the coaching-to-assessment role change made the central case (absorbing the shadow-hierarchy and coaching-confidentiality material from decide-who-decides), engagement mechanics moved to links, the billing-code example replaced, the ending returned to the opening meeting; comic panels 2 and 6 reworded (regeneration flagged); permalink and id unchanged.
- 2026-09-14: Retitle the post from “Working With the Investor’s Technology Adviser” to “Is the Investor’s Adviser Helping, Assessing or Deciding?”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12: Add the author-requested ai-notes KEY POINTS opening; preserve article-specific conclusions and caveats.
- 2026-09-12: Initial spec, status draft; supports a substantial first manuscript and later evidence-led revision.
