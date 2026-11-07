# Illustrator Brief — ORDERED visual layer

You are adding the visual layer to pages of **ORDERED: Architecting Commerce Platforms** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/commerce-platform-architecture/`), a book for readers new to commerce architecture. It must match its sibling books (BOOKED, LISTED, Architecting Agentic Systems), which use generated illustrations instead of mermaid. For each assigned page:
- **(A)** Redraw every mermaid diagram as a generated illustration, keeping its caption.
- **(B)** Add conceptual inline figures.

`GEMINI_API_KEY` is set in the environment. Never print it. Repository root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals` (run scripts from there).

## Read first

1. `.claude/skills/article-illustrator/SKILL.md`: placeholder format, asset paths, scripts, and the section "Replacing mermaid diagrams with illustrations".
2. For each assigned page: its `index.md` in full and its `spec.md`.

Scripts: `S=.claude/skills/article-illustrator/scripts`. Reference screenshots of every diagram already exist: `ROOT/_research/diagram-illustrations/refs/<folder>/<k>.png` (k = 1.. in document order). Do not rerun the snapshot script.

**Private scratch:** several illustrators run in parallel. Keep any helper file you write in `/private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/12bfd7f3-746f-4091-bfd9-b1ac7593d6a5/scratchpad/illus-<your first folder>/`, never in a shared location. Edit only your own pages.

## Phase A — redraw the diagrams (per page)

1. Stage: `python3 $S/mermaid_to_illustrations.py stage ROOT/posts/<folder>/index.md --refs ROOT/_research/diagram-illustrations/refs --archive ROOT/_research/diagram-illustrations/mermaid-<folder>.json`. The archive keeps every mermaid source so a figure can be regenerated later.
2. Edit each staged placeholder's `prompt` only where it helps: the script's style line names "marketplace platform architecture"; make it "commerce platform architecture" and append the book suffix below. Keep the reference-image instruction and the checklist.
3. Generate: `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md` (no `--replace`).
4. **Inspect every image** with the Read tool against its reference screenshot and checklist, comparing structure, not looks. Reject an image with a misspelled, garbled or extra label; a wrong number; a missing, extra or misrouted arrow; a logo or brand; or anything that contradicts the caption. Retry by appending `Corrections: …` to the prompt, then regenerate that one image with `--only <id> --overwrite`. At most 3 attempts; if still wrong, simplify the prompt to the 5–8 elements that carry the caption's point.
5. Finalize: `python3 $S/mermaid_to_illustrations.py finalize ROOT/posts/<folder>/index.md`. The existing `**Figure N:**` captions stay. Confirm no `begin mermaid` remains.

## Phase B — conceptual figures (per page)

**Order matters:** finish Phase A, including `finalize`, before inserting any Phase B placeholder. If finalize runs while Phase B placeholders exist, it fails on JSON parsing and leaves each mermaid block and its caption on the page twice.


- **How many:** 2 per chapter (folders 01–49); 1 per part intro, `introduction`, `where-commerce-platforms-go-wrong` and `meet-kestrel-and-pine`; none on `toolkit`, `glossary`, `bibliography`, `domain-coverage`.
- **What:** informational and memorable, complementing (never redrawing) the diagrams. Draw from the chapter's central argument or its Kestrel & Pine example. Good forms: a metaphor (a promise as a ticket each system must honour; stock as one jar several hands reach into; an order as a parcel handed along a relay; a reconciliation as two ledgers being matched line by line), a before/after comparison, a layered stack, a decision landscape, a lifecycle loop, a Kestrel & Pine scene (the Duiven warehouse at Black Friday, Eva unboxing the wrong size, Noor's whiteboard).
- **Placement:** an `illustration-placeholder` block (skill format) after the paragraph or table it serves. The `caption` states the figure's point in one sentence and uses only numbers that appear in the chapter. Asset path `assets/images/<folder>/<id>.jpeg`; ids are kebab-case and start with the folder number or slug.
- **Prompt:** 5–9 elements with positions and quoted 1–3 word labels (0–6 labels); describe only what should appear; avoid "column 1"/"step 2" wording. End every prompt with the book suffix.
- **Steps:** validate (`python3 $S/extract_illustration_placeholders.py <index.md>`), generate without `--replace`, inspect and retry as in Phase A, then `--replace --start-figure 101`, then renumber: `python3 ROOT/_research/tools/renumber_figures.py <index.md>`. Grep `**Figure` and confirm 1..N with no gaps, every image followed directly by its caption, and in-text "Figure N" references still pointing at the right figure.

## Book suffix (append to every prompt)

"Style: polished business explainer illustration for a book on commerce platform architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, platform, marketplace, carrier, payment or software names; show storefronts, marketplaces, warehouses, carriers, payment providers and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic shoppers, warehouse staff and professionals, never real people."

## Finish each page

- Append to `spec.md` Changelog: `- **2026-11-07** — Visual layer: redrew N mermaid diagrams as illustrations and added M conceptual figures (article-illustrator). *(AI-mediated session)*`
- Do not change prose, except figure-number references handled by the renumber script.
- **Never edit front matter** (another process adds `icon:` and `logo:` lines later), `config.yaml`, the ledger or other pages.

## Verify at the end

- Build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (errors from other journals or a transient OSError from a parallel build can be ignored if a rerun passes).
- Render check: `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`: every page `OK` with `mermaid=0`.
- `grep -l illustration-placeholder <index.md files>` prints nothing.
- Log any figure accepted with a known flaw to `ROOT/_research/figure-issues.md` (one small append; re-read its tail first; create it if missing).

## Report back

Under 150 words: per page, diagrams redrawn and conceptual figures added; images retried or simplified; any figure dropped or accepted with a flaw.
