# Illustrated Edition — 2026-09-13

The author requested illustrations and bold emphasis, then expanded the request to logos, comics and icons, followed by one whole-post visual in each TL;DR and a new journal logo. Changes were made directly in this journal, following the editorial polish recorded in [the earlier review](editorial-polish-20260913.md).

The edition contains 66 explanatory figures in the 29 main chapters, two appendix essays, reading guide and toolkit; 31 TL;DR overview visuals; 42 article header logos; 42 navigation icons; and 31 six-panel comics (186 panels). A dedicated Owned logo identifies the journal. All 368 new public image assets use unique paths beside their posts or in the journal’s shared assets. Short introductions retain a concise article format. Body and summary emphasis highlights short key claims, and the three opening key points use narrower emphasis.

The article-illustrator and bold-highlighter repository skills guided the work. Article figures use the bundled `generate_illustrations_nanobanana.py` script. Header logos and icons use `_wiring/generate_logos.py` and `_wiring/generate_icons.py`. The journal-specific [comic generator](generate_comics.py) reuses the article generator’s format handling and the Gemini API with a shared character reference. API keys remain in the local environment.

Article and TL;DR figures, logos and comics use `gemini-3-pro-image-preview`; icons use `gemini-3.1-flash-image-preview`. The palette uses warm ivory, navy, muted teal and ochre. Comic characters are fictional; historical cases are discussed through documents. Alt text and captions accompany the figures, and comic dialogue is also provided as readable text.

Prompt and review records:

- [Article figure prompts and correction history](article-illustration-prompts-20260913.json)
- [TL;DR summary visual prompts](summary-visual-prompts-20260913.json)
- [Header logo and icon prompts](logo-and-icon-prompts-20260913.json)
- [Comic prompts and generated asset checksums](comic-generation-prompts-20260913.json)
- [Owned journal logo prompt](journal-logo-prompt-20260913.json)
- [Shared cast prompt](comic-cast-prompt-20260913.json)
- [Reviewed comic corrections](comic-visual-corrections-20260913.json)
- [Accepted artwork and checksums](artwork-review-20260913.json)
- [Source and static build validation](illustrated-edition-validation-20260913.json)
- [Browser verification](illustrated-edition-browser-20260913.json)

Visual review covered every public image. Corrections removed misleading financial diagrams, invented case-history labels, crowded logos, repeated dialogue and conspicuous drawing defects. The standard builder produced 85 pages. Source checks cover article wording, financial tables and citations, all 31 summary prose word limits, image paths, numbered captions, alt text and comic transcripts. Browser checks cover reading-format tabs, loaded images, index icons and desktop/mobile layout. Private inputs, research records and discarded variants are excluded from the site.

To review planned comic work without calling the API:

```sh
python3 _journals/private-techuity/_research/generate_comics.py --dry-run
```

To regenerate a selected panel after revising and reviewing its prompt, use `--post`, `--only` and `--overwrite` with `GEMINI_API_KEY` set locally. Existing assets are preserved by default. Rebuild the journal after image or source changes.

The [summary visual generator](generate_summary_visuals.py) imports the native Nano Banana article illustrator and resolves each `summary.md` into its post’s asset namespace. It preserves existing images unless `--overwrite` is supplied and accepts `--post` for a selected revision. Dry-run before generating. Each TL;DR keeps its original 300–500-word prose, with one overview figure after the opening paragraph, accessible alt text and a concise caption. Figure numbering starts at one within that modality.
