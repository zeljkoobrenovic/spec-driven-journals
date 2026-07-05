# Review: You Can Outsource Thinking. You Cannot Outsource Understanding.

**Reviewed:** 2026-07-05 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, summary.md, dialog.md

## Verdict

Publish-ready. The post lands its thesis cleanly, the thinking/understanding
distinction is held consistently across all three modalities, and every
load-bearing claim is attributed to a real, well-chosen source. The single
outstanding item is not editorial: the three inline figures are still
placeholders and need image generation before publish (same staging pattern the
amplifier post used). No blockers in the prose; a handful of minor polish notes.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · figures]** All three figures (`diverging-curves`,
  `last-human-mile`, `naive-to-evolved-staircase`) are placeholder refs; the
  `assets/images/.../` files don't exist yet. Not a prose problem — run
  image generation (article-illustrator / `generate_logos.py`) before publish.
  The logo hero is also referenced but not yet generated.
- **[index.md · "The Cost of Outsourcing Understanding"]** This section leans on
  four studies in close succession (Bainbridge, Microsoft/CMU, Anthropic, MIT).
  It's well-hedged, but it's the densest evidence stretch in the piece; a reader
  skimming could lose the thread. Considered acceptable — each study is doing
  distinct work — but it is the section most likely to feel like a list.
- **[summary.md · Karpathy quote]** The summary reuses the full Karpathy quote
  verbatim from the article and KEY POINTS. Fine for a standalone tab, but it's
  the one phrase repeated in all three modalities; intentional (it's the anchor),
  noted for awareness, not a fix.

### Nits

- **[index.md · em-dash density]** A few paragraphs stack multiple em-dashes
  (house voice, matches the amplifier/reactor posts, so left as-is).
- **[dialog.md · "*(laughs)*"]** One stage direction, within the skill's
  "sparingly" guidance. Fine.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| State the core distinction + why in one line | met | index KEY POINTS; summary opening; dialog "The Line" |
| Central asymmetry (AI improves; humans stay) relocates the bottleneck | met | index "AI Improves. You Stay the Same."; dialog "AI Improves, You Don't" |
| Distinguish thinking vs. understanding (Searle/Polanyi/Naur) | met | index "Thinking Is Not Understanding" + contrast table |
| The "last human mile"; value at point of use (Levitt) | met | index "Understanding Is Where the Artifact Meets Reality" |
| Cost of confusing them — comprehension debt / offloading | met | index "The Cost of Outsourcing Understanding" |
| Concrete method: re-derive naive→improved (system-design example) | met | index "Manufacturing Understanding"; dialog "How You Actually Get Understanding" |
| Reader does NOT read it as anti-AI | met | index Closing + Monday intro; summary "What we are not doing"; dialog "What This Isn't" |

Non-goals respected: yes. Not AI-doom (explicit disclaimers in all three
modalities); not a reactor/amplifier re-run (positioned as the *epistemic*
companion, cross-linked not duplicated); not a philosophy paper (Searle/Polanyi/
Naur serve the practical point); not a pitch for the side project (used as one
worked example, framed as "a little side project"); numbers attributed and
hedged (MIT preprint flagged, METR/Anthropic flagged as preprints).

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent. Same studies, same numbers (7-month doubling,
  17% comprehension drop, 319 workers), same Karpathy anchor, same Naur keystone
  across article, summary, and dialog. No modality introduces a claim absent from
  the others or the spec.
- **Terminology:** consistent. "Last human mile," "comprehension debt," "legacy
  on arrival," "re-derive, don't consume," "the bottleneck moves" all used the
  same way in every modality.
- **Voice & tone:** consistent with the journal. Ana/Ben cast matches the other
  ai-notes dialogs; article register matches reactor/amplifier.
- **Coverage parity:** even. Every load-bearing beat in `index` appears,
  compressed, in summary and dialog. The re-derivation method and the
  system-design example — the constructive heart — carry through all three.

## Layer-by-layer notes

### Spec
- Clean contract: checkable Success criteria, Non-goals that actively fence the
  piece, a Decision log that captures rejected alternatives. Sources finalized
  against research with credibility flags. Not bloated relative to the post.

### index.md
- Strong arc: distinction → asymmetry (why now) → mechanism (why it can't be
  handed over) → where value lands → the two things to understand → the cost →
  the method → Monday → close. Each section hands off cleanly.
- The Naur "legacy on arrival" section is the strongest beat and correctly the
  most developed.
- Title Case headings throughout; six `[[…]]` cross-links, all resolving.

### summary.md
- 443 words, within target. Leads with the distinction, then asymmetry, then the
  four "what changes" moves. A leader who stops after the first two sentences has
  the direction. "What it costs" / "What we are not doing" both present.

### dialog.md
- 1,889 words, within target. Ben carries real skepticism ("isn't the
  understanding included?", "that's forty years old and about factories", "this
  sounds like 'AI makes us stupid'"); Ana answers from the article's rationale.
  Sounds spoken. Covers every load-bearing beat without lecturing.

## Notes for publish

1. Generate the logo hero and the three inline figures, then rebuild.
2. Optionally add an icon (`generate_icons.py`) — the card icon ref is staged.
3. Consider the `comics` modality (deferred in spec) only if the visual gag
   earns it; the naive→evolved staircase is the natural candidate.
