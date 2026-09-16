# Review: Introduction & Reading Guide

**Reviewed:** 2026-09-16 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, the previous REVIEW.md, and all four local image assets.

Supporting checks covered the journal configuration, existing generated guide and spec, chapter/modality inventory, selected linked chapters, bibliography policy, structural history and revision log. This reviews the current working files, including the new “Why This Book Exists” section.

## Verdict

The guide gives company leaders a clear audience promise and useful decision routes. Its contents and format inventory are accurate, and the earlier recommendations about the separate financing-delay example, format caveats and further-reading policy have been implemented. Keep the present structure. The most important remaining correction is to bring the illustrations into agreement with the revised text and contents; also qualify the venture-investor definition. The page works as a living draft, but these accuracy issues should be corrected before calling the guide reconciled.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 5 · nit 0

### Blockers

None found.

### Major

1. **[index.md · lines 54–63 and 71–72 · both explanatory figures] The illustrations teach an older version of the guide.** Figure 1 shows owners, funding, decision rights and **expectations**, while the text explicitly defines its fourth question as **what is changing**. Its notebook also maps “owners” to “clear accountability,” although the text distinguishes ownership from the company leader’s responsibility. Figure 2 still advertises **“Optional Branch: Productscapes”**; the appendix is absent from both the contents and configuration, and STRUCTURE.md records its removal on 13 September. Both current generated-site images are identical to these source assets, so these discrepancies reach readers. *Suggested direction: align Figure 1 and its caption with the four stated questions, and remove the discontinued branch from Figure 2.*

