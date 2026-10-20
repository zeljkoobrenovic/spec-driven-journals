---
name: sharpen-post
description: Make one post less vague and easier to follow. Works iteratively on a whole index.md (or modality file): first the opening, so it says why the post belongs in its book or journal, then the section-heading outline, then the paragraph order within each section, then the first sentence of every paragraph, then the sentences themselves. Writes in a plain, simple style, cuts needless words, and prefers deleting vague or confusing content to adding new content. May also tighten the post's spec.md when it is vague or out of step with the sharpened post. Use when asked to sharpen, tighten, de-vague, simplify, clarify or cut down a post in _journals/*/posts/*/.
---

# Sharpen Post

## Goal

Make one post **sharp**. A reader who reads only the opening knows why the
post belongs in its book or journal, not just what it covers. A reader who
reads only the section headings knows what the post covers and in what order.
A reader who reads only the first sentence of each paragraph gets a faithful
summary. Every remaining sentence
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
  You may delete a whole quotation when it adds nothing, but never edit words
  inside one, and report every quotation you delete.
- **Text that mirrors another page counts as quoted text.** This includes:
  - another page's title, excerpt or key point repeated in this post (common in
    part intros, hand-offs, toolkits and tables of chapters);
  - a term defined in the glossary;
  - a heading name that another page cites.

  Leave its wording alone even when it is vague. If it should change, change it
  at its source, and report that instead of editing it here.
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
- **Settled heading decisions win.** If the journal has
  `_research/heading-decisions.md`, read it before renaming any heading. It
  lists the fixed headings, and the variations the author has decided to
  keep. Do not rename a heading against it. If you think a decision is wrong,
  report that instead.
- **Parallel pages share headings.** Books often give pages of the same kind
  the same section names: case studies, part intros, the "Setting the Scene"
  or worked-example sections of chapters. Before renaming a heading, compare
  it with two or three sibling pages:

  ```bash
  python3 .claude/skills/sharpen-post/scripts/skeleton.py <sibling>/index.md --headings
  ```

  If the siblings use the same heading, it is part of the house shape. Keep it,
  and sharpen the paragraphs under it instead.
- **Headings may be referenced from elsewhere, by link or by name.** Before
  renaming a heading, make two checks:
  - links: run `grep -rn "<permalink>.html#" _journals/`. If a link points at
    the heading, keep the anchor working with an explicit id, or update the
    link;
  - plain-text mentions: run `grep -rnF "<old heading text>" _journals/<journal>/`
    to find prose such as "see the Layer Map" or captions that name the section.
    Inside this post, update the mention. In another page, keep the old heading,
    or report the mention so the author can update it;
  - pointers by position: moving or deleting a section can strand phrases such
    as "the final section", "the next section" or "below", in this post or in
    a page that links to it. `factcheck.py` lists them when the outline
    changed; confirm each one, fix those in this post, and report the others.
- Edit only the requested file and its `spec.md`. Report problems in other
  pages instead of fixing them.

## Tool

`scripts/skeleton.py` prints a post's skeleton. It skips front matter, code,
diagrams and tables. For a paragraph that opens with a bold run-in label
(`**Data.**`), it shows the label plus the sentence after it.

`scripts/factcheck.py` compares the post with its last committed version (or
`--base REF`). It reports what was lost or changed:
- every number, date, `[[link]]`, URL, evidence label, callout label and
  quotation whose count fell;
- every number word in prose ("three", "dozen") whose count fell, with the old
  sentences that held it and the closest new sentence, so a rewording can be
  told from a lost fact;
- any number word that changed in a heading, such as "four stages" becoming
  "five stages";
- figure captions that no longer run 1, 2, 3 in order;
- when the outline changed, positional pointers ("the final section", "below")
  in this post and in other posts that link to it.

It exits with status 1 when anything is flagged.

```bash
S=.claude/skills/sharpen-post/scripts
python3 $S/skeleton.py <file.md> --headings   # the outline only
python3 $S/skeleton.py <file.md>              # headings + first sentence of every paragraph (P1, P2, …)
python3 $S/skeleton.py <file.md> --stats      # headings, paragraphs, prose words
python3 $S/factcheck.py <file.md>             # what was lost compared with HEAD
```

If the post has uncommitted changes from before this pass, note the commit or
copy you started from and pass it as `--base`. Otherwise those earlier changes
are counted as part of this pass.

## Workflow

### 0. Baseline

1. Read `spec.md`, then the whole post once.
2. Record `--stats` as the baseline.
3. In one sentence, write down what the post argues. If you cannot, find that
   sentence first: the spec's Intent or the post's KEY POINTS usually hold it.
   Every later cut is judged against it.
4. If the post belongs to a book-shaped journal, write down in one sentence
   why the book needs this chapter. A book-shaped journal has parts, part
   intros, or an introduction that states an argument. Use these sources:
   - the journal's `config.yaml` description;
   - the introduction or opening guide;
   - this part's intro;
   - the book's PLAN or README, if one exists;
   - the hand-offs in the previous and next posts.

### 1. Place in the book (the opening)

A reader who reads only the opening elements should see why this chapter is
in the book, not just what it is about. The opening elements are the title,
the excerpt, any fixed callouts or KEY POINTS, and the lead paragraphs before
the first section. A post that could sit unchanged in any blog has lost its place in
the book.

