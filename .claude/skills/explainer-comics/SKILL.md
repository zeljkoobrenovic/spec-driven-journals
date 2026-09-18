---
name: explainer-comics
description: Write the comics modality (comics.md) of a spec-driven journal post — an explainer comic of generated comic pages (each page one image of stacked strips with the dialogue, labels and numbers drawn in the artwork) derived from spec.md and index.md, rendered as the Comic tab on the post page. Use when asked to add, write, generate, or update an explainer comic, comic strip, comic pages or panels, or comic tab for a post in _journals/*/posts/*/.
---

# Explainer Comics (the `comics` modality)

## Goal

Write `comics.md` next to a post's `index.md` — an explainer comic of 5–8
generated **pages** that renders as the **Comic** tab on the same post page.
Each page is one portrait image of **three stacked strips** (two when the beat
is simple). The comic teaches the record's core idea to someone who will never
read the article, so **the picture must explain the beat by itself**: the
exchange between characters, the short labels and the real numbers are drawn in
the artwork, and the caption under the image stays short.

The test for every page: cover the caption — does the page still teach its
point? Cover the image — is anything lost? Both answers must be yes.

> **Legacy format.** Comics written before September 2026 use one
> single-scene panel per image (`comic-panel` blocks, one bubble, no numbers
> in the art, the caption carrying the explanation). They keep working and are
> maintained with `scripts/generate_comic_panels.py` (`--dry-run`,
> `--print-prompts`, `--only`, `--overwrite`, `--replace`). Write new comics,
> and rewrite weak ones, in the page format below. One file never mixes the two
> block types.

## Contract rules

- `spec.md` is the contract; `index.md` is the source content. **Never edit
  the article from this skill.** If the spec describes the comic in terms the
  page format breaks (a panel count, per-panel requirements), update the spec
  *first*, keeping the intent of every requirement, and add a Changelog line.
- The comic compresses, it does not invent: every amount, label and line of
  dialogue must trace to the article or the spec.
- Do not generate images unless the user explicitly asks for generation.
  Authoring the page script and generating images are separate steps.
- Generated artwork is **inspected, never assumed** (see Verification).

## Workflow

1. Read `spec.md` (Intent, Audience, Success criteria, Non-goals, any
   comic-specific requirements) and `index.md`. Check an existing `comics.md`
   in the same journal for the cast and style, and reuse them.
2. Plan 5–8 beats: hook → the core mechanism → how it misleads or fails →
   the decision or principle → how it plays out → closer. **One worked example
   should run through the comic**; open with the question the closer answers.
3. For each beat choose **one physical device that carries the numbers** (a
   tower of gold bars going into labelled trays, priced boxes and a frame one
   of them cannot pass, a dial and a growing bill, a floor timeline with a torn
   end). If a beat has no device, it is a caption, not a page.
4. Write `comics.md`: one `comic-style` block, an intro paragraph, one
   `comic-page` block per beat (formats below).
5. Check and render — this rewrites the visible caption and transcript under
   each block and prints each prompt with its text-to-verify list:

   ```bash
   python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
       _journals/<journal>/posts/<slug>/comics.md --render --print-prompts
   ```

6. Only when the user asks for image generation:

   ```bash
   GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
       _journals/<journal>/posts/<slug>/comics.md --generate [--only <page-id>] [--overwrite]
   ```

   Start with the one or two most label-heavy pages; if they hold, do the rest.
7. **Verify every generated image** (next section); fix the block and re-roll
   or `--retext` until each page passes or the remaining flaw is reported.
8. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` contains `"key": "comics"` and every
   `comic-page-*.jpeg`.
9. Tell the user the Comic tab is live at `<permalink>.html#comics`, how many
   generations it took, and any flaw you accepted.

## Verification (mandatory after every generation)

Read each new image and check it against the block:

- **Text:** every string in the text-to-verify list is present, spelled
  exactly (amounts, signs, decimals), once; **no unsupplied text** (invented
  narration boxes, extra labels, numbers).
- **Cast:** each character matches the style block (skin tone, hair, clothes)
  in every strip; nobody extra from the cast.
- **Attribution:** each bubble's tail reaches the speaker the block names.
- **Counts and sizes:** countable things show the stated counts and the
  picture adds up; "bigger", "does not fit", "ends before" are visibly true.
