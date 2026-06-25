# Review: AI Is the Reactor, Not the Plant

**Reviewed:** 2026-06-25 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, summary.md, dialog.md, comics.md

## Verdict

Strong, publish-ready post. The analogy is disciplined — it earns its claims with
attributed, conservative facts and includes an explicit "Where the Analogy Breaks"
section, which is exactly the move that keeps it from becoming a slogan. Voice,
facts, and terminology are consistent across all four modalities. The single most
important thing to address is a minor conceptual seam: the article borrows the
IAEA's "three fundamental safety functions" to license its own *control / channel
/ contain* triad, but the middle term does not map cleanly — the IAEA's "remove
the heat" is a *safety/cooling* function, whereas the article's "channel" means
*convert heat into sellable electricity* (the turbine). The triad is good; the
citation that licenses it is slightly over-claimed. Nothing here blocks
publishing. (Comic panel images are not yet generated — `status: pending` — which
is expected, not a defect; noted under cross-modality so it isn't forgotten.)

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 3

### Blockers

None.

### Major

None.

### Minor

- **[index.md · "The Three Jobs of the Plant", line 56]** The article cites the
  IAEA's three fundamental safety functions ("control the reaction, remove the
  heat, confine the material") as mapping "cleanly" onto *control / channel /
  contain*. The mapping is clean for control and contain, but "remove the heat"
  (a safety function: stop the core melting) is not the same as the article's
  "channel" (an economic function: send heat to the turbine to make
  electricity). *Soften "map cleanly" to "echo" / "rhyme with", or note that the
  triad is the article's own framing that the IAEA functions loosely parallel —
  so the citation isn't carrying more than it should.*
- **[index.md · "Most of the Plant Is Not the Core", lines 41–44]** The cost
  bullets mix two source families (WNA 2020 percentages and the 1980 DOE
  breakdown) whose denominators differ — WNA is "% of total capital cost by
  activity," the DOE figures are "% of *direct* cost." Both are correctly
  attributed individually, but a careful reader could read the 28% and the
  15–20% as describing the same base. *One half-sentence noting the DOE figure is
  a share of direct cost would forestall the apples-to-oranges read.*
- **[summary.md / dialog.md · cost section]** The summary and dialog both carry
  the "~28%" and "15–20%" figures but drop the "direct cost" qualifier the index
  also omits — so the same minor ambiguity propagates. If the index is clarified,
  mirror it in both. *Low effort once index is fixed.*
- **[index.md · "Widening Out", line 90]** The society paragraph asserts that the
  hard part of nuclear's social acceptance "was never the physics of the core …
  it was regulation, operating discipline, liability, oversight, and public
  trust." This is plausible and on-theme but, unlike the engineering claims, is
  not backed by any cited source — it is the one historical assertion in the
  piece doing rhetorical work without support. *Either soften to a clearly
  framed observation ("arguably") or leave as is, but be aware it is the softest
  factual link in an otherwise well-sourced article.*

### Nits

- **[index.md · excerpt, line 7]** "Generative AI gives us raw power, the way a
  reactor core gives off heat." — the comma before "the way" is slightly heavy;
  reads fine without it. Cosmetic.
- **[dialog.md · "Most of the Plant Isn't the Core"]** "co-equal with the
  *buildings*" (italic emphasis) lands well spoken, but the index says "plant
  structures" — minor wording drift (buildings vs. structures). Harmless;
  flagging only for terminology tidiness.
- **[comics.md · panel 02 caption]** Caption uses an ellipsis inside the NRC
  quote ("the heat source... just like the boiler"). Correct, but the index
  quotes it in full without elision; trivial inconsistency in how the same quote
  is presented.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Sticky mental model (model = core, plant = value/work) | met | index KEY POINTS, Closing; summary lead; dialog throughout |
| Citable nuclear facts that most of a plant ≠ reactor | met | index "Most of the Plant Is Not the Core" (attributed) |
| Three jobs (control/channel/contain) mapped to AI | met | index "The Three Jobs of the Plant" table |
| Defense-in-depth mapped to AI (layers, not one guardrail) | met | index "Defense in Depth"; summary; dialog "No Single Guardrail" |
| Widens to org/society without forcing | met | index "Widening Out" with explicit structure-not-danger caveat |
| Explicitly names where the analogy breaks | met | index "Where the Analogy Breaks" (4-row table); dialog "Where It Breaks" |
| Concrete, actionable "what to do" | met | index "What to Do on Monday"; summary; dialog |
| Reader not left thinking models don't matter / AI as physically dangerous | met | "Where the Analogy Breaks" row 1 + 4; widening caveat |

All eight success criteria met. **Non-goals respected:** yes — no nuclear
tutorial, no literal-meltdown claim (explicitly negated), no specific toolchain
push, no x-risk argument, no universal cost percentage (figures attributed). The
refuted "~80% EPC" figure is absent everywhere, per the spec's decision log.
**Drift:** none. Spec `status: accepted` is accurate; no change recommended.

## Cross-modality alignment

- **Facts & framing:** Consistent. Core-as-heat-source, the cost-minority point,
  the three jobs, defense-in-depth, and the four break-points appear in all
  modalities with the same numbers and the same NRC/WNA/IAEA/DOE attributions.
  The cost-base ambiguity (above) is shared, not contradictory.
- **Terminology:** Consistent. "Reactor/core," "the plant," "control / channel /
  contain," "throttle," and "defense in depth" are used the same way throughout.
  One trivial drift: "structures" (index) vs. "buildings" (dialog).
- **Voice & tone:** Consistent and on-journal. Declarative article; tight
  summary; the dialog keeps Ana (advocate) and Ben (skeptic) distinct and uses
  Ben to surface the analogy's limits, which is well-judged. Cast (Maya/Rex) in
  the comic matches the journal's existing comics.
- **Coverage parity:** Even. Every load-bearing beat in `index` is carried,
  appropriately compressed, by summary, dialog, and comic. No modality
  introduces a major beat the others lack. **Note (not a defect):** all eight
  `comic-panel` blocks are `status: pending` — panel images are not yet
  generated, so the Comic tab will show no images until
  `generate_comic_panels.py` is run with a `GEMINI_API_KEY`.

## Layer-by-layer notes

### Spec
- Follows the template; Success criteria are concrete and checkable (each maps to
  a verifiable spot in the post). Decision log is unusually strong — it records
  the research-driven choices (dropping the 80% figure, scoping the danger claim)
  that are the post's main integrity guarantees.
- Slightly long, but justified: most of the length is the Sources block, which is
  doing real work (it is the audit trail for every nuclear claim). Not bloat.

### index.md
- Clean house shape: KEY POINTS (exactly three bullets), MADR-ish flow, contrast
  tables, Title-Case headings, resolving cross-links, "Monday"/"Closing"/"Probe"/
  "Questions" closers. Reads in one pass.
- The two genuinely smart moves are the "Where the Analogy Breaks" table and the
  structure-not-danger caveat in the widening section — they pre-empt the
  predictable misreadings.
- Two soft spots: the IAEA-functions citation over-licenses the triad (minor #1),
  and the society paragraph is the one unsourced historical claim (minor #4).

### summary.md
- Genuinely short, leads with the answer, mirrors the index's structure without
  copying its sentences. Keeps the "where it breaks" caveat, which a lesser
  summary would drop — good for a leader audience.

### dialog.md
- Sounds spoken; the two voices carry real positions rather than narrator-with-
  names. Ben's pushback ("somebody walks out saying AI is going to melt down") is
  the best vehicle in the whole post for the limits section. Covers every
  load-bearing beat without lecturing.

### comics.md
- Eight panels, one idea each, captions short and matched to alt text; visual
  metaphor (glowing core → full plant) is consistent and tracks the argument arc.
  Panel 7 ("NOT a bomb") cleverly carries the limits beat visually.
- All panels `status: pending`; `--dry-run` validates cleanly. Generate images
  before relying on the Comic tab.

*No build was run — nothing rendered changed. One non-blocking build-relevant
note: the Comic tab has no images until panels are generated.*
