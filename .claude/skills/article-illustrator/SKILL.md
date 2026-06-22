---
name: article-illustrator
description: Add inline illustrations to a post's main article (index.md) — propose 2–5 figure placeholders where a visual aids comprehension, generate Gemini/Nano-Banana images for them, and replace each placeholder with a markdown image + numbered caption. Complementary to the explainer-comics modality (this illustrates the article body; comics is its own tab). Use when asked to illustrate, add figures/diagrams/images to, or stage illustration placeholders for a post's article in _journals/*/posts/*/index.md.
---

# Article Illustrator (inline figures in `index.md`)

## Goal

Add **inline article figures** to a post's `index.md` — the images that sit
between paragraphs with a `**Figure N:**` caption — and generate them from
Gemini. This is the article-body illustration path: it improves the detailed
article itself, distinct from the standalone visual modalities.

Where this sits among the visuals:

- **This skill** — figures embedded *in* `index.md`, illustrating specific
  passages. They render on the Article tab inline with the prose.
- **`explainer-comics`** (`comics.md`) — a separate Comic *tab*: a 6–10 panel
  narrative walk, not tied to specific article paragraphs.
- **Hero logo** (`logo:` front matter) — the single top-of-post image, handled
  by `_wiring/generate_logos.py`, **not** this skill.

The three are complementary; a post can have all three. When illustrating an
article that already ships a comic, keep the figures *informational* (diagrams,
maps, comparisons) and let the comic carry the *emotional/narrative* register, so
the two do not duplicate each other.

## Contract rules

- **`spec.md` is the contract** (when present). Figures must serve the spec's
  Intent and Audience and must not breach its Non-goals. **Never edit `spec.md`
  from this skill.** For a private reflective post, that means quiet, metaphor-
  first figures — never literal depictions the post's Non-goals fence off
  (e.g. real family members).