- **Consistency across strips:** a prop shown twice looks the same twice.

The model spells supplied text reliably; it fails on the other four. Budget
two to three generations per accepted page. Replaced images are archived
automatically (`<journal>/_research/discarded-comic-variants/` when the journal
has a `_research/` folder). If both speakers could say either line and the
render swapped them, changing the block to match the image is a legitimate fix.

To change wording on an accepted page whose lettering is all large, edit the
block, then re-letter in place instead of re-rolling the scene (`--edit
"instruction"` does the same for one stray detail). **An in-place edit redraws
the whole image:** it has garbled small labels and deleted a labelled prop it
was not asked to touch. After any `--retext` or `--edit`, verify the *entire*
page again, and on pages with small lettering prefer a re-roll. The replaced
image is archived, so a bad edit is recoverable.

```bash
GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
    _journals/<journal>/posts/<slug>/comics.md --only <page-id> --retext "old words" "new words"
```

## Style block (one per file, first)

```markdown
<!-- comic-style
{
  "cast": "MAYA: a pragmatic staff engineer, short dark hair, rolled-up sleeves. REX: an over-eager robot assistant, boxy, one antenna.",
  "style": "Clean editorial explainer comic pages, each one image of three stacked full-width strips: dark ink outlines, flat colors with two accent colors on a light background, generous space, expressive people and simple physical props. Dialogue, short labels and the supplied amounts are lettered in the artwork, exactly as scripted. No photorealism, logos, titles or unsupplied text.",
  "identity": {
    "Maya": "MAYA is a WOMAN with short dark hair, rolled-up grey sleeves and a marker in her hand.",
    "Rex": "REX is a boxy ROBOT with one antenna and a blue chest panel."
  },
  "reference": "_research/comic-cast.jpeg"
}
-->
```

`cast` and `style` are required and go into every prompt. `identity` (one
emphatic sentence per character, keyed by the name used in page `cast` lists)
closes every prompt and is what stops character drift — write it whenever skin
tone, hair colour or age matter. `reference` is an optional cast sheet image,
path relative to the journal directory, attached to every generation. Keep the
same cast, identity and reference across all comics in a journal.

## Page block (one per page)

```markdown
<!-- comic-page
{
  "id": "01-profit-is-not-cash",
  "title": "Profit is not cash",
  "asset": "assets/images/<post-slug>/comic-page-01-profit-is-not-cash.jpeg",
  "aspect_ratio": "3:4",
  "cast": ["Alex", "Sam"],
  "strips": [
    {
      "scene": "Alex strides in, cheerful, holding up a one-page report. Sam sits at a desk. On the desk stands ONE single tall tower of exactly ten thick gold bars, each the same size.",
      "labels": ["EBITDA €10.0m"],
      "label_notes": "The label is a printed card standing in front of the tower.",
      "bubbles": [
        {"who": "Alex", "text": "We earned €10 million. Can I have €1 million?"},
        {"who": "Sam", "text": "That's profit, not cash. Watch what comes out of it."}
      ]
    }
  ],
  "alt": "Comic page in three strips: …",
  "caption": "Two or three sentences: what the numbers are, plus any first-use explanation the spec requires."
}
-->
```

Required: `id` (`NN-kebab-case`), `title`, `asset`
(`assets/images/<post-slug>/comic-page-<id>.jpeg`), `strips` (2 or 3), `alt`,
`caption`. Optional: `aspect_ratio` (default `3:4`; stacked strips in portrait
stay legible on a phone), `cast`. Per strip: `scene` (required), `narration`
(≤ 14 words), `bubbles` (≤ 2, each ≤ 14 words, `who` from the page cast),
`labels` (each ≤ 5 words) and `label_notes` (where each label sits). The script
enforces these limits. `status` and `generation` are written by the script.

Everything visible under a block — the image line, `**Page N: Title.**`
caption and the per-strip transcript — is **rendered from the block**. Edit the
block and re-run `--render`; never edit the rendered lines.

## Writing strips that generate well

- **One chart, three strips.** When the point is "everything is the same
  except X", put the comparison on ONE page: describe the fixed element once,
  word for word, in each strip and say it is drawn identically in all three.
  Within one image the model keeps it identical; across separate images it
  does not.
