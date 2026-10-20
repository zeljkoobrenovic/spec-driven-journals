# Review — Part III (LIFECYCLE), 2026-10-20

Pages: 11 plans-as-source-of-truth, 12 minion, 13 inner-loop-and-self-healing-ci, 14 slate, 15 capri, 16 code-review-signals, 17 shepherd-and-fox, 18 wisdom-and-debug-assist.

## Cross-chapter consistency (focus items)

- **Agent share of PRs:** canonical set used everywhere: ~10% of committed code (CEO, Fortune, May 2026); 11% of PRs opened (Pragmatic Engineer, 10 Mar 2026); 11% of merged PRs (Ramakrishnan, Background Agents Summit, 7 May 2026); ~15% of production PRs that "go through Minion" (episode, Oct 2026); 70%+ with any agent involvement (Uber blog, 27 Aug 2026). Ch.12 owns the reconciliation table; ch.11, 13, 14 and 16 now give one sentence and link [[minion]] (ch.16's duplicate table removed).
- **DebugAssist → Minion:** ch.12 now mentions the hand-off and links [[wisdom-and-debug-assist]]; ch.18 phrases it as in the transcript (the engineer judges the root cause right and hands off; Minion opens a PR attached to the Jira task holding the RCA) and dates the Sep 2026 MCPCon variant that opens PRs itself.
- **Slate dependency default:** ch.14 states once that the 2022 post says production dependencies by default and the episode says "the other staging setups", unreconciled; later mentions name their source. Ch.15's replay inference aligned to that; ch.18 does not touch it.
- **Pronouns:** "he/his" for Medisetty replaced in ch.11, 12, 13, 16, 17.
- **Render:** ch.16 state-diagram transition labels unquoted (quotes would show on the page). Build and render check: all eight OK.

## plans-as-source-of-truth (11)

- Pronouns for Medisetty ("his screen", "he said", "He also said", "he hands it") → fixed: surname or neutral wording.
- Agent-share sentence gave 11% (Mar) and ~15% without definitions → fixed: quotes "go through Minion", says the figures count different things, links [[minion]] for the reconciliation.
- Subheadings not Title Case → fixed (and "Plans as measurement substrate" → "Plans as the Basis for Measurement").
- PRD expanded as "product requirements document" in the lead but "product design doc" in the table; the episode uses both (Orosz: requirements; Medisetty: product design doc) → lead now "product requirements or design document".
- Quote "engine design doc" (transcript "engine design dog") → "[engineering] design doc".
- Spot-checks OK against transcript (hub contents, Jira/Linear links, "source of truth system for both humans and agents", heterogeneity rationale, minimal steering, Slack thread) and ledger (24M nodes/80M edges/30+ systems, Spec Kit 2 Sep 2025, Thoughtworks Assess Nov 2025, Stripe 9 Feb 2026).
- Format, required sections, figure numbering, closing sentence: OK. Length 5,300 words: in range. Spec Changelog line added.
- Left: the AI Engineer talk is cited by a different URL slug here than in the devpods chapter (both appear in the ledger); not in my scope to unify.

## minion (12)

- DebugAssist → Minion hand-off missing → fixed: short "third entry point" paragraph (engineer accepts DebugAssist's RCA, Minion creates the PR and attaches it to the Jira task with the RCA; the Sep 2026 MCPCon abstract variant opens PRs itself), linked to [[wisdom-and-debug-assist]]; MCPCon abstract added to Sources (title matching chapter 18); spec internal sources updated.
- Reconciliation table text said "the first four rows count authorship", but row 4 is the AAIF volume/adoption figure → fixed wording.
- Failure mode "agents were part of the cause" of CI code red was unsupported → now quotes Medisetty ("doubled or more than doubled", "influx of PRs").
- "Nikhil Ramakrishnan of Uber's AI Foundations and Developer Experience group" not confirmed in the briefs → "Uber engineer Nikhil Ramakrishnan". Ty Smith given a role clause (principal engineer, per brief).
- Pronouns ("He also described", "His example") → surname. Subheadings → Title Case.
- Spot-checks OK: 15% / Minion v2 / plan mode / one-shot / mega DevPod / maintenance-first / self-validate (transcript 196–204); Fortune, PE, Ramakrishnan, AAIF, Aug blog figures and dates match the ledger.
- Format, sections, figures, closing sentence: OK. Length ~5,300 words: in range. Spec Changelog line added.
- Left: DevPods date sentence in "Iterations and Lineage" is close to but not word-for-word the ledger phrasing; meaning matches, left as is.

## 13-inner-loop-and-self-healing-ci

Spot-checked against the transcript: the "code red" / "doubled or more than doubled" quote, the `aifx validate` rule list, "per PR or all the PRs" self-healing, the "beef up … foundations" quote, the review-bottleneck quote and Fox's "every Sunday". All accurate.

- "he said" / "He did not say" referred to Medisetty → changed to the surname and "The episode does not say".
- British "licences" → "licenses".
- Agent-share bullet gave only 11% opened (Mar) → added 11% merged PRs (Ramakrishnan, Background Agents Summit, 7 May 2026) plus its Sources entry; the 15% now reads "go through Minion", with a [[minion]] link for the definitions.
- Odd Slate sentence ("environments, which own the end-to-end story") → "[[slate]] owns that story".
- Subheadings were in sentence case → Title Case. Sources groups were bold lines → `###` headings, as in the other chapters.
- Fox's Sunday scheduling is one bullet with a [[shepherd-and-fox]] link, so it is not re-taught. Left as is.
- Format, sections, figure numbering and spec criteria all OK. Length is about 5,350 words. Spec Changelog line added.

## 14-slate

Spot-checked against the transcript: "other staging setups", "took years … retrofitted", "self-validate", the Deputy/Cerberus routing description, Orosz's "took years to build" and the A/B report. Also checked against the 2022 facts in the ledger. All accurate.

- **Staging vs production default:** this is now stated once, plainly, in the episode bullet: the 2022 post says production instances, the episode says "other staging setups", and the question is unreconciled. Every later mention is now qualified or attributed to the 2022 post:
  - the trade-off table's dependencies row;
  - the Lyft comparison ("Uber's 2022 design isolates within production …");
  - the test-data-leak failure mode ("as in the 2022 design");
  - the "Record Does Not Say" bullet.
- The KEY POINTS and Figure 1 already say "shared fleet", which is neutral. Left as is.
- "Two corrections to the episode's dating" listed only one → "One correction".
- Unnamed "an Uber engineer at a May 2026 summit" → Nikhil Ramakrishnan, Background Agents Summit, 7 May 2026.
- Subheadings → Title Case.
- No he/him pronouns and no banned words. "Leverage" appears only in an Uber post title, which is allowed. Length is about 5,250 words. Spec Changelog line added.

## Neighbour check (not edited)

- 15-capri: its one Slate-dependency mention (line 79, the inference callout) already says the record is unsettled on staging vs production and links [[slate]]. Consistent.
- 18-wisdom-and-debug-assist: does not mention Slate's dependencies.

## capri (posts/15-capri/)

Spot-checked against the transcript (lines 256–282, 360–362) and the testing brief: the four steps, the "cash trips only in Brazil" quote, the SF Uber Eats replay, the "many versions" remark, Edge Gateway using Capri, Orosz's outro quote and the Ballast/Shadower details all match. Capri and MatchGuard are flagged as names that appear only in the podcast.

- KEY POINTS said earlier tools avoided in-process capture because it was "too hard to deploy everywhere". Shadower's stated reasons were complex filtering plus CPU and memory cost → fixed.
- The inference block said single-session replay runs "against the shared fleet", which glossed over the Slate dependency question → reworded to match [[slate]]: the record does not settle whether Slate routes to staging or production instances.
- The foundation table cited "Edge Gateway posts (2020, 2021)" but only the 2020 post is sourced → fixed.
- "closing remarks" → "the episode's outro". Expanded BITS and PII on first use. Title Case on the "Before and After" subheading.
- Spec: added a Changelog line. Length is about 4,400 body words, inside the limit. Left as is.

## code-review-signals (posts/16-code-review-signals/)

Spot-checked against the transcript (lines 216–230, 363–364), show notes line 61 and the agents/pre-AI briefs: the bottleneck quote, the "safer side" quote, the green-lane and P1/P0 quotes, the 1.4%/0.3% monorepo figures, the RADAR numbers, Faros and the LOC doubling all check out.

- "As he described it" and "He sets the priority" → changed to the surname, Medisetty.
- Paraphrase error: "When Orosz asks whether human review will always be needed". Orosz actually observed that engineers can no longer review every PR with the old rigor → fixed.
- The six-row agent-share table and the paragraph after it repeated the [[minion]] reconciliation → replaced with two sentences that keep the canonical figures and their definitions (11% opened, Mar 2026; 11% merged, May 2026; about 15% via Minion, Oct 2026; 70%+ any involvement, Aug 2026), plus a link. Kept the LOC and CI-doubling facts in one sentence with a link to [[inner-loop-and-self-healing-ci]].
- Over length. Measured as wc on the markdown, the article went from 6,532 to about 6,100 words. The body before Sources went from about 6,000 to 5,465 words. Cuts:
  - the lead that re-taught Minion, aifx, Slate and Capri
  - the uReview five-step list, folded into one paragraph
  - the RADAR, Google and Spotify paragraphs, trimmed
  - the "Risk score visibility" paragraph, which repeated green-lane reason 3
  - five filler table and diagram intro sentences, and duplicate "so the tool exists" sentences
- KEY POINTS stated as fact that blast radius "comes from" the Bazel graph and the tier gates. That is undocumented for Code Inbox → softened to "can be computed from …" with the gap stated.
- Format: Title Case on the two H3 subheadings; Sources groups changed from bold lines to ### headings; PR and LGTM expanded on first use; timetoread 24 → 22 min.
- Spec: success criteria still met; added a Changelog line.
- Left: the stateDiagram transition labels use quoted text (`: "…"`). They may render with visible quotes. The render check should confirm this; it is not changed here.

## 17-shepherd-and-fox

- Facts spot-checked against the transcript (lines 283–301) and brief-agents-review-ci §6: JUnit numbers (600K+ tests, 75,000+ classes, 1.25M+ lines, ~4 months, 5,000+ diffs, 2,000+ initial), failed generative-AI bulk attempt, Piranha (~2,000 flags; 1,381 flags, two-thirds unmodified), 250+ migrations/~9M lines, Fox on Sunday, opt-in → opt-out, "a few months ago", Port summary's Monday cap. All match → no change.
- Gendered pronouns for Medisetty ("his campaign example", "He framed", "His description", "he said") → fixed (surname/neutral).
- Over length (6,232 words) from repetition → cut ~400 words: PolyglotPiranha detail, the "AI lesson misread both ways" framing, planned next JUnit campaigns, Rosie and Spotify detail (Honk time-savings, 10–20% LSC share, file counts), a Jaeger foundation row and the campaign-owner trade-off row, a duplicated opt-out failure mode, the PR-tagging record gap (owned by feature-velocity), seven sequencing steps merged to five, the "what not to copy" paragraph shortened, one question removed. Now ~5,830 words including Sources.
- Opt-out criteria were stated as "a reasonable reading" → relabeled with the style-guide inference phrase.
- Subheading "The worked example: JUnit 4 to JUnit 5" → Title Case.
- No re-teaching of ch.13 (CI code red only referenced in one sentence with a link) or ch.12 → left.
- Spec: Changelog line added; success criteria still met.

## 18-wisdom-and-debug-assist

- Facts spot-checked against transcript lines 302–316 and brief-testing-debugging §8: Wisdom features, "huge problem to reproduce", network replay by bug UID, DebugAssist RCA/impact/evidence timeline, hand-off to Minion, PR attached to Jira with RCA, corrections as improvement data; MCPCon Japan abstract (Kriti Dangi, 11 Sep 2026: LangGraph, 11 MCP servers, ~30 min to PR, ~5,000 RCAs/month, 5% → 30%, opens PRs itself); Genie (154 channels, 48.9%, ~13,000 hours); DragonCrawl 85 of 89; show page names Wisdom among four day-to-day tools. All match.
- Hand-off phrasing: KEY POINTS said "an engineer accepts it" → now "once the engineer judges the root cause right, they hand it to Minion, which opens the PR and attaches it to the Jira task that holds the analysis"; lead paragraph and excerpt aligned the same way; body now quotes "okay, this is the right root cause". The talk variant is dated (Sep 2026 abstract) in KEY POINTS. Diagrams/captions were already consistent → left.
- The DebugAssist quote was ~43 words and paraphrased as verbatim ("we built… looks at all of this") → shortened to the transcript's words.
- "That is a good number for this kind of tool" (unsupported) and "deserves a moment" / "honest range" filler → cut.
- Three "as described" subheadings → Title Case.
- No gendered pronouns for Medisetty/Orosz found. Length 4,600 words → fine.
- Spec: Changelog line added; success criteria met.
- Outside scope (for the parent): ch.12 Minion does not mention DebugAssist as an entry point for hand-offs; the transcript (line 308) supports a one-line mention with a link to [[wisdom-and-debug-assist]].

## Left for the author

- Ch.11 and the devpods chapter cite the AI Engineer 2026 talk under two different URL slugs (both in the ledger); pick one canonical URL.
- Ch.16 (≈5,465 body words) and ch.17 (≈5,834 incl. Sources) remain near or slightly above the 5,500 limit after cuts; further trimming would remove substance, not repetition.
