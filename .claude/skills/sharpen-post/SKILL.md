---
name: sharpen-post
description: Make one post less vague and easier to follow. Works iteratively on a whole index.md (or modality file): first the section-heading outline, then the paragraph order within each section, then the first sentence of every paragraph, then the sentences themselves. Writes in a plain, simple style, cuts needless words, and prefers deleting vague or confusing content to adding new content. May also tighten the post's spec.md when it is vague or out of step with the sharpened post. Use when asked to sharpen, tighten, de-vague, simplify, clarify or cut down a post in _journals/*/posts/*/.
---

# Sharpen Post

## Goal

Make one post **sharp**: a reader who reads only the section headings knows
what the post covers and in what order. A reader who reads only the first
sentence of each paragraph gets a faithful summary. Every remaining sentence
says something specific in plain words.

This is a **cutting pass**. Prefer removing to adding. When a passage is vague
or confusing, first ask whether the post needs it at all. Delete it if not.
Rewrite it in one plain sentence only if a needed point is buried in it. Add
new material only to keep the flow intact, for example when the reader would
otherwise miss a link between two sections.

The work is iterative. Fix the structure before the paragraphs and the
paragraphs before the sentences. Polishing a sentence that a later pass
deletes wastes the effort.

## Contract rules

- **`spec.md` is the contract.** Read its Intent, Audience, Success criteria and
  Non-goals before cutting. Do cut material the Non-goals exclude. By default,
  do not cut something a success criterion requires.
- **You may update `spec.md` when sharpening exposes a problem in it.** This is
  optional; most passes need only the Changelog line. Update the spec when:
  - a success criterion is vague in the same way the post was;
  - a criterion requires material that is only padding;
  - the sharpened post's structure no longer matches what the spec describes;
  - an Open question has been answered.

  Follow the repo's rule and edit the spec first, then cut the post to match.
  Apply the same plain style to the spec. Do not change the spec's Intent to
  justify a cut; if the post's purpose itself seems wrong, raise that with the
  author instead.
- **Keep the meaning and the facts.** Do not change claims, numbers, dates,
  names, citations, quoted text, or the labels that mark evidence (for example
  `INFERENCE, NOT DOCUMENTED`). If a fact sits in a vague paragraph you delete,
  move it into a paragraph you keep, or confirm the post states it elsewhere.
- **Keep the house shape.** Fixed elements stay in place with their exact
  labels:
  - front matter;
  - ADR or KEY POINTS opening blockquotes, with KEY POINTS kept at exactly three
    bullets;
  - a journal's fixed callouts and fixed section names (see its style guide or
    README, for example `_research/style-guide.md`);
  - `Sources`, `References` and `To Probe Further` sections;
  - the closing hand-off.

  You may tighten the wording inside these elements, but do not rename or
  remove them.
- **Keep the markup working**, including:
  - `[[permalink]]` cross-links and markdown links;
  - bold text;
  - image references;
  - `---begin mermaid---` blocks and their `**Figure N:**` captions;
  - tables, HTML, and explicit anchors such as `<a id="…">`.

  If you delete a figure, renumber the remaining figures and every "Figure N"
  reference in the text.
- **Heading anchors may be linked from elsewhere.** Before renaming a heading,
  run `grep -rn "<permalink>.html#" _journals/` to check for links into this
  page. If a link points at that heading, keep the anchor working: keep an
  explicit id, or update the link.
- Edit only the requested file and its `spec.md`. Report problems in other
  pages instead of fixing them.

## Tool

`scripts/skeleton.py` prints a post's skeleton. It skips front matter, code,
diagrams and tables.

```bash
S=.claude/skills/sharpen-post/scripts/skeleton.py
python3 $S <file.md> --headings   # the outline only
python3 $S <file.md>              # headings + first sentence of every paragraph (P1, P2, …)
python3 $S <file.md> --stats      # headings, paragraphs, prose words
```

## Workflow

### 0. Baseline

1. Read `spec.md`, then the whole post once.
2. Record `--stats` as the baseline.
3. In one sentence, write down what the post argues. If you cannot, find that
   sentence first: the spec's Intent or the post's KEY POINTS usually hold it.
   Every later cut is judged against it.

### 1. Section flow (headings only)

Run `--headings` and read the outline as if it were the whole post.

- **Each heading names its content.** Replace generic headings such as
  Overview, Background, Discussion, Considerations, Other Aspects or Final
  Thoughts with the specific topic or claim, for example "Why Feeds Need
  Contracts" or "Three Kinds of Ingestion Key". Keep headings short (2–7 words)
  and parallel in form within a level.
- **The order tells a story.** A typical order is problem, then idea, then how
  it works, then trade-offs, then what to do. Move whole sections when the
  order does not follow.
- **Each section has one job.** Merge two sections that cover the same ground.
  Delete a section that serves neither the post's one-sentence argument nor the
  spec. Split a section that does two unrelated jobs only if both jobs stay.
- **Use few heading levels.** A subsection with a single paragraph usually
  belongs in its parent.

Re-run `--headings`. Repeat until the outline alone gives the reader the
post's shape.

### 2. Paragraph order (per section)

For each section, read its paragraphs in order.

- **One paragraph, one point.** Split a paragraph that carries two points.
  Merge or delete paragraphs that repeat each other; keep the clearer one.
