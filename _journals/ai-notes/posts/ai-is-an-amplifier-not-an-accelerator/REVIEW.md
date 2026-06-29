# Review: AI Is an Amplifier, Not an Accelerator

**Reviewed:** 2026-06-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, summary.md, dialog.md

> **Expansion (2026-06-29, later same session):** Added a systems/friction
> strand at the author's request — two new article sections ("It Amplifies the
> Bottleneck", "Why Your Team Didn't Get Faster"), grounded in the Theory of
> Constraints, DORA 2024 (individual-vs-system gap), CircleCI feature-vs-main
> throughput, and Brooks's Law. Propagated to all modalities (summary bullets,
> a two-segment dialog addition, a new comic panel → 9-panel strip) and the KEY
> POINTS / Monday-moves / Closing / sources / questions. A fresh post-review pass
> is warranted on the expanded post; the verdict below predates the expansion.
>
> **Post-review actions taken (2026-06-29, earlier same session):**
> - Applied the two flagged minor fixes: moved the "directional, not decimal"
>   hedge ahead of the cost figures in `index.md`; varied Ben's third skeptic
>   beat in `dialog.md` (now concedes the number and pushes on implication).
> - Added `comics.md` — an 8-panel explainer comic built on the sign-preserving
>   multiplier gag (cast Maya + Rex, consistent with the reactor comic). Spec
>   updated: comics now a checked modality; status `draft → accepted`.
> - Added a restrained bold-highlighter skim path to `index.md`.
> - Commented out `icon`/`logo` front matter (images not yet generated) so no
>   broken images render; left a TODO.
> - **Still open:** 4 inline figures + 8 comic panels staged as placeholders,
>   awaiting `GEMINI_API_KEY` to generate. Hero logo + icon likewise.

## Verdict

Strong, publish-ready post. The thesis is sharp and falsifiable (the
multiplier-vs-adder / sign-preservation framing earns its keep instead of being
a slogan), the evidence is well-chosen and load-bearing where it should be, and
the three modalities agree on every fact and frame. It hits all eight spec
success criteria. The single most important thing to address before calling it
done is operational, not editorial: **four inline figures are staged as
placeholders but not yet generated** (no `GEMINI_API_KEY` was available), so the
Article tab currently renders with no figures and no visible captions. Generate
them (or remove the placeholders) before publishing. Everything else is minor
polish.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 3

### Blockers

- None. (The unrendered figures are tracked below as a build/asset task, not a
  content blocker — the page renders cleanly without them because the
  placeholders are inert HTML comments.)

### Minor

- **[index.md · figures]** Four `illustration-placeholder` blocks are staged but
  the images are not generated, so the article ships with zero figures despite
  the prose being written to be figure-supported. Not breaking, but the post is
  visually flatter than intended. *Generate via the article-illustrator script
  with `--start-figure 1`, then rebuild.*
- **[index.md · "It Amplifies Cost"]** The cost section leans on the most
  vendor-sourced numbers in the piece (1.7× issues, 8×, 4×). The text does hedge
  ("directional, not decimal"), which is correct — but the hedge appears *after*
  the numbers. Consider leading the paragraph with the hedge so a skim reader
  doesn't carry away the figures as settled. *One clause moved earlier.*
- **[dialog.md · cost beat]** Ben's "Those are vendor-ish figures" and Ana's
  "several are, which is why I say directional" is good, but it's the third time
  the dialog stages a "give me a number / I'm skeptical" exchange (speed, then
  cost). The skeptic's move is slightly formulaic by the third use. *Vary Ben's
  angle once — e.g. have him concede a number and push on implication instead.*
- **[index.md · length]** At ~15 min it is on the long side for the journal,
  largely because four axes each get a full treatment. This is defensible (the
  spec chose four axes deliberately) but the Quality section is the thinnest and
  could fold into the cost or organization section if a trim is ever wanted.
  *Optional; no action required.*

### Nits

- **[index.md · "It Amplifies Quality — and Slop"]** Two `[[risc-...]]` and
  `[[ai-is-the-reactor-...]]` links land in one short paragraph; reads slightly
  link-dense. *Optional: move one to "To Probe Further" only.*
- **[summary.md · em-dash density]** Several em-dash asides in consecutive
  bullets; fine, but one could become a comma. *Trivial.*
