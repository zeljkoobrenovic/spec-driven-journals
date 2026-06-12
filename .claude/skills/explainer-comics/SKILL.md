---
name: explainer-comics
description: Write the comics modality (comics.md) of a spec-driven journal post — an explainer comic of generated panel images derived from spec.md and index.md, rendered as the Comic tab on the post page. Use when asked to add, write, generate, or update an explainer comic, comic strip, comic panels, or comic tab for a post in _journals/*/posts/*/.
---

# Explainer Comics (the `comics` modality)

## Goal

Write `comics.md` next to a post's `index.md` — an explainer comic of 6–10
generated panels that renders as the **Comic** tab on the same post page.
The comic teaches the record's core idea to someone who will never read the
article: each panel is one beat of the argument.

## Contract rules

- `spec.md` is the contract; `index.md` is the source content. **Never edit
  either from this skill.** Flag spec/article drift instead of working
  around it.
- The comic compresses, it does not invent: every panel's beat must trace to
  the spec's Intent/Success criteria or the article's body.
- Do not generate images unless the user explicitly asks for generation.
  Authoring the panel script (placeholders) and generating images are
  separate steps.

## Workflow

1. Read `spec.md` (Intent, Audience, Success criteria, Non-goals) and
   `index.md`. The post must already have an `index.md`.
2. Plan the strip: 6–10 beats — hook → problem → wrong way (anti-pattern) →
   the decision/principle → how it plays out → what it costs → closer. Each
   beat becomes one panel.
3. Write `comics.md`: one `comic-style` block, then one `comic-panel` block
   per beat (formats below). Optionally a one-line intro paragraph above the
   panels.
4. Validate and preview prompts:

   ```bash
   python3 .claude/skills/explainer-comics/scripts/generate_comic_panels.py \
       _journals/<journal>/posts/<slug>/comics.md --dry-run --print-prompts
   ```

5. Only when the user asks for image generation:

   ```bash
   GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_panels.py \
       _journals/<journal>/posts/<slug>/comics.md --replace
   ```

   `--replace` swaps each completed placeholder for a markdown figure
   (`![alt](asset)` + `**Panel N:** *caption*`).
6. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` contains `"key": "comics"`.
7. Tell the user the Comic tab is live at `<permalink>.html#comics`.

## Style block (one per file, first)

The `comic-style` block is the cross-panel consistency layer: the generator
prepends it to every panel prompt so characters and visual style stay
recognizable across panels.

```markdown
<!-- comic-style
{
  "cast": "MAYA: a pragmatic staff engineer, short dark hair, rolled-up sleeves, always sketching on a whiteboard. REX: an over-eager robot assistant, boxy, one antenna, perpetually holding too many cables.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with blue/teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->
```

Keep the same cast across all comics in a journal — check an existing
`comics.md` first.

## Panel block (one per panel)

```markdown
<!-- comic-panel
{
  "id": "01-the-friday-deploy",
  "status": "pending",
  "asset": "assets/images/<post-slug>/comic-01-the-friday-deploy.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 1 of an explainer comic. Maya watches Rex proudly wheel an enormous, over-engineered deployment machine toward a tiny door labeled PROD. Speech bubble from Maya: 'It doesn't fit.' Convey: complexity fails at the last step.",
  "alt": "Comic panel: a robot wheels a huge machine toward a tiny door labeled PROD while an engineer watches.",
  "caption": "Complexity always meets a door it doesn't fit through."
}
-->
```

Required fields: `id` (kebab-case, `NN-` ordinal prefix), `status`
(`pending` until generated), `asset`
(`assets/images/<post-slug>/comic-<id>.jpeg`), `aspect_ratio` (`16:9` for
scene panels, `1:1` for portrait/punchline panels), `prompt`, `alt`,
`caption`.

Prompt guidance:

- Start with "Panel N of an explainer comic" so the model keeps comic
  framing; the generator adds the cast and style automatically.
- One idea per panel; speech-bubble text of at most ~8 words, quoted
  verbatim in the prompt.
- No dense text, no title text, no diagram dumps — a panel is a scene, not
  a slide.

## Asset paths

- Comic source: `_journals/<journal>/posts/<slug>/comics.md`
- Panel `asset`: `assets/images/<slug>/comic-<id>.jpeg`
- Generated file on disk:
  `_journals/<journal>/posts/<slug>/assets/images/<slug>/comic-<id>.jpeg`

The build merges per-post `assets/` into `docs/<journal>/assets/`, so the
same markdown path resolves on the rendered page.

## Generator options

`scripts/generate_comic_panels.py` is standard-library-only (same Gemini API
pattern as the repo's other generators) and idempotent — existing images are
skipped unless `--overwrite` is passed.

- `--dry-run` / `--print-prompts`: plan without API calls or writes.
- `--only <id-or-filename>`: generate a single panel.
- `--overwrite`: regenerate existing images.
- `--replace`: replace placeholders whose images exist with markdown figures.
- `--limit N`, `--sleep S`, `--model M`, `--api-key-env GEMINI_API_KEY|GOOGLE_API_KEY`.
