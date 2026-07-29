# Review: EMPOWERED Product Strategy

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, internally consistent record: the spec is a tight contract, the article delivers the focus–insight–action loop in the house voice with well-placed figures, the checklist reproduces all ten sections cleanly, and the comic covers the core beats with all eight panel images present. The post is publish-ready except for one cross-post issue: the sibling record [[product-strategy]] describes this record's frame as "focus, insights, bets," while this record (and its spec) consistently say "focus–insight–action" ending in team objectives — the two posts should name the shared frame the same way. Below that, the findings are polish: some verbatim repetition of the insight-source enumeration, a hard-to-parse highlight sentence, and a spec criterion ("numbering preserved") the checklist does not visibly satisfy.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 2

### Blockers

- None.

### Major

- **[index.md · How to Read This / Related Records — vs. sibling product-strategy/index.md]** Cross-post terminology drift: this record frames itself as the "focus–insight–action loop" (highlight, How to Read This, spec Intent), but the Build-What-Matters sibling (`product-strategy/index.md`, How to Read This and Related Records) describes it as "Cagan's insight-driven strategy — focus, insights, bets." "Bets" appears nowhere in this record; a reader following the cross-link gets a frame the target never uses. Not a substantive contradiction — the boundary (bridge vs. loop) is stated identically in both — but the load-bearing name must match. *Align on "focus–insight–action" in the sibling (the fix lives in `product-strategy/index.md`, outside this review's write scope).*

### Minor

- **[index.md · opening highlight blockquote]** The Principle sentence chains three independent clauses ("I choose… — and make explicit… — I do the hard work…, and I convert…") with only an em-dash pair joining the first two; it cannot be parsed in one pass. *Split after "prioritized —" into a second sentence.*
- **[index.md · highlight + Statement bullet 3 + Rationale "Insights are earned" + Figure 2 caption + table row 3]** The four-source enumeration (data, customers/user research, enabling technologies, industry trends) appears near-verbatim five times. House style repeats the Statement in the Rationale, but five full enumerations is heavy. *Compress two of the later occurrences to "the four sources."*
- **[index.md · highlight, last sentence]** "Then I get out of the way" sits in tension with the Rationale's own point that "empowering teams does not mean disappearing" and the "management by absence" anti-pattern. The trailing qualifier rescues it, but the phrase hands a skim reader the wrong takeaway. *E.g. "then I hand over the how."*
- **[spec.md · Success criteria, "The checklist survives intact"]** The criterion requires "items and numbering preserved," but checklist.md's ten sections are unnumbered headings (matching the journal's house checklist style — the product-strategy sibling is also unnumbered). As written, the criterion is not verifiably met. *Reword to "items and section order preserved" (or number the sections).*

### Nits

- **[comics.md · Panel 5 caption]** "Strategy is a team sport" introduces a mini-frame that appears in no other modality; the insight-sharing beat itself is faithful. *Optional: "insights that stay local die local" would echo the article.*
- **[checklist.md · Support Empowered Product Teams, last item]** "Distinguish between serving the business and serving customers in ways that work for the business" is the one item in the file that takes two reads; it mirrors the article's anti-pattern wording but is tangled as an action bullet.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · opening highlight (one paragraph, states the loop; parse-ability nit noted above) |
| Strategy defined by contrast | met | index.md · Statement bullet 2; Rationale paras 1–2; table rows 1–2 |
| Insight sources explicit | met | index.md · Rationale "Insights are earned" + Figure 2; checklist.md · Generate Insights section |
| Action means objectives, not orders | met | index.md · Rationale "Action means objectives" + Figure 3; checklist.md · Turn Insights into Action |
| Active management ≠ micromanagement | met | index.md · Rationale "Active management is not micromanagement"; checklist.md · Practice Active Management |
| Checklist survives intact | partial | checklist.md — all ten sections and items present; no numbering, so "numbering preserved" is not visibly satisfied (see Minor finding) |
| Credit is explicit | met | index.md · Authoritative References (Cagan & Jones, *EMPOWERED*; svpg.com essay origins) |

