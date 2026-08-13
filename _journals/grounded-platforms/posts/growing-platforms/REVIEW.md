# Review: Growing Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A clean, publish-ready record. All seven spec criteria are met, the "grow adoption, not functionality" spine carries identically through article, checklist, and comic, and the argument quality in the Rationale — especially the biased-sample and scaling-down paragraphs — is among the best in the journal. The most important thing to address is small: the comic's Panel 7 caption wears the series' "The cost:" label on content that is actually the protection move (the principled no), which mislabels the beat.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[comics.md · Panel 7 caption]** The series template's "The cost:" label fronts a beat about roadmap triage and the principled no — a protection mechanism, not a cost. The cost idea the article actually names is "every request accepted is cohesion spent". *Suggest recasting the label ("The discipline:") or leading the caption with the cohesion-spent line.*
- **[index.md · highlight blockquote]** At ~150 words and six load-bearing clauses this is the longest highlight of the three sibling records, and the "decided in the new user's first hour" sentence stacks three sub-clauses. The spec does demand all six elements, so it complies — but one pass of tightening (e.g. dropping the parentheticals already defined in the Statement) would sharpen the quotability the spec asks for. *Trim, don't cut elements.*

### Nits

- **[index.md · front matter `excerpt`]** The excerpt near-duplicates the highlight's phrasing ("wins or loses on the new user's first hour", "scales down through tiers and slices as deliberately as it scales up") — the house pattern, but this pair is close to verbatim.
- **[comics.md · Panel 4 image]** The tree metaphor stacks REACH foliage directly above the BREADTH canopy — two visually similar leafy layers whose labels do all the disambiguating work; DEPTH-as-roots lands well. Acceptable as shipped; noted in case the panel is ever regenerated.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (see Minor on length) |
| The three growth dimensions survive | met | index.md · Statement b2, Rationale ¶2, Figure 1; checklist.md §1 |
| The lifecycle survives | met | index.md · Statement b3, Rationale ¶1; checklist.md §2 |
| The on-ramp survives | met | index.md · Statement b4, Rationale ¶3; checklist.md §4 |
| The roadmap triage survives | met | index.md · Statement b5, Rationale ¶4–5, Figure 2; checklist.md §6 |
| Tiering and slicing survive | met | index.md · Statement b6, Rationale ¶6, Figure 3; checklist.md §8 |
| Credit is explicit | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes. Mandates appear only to be dismissed ("a mandated platform learns nothing"), which serves the voluntary-adoption premise rather than breaching the no-mandate-policy fence; the product-mode, implementation, and success-definition territory stays with the sibling records it is fenced to.
Drift: none — spec `accepted` stands.

## Cross-modality alignment

- **Facts & framing:** consistent — adoption over functionality, reach/breadth/depth, Explore → Expand → Extract, impact × fit triage with the four quadrant verbs, and tiers-and-slices-on-shared-assets appear identically everywhere.
- **Terminology:** consistent — "hockey-stick experience", "the initial cliff", "biased sample", "professional-services team for one account", "escape hatches" carry across article, checklist, and comic without renaming.
- **Voice & tone:** consistent first-person declarative; comic captions compress the article's own sentences.
- **Coverage parity:** even for the spec's beats. Checklist §5 (Platform Visualization) and §7 (Metrics & Adaptation) have no Rationale treatment, but the article's "How to Read This" explicitly names both as living in the Checklist tab — the parity gap is acknowledged, which is the right handling.

## Layer-by-layer notes

### Spec

- Tight contract: seven enumerable criteria, a logged framing decision ("adoption, not functionality" as the spine), and non-goals that fence against three sibling records plus mandate policy.
- Like its siblings, the criteria stay silent on two checklist sections (§5 Visualization, §7 Metrics); the article compensates by naming them in "How to Read This", so nothing dangles.

### index.md

- The best Rationale paragraphs in the set: "features are what we spend; adoption is what we earn" and the biased-sample argument give the record genuine analytical bite beyond the source checklist.
- The biased-sample paragraph quietly absorbs a metrics beat ("measure outcomes and customer experience rather than platform activity", checklist §7) — it fits the argument, but it is the one place two checklist concerns share a paragraph seam.
- All three figures exist on disk and are captioned; all five `[[…]]` cross-links resolve to existing posts; Figure 2's quadrant labels match the Statement's four triage verbs exactly.
- Highlight status DRAFT matches front-matter `status: draft:gray` and the Scope section.

### checklist.md

- Faithful and runnable: eight numbered sections plus a Final Review of eight questions that map cleanly onto the article's commitments.
- Terminology tracks the article throughout; the bolded **Explore/Expand/Extract** items make the lifecycle scannable inside the flat list.

### comics.md

- Eight panels, all image files present, captions run Panel 1–8, captions match alt text and (spot-checked) images; VERA/KAI cast consistent with the declared style.
- Beat selection mirrors the article (hook → feature victory lap → perfect-for-one-customer → dimensions → lifecycle → on-ramp → principled no → slices), with Panel 7's label as the only wrinkle (see Minor).

## Fixes applied (2026-08-13)

- comics.md · Panel 7 caption — fixed: label recast to "The discipline:" and the caption now leads with the article's actual cost line ("every request accepted is cohesion spent"); text-only edit, no image regeneration.
- index.md · highlight blockquote — fixed: trimmed without cutting elements — dropped the three dimension parentheticals (already defined in the Statement) and the third sub-clause of the first-hour sentence; all six load-bearing elements retained.
- index.md · front matter `excerpt` — fixed: lightly paraphrased the two near-verbatim highlight phrases ("its fate is set in a new user's first hour"; "tiers and slices give smaller customers an appropriately sized way in").
- comics.md · Panel 4 image — skipped: reviewer marked it acceptable as shipped, advisory only for a future regeneration; no image-content fix was flagged.