- **When two speakers stand together, give their order explicitly** ("in this
  left-to-right order: first Alex, then Morgan") and match the bubble order;
  "Alex, with Morgan beside him" produced swapped tails.
- **An exchange, not a statement.** Two bubbles: the tempting wrong idea, then
  the correction. List bubbles in reading order and say in the scene who
  stands left and who stands right, in that same order.
- **Numbers live in the picture**, as labels on the device; dialogue carries
  the reasoning. A reader should be able to check the arithmetic by looking.
- **Number the things whose count matters.** "A row of four chairs" came back
  as three; four chairs with the numerals 1–4 on their backrests (listed as
  labels) came back as four. Pin cards side by side "with clear gaps" rather
  than fanned in a hand, or their words get cut off.
- **Countable, equal units.** "A column of exactly 4 bars, one bar per layer,
  never a pyramid" — not "a bigger stack". Make the picture add up.
- **Draw the relation, not the adjacency.** "Does not fit" is a box jammed in
  the frame; "has not arrived" is a bar still in the customer's arms.
- **People stand clear of lettered boards.** "Sam writes the last line" or
  "taps the second line" puts a hand over the words; a board behind a group puts
  a head over them. Hang boards "high on the wall, above everyone's heads", have
  characters gesture "with an open hand" from the side, and say that no head,
  hand, marker or bubble covers the lettering. Whiteboard sums with a few large
  lines are the most reliable device for arithmetic.
- **Objects already placed.** Things being carried get their labels covered by
  hands; put labelled objects down and say the labels face the reader.
- **No place names in scenes** ("back at the office", "in Sam's office"): they
  come back as invented narration boxes.
- **Describe what is there, never what is absent.** "The torn end is not
  visible" produces a tear; "five whole tiles, numbered 3 to 7" does not.
- **Keep a changing prop out of later strips** when its exact state matters;
  crop the later strip so the detail is out of frame.
- **Label a change of example once, in the artwork, by stating the new
  assumption** ("Now suppose €60 million of floating-rate debt"). Do not repeat
  a disclaimer phrase ("a separate illustration") across intro, art and caption.
- **Captions are short.** What the numbers are, the one qualification that
  matters, and first-use explanations the spec demands. Definitions and
  caveats that the article carries stay in the article.
- **Say every character's gender, skin tone and hair in both `cast` and
  `identity`.** "A CFO with round glasses" came back as a woman twice; "a man
  with short brown hair" did not. Expect drift anyway on roughly one page in
  three, and re-roll it.
- **Props attract lettering.** Money bags get a `$`, cheques a payee name,
  certificates a garbled heading, whiteboard arrows pseudo-text, a "tag from the
  money bag" the words MONEY BAG. Describe such props positively as plain
  ("a sheet with only a gold seal and ruled lines", "the amount is the only
  lettering on the cheque"), put a currency rule in the style text, and drop
  props the beat does not need. A correct, helpful extra label (`ESTIMATE`,
  `€100,000`) may be kept: add it to the block so script and image agree.
- Supporting people are "unnamed, in plain grey clothes"; give their exact
  number ("exactly three customers").

## Asset paths

- Comic source: `_journals/<journal>/posts/<slug>/comics.md`
- Page `asset`: `assets/images/<slug>/comic-page-<id>.jpeg`
- Generated file on disk:
  `_journals/<journal>/posts/<slug>/assets/images/<slug>/comic-page-<id>.jpeg`

The build merges per-post `assets/` into `docs/<journal>/assets/`, so the same
markdown path resolves on the rendered page. The post template links every
image to its full-size file, so a reader on a phone can tap a page to zoom.

## Script options

`scripts/generate_comic_pages.py` is standard-library-only and idempotent —
existing images are skipped unless `--overwrite` is passed.

- `--render`: check the blocks and rewrite the visible figures, captions and
  transcripts (no API calls).
- `--print-prompts`: print each prompt and its text-to-verify list.
- `--generate`: generate missing pages, then render. `--only <page-id>`
  (repeatable), `--overwrite`, `--sleep S`, `--model M`,
  `--api-key-env GEMINI_API_KEY|GOOGLE_API_KEY`, `--archive-dir DIR`.
- `--only <page-id> --retext OLD NEW`: re-letter one string on an accepted
  image; the new words must already be in the block.
- `--only <page-id> --edit "INSTRUCTION"`: one small correction on an accepted
  image. Both redraw the whole page — re-verify everything afterwards.
