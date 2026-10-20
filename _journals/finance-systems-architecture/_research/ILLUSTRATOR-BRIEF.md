# Illustrator Brief — RECONCILED inline figures

You are adding inline article figures to pages of **RECONCILED: Architecting Finance Systems** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/finance-systems-architecture/`). The user explicitly asked to **illustrate the articles and generate the images** (`GEMINI_API_KEY` is set in the environment — never print it).

## Read first

1. The skill: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/SKILL.md` — follow its placeholder format, contract rules and asset paths exactly (with the overrides below).
2. For each assigned page: its `index.md` (whole) and `spec.md`. Note the existing `**Figure N:**` figures so you do not duplicate them.

## What to add

- **2 figures per page** (3 only if the chapter is long and a third clearly earns its place; the preface pages may take 2). Placed after the paragraph/table they serve.
- Figures must be **informational and conceptual**, complementing (never redrawing) the existing diagram figures: e.g., a metaphor that makes the chapter's core idea memorable (the volume gradient as a funnel, suspense as sediment, a clean core as a sealed engine with extension ports), a before/after comparison, a layered stack, a decision landscape, a lifecycle loop, a risk/control matrix, a Northmere scene that shows the chapter's problem concretely. Prefer the chapter's central argument and its worked Northmere example.
- Each placeholder's `caption` states the point of the figure in one sentence, consistent with the chapter's facts and numbers (use only numbers that appear in the chapter).

## Visual style (all prompts)

Match the book's header images: "polished business explainer illustration, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins". Labels: few, short, generic, correctly spelled (prefer 0–6 short labels). Always append to every prompt: "No photorealism, no 3D render, no dense text, no title text. Do not draw any company logos, brand marks, trademarks or vendor product names; show ERP systems, payment providers and SaaS tools as generic unbranded components; never draw payment-card network symbols." Northmere characters (if shown) are generic professionals — never real people. Aspect ratio 16:9 by default; 1:1 for compact concept figures.

## Generation procedure (per page)

Script dir: `S=/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/scripts`

1. Insert the placeholders; validate: `python3 $S/extract_illustration_placeholders.py <index.md>`.
2. Dry run: `python3 $S/generate_illustrations_nanobanana.py <index.md> --dry-run --print-prompts`.
3. Generate images **without** `--replace`: `python3 $S/generate_illustrations_nanobanana.py <index.md>` (check `--help` for the exact flags; if it needs a flag to only generate, use it).
4. **Inspect every generated image** with the Read tool. Reject and regenerate (`--only <id> --overwrite`, after improving the prompt) any image with: misspelled or garbled text, a brand/logo/card-network mark, wrong numbers, photorealism, clutter, or a meaning that contradicts the caption. Max 2 retries per image; if still poor, remove that placeholder.
5. Replace placeholders with figures, using temporary high numbers: `python3 $S/generate_illustrations_nanobanana.py <index.md> --replace --start-figure 101` (it must not regenerate existing files; confirm).
6. Renumber all figures in document order and fix prose references: `python3 ROOT/_research/renumber_figures.py <index.md>`. Then grep the page for `**Figure` and confirm numbers run 1..N without gaps and every image's caption follows it directly.
7. Append to the page's `spec.md` Changelog (the user asked for the illustration; this is the one spec edit allowed): `- **2026-10-18** — Added N inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*`

Do NOT touch other pages, `config.yaml`, or the scenario ledger. Do not change prose except figure-number references handled by the script.

## Verify at the end

`cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient error from parallel builds in another journal can be ignored if a rerun passes), then `python3.11 /private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/d17de6c1-27df-4ac8-963a-4f42cb16c093/scratchpad/render_check.py <permalinks...>` — all OK — and confirm no `illustration-placeholder` remains: `grep -l illustration-placeholder <index.md files>` must print nothing.

## Report back

Under 120 words: per page, the figures added (id + one-line purpose), images regenerated or dropped, and any problem.

## Diagram figures (added 20 Oct 2026)

The book's former mermaid diagrams are now generated illustrations. To draw a new diagram, write a placeholder whose prompt simplifies to the 5–9 elements that carry the caption's point, gives each element's position and quoted 1–3 word label, and names every arrow ("one arrow from 'A' into 'B'"). Describe only what should appear (naming forbidden things makes the model draw them); avoid "column 1"/"step 2" (drawn as numbers) and label-like icon nouns such as "a statement document" (drawn as labels). The converter with the shared style suffix is `_research/diagram-illustrations/mermaid_to_illustration.py` (`--update` rewrites a pending placeholder's prompt for a retry); the prompts behind every diagram figure are archived per page in `_research/diagram-illustrations/figs/<folder>.json` (the `*-fallback.json` files hold the final prompt for chapters 32 and 33's hardest diagrams).
