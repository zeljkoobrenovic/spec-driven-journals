# Review: Thriving in Different Environments

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready after one trim. The "no context-free great engineer" frame is the
strongest single idea in this four-post batch, the checklist is an exact
faithful reproduction of the source PDF (verified against
`Checklist_ TSEG _ Different Environments (1).pdf`), and the comic compresses
the argument well. The one real quality problem is that the universal set is
enumerated in full twice in the article (plus a shortened third pass in the
highlight) — the Rationale's re-listing should be cut down to its *why*.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Blockers

- None.

### Major

- **[index.md · Statement bullet 5 + Rationale ¶5]** The universal set is listed
  in full twice: Statement bullet 5 gives all seven items, and Rationale ¶5
  ("The universal set is what survives…") re-lists six of the seven nearly
  verbatim — after the highlight has already run a four-item version. The
  Rationale paragraph's real content is the *why* ("careers are long and
  environments are temporary; the colleagues you helped … follow you"). *Keep
  the why, gesture at "the invariants", and let Statement bullet 5 own the
  enumeration.*

### Minor

- **[index.md · Statement bullet 1]** A 75-word dual-scenario bullet packing the
  full product-team and platform-team behavior sets into one sentence pair —
  the heaviest bullet in the batch. *Split into two bullets (or sub-bullets),
  matching how the checklist and Figure 1 already separate the two.*
- **[index.md · Rationale ¶3, last sentence]** "The source's recognition signs
  (…) are precisely the instruments I point engineers at — and in wartime I add
  its warning explicitly: …" — the antecedent of "its" (the source) sits three
  clauses back, and the sentence carries two colons' worth of content. *Split
  after "instruments I point engineers at."*

### Nits

- **[comics.md · Panel 5]** The caption's "the customer holds a phone" detail is
  not in the alt text ("talks with an end user … hands a feedback card") —
  align caption and alt so both describe the same image.
- **[index.md · What This Means in Practice, row 2]** "Wartime is permanent or
  free" is a compressed double negation that takes a second read as a
  does-not-say entry — "Wartime is permanent, or costless" (or splitting the
  two) reads cleaner.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Team types survive | met | index.md · Statement bullet 1, Rationale ¶2; checklist.md · §1 |
| Wartime/peacetime survives | met | index.md · Statement bullets 2–3, Rationale ¶3; checklist.md · §2–3 (incl. wartime stress/burnout and peacetime stagnation) |
| Company types survive | met | index.md · Statement bullet 4, Rationale ¶4; checklist.md · §4 |
| Universal set survives | met | index.md · Statement bullet 5, Rationale ¶5; checklist.md · §5 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — the record never turns wartime/peacetime into
executive doctrine (it stays a read-and-adapt skill), and environment choice
vs. environment adaptation is kept on the right side of the
[[engineering-career-paths]] fence. All `[[…]]` targets resolve
(engineering-career-paths, changing-jobs, own-your-career, promotions,
managing-downturn — all in this journal).

Drift: none — spec `accepted` stands; the reassess-on-shift beat the Intent's
universal set names is carried by Statement bullet 6 and checklist §5.

## Cross-modality alignment

- **Facts & framing:** consistent — the wartime/peacetime signs, the
  product/platform instinct split, the three company-type visibility games, and
  the universal set match across article, checklist, and comic; the article's
  wartime warning (stress, uncertain stability) is carried by comic panel 7.
- **Terminology:** consistent — "mode", "instruments" (Figure 2 and comic panel
  6 share the dial-and-gauges metaphor), "playing the previous game",
  "universal set" travel intact.
- **Voice & tone:** consistent — manager's voice in the article, engineer's
  first person in the checklist, per the spec's Audience section.
- **Coverage parity:** even — every Statement beat lands in the checklist; the
  checklist's few extra items (e.g. platform "balance deep focus with urgency")
  are appropriate compression casualties in the article, not gaps.

## Layer-by-layer notes

### Spec

- Tight contract: five substantive criteria that partition the chapter cleanly;
  the "not executive doctrine" non-goal is a smart fence given the
  wartime/peacetime material's usual usage.
- Decision log records the framing decision (lead with reading, end with the
  universal set) that the article visibly follows.

### index.md

- House shape fully observed; "Most 'underperformance' I've seen was a context
  mismatch, not a skill gap" is an excellent opening rationale and the post's
  best line.
- The Rationale's five paragraphs map onto the Statement's beats in order;
  Figure 2 (instrument panel) is the strongest figure in the batch and is
  reused coherently by the comic.
- All three figures exist on disk and are captioned.

### checklist.md

- Verified against the source PDF: sections 1–5 reproduced essentially verbatim
  (the PDF is already in the first person), with bold sub-headings
  (product/platform, wartime/peacetime signs, company types) preserved.
  Task-list markdown is well formed; numbering matches the PDF.

### comics.md

- Eight panels, all image files present under
  `assets/images/thriving-in-different-environments/`; the
  same-work-different-verdict hook (panel 1) is a strong visual translation of
  the principle, and panel 3 (polishing while the building burns) compresses
  "playing the previous game" perfectly.
- One caption/alt mismatch (panel 5, nit above); otherwise captions match
  images and the article's terminology.

## Fixes applied (2026-07-29)

- **Major (duplicate enumeration of the universal set)** — Rationale ¶5 no longer re-lists the universal set; it now gestures at "invariants that hold in every environment" and keeps the why (long careers, temporary environments, colleagues and bridges follow you). Statement bullet 5 owns the full enumeration.
- **Comic caption fix** — Panel 5 caption aligned with the alt text/image: "the customer is an end user" (was "the customer holds a phone", a detail not in the drawn panel).
