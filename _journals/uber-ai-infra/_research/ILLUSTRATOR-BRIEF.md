# Illustrator Brief — RETROFITTED inline figures (staging phase)

You are staging inline article figures for pages of **RETROFITTED** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/uber-ai-infra/`). The user asked for the full visual layer. In this phase you **stage placeholders only** — the Gemini key is not available yet; generation happens in a later phase.

## Read first

1. The skill: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/SKILL.md` — follow its placeholder format, contract rules and asset paths exactly. The `<post-slug>` in asset paths is the **post folder name** (e.g. `assets/images/12-minion/<id>.jpeg`).
2. For each assigned page: its `index.md` (whole) and `spec.md`. Note the existing `**Figure N:**` mermaid diagrams so you do not duplicate them.

## What to add

- **2 figures per chapter** (3 only if the chapter is long and a third clearly earns its place). Placed right after the paragraph/table they serve.
- Figures are **informational and conceptual**, complementing (never redrawing) the mermaid diagrams: a metaphor that makes the chapter's core idea memorable (e.g. the harness as a thin roof on a deep foundation; a gateway as a single checked door; skills as a curated library; a context graph as a city map an agent navigates; spend tiers as a staircase with a manager's gate; capture-replay as a recording studio; review risk as triage lanes), a before/after comparison, a layered stack, a lifecycle loop, a control matrix, a scene that shows the chapter's problem concretely (an engineer juggling parallel agent sessions; a CI queue overflowing).
- Each placeholder's `caption` states the point of the figure in one sentence, consistent with the chapter (use only numbers that appear in the chapter, attributed the same way).

## Visual style (all prompts)

"Polished technical explainer illustration, flat vector style, crisp outlines, minimal shading, light warm-white background, disciplined palette of deep indigo, teal and amber accents, generous margins." Labels: few, short, generic, correctly spelled (prefer 0–6 short labels of one to three words). Always append to every prompt: "No photorealism, no 3D render, no dense text, no title text. Do not draw any company logos, brand marks or trademarks — no Uber logo or wordmark, no vendor or product logos (Anthropic, OpenAI, Claude, GitHub, Slack, Google, Jira, Kubernetes); show tools, models and services as generic unbranded components. No real people; people are generic engineers." Aspect ratio 16:9 by default; 1:1 for compact concept figures. Do not depict Uber's actual UI screens.

## Staging procedure (per page)

Script dir: `S=/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/.claude/skills/article-illustrator/scripts`

1. Insert the placeholders (`"status": "pending"`).
2. Validate: `python3 $S/extract_illustration_placeholders.py <index.md>`.
3. Dry run: `python3 $S/generate_illustrations_nanobanana.py <index.md> --dry-run --print-prompts` — confirm discovery.

Do NOT call the generator without `--dry-run`. Do NOT touch other pages, specs, `config.yaml` or the ledger. Do not change prose.

The page will temporarily render the placeholder as an HTML comment (invisible) — that is fine.

## Report back

Under 100 words: per page, the placeholder ids and one-line purposes.
