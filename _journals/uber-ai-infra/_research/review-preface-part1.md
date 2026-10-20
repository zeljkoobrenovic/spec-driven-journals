# Review: Preface (thesis, timeline) and Part I (01–04)

Reviewed 2026-10-20 against the reviewer brief, style guide, PLAN and fact ledger. Quotes spot-checked against the transcript; the 38-second context-graph example (Aug 2026 blog) checked with WebFetch; the NSDI '26 "4,000+ fail-close dependencies" checked in the paper text. Build OK; render check OK. The only unresolved links go to `the-retrofit-playbook` and `system-catalog`, which are not written yet.

## the-harness-is-the-easy-part
- A failure mode said the host had noted that engineers approve PRs without reading them. The transcript does not support this (it is a sponsor read and an LGTM remark). **Fixed**: the attribution is removed.
- The "elastic numbers" paragraph left out the ~10% earnings-call figure that the ledger lists. **Fixed**.
- LiteLLM was described as "in the Trial ring since late 2024". **Fixed**: now "since October 2024", per the brief.
- The third lead paragraph previewed the chapter at length. **Fixed**: tightened.
- Length is about 6,100 words against the 4,500 Preface limit. **Left**: most of it is the dependency-map and properties tables, which carry the chapter, not repetition.
- Format, evidence labels and the quotes checked otherwise (Orosz's intro line, "self-validate", "maintenance kind of tasks", "carry forward"): all fine.

## timeline
- The title said 2015–2026 while the entries start in 2014. **Fixed**: retitled to 2014–2026 in the front matter and the spec heading. The permalink is unchanged. Spec decision log and changelog updated.
- KEY POINTS said the foundations came "seven to ten years" before the AI systems, but Slate (2022) precedes its agent use (2026) by four years. **Fixed**: now "four to ten years".
- The Model Gateway row said the "late 2013" slip was "corrected in the episode". It is not. **Fixed**: the date is now inferred from Medisetty's reference to ChatGPT.
- `PLAN.md` still says "2015–2026". **Left**: the file is outside my folders.
- The opening label is `IN THIS PAGE, YOU WILL:`, as the spec specifies. **Left** as is.

## 01-build-what-does-not-exist
- The build/buy/open-source quote was about 45 words and rebuilt with inserted brackets ("[we build], [otherwise]"), which changed the meaning of an ambiguous line. **Fixed**: replaced with a paraphrase plus two short, accurate quotes.
- The lifecycle table gave Cadence's open-source date as "Before 2019". **Fixed**: now "2017 (per its repository)", matching the timeline.

## 02-monorepos-and-one-build
- The service-count paragraph claimed the count "stayed in the 4,000–6,000 range since 2017", which contradicts the chapter's own 2019–2020 figure of 2,200+. **Fixed**: rewritten per the ledger (counts depend on what is counted; plateau, not decline).
- The paragraph also put "about the same number of services" in quotes, which is not verbatim. **Fixed**: now the transcript's "similar ballpark of number of services".
- The AGENTS.md quote ran over 40 words. **Fixed**: trimmed.
- The claim that in 2018 the monorepo "let a platform team upgrade a library in every Go service at once" is not documented. **Fixed**: softened.

## 03-devpods
- The Sources groups used bold labels instead of `###` headings. **Fixed**.
- The cloud list left out Uber's own data centers. **Fixed**: added next to Oracle Cloud and Google Cloud.
- Quotes checked against the transcript: all fine.

## 04-contracts-and-context-propagation
- PLAN says the mesh reads the baggage, but the chapter never covered that step. **Fixed**: added Medisetty's mesh-routing description and the documented Muttley sidecar name (Oct 2026 MCP blog). Which component acts on the routing overrides today is flagged as unknown.
- The Lyft citation included process wording ("could not be fetched"). **Fixed**: removed.
- The Sources headings had the same bold-label problem as 03. **Fixed**.

## For the author
- Update PLAN.md's timeline title to 2014–2026.
- Decide whether the thesis page should be cut toward the 4,500-word Preface limit.
