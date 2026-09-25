# Part overviews re-rendered as compact landscape figures (24 September 2026)

**Request:** the stacked 9:16 chapter overviews in the Part II, V, VI, VII and VIII introductions rendered at the full content width of the page with lettering far larger than the surrounding prose. Regenerate them in the style of the compact landscape overviews the author kept for Parts I, III and IV.

**Driver:** `regen-part-overviews-landscape-20260924.py` (one run, `gemini-3-pro-image-preview`, 4:3, style block copied from `regen-part-4-overview-20260924-r4.py`). Every card title, explanation, connector and banner of the accepted stacked versions was kept; only the arrangement changed: cards in rows inside labelled bands, band labels beside or above the cards, ochre banner across the bottom.

| Part | Layout now | Previous render archived as |
| --- | --- | --- |
| II ALIGN | three cards in a row with two arrows and the "Revisit the arrangements" return arrow above; one wide "Build shared evidence" foundation slab beneath with three connectors | `discarded-illustration-variants/part-2-intro-chapter-overview-158d19ae23a7.jpeg` |
| V SCALE | three bands separated by ochre rules: three team cards in a row (one arrow between the first two), one systems card, one boundary card | `…/part-5-intro-chapter-overview-cd4065a4f10b.jpeg` |
| VI SUSTAIN | one debt card under "The estate on three columns: cost, risk and speed"; ochre rule; three independent cards in a row under "Three applications of the same method" | `…/part-6-intro-chapter-overview-03b05027d791.jpeg` |
| VII LEAD | one-line band label, three cards in a row with two arrows | `…/part-7-intro-chapter-overview-11481811337b.jpeg` |
| VIII LEARN | four case cards in a row under a bracket, the reading-method line written horizontally, the ochre-edged closing card, banner | `…/part-8-intro-chapter-overview-fdb4b533c8cb.jpeg` |

All five renders are 1200 × 896 and were read against their prompts: every label spelled as supplied, no extra words, no stray connectors.

**Article edits:** Figure 1 alt text in the five `part-N-intro/index.md` files now describes rows instead of a stacked column (Part V's alt text was already layout-neutral and is unchanged in substance). The "[Open diagram at full size]" links that Parts II and VII carried for the stacked versions were removed, matching Parts I, III and IV; the renderer still wraps every figure in a full-size link.

**Verification:** `python3 _wiring/build.py` printed `[built] private-techuity`; the five `docs/private-techuity/assets/images/part-N-intro/chapter-overview.jpeg` files are byte-identical to the sources and each `part-N.html` references its figure once. Manuscript re-exported with the manifest's recorded options (`--jpeg-quality 85`, `--site-url https://zeljkoobrenovic.github.io/spec-driven-journals`, `--max-manuscript-mb 60` as in the previous rounds, since the manuscript already stood at 47 MB before this change); `validate_manuscript.py` prints `[valid]` (48.34 MB total; the five exported overviews are 1200 × 896).

The 22 September record `part-overview-images-20260922.json` describes the stacked layouts of its date and is left as is.
