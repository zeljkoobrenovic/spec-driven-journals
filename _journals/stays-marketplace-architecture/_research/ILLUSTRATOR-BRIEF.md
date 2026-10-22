# Illustrator Brief — BOOKED visual layer

You are adding the visual layer to pages of **BOOKED** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/`).

The author asked for the book to match its sibling books LISTED and RECONCILED, which use generated illustrations instead of mermaid. Your pages need two things:
- **(A)** Convert every mermaid diagram into a generated illustration, keeping its caption verbatim.
- **(B)** Add conceptual inline figures.

`GEMINI_API_KEY` is set in the environment. Never print it.

## Read first

1. The skill `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/SKILL.md`, for the placeholder format, asset paths and script usage.
2. The diagram converter `ROOT/_research/diagram-illustrations/mermaid_to_illustration.py`. Read its docstring and STYLE suffix.
3. One converted sibling figures file, as a model for prompts. Read `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/finance-systems-architecture/_research/diagram-illustrations/figs/20-payments-fundamentals.json`.
4. For each assigned page: its `index.md` (whole) and `spec.md`.

Scripts: `S=/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/scripts`. Each page's folder name is `<folder>`.

## Phase A — convert the mermaid diagrams (per page)

1. **Write the prompts.** Write `ROOT/_research/diagram-illustrations/figs/<folder>.json`: a list with one entry per mermaid block, in document order. Each entry is `{"id", "prompt", "alt", "visual_goal", "aspect_ratio"}`; the default aspect ratio is 16:9.
   - Each prompt redraws the diagram's *point* with **5–9 elements**, not every node. Give each element's position and a quoted label of 1–3 words, and name every arrow explicitly ("one arrow from 'Channel manager' into 'Connectivity gateway', labeled 'rate update'").
   - Describe only what should appear. Naming forbidden things makes the model draw them.
   - Avoid "column 1" or "step 2", which get drawn as numbers. Avoid label-like icon nouns.
   - Sequence diagrams become left-to-right swimlanes with a few labeled messages. State diagrams become a few rounded states with labeled arrows.
   - Use only labels and numbers that appear in the caption or diagram.
   - Ids are kebab-case and start with the page's folder number, e.g. `08-ari-push-path`.
2. **Convert.** Run `python3 ROOT/_research/diagram-illustrations/mermaid_to_illustration.py ROOT/posts/<folder>/index.md ROOT/_research/diagram-illustrations/figs/<folder>.json`.
3. **Generate.** Run `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md`, without `--replace`.
4. **Inspect every image** with the Read tool. Reject an image if it has:
   - a misspelled, garbled or extra label;
   - a wrong number;
   - a missing or misrouted arrow;
   - a logo or brand;
   - photorealism or clutter;
   - a meaning that contradicts the caption.

   To retry, improve the entry in the json, run the converter with `--update` (it rewrites still-pending placeholders), then regenerate that one image with `--only <id> --overwrite`. Allow at most 3 attempts. If an image is still wrong, simplify the prompt further, down to 4–5 elements.
5. **Replace and number.** Run `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md --replace --start-figure 1`. All of the page's figures were mermaid diagrams numbered 1..N, so the converted figures keep their numbers and the in-text references stay valid. Confirm that the page has no `begin mermaid` left and that its captions run 1..N.

## Phase B — conceptual figures (per page)

- **How many.** Add **2 figures per chapter** and **1 per part intro or preface page**. Add **none** to the toolkit, glossary, bibliography and domain-coverage pages.
- **What they show.** They are informational and conceptual, complementing (never redrawing) the diagrams. Draw from the chapter's central argument or its worked Corvane example. Good forms:
  - a metaphor that makes the core idea memorable (the perishable promise as melting ice, a calendar as a single key two hands reach for, a rate-plan thicket, a price that grows at each step of a staircase);
  - a before/after comparison;
  - a layered stack;
  - a decision landscape;
  - a lifecycle loop;
  - a Corvane scene that shows the problem concretely.
- **Placement and captions.** Insert placeholders in the skill's format after the paragraph or table each one serves. Each `caption` states the figure's point in one sentence and uses only numbers that appear in the chapter. Asset path: `assets/images/<folder>/<id>.jpeg`.
- **Prompt style.** End every prompt with: "Style: polished business explainer illustration, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels (0–6), spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos, brand marks, hotel-chain, travel-site, marketplace or vendor names; show booking platforms, channel managers, property systems and payment providers as generic unbranded components; never draw payment-card network symbols. Corvane people are generic professionals and guests; never real people."
- **Steps.**
  1. Validate: `python3 $S/extract_illustration_placeholders.py <index.md>`.
  2. Generate without `--replace`, then inspect and retry as in Phase A.
  3. Replace with `--replace --start-figure 101`.
  4. Renumber: `python3 ROOT/_research/tools/renumber_figures.py <index.md>`.
  5. Grep `**Figure` and confirm the numbers run 1..N with no gaps, and that every image's caption follows it directly.

## Finish each page

- Append to `spec.md` Changelog: `- **2026-10-21** — Visual layer: converted N mermaid diagrams to illustrations and added M conceptual figures (article-illustrator). *(AI-mediated session)*`
- Do not change prose, except figure-number references handled by the script.
- Do not touch other pages, `config.yaml` or the ledger. The front matter's `icon:` and `logo:` lines are set by another process; keep them.

## Verify at the end

- Build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. A transient OSError from a parallel build can be ignored if a rerun passes.
- Render check: `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`. Every page must print `OK`, with `mermaid=0`.
- Placeholders: `grep -l illustration-placeholder <index.md files>` must print nothing.

## Report back

Under 150 words: per page, the diagrams converted and the conceptual figures added; images regenerated or simplified; and any figure you had to drop.
