# Comic pages pilot (18 September 2026)

Record of the pilot that replaced chapter 04's six single-scene comic panels with seven comic pages of three strips each, after the author found the panels unclear and uninformative.

- `04-obligations-before-budget.json` — the pilot page script. **Superseded:** the source of truth is now the `comic-page` blocks in `posts/04-obligations-before-budget/comics.md`.
- `04-obligations-before-budget.storyboard.md` — readable storyboard of the pilot script.
- `04-obligations-before-budget.comics-six-panel.md` — the six-panel `comics.md` as it stood before conversion (restore it to go back; the six `comic-0N-scene.jpeg` images are still in the post's assets).
- `04-obligations-before-budget.generation-log.json` — prompts and checksums of the pilot generations (pages 1 and 6 are missing from it).
- `images/04-obligations-before-budget/` — accepted pilot pages, rejected variants (`.vN.jpeg`) and pre-edit copies (`.before-retext.jpeg`), kept for comparison.

The pilot generator was folded into the `explainer-comics` skill: `.claude/skills/explainer-comics/scripts/generate_comic_pages.py`. The authoring rules learned here are in that skill's `SKILL.md`.