2. **[index.md · line 56 · “Owners, Rights, Funding, and Change”] The venture-investor definition makes an early-stage example sound universal.** “Funds a young company still searching for a repeatable business” excludes venture investment in businesses already scaling a working product. The [SEC capital-raising glossary](https://www.sec.gov/resources-small-businesses/glossary), under “Series Rounds,” includes venture funds across rounds that support established customer demand, expansion and later-stage preparation for an IPO. The journal’s own [glossary](../glossary/index.md), line 81, uses a less restrictive definition. This matters because the guide is teaching finance beginners how to interpret these labels. *Suggested direction: qualify the early-stage description and make clear that venture and growth labels overlap.*

### Minor

1. **[spec.md · lines 2–3, 34 and 61] The accepted spec has stale coverage and revision metadata.** It still says 29 main chapters have comics and that handover has none; the article correctly says 30, and the inventory confirms 30 comics with six existing panel images apiece. The generated spec repeats the stale claim. The newly added changelog entry is dated 16 September, but the front-matter revision date remains 15 September. *Suggested direction: reconcile the modality count and revision metadata; the article’s coverage statement is the accurate one.*

2. **[index.md · line 30 · “Why This Book Exists”] The new motivation overstates what has been established.** “Very few” sources address these leadership questions, the claim that this gap produces confusion and missed opportunities, and the account of agendas promoted under investor authority are presented as general findings without support or attribution to the author’s experience. The review does not establish that these claims are false; their scope is unsupported here. The 166-word paragraph also combines the literature gap, its consequences, misuse and the book’s promise before readers reach a route. *Suggested direction: frame the motivation as the author’s observed gap, qualify claims about frequency and motives, and separate the problem from the book’s response.*

3. **[index.md · line 82 · “Meet the Fictional Company”] The shared-example map omits two important earlier destinations and is difficult to scan.** The paragraph identifies recovery and support episodes but omits [[cannot-fund-everything]] and [[roadmap-to-revenue]]. The former explicitly allocates the same first-hundred-days envelope and initiative identifiers; the latter reports the ONB-1 cohort and review. Readers meet those substantial parts of the shared story before recovery. With cross-links expanded to full chapter titles, this paragraph is approximately 236 words, including both the shared chain and the separate financing example. *Suggested direction: include allocation and measured outcomes in the map, and separate the chronological chain from the alternate-scenario note.*

4. **[index.md · line 88 · “Choose a Reading Format”] “Only the article” is too exclusive.** The funding-sources summary contains an inline SEC citation, while the roadmap-to-revenue summary includes a source and worked capacity calculations. The article therefore does not uniquely carry “the worked figures” and “the sources.” Saying that only it contains cases where the conclusion changes also blurs the preceding promise to retain material conditions in every format. *Suggested direction: describe the article as providing the fullest calculations, source discussion and alternative cases, while keeping decision-changing conditions in all formats.*

5. **[index.md · line 32 · living-journal paragraph] The promised revision log is not where a site reader is told to find it.** Each chapter has a published “View spec” link with a changelog, but the separate revision log is one collection-level file, posts/REVISION_LOG.md; it is neither beside each chapter nor exposed by the site. The guide supplies no link that resolves this distinction. *Suggested direction: point readers to the changelog in each linked specification.*

### Nits

None recorded.

## Spec ↔ post alignment

| Success criterion | Status | Evidence |
| --- | --- | --- |
| Distinctive header logo and navigation icon, with unique paths | met | Both assets exist, have unique references within this journal, and match the generated copies. |
| Two explanatory figures with accurate labels, alt text, captions and restrained emphasis | partially met | Both figures exist and are captioned; their conceptual/structural labels need the corrections in major finding 1. |
| Explicit company-leader decisions, authority and funding assumptions | met | Opening, decision routes and ownership discussion retain the company leader’s responsibility and distinguish actual terms from labels. |
| Scoped historical evidence and a clearly distinguished fictional chain | met | Historical evidence limits are explicit; the financing-delay scenario is correctly separate. Minor finding 3 improves the map’s completeness and readability. |
| Companion formats retain the decision and material conditions; coverage is accurate | partially met | The 30-chapter coverage and reconciliation caveat are accurate. The “only the article” wording and spec’s 29-comic count need correction. |
| Beginner usability, plain labels and relevant teaching links | partially met | Practical routes and accessible explanations work; the venture definition is too restrictive. |
| Clear primary reader, accurate accessibility promise, routes before contents, configured Part IV heading | met | Audience, ordering and heading match the contract and configuration. |

**Non-goals respected:** yes. The guide does not claim exhaustive coverage or completed professional review.

**Drift:** the accepted spec’s modality inventory is behind the current article and files. Recommend marking it drifted until the inventory and revision metadata are reconciled. The central intent and audience remain aligned.

## Cross-modality alignment

This guide intentionally has only the Article modality. No summary, conversation, checklist or comic is missing for this page. Its statements about other chapters were checked against their file inventory and selected summaries; this was not a full re-review of the book’s companion formats.

## Layer-by-layer notes

### Spec

- The contract has the expected sections and remains shorter than the guide.
- Its success criteria support concrete checks; the source-scope and audience boundaries are useful.
- The historical changelog is legitimate context, but its latest entry and front-matter date should agree.
- The stale comic count is a spec error, not a reason to change the accurate article count.

### index.md

- The opening situation, explicit reader and routes serve the intended audience. The full contents appropriately remains a lookup aid.
- The ownership discussion distinguishes identity, rights, funding and transaction context; preserve that distinction when repairing the figure.
- The historical-evidence boundary and explanation of optional further reading agree with the bibliography.
- The separate financing scenario and article-precedence caveat address the previous review’s substantive concerns. The remaining changes are local accuracy and readability corrections.

## Verification and limits

- Confirmed 41 configured pages: 30 main chapters, six part introductions, the guide and four references.
- All 77 guide cross-link occurrences resolve; the 40 contents entries match configuration order and have generated target pages.
- All 30 main chapters have summaries and comics. Each comic references six existing panel images. Summary body counts fall between 490 and 500 words under a count excluding figure material, inline source labels and markup.
- All four guide assets exist and match the generated copies. The source figures and header were visually inspected; no artwork was changed.
- The existing generated guide includes the new introduction, and the generated spec reproduces the stale inventory statement.
- External verification was limited to the venture-stage definition, checked against the SEC glossary on 16 September 2026. No full historical-source or browser-layout audit was undertaken.
- No build was run: this review changes only REVIEW.md.