Check that the opening answers three questions, in plain words:

1. **Which question of the book does this chapter answer?** Tie it to the
   book's argument, or to the problem its part addresses. A sentence such as
   "Search is important for marketplaces" is not enough. A sentence such as
   "A marketplace's liquidity is wasted if buyers cannot find the supply Part
   III brought in; this chapter is where finding begins" is.
2. **What does it build on?** Name the earlier chapter, concept or running
   example the reader already has. Use a `[[link]]` where it helps.
3. **What depends on it?** Name what later chapters, decisions or the running
   example will use from this one.

How to make the opening answer them:

- **Strengthen what is there.** Make the lead paragraphs or the "why it
  matters" callout carry the answers. Usually one or two sentences are
  enough. Do not add a new section or a new callout type.
- **Prefer replacing a generic opener to adding text.** Many leads start with
  a sentence true of any system ("Search is at the heart of every
  marketplace"). Replace it with the book-specific reason.
- **Use the book's own vocabulary.** Use the terms of its argument, its named
  failure patterns and its running example. Do not invent a new framing.
- **Keep it short.** The opening states the chapter's place in the book; it
  does not retell the previous chapter.
- **Standalone journals need less.** For a journal of standalone records (ADRs,
  principles, essays), the opening should still say why the record matters to
  that journal's purpose and name its closest related records. It does not
  need a part-level framing.

**Check the title and excerpt against the book's terms.** They appear on the
index page, in every cross-link and in search results, so a stale term there
is the most visible one in the post. Compare them with:
- the glossary;
- the scenario ledger or another canonical facts file;
- the post's own headings and body.

You may edit the excerpt, under the same rules as the lead. **Do not change
the title.** It is the author's, and changing it renames every cross-link to
the post. Instead, report the mismatch and suggest a wording, for example:
"title says Sunday Night; the ledger and the post say Sunday evening". Never
touch `permalink:`.

Do not move the chapter's place in the book. If the post's role and its
neighbors' hand-offs disagree, align the opening with the plan and report the
mismatch.

### 2. Section flow (headings only)

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

### 3. Paragraph order (per section)

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

### 4. First sentences (the skim path)

Run the full skeleton and read the `P1, P2, …` lines alone, top to bottom.

- **Each first sentence states its paragraph's point**, as a claim the reader
  could disagree with. It is not a teaser, a question, a transition ("However,
  there is more to it.") or scene-setting.
- **Bring buried points forward.** If a paragraph's point appears in its third
  sentence, restructure the paragraph so that point comes first, then the
  support.
- **The P-lines together summarize the post.** Where one does not follow from
  the one before it, the problem is the paragraph order (step 3), not the
  wording.
- **Keep narrative paragraphs as they are.** Scenes, case narratives and quoted
  dialogue may open with action, but the paragraph that interprets a scene
  states its point first.

### 5. Sentences (vagueness and needless words)

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

### 6. Iterate, then verify

1. Re-run steps 1–4 on the edited post. Edits often expose a new ordering or
   topic-sentence problem. Repeat until a full round produces no structural
   change. Stop after **three rounds**.
2. Run `--stats` and compare it with the baseline. Use the word count as a
   check against padding, not as a target. Never cut a fact to reach a number.
   Expected change by kind of post:

   | Kind of post | Expected change in prose words |
   | --- | --- |
   | Essays, concept chapters, explanations | Usually fall 10–30% |
   | Fact-dense case studies, evidence-heavy chapters | Often fall less than 5%; the gain is in structure and openings |
   | Part intros, hand-offs, toolkits, references | About flat; often only a few sentences change |

   If the count rose by more than about 2%, review every addition and keep
   only what the flow needs.
3. Run `factcheck.py` and resolve every `LOST` or `CHANGED` line in one of
   three ways:
   - restore the item, if the cut was accidental, or a number was dropped
     while rewording a sentence;
   - list it in the report as a deliberate cut, with the reason;
   - for a changed heading number, confirm the section's content and list it
     as a checked correction (for example "the table lists five stages").

   Then read the `git diff` once for what the script cannot see: names, claims
   and house-shape elements.
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
- each **deleted passage that carried a claim**, and every deliberate cut that
  `factcheck.py` reported, with a one-line reason, so the author can restore
  it;
- plain-text references in other pages to a heading you renamed;
- how the opening now states the chapter's place in the book, or why it
  already did;
- any mismatch between the title and the book's terms, with a suggested title
  (the title itself is left unchanged);
- anything left vague because fixing it needs facts the post does not have.
  These are questions for the author.

When `sharpen_journal.sh` runs the skill, its prompt also asks for a closing
`REPORT … END REPORT` block (title, deleted claims, questions), which the
script copies into `results.md`.

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
- Cutting facts to hit a word-count target.
- An opening that explains the topic but never says why this book needs the
  chapter, or a generic first sentence that would fit any blog post on the
  subject.
- Editing a quotation, or wording that mirrors another page's title, excerpt or
  glossary entry.
- Finishing without running `factcheck.py`, or with `LOST` lines left
  unexplained.
- Editing several posts in one pass. This skill works on one post at a time.
