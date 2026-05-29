---
name: article-illustrator
description: Analyze spec-driven-journals markdown posts, insert machine-readable illustration placeholders, generate Gemini/Nano Banana images for those placeholders, and replace generated placeholders with markdown image links and captions. Use when Codex is asked to suggest, add, stage, generate, or prepare article illustrations, figure placeholders, Gemini image-generation prompts, or generated article figures in _journals/*/posts/*/index.md files.
---

# Insert Article Illustration Placeholders

## Goal

Add source-level illustration placeholders to journal posts, generate images
from those placeholders when explicitly requested, and replace completed
placeholders with normal markdown images and captions.

Use this skill for article illustrations, not post hero logos. Hero logos are
handled by `_wiring/generate_logos.py`.

## Workflow

1. Read the target `index.md`, its sibling `spec.md` if present, and nearby
   posts only when needed for tone and cross-link context.
2. Identify 2-5 places where a visual would materially improve comprehension.
   Prefer diagrams, maps, comparisons, flows, and conceptual figures. Avoid
   decorative images.
3. Insert one placeholder immediately after the paragraph, table, or heading it
   should illustrate.
4. Use the JSON comment format below exactly. Keep JSON valid.
5. Do not generate images unless the user explicitly asks for image generation.
6. When generating, run the bundled generator with `--dry-run` first. Then run
   it with `GEMINI_API_KEY` or `GOOGLE_API_KEY` and normally include
   `--replace` so completed placeholders become markdown figures.
7. After generated files exist on disk, replace each placeholder with a markdown
   image and caption using the replacement format below.
8. Run `python3 _wiring/build.py` after edits.

## Placeholder Format

Use one HTML comment block per image:

```markdown
<!-- illustration-placeholder
{
  "id": "trust-bottleneck-review-surface",
  "status": "pending",
  "asset": "assets/images/risc-for-ai-software-development/trust-bottleneck-review-surface.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that introduces trust as the adoption bottleneck",
  "visual_goal": "Show that AI-generated code must pass through human review, tests, observability, and version-control diffs before it becomes trusted software.",
  "prompt": "Create a polished business explainer illustration showing an AI coding agent producing source-code diffs that flow through four review gates: human inspection, automated tests, observability, and version control. Use a clean technical style, light background, blue/teal accents, readable but minimal labels, no photorealism, no dense text.",
  "alt": "Diagram showing AI-generated code passing through review gates before becoming trusted software.",
  "caption": "Trust comes from inspectable review surfaces, not from the model generating more code."
}
-->
```

Required fields:

- `id`: kebab-case, unique within the post.
- `status`: `pending` before image generation; change to `generated` only if
  keeping the block temporarily after a file exists.
- `asset`: journal-root-relative markdown path, always
  `assets/images/<post-slug>/<id>.jpeg` unless the user requests another format.
- `aspect_ratio`: usually `16:9`; use `1:1` only for compact diagrams.
- `placement`: short source-location hint for agents.
- `visual_goal`: what the image should help the reader understand.
- `prompt`: complete Gemini prompt with enough context to generate the image.
- `alt`: accessibility text.
- `caption`: reader-facing figure caption.

Do not include Markdown code fences inside JSON strings. Do not include `-->` in
any field.

## Asset Paths

For a folder-layout post:

- Article source:
  `_journals/<journal>/posts/<post-slug>/index.md`
- Placeholder `asset`:
  `assets/images/<post-slug>/<id>.jpeg`
- Generated image on disk:
  `_journals/<journal>/posts/<post-slug>/assets/images/<post-slug>/<id>.jpeg`

The build merges per-post `assets/` into `docs/<journal>/assets/`, so the
markdown path resolves from rendered post pages.

## Prompt Guidance

Write prompts as if they will be sent directly to the image model.

Include:

- subject matter and metaphor
- concrete objects in the scene
- preferred diagram style
- labels only when useful
- color/style direction consistent with existing journal visuals
- exclusions such as `no photorealism`, `no dense text`, `no title text`

Prefer reusable article figures:

- concept map
- lifecycle loop
- before/after comparison
- layered stack
- decision tree
- review pipeline
- risk/control matrix

Avoid:

- generic people staring at dashboards
- stock-photo-like scenes
- decorative hero art
- images that repeat an existing table without adding insight

## Replacement Format

After the image exists at the expected disk path, replace the entire placeholder
comment with:

```markdown
![Alt text from placeholder](assets/images/<post-slug>/<id>.jpeg)
**Figure N:** *Caption from placeholder.*
```

Number figures in article order. If the article already has figures, continue
the existing numbering. Use the exact `asset`, `alt`, and `caption` values from
the placeholder unless the generated image clearly requires a caption adjustment.

## Generator Script

Use `scripts/generate_illustrations_nanobanana.py` to generate images from
placeholder comments. It uses the same standard-library-only Gemini API pattern
as the repo's `generate_illustrations_nanobanana.py` scripts, but reads
`illustration-placeholder` blocks instead of existing markdown image links.

Dry-run first:

```bash
python3 .codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py _journals/ai-notes/posts/risc-for-ai-software-development/index.md --dry-run --print-prompts
```

Generate images and replace placeholders with markdown figures:

```bash
GEMINI_API_KEY=... python3 .codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py _journals/ai-notes/posts/risc-for-ai-software-development/index.md --replace
```

Useful options:

- `--only <id-or-filename>`: generate one placeholder.
- `--post <slug-or-permalink>`: filter when scanning a larger posts directory.
- `--overwrite`: regenerate an existing image.
- `--replace`: replace placeholders whose image files exist after generation or
  from a previous run.
- `--start-figure N`: start markdown figure numbering at `N`.

The script writes each image to the source path implied by the placeholder, for
example
`_journals/ai-notes/posts/risc-for-ai-software-development/assets/images/risc-for-ai-software-development/trust-bottleneck-review-surface.jpeg`.
It does not run the site build; run `python3 _wiring/build.py` after generating
or replacing figures.

## Parser Script

Use `scripts/extract_illustration_placeholders.py` to list or validate
placeholders:

```bash
python3 .codex/skills/article-illustrator/scripts/extract_illustration_placeholders.py _journals/ai-notes/posts/risc-for-ai-software-development/index.md
```

The script prints JSON records including the expected source image path and the
markdown replacement text. It does not call Gemini or edit files.