- **Edit only `index.md`** (and write image files under the post's `assets/`).
  Do not touch other modality files, `config.yaml`, or the spec.
- **Two-step, opt-in generation.** Inserting placeholders and generating images
  are separate. **Never call the Gemini generator unless the user explicitly
  asks to generate** — staging placeholders is the safe default.
- **Continue existing figure numbering.** Many posts already have `**Figure 1:**`
  etc. New figures continue the sequence; never restart at 1 or collide.
- `permalink:` and `id:` front matter never change.

## Workflow

1. Read the target `index.md`, its sibling `spec.md` if present, and `comics.md`
   if present (to avoid duplicating what the comic already shows). Skim a
   neighboring post only if you need the journal's visual register.
2. Identify **2–5** places where a visual *materially* improves comprehension —
   diagrams, maps, comparisons, flows, conceptual figures. Skip decorative images
   and anything that just restates a table.
3. Insert one `illustration-placeholder` block (format below) immediately after
   the paragraph, table, or heading it illustrates. Keep the JSON valid.
4. **Stop here unless the user asked to generate.** Report the staged
   placeholders and let them review the prompts first.
5. **When generating:** run the bundled generator with `--dry-run --print-prompts`
   first to confirm discovery and prompts. Then run it with `GEMINI_API_KEY`
   (or `GOOGLE_API_KEY`) set and `--replace`, passing `--start-figure N` so
   numbering continues after any existing figures.
6. Confirm every generated image file exists on disk and each placeholder became
   a `![alt](asset)` + `**Figure N:**` figure.
7. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that the
   figures resolve in `docs/<journal>/<permalink>.html`.

## Placeholder format

One HTML comment block per image, inserted right after the passage it serves:

```markdown
<!-- illustration-placeholder
{
  "id": "trust-bottleneck-review-surface",
  "status": "pending",
  "asset": "assets/images/<post-slug>/trust-bottleneck-review-surface.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that introduces trust as the adoption bottleneck",
  "visual_goal": "Show that AI-generated code passes through human review, tests, observability, and version control before it becomes trusted software.",
  "prompt": "Create a polished explainer illustration showing an AI coding agent producing source-code diffs that flow through four review gates: human inspection, automated tests, observability, and version control. Clean technical style, light background, blue/teal accents, minimal labels, no photorealism, no dense text, no title text.",
  "alt": "Diagram showing AI-generated code passing through review gates before becoming trusted software.",
  "caption": "Trust comes from inspectable review surfaces, not from the model generating more code."
}
-->
```

Required fields: `id` (kebab-case, unique in the post), `status` (`pending`
before generation), `asset` (always `assets/images/<post-slug>/<id>.jpeg`),
`aspect_ratio` (`16:9` default; `1:1` for compact diagrams), `placement`,
`visual_goal`, `prompt` (complete, self-contained), `alt`, `caption`.

Do not put markdown code fences or `-->` inside any JSON string.

## Asset paths (folder-layout post)

- Article source: `_journals/<journal>/posts/<post-slug>/index.md`
- Placeholder `asset`: `assets/images/<post-slug>/<id>.jpeg`
- Image on disk: `_journals/<journal>/posts/<post-slug>/assets/images/<post-slug>/<id>.jpeg`

The build merges per-post `assets/` into `docs/<journal>/assets/`, so the
markdown `assets/images/...` path resolves from the rendered page.

## Prompt guidance

Write prompts as if sent straight to the image model. Include subject/metaphor,
concrete objects in the scene, the diagram style, labels only where useful,
color/style direction consistent with the journal's existing visuals, and
exclusions (`no photorealism`, `no dense text`, `no title text`).

Prefer reusable article figures: concept map, lifecycle loop, before/after
comparison, layered stack, decision tree, review pipeline, risk/control matrix.
For reflective/private posts, prefer quiet metaphor over diagram chrome and match
the established palette (e.g. the warm gouache look the comic uses).

Avoid: generic people staring at dashboards, stock-photo scenes, decorative hero
art, and images that merely repeat an existing table.

## Replacement format

After the image exists on disk, replace the whole placeholder comment with:

```markdown
![Alt text from placeholder](assets/images/<post-slug>/<id>.jpeg)
**Figure N:** *Caption from placeholder.*
```

Number in article order, continuing any existing figures (`--start-figure N`).
Use the placeholder's exact `asset`, `alt`, and `caption` unless the generated
image clearly needs a caption tweak.

## Scripts

Both live in this skill's `scripts/` and must stay together (the generator
imports the parser). Standard-library only; same Gemini API pattern as the repo's
other generators.

Parser — list/validate placeholders (no Gemini, no edits):

```bash
python3 .claude/skills/article-illustrator/scripts/extract_illustration_placeholders.py \
  _journals/<journal>/posts/<slug>/index.md
```

Generator — dry-run first, then generate + replace:

```bash
python3 .claude/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py \
  _journals/<journal>/posts/<slug>/index.md --dry-run --print-prompts

GEMINI_API_KEY=... python3 .claude/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py \
  _journals/<journal>/posts/<slug>/index.md --replace --start-figure 5
```

Useful options: `--only <id-or-filename>` (one image), `--post <slug-or-permalink>`
(filter when scanning a directory), `--overwrite` (regenerate), `--start-figure N`
(continue numbering), `--limit N`. The generator does not run the site build —
run `python3 _wiring/build.py` yourself after.

## Anti-patterns

- Generating images without explicit user request — staging placeholders is the
  default; generation is a separate opt-in step.
- Editing `spec.md`, `comics.md`, other modality files, or `config.yaml`.
- Restarting figure numbering at 1 when the post already has figures.
- Decorative or stock-photo-style images; figures that just restate a table.
- Duplicating the comic's narrative beats as article figures — keep figures
  informational where a comic already carries the emotional register.
- Literal depictions a private post's Non-goals fence off (e.g. real family
  members) — stay metaphor-first.
- Forgetting to run the build, or leaving a `pending` placeholder whose image
  file does not yet exist (it renders as a raw HTML comment).