- **Each paragraph follows from the one before it**, by cause, sequence,
  example, contrast or consequence. If you need a bridging sentence to make a
  paragraph fit, first check whether the paragraph belongs elsewhere or nowhere.
- **Put the most important paragraph first** in its section, unless the section
  tells a story in time order.
- **Delete paragraphs that only announce or recap**, such as "In this section we
  will…", "As discussed above…" or "In summary…". Fixed preface or hand-off
  elements required by the house shape are the exception.

### 3. First sentences (the skim path)

Run the full skeleton and read the `P1, P2, …` lines alone, top to bottom.

- **Each first sentence states its paragraph's point**, as a claim the reader
  could disagree with. It is not a teaser, a question, a transition ("However,
  there is more to it.") or scene-setting.
- **Bring buried points forward.** If a paragraph's point appears in its third
  sentence, restructure the paragraph so that point comes first, then the
  support.
- **The P-lines together summarize the post.** Where one does not follow from
  the one before it, the problem is the paragraph order (step 2), not the
  wording.
- **Keep narrative paragraphs as they are.** Scenes, case narratives and quoted
  dialogue may open with action, but the paragraph that interprets a scene
  states its point first.

### 4. Sentences (vagueness and needless words)

Go through each paragraph. Work on a block with `**bold**` lead-in phrases as
you would on a paragraph.

**Vague → concrete or gone.** For every vague sentence, ask three questions:

1. What exactly is the thing?
2. What does it do or mean?
3. What follows from it?

If the post's context answers them, rewrite the sentence with the answer. If it
does not, delete the sentence. Do not invent specifics to fill the gap.

Common vague patterns:

- Abstract nouns with no referent: *aspects, considerations, factors, elements,
  dimensions, things, landscape, ecosystem, space*.
- Weak verbs: *plays a role in, contributes to, impacts, addresses, leverages,
  enables, drives, facilitates*. Say what actually happens.
- Unquantified size: *significant, substantial, various, a number of, many,
  key, critical, important*. Give the number or the comparison, or drop the
  word.
- Stacked hedges: *may potentially, could possibly, in some cases it might*.
  Keep one hedge, and only where the evidence is uncertain.
- Empty openers: *It is important to note that, It is worth mentioning, In
  today's world, When it comes to, In terms of*.
- Buzzwords: *robust, seamless, holistic, cutting-edge, best-in-class,
  world-class, game-changer, synergy*.

**Needless words.** Prefer short words and short sentences.

| Instead of | Write |
| --- | --- |
| in order to | to |
| due to the fact that | because |
| at this point in time | now |
| has the ability to | can |
| a large number of | many (or the number) |
| make a decision | decide |
| is able to | can |
| the fact that | (delete) |
| very, really, quite, basically, actually, simply | (delete) |

- Prefer the active voice: "The feed service rejects the batch", not "The
  batch is rejected".
- Prefer verbs to nouns: "validate", not "perform validation of".
- Split sentences longer than about 30 words.
- Drop adjectives and adverbs that do not change the meaning.
- Say a thing once. Delete restatements of the previous sentence.
- Use the same term for the same thing throughout. Do not switch between
  synonyms for variety.

### 5. Iterate, then verify

1. Re-run steps 1–3 on the edited post. Edits often expose a new ordering or
   topic-sentence problem. Repeat until a full round produces no structural
   change. Stop after **three rounds**.
2. Run `--stats` and compare it with the baseline. Prose words should fall,
   usually by 10–30%. If they rose, you added rather than cut; review the
   additions.
3. Check the `git diff`:
   - no number, date, name, citation, link or evidence label was lost or
     altered by accident;
   - every `[[…]]` link is intact;
   - figure numbers run consecutively;
   - the house-shape elements are still present.
4. Run `python3 _wiring/build.py 2>&1 | grep -iE "<journal>|error|Traceback"`
   and confirm `[built] <journal>`. If the journal has a render check, run it
   on the page.
5. Append to `spec.md`'s Changelog:
   `- **YYYY-MM-DD** — Sharpening pass: <one-line summary, e.g. 7,410 → 6,120 words; 3 headings renamed; 2 sections merged; spec success criteria tightened>. *(AI-mediated session)*`
   Then update `revised:` in the spec's front matter. If you changed the spec
   itself, say what changed in the same Changelog line. Check that the spec and
   the post agree. If the spec's status was `drifted` and this pass reconciled
   them, set it to `accepted`.

## Report back

Keep the report short:

- prose words before → after;
- the new heading outline, if it changed;
- sections merged, moved or deleted;
- spec changes, if any, with the reason for each;
- each **deleted passage that carried a claim**, with a one-line reason, so the
  author can restore it;
- anything left vague because fixing it needs facts the post does not have.
  These are questions for the author.

## Anti-patterns

- Polishing sentences before the outline and paragraph order are right.
- Fixing vagueness by adding explanation when deleting would serve the reader
  better.
- Inventing examples, numbers or sources to make a sentence concrete.
- Changing the argument, the facts or the author's conclusions. This pass is
  about clarity, not content.
- Rewriting the spec's Intent so that a cut looks justified.
- Removing a journal's fixed callouts, evidence labels, sources or hand-off.
- Making every paragraph identical in shape. Narrative and case sections keep
  their rhythm.
- Leaving heading-anchor links, `[[…]]` links or figure numbering broken.
- Editing several posts in one pass. This skill works on one post at a time.