Non-goals respected: yes — the article stays out of the vision-to-roadmap bridge (boundary stated explicitly in How to Read This), does not cover objective assignment mechanics, treats vision as input only, names no specific product, and explicitly makes OKRs optional ("only if they support empowered teams").
Drift: none — spec `status: accepted` is accurate; the spec's changelog note about "pending panel blocks / illustration placeholders" has been superseded by the finished images, which is normal completion, not drift.

## Cross-modality alignment

- **Facts & framing:** consistent — the loop (focus → insight → action), the "twenty priorities means none" hook, the four insight sources, problems-not-features, and active-management beats match across article, checklist, and comic.
- **Terminology:** consistent within the post ("vital few," "focus, insight, action," "problems to solve, not features to ship," "command-and-control"). The one drift is cross-post, in the sibling record (Major finding).
- **Voice & tone:** consistent — first-person declarative article; imperative checklist and terse comic captions are the expected register for their forms.
- **Coverage parity:** good — the comic compresses out "Establish Strategic Context" and "Stay Adaptive" (acceptable for eight panels; the closer still lands "choice, thinking, and effort"); the checklist's "Support Empowered Product Teams" section is folded into the article's action/active-management paragraphs rather than getting its own beat, which reads fine.

## Layer-by-layer notes

### Spec

- Tight and internally consistent: Intent, Audience, Non-goals, Decision log, and Sources all agree; the source-PDF-swap note is a genuinely useful provenance record.
- Success criteria are checkable except the "numbering preserved" clause (Minor finding); no dangling open questions; length is proportionate to the post.

### index.md

- House record shape is fully observed: status highlight matches front matter (DRAFT/draft:gray), MADR-inspired section order, Title Case headings, contrast table, cross-links all resolving, three figures present and captioned.
- The Rationale is the strongest section — each paragraph carries a claim and a test ("If nothing was hard to leave out, no strategy was made"; "stamina failures" is a memorable close).
- Main weaknesses are repetition of the Statement enumeration in the Rationale (Minor) and the overlong highlight sentence (Minor).

### checklist.md

- Serves its modality well: ten grouped sections, imperative single-action bullets, renders as task-list checkboxes; the Final Health Check works as the standing test the article points at.
- Order and content align one-to-one with the article's Statement and Rationale; only the last Support item is tangled (Nit).

### comics.md

- All eight referenced panel images exist under `assets/images/empowered-product-strategy/`; captions match their alt text; the VERA/MILA cast and comic-style block match journal convention.
- Clear arc: hook → problem → principle → insight → sharing → action → management → closer; the mining/gem metaphor for insight is consistent across panels 4–5.
- Panel 5's "team sport" caption is the only phrase without an echo elsewhere (Nit).

## Fixes applied (2026-07-29)

- **Major — cross-post frame drift ("focus, insights, bets" in sibling)**: fixed in sibling — the alignment edit lives in `product-strategy/index.md` and was applied by a separate session in that folder; no change needed in this post.
- **Minor — highlight Principle sentence chains three clauses**: fixed — split into two sentences after "prioritized" in index.md's opening highlight.
- **Minor — four-source enumeration appears near-verbatim five times**: fixed — kept in full in the Statement bullet and Figure 2 caption; highlight varied to "from product data to industry trends", Rationale paragraph reworded around "each of the four sources" with varied per-source phrasing, table row compressed to "Insights are earned from all four sources."
- **Minor — "Then I get out of the way" tensions against active management**: fixed — highlight now reads "Then I hand over the how", per the reviewer's suggestion.
- **Minor — spec criterion "items and numbering preserved" not verifiably met**: fixed — spec criterion relaxed to "items and section order preserved" (checklist keeps house-style unnumbered sections); spec `revised:` bumped to 2026-07-29 with a Changelog line.
- **Nit — comics Panel 5 "team sport" mini-frame**: fixed — caption now echoes the article: "insights that stay local die local."
- **Nit — tangled Support item in checklist.md**: fixed — reworded to "Serve customers in ways that work for the business — not the business by accepting every request."
