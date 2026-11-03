# Illustrator Brief — Architecting Agentic Systems visual layer

You are adding the visual layer to some pages of **Architecting Agentic Systems**. ROOT is `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/agentic-systems-architecture/`.

The sibling books (BOOKED, LISTED, the vehicle-data book) replaced their mermaid diagrams with generated illustrations and added conceptual figures. This book does the same. Your pages need two things:
- **(A)** Check and finish the diagram illustrations. These are already generated.
- **(B)** Add conceptual figures.

`GEMINI_API_KEY` is set in the environment. Never print it. Run all commands from the repository root, `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals`.

## Read first

1. `.claude/skills/article-illustrator/SKILL.md`, for the placeholder format and the generator.
2. For each assigned page, its `index.md` (whole) and its `spec.md`.

In the commands below, `S=.claude/skills/article-illustrator/scripts`, and `<folder>` is the page's folder name under `ROOT/posts/`.

## Phase A — finish the diagram illustrations (per page)

Every mermaid block on your pages already has an `illustration-placeholder` staged in front of it, and its image was generated from a screenshot of the rendered diagram. That screenshot is at `ROOT/_research/diagram-illustrations/refs/<folder>/<k>.png`, where k is the k-th diagram on the page. The image is at `ROOT/posts/<folder>/<asset>`, where `asset` comes from the placeholder JSON.

1. **Inspect every image** with the Read tool, next to its reference screenshot. Compare the **structure**, not the looks. Reject an image if it has any of these:
   - a missing, duplicated or extra box;
   - a missing, extra or reversed arrow;
   - a misspelled, garbled or invented label;
   - a wrong number;
   - a logo, brand, robot or face;
   - clutter or photorealism.
2. **Retry** a rejected image. Append one `Corrections: …` sentence to that placeholder's `"prompt"` in `index.md`; edit only that JSON string and keep the JSON valid. Then run `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md --only <id> --overwrite`. Allow at most 3 attempts. If a dense diagram still fails, you may shorten its prompt's checklist to the essential elements. Whatever you shorten, the image must still show everything the **caption** names.
3. If a missing image file is the only problem (generation failed), generate it with the same command, without `--overwrite`.
4. **Finalize:** `python3 $S/mermaid_to_illustrations.py finalize ROOT/posts/<folder>/index.md`. This swaps each placeholder and its mermaid block for the image and keeps the existing `**Figure N:**` caption. The page must end with no `begin mermaid` and no `illustration-placeholder` left.

## Phase B — conceptual figures (per page)

- **How many.** Add **2 figures per chapter** and **1 per part intro or preface page** (introduction, where-agentic-systems-go-wrong, meet-ostrell). Add **none** to toolkit and source-coverage.
- **What they show.** They are informational and conceptual. They complement the diagrams and never redraw one. Draw from the chapter's central argument or its worked Ostrell example. Good forms:
  - a memorable metaphor. Examples:
    - the model as a bright but variable spark inside a sturdy frame of code;
    - an autonomy dial set per action class;
    - an approval card stamped with a fingerprint of exactly what was approved, and an expiry;
    - a receipt that proves an effect happened once;
    - a sandbox as a sealed glass box;
    - a poisoned note slipped into a stack of documents;
    - an evidence ledger that unlocks the next autonomy step;
  - a before/after comparison;
  - a layered stack;
  - a decision landscape;
  - a lifecycle loop;
  - an Ostrell scene showing the problem concretely: a dispatcher, a field technician, a finance clerk at close week, a support agent, a reviewer at a queue.
- **Placement and captions.**
  - Insert each placeholder, in the skill's format, after the paragraph or table it serves.
  - Ids are kebab-case and start with the folder number or slug, e.g. `23-wait-holds-no-worker`.
  - Asset path: `assets/images/<folder>/<id>.jpeg`.
  - Each `caption` states the figure's point in one sentence and uses only numbers that appear in the chapter.
  - Write the prompt as a scene: give each element's position and a quoted label of 1–3 words (0–6 labels in total), and name every arrow explicitly. Describe only what should appear; naming forbidden things makes the model draw them. Avoid "step 2" and "column 1", which get drawn as text.
- **Prompt style.** End every prompt with: "Style: polished business explainer illustration for a book on agentic AI system architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes; no other words. No photorealism, no 3D render, no dense text, no title text. Models, agents and tools are generic unbranded components (a model is a simple spark or chip shape); no robots, no humanoid AI, no faces on machines. Draw no logos, brand marks, or vendor, model-provider, cloud, chat-app or code-hosting names. Ostrell people are generic professionals, field technicians and customers; never real people. Money, if shown, is in euros."
- **Steps.**
  1. Validate: `python3 $S/extract_illustration_placeholders.py ROOT/posts/<folder>/index.md`.
  2. Generate without `--replace`: `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md`. Inspect and retry as in Phase A. For a conceptual figure, also reject one whose meaning contradicts its caption.
  3. Replace: `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md --replace --start-figure 101`.
  4. Renumber: `python3 ROOT/_research/tools/renumber_figures.py ROOT/posts/<folder>/index.md`. This makes the captions run 1..N in document order and updates in-text references such as "Figure 3".
  5. Grep `**Figure` and confirm two things: the numbers run 1..N with no gaps, and each image's caption follows it directly.

Do Phase A before Phase B on each page, because renumbering expects the diagram captions to be final.

## Finish each page

- Append to the `spec.md` Changelog: `- **2026-10-28** — Visual layer: converted N mermaid diagrams to illustrations and added M conceptual figures (article-illustrator). *(AI-mediated session)*`
- Do not change prose, except the figure-number references the renumber script updates.
- Do not touch other pages, `config.yaml`, the ledger or the style guide.
- **Never edit the front matter.** Icons and logos are linked later by another process.

## Verify at the end

- **Build:** `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. A transient error from a parallel build is fine if a rerun passes. Errors in other journals are not yours.
- **Render check:** `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`. Every page must print `OK`.
- **Leftovers:** `grep -lE "illustration-placeholder|begin mermaid" <your index.md files>` must print nothing.

## Report back

Under 150 words. For each page, give the number of diagrams finalized and the number of conceptual figures added. Name any image you regenerated or simplified, and any figure you dropped.

Log every figure you accepted with a known flaw to `ROOT/_research/figure-issues.md`, as one line in the form `- <folder> / <id> (Figure N): flaw; accepted after K attempts`. Append only, re-read the file's tail first, and create the file if it is missing.

## Notes specific to this book

- Ostrell Group is fictional: a field-service SaaS company in Rotterdam whose agent platform is Keelson. Never draw real companies or products: no OpenAI, Anthropic, Claude, GitHub, Slack, AWS, MCP logos and the like.
- Currency is euro.
- For the "Across Domains" content, draw a figure only if it is genuinely about how the domains differ.
- Other illustrators are working on other pages at the same time. Touch only your own pages.
