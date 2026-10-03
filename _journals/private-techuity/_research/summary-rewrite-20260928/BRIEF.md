# Summary rewrite brief (28 Sept 2026)

Author's request: the chapter summaries (`summary.md`, the TL;DR tab) have become hard to read and feel randomly
structured — crammed with inline definitions and every detail review passes asked for. Rewrite each to be fluent,
conversational and logical as a whole. They do NOT have to cover 100% of index.md — just the key points and
examples. Polish, and remove every needless sentence and word. Regenerate the summary image to be more detailed,
so a reader can grasp the key concepts from the picture alone.

Reference example (done): `posts/05-understand-cash-flow/summary.md`, its prompt
`_research/summary-rewrite-20260928/05-understand-cash-flow.json` and the image it produced.

## Writing the summary

- Read `index.md` (the source of truth), the current `summary.md`, and the spec's Intent. Never edit index.md.
- 300–500 words of prose (count excludes the figure line and caption; aim ~380–470). No heading, no front matter
  unless the file already has some (keep it then).
- Shape: one bold opening sentence or two stating the chapter's core idea → the figure + caption → a flowing
  narrative: the problem/question, the key insight, ONE worked example (usually fictional Rotaline, with the
  article's own numbers), the decision or practice that follows, a caveat or trade-off if it matters, and a final
  sentence that hands over to the next chapter with a `[[permalink]]` cross-link (keep the next-chapter link the
  current summary uses).
- Conversational: plain words, short-to-medium sentences, "you"/"the company" voice, connectives that carry the
  reader from one paragraph to the next. Paragraphs over bullets; a short list only if the content is genuinely a
  list. 2–5 bolded phrases total, for skimming.
- Explain a term in plain words only if the summary actually uses it; drop terms the summary doesn't need.
  No parenthetical definition chains.
- Every number, name, role and claim must come from index.md. Do not invent figures, dates or recurring costs;
  keep the Rotaline shared scenario exactly as the article states it. Keep any fictional scenario labelled fictional.
  For case-study chapters (real companies) keep sourced facts precise and within the article's source scope.
- Keep existing `[[…]]` links only where useful; they must be real permalinks (check front matter of targets).

## Regenerating the image

1. Write `_research/summary-rewrite-20260928/<post-folder>.json` with keys `asset`, `aspect_ratio` ("16:9"),
   `scene`, `alt`, `caption` (see the 05 example). `asset`: if the summary already points at a
   `.../summary-at-a-glance.jpeg`, reuse that exact path (relative to the post folder). If it points at an article
   figure instead, use `assets/images/<post-folder>/summary-at-a-glance.jpeg` (new file; leave the article figure alone).
2. Scene: a detailed editorial infographic, 2–3 zones in reading order (e.g. contrast / steps / flow / options /
   timeline), concrete drawn objects, 10–18 short UPPERCASE labels. Numbers only where they are the chapter's key
   figures and appear in your summary. End with `TEXT: draw exactly these labels, each once and nothing else: … Any
   other text is a defect.` Describe positions and which icon sits where so nothing is ambiguous.
3. Generate: `python3 _research/regen-summary-visuals-20260928.py generate <post-folder> --out <SCRATCH>/<post-folder>-a.jpeg`
   (run from `_journals/private-techuity`; `GEMINI_API_KEY` is in the env; each call takes ~1 minute).
4. INSPECT the candidate with the Read tool: every label spelled exactly, no extra/duplicated text, no stray numbers
   or currency signs, arrows point the right way, the concept reads correctly. If defective, adjust the scene
   (be more explicit about the failed part) and regenerate (-b, -c …; at most 4 tries; pick the best).
5. Accept: `python3 _research/regen-summary-visuals-20260928.py accept <post-folder> <candidate> "<short review note>"`.
6. In summary.md the figure line is `![<alt>](<asset>)` then `**Figure 1:** *<caption>*`, placed right after the
   opening bold sentence(s), exactly like the 05 example.

## Spec and close-out

- After the summary is written: `python3 _research/spec-note-summary-20260928.py <post-folder>`.
- Do NOT run the site build or manuscript export (the coordinator does it once). Do not commit. Do not touch
  other posts, index.md, comics, dialog, checklist, or the shared archive JSON by hand.
- Word count check: `python3 -c "import re,sys;t=open(sys.argv[1]).read();t=re.sub(r'^!\[.*\n\*\*Figure.*\n','',t,flags=re.M);t=re.sub(r'\[\[[^\]]*\]\]','x x x x',t);print(len(t.split()))" posts/<folder>/summary.md`
- Report per post: word count, accepted candidate, any image defects you accepted, and anything doubtful.
