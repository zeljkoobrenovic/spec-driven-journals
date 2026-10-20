# Reviewer Brief — RETROFITTED review-and-fix pass

You are a demanding editor of **RETROFITTED** who knows Uber's public engineering record. Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/uber-ai-infra/` (ROOT). You review **and fix** your assigned pages directly.

## Read first

`ROOT/_research/style-guide.md`, `ROOT/PLAN.md`, `ROOT/_research/fact-ledger.md` (especially "Cross-source reconciliation" and "Additions by chapter"), then your pages (index.md + spec.md), then skim the neighbouring chapters your pages link to. Use the briefs (`ROOT/_research/brief-*.md`) and the transcript (`ROOT/_input/pragmatic-engineer-podcast/transcript.txt`) to check facts.

## Check and fix

1. **Evidence**: every Uber AI-era claim attributed (episode or dated written source); podcast numbers attributed; disputed numbers handled as the reconciliation table says; inferences labeled; no invented internals; no claim that the author has inside knowledge. Spot-check 3–5 key facts per page against the briefs; verify any doubtful one with WebFetch.
2. **Cross-chapter consistency**: the same fact stated the same way across your pages and their neighbours (dates, numbers, names, spellings from the corrections table: Claude Code, OpenCode, AIFX, uOwn, Shepherd, Medisetty …). No chapter re-teaching at length what another chapter owns — replace with a sentence and a `[[link]]`.
3. **Format**: front matter; the opening blocks with exact labels (IN THIS CHAPTER / WHY IT MATTERS / KEY POINTS with exactly three bullets / BUILT ON / `<br>`); required sections present (problem, what Uber built, foundation underneath, trade-offs table, elsewhere in the industry, if you are not Uber, failure modes, what the record does not say, questions to ask, handoff, Sources and Evidence with the closing sentence); Title Case headings; figure captions numbered in order.
4. **Prose**: cut generic or brochure sentences, repetition, filler, banned words (style guide list); plain declarative English; acronyms expanded on first use; quotes ≤ 40 words and accurate to the transcript meaning.
5. **Spec alignment**: the spec's success criteria are met; update spec `revised:` only if you change the spec; add a Changelog line to the spec when you make substantive changes to the article: `- **2026-10-20** — Review pass: <what changed>. *(AI-mediated session)*`.
6. Lengths: if a page is far over the limit because of repetition, cut; do not pad short pages.

Do not change `permalink:` values. Write only in your assigned folders (and append-only to the ledger). Do not edit config.yaml.

## Verify

`cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "uber-ai-infra|error|Traceback" | head` (a traceback in another journal's docs folder is a parallel-build collision — rerun), then `python3.11 /private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/feb98e04-fc5d-4fdb-beb5-554c2a2c1a91/scratchpad/render_check.py <permalinks…>` — all OK (unresolved links only to the not-yet-written `introduction`, `the-retrofit-playbook`, `system-catalog`, `glossary`, `bibliography` are acceptable).

## Report

Write your findings and the fixes you applied to `ROOT/_research/review-<part>.md` (short: per page, issues found → fixed / left with reason). Report back in under 150 words: pages reviewed, the most important fixes, anything left for the author to decide.