- **[dialog.md · "twenty-three percent"]** Article says "23.5%"; dialog rounds to
  "twenty-three percent." Acceptable spoken rounding, but flag for awareness — if
  exactness matters, say "about twenty-three and a half." *Trivial.*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Sticky model: multiplier not adder, input can be negative | met | index KEY POINTS + "A Multiplier, Not an Adder" + Closing; summary lead; dialog cold open |
| Why "accelerator" is wrong (additive/positive vs multiplicative/signed) | met | index "The Wrong Word"; dialog "The Wrong Word" |
| Speed cuts both ways, cited (METR −19%/+20%, juniors vs seniors, jagged frontier) | met | index "It Amplifies Speed" + table; dialog "The Speed Story Cuts Both Ways" |
| Cost cuts both ways (cheap to generate, expensive to own) | met | index "It Amplifies Cost" + table; summary "What changes"; dialog cost beat |
| Quality + org set by input; DORA amplifier finding | met | index Quality + Organizations sections; dialog DORA beat; summary bullet |
| Metaphor limits named (adds new capability; jagged gain) | met | index "Where the Metaphor Breaks"; dialog "Where It Breaks" |
| Concrete "what to do" following from the model | met | index "What to Do on Monday" table; summary "What changes"; dialog closer |
| Not anti-AI / a verdict | met | index lead + Closing; summary "What we are not doing"; dialog final turn |

Non-goals respected: **yes.** Not hype/doom (stays a model correction); not a lit
review (studies serve the idea); concedes AI adds new capability and gain is
jagged; references rather than duplicates [[ai-is-the-reactor-not-the-plant]]
(explicitly framed as the "static companion / dynamic twin"); cost figures
attributed and hedged, not treated as constants.

Drift: **none.** Post and spec agree. Recommend the spec move `status: draft →
accepted` and `revised:` stay 2026-06-29. (Author's call; this skill does not
edit the spec.)

## Cross-modality alignment

- **Facts & framing:** consistent. Every load-bearing number matches across
  index/summary/dialog (19%/20%, 27–39%, 8–13%, 12.2%, 25.1%, 1.7×, ~23.5%, 8×,
  90%, 4×, seven profiles). The dialog spells numbers as words; values identical.
- **Terminology:** consistent. "Multiplier, not an adder," "gain × input," "sign,"
  "amplify what?", "cheap to generate, expensive to own," "jagged frontier,"
  "the input" all used the same way in all three.
- **Voice & tone:** consistent declarative register; the dialog is audibly
  spoken (Ben blunt, Ana defends) without becoming prose-with-names. Summary is
  appropriately terse and leader-facing.
- **Coverage parity:** even. All four axes (speed, cost, quality, organization),
  the limits, and the Monday moves appear in index and dialog; summary carries
  speed + cost + quality + org as compressed bullets, which is the right
  compression for its form. No modality introduces a beat the others lack.

## Layer-by-layer notes

### Spec
- Follows the template; adds a Structure section that genuinely earns its place
  (the nine-section order is a real decision). Success criteria are checkable and
  non-overlapping. Decision log captures rejected alternatives (looser framing,
  single-software focus, pure org essay). Not bloated.
- One Open question (ship comics?) is genuinely deferred, not a dangling resolved
  note — correct use.

### index.md
- House shape is right: KEY POINTS (exactly three bullets) → `<br>` → lead, then
  MADR-ish body, contrast tables, Monday-moves table, Closing, To Probe Further,
  Questions to Consider. All headings Title Case.
- The arithmetic spine (`output = gain × input`, sign preserved) is the post's
  best move — it converts a slogan into a testable claim and the whole body pays
  it off. The Engelbart/Jobs lineage grounds it without padding.
- Strongest evidence (METR, Copilot RCTs, BCG-HBS, DORA) is load-bearing; the
  debt cluster is correctly demoted to "directional colour."
- Four contrast tables is a lot of tables; they read well in HTML and each is
  distinct, so this is a feature, not a flaw — noted only for awareness.

### summary.md
- Within target length, leads with the decision ("AI is not an accelerator… it is
  an amplifier"), and the What changes / What it costs / What we are not doing
  shape maps cleanly to the spec. A leader who stops after the first paragraph
  still has the thesis.

### dialog.md
- Two voices stay distinct; Ben raises the *real* objections (it's a word game;
  maybe they were bad at the tools; those are vendor figures; steelman against
  yourself) and Ana answers from the article's reasoning. Sounds spoken.
- The "skeptic asks for a number" beat recurs; vary it once (see Minor).
- Lands the Non-goals in the final turn ("not saying AI is overrated… a
  correction to the mental model"), matching the spec.
