---
status: accepted
revised: 2026-09-25
---

# Spec: PART III — Turning Investor Expectations Into Commitments

## Intent

Connect the owner’s proposed business outcome to product choices, engineering commitments and company capacity. Explain what changes across learning, expansion, debt and integration scenarios.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the existing header logo. Give every configured chapter its own box, use short recognizable title labels without duplicating chapter numbers, and connect the chapters to the part's overall purpose. Each box's second line, the band labels and the alt text use ordinary words a newcomer can follow without the later chapters (rented computing, restoring service after failure, artificial intelligence spelled out and its three questions named in verbs rather than counted, buying or splitting off a business). The diagram carries a short key stating what artificial intelligence does, so it reads standalone.
- Keep the six chapters in three moves: choose and justify work, assess what delivery requires, then apply the reasoning to cloud, resilience and AI. The three applications share a method; none is a prerequisite for the next. The hiring, layoff, system-change and acquisition chapters belong to Part IV (SCALE), and the closing line hands off to Part IV and then Part V.
- Generate the overview through the Gemini API, matching the book's ivory, navy, teal and ochre illustration style. Publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export. Keep the linked chapter walkthrough as the full-title reading guide.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Make the company leader’s decision, authority and funding assumptions explicit: recall that Part II established who decides and which approvals are needed, and say that this part works within those limits and returns for a decision when a limit or assumption must change. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Orient a beginner using ordinary language, briefly recall what the previous part established, and explain the next learning step without assuming later vocabulary. Explain investor, thesis and the three planning questions (expected benefit, how long the available money covers the work, which other work must wait) in plain words at first use; give the planning example concrete actors (customer setup, a corporate owner's sister companies). The investor definition must not imply that the company necessarily receives the money: an investor may fund the company or buy shares from an existing owner, consistent with [[customers-lenders-investors]]; because a newcomer may not know the word, say in passing that shares are units of ownership. Describe each chapter through the question it answers, one line each. Where the build-expanded chapter title or the chapter line introduces a term a newcomer cannot follow (headcount versus capacity, backups, artificial intelligence), give a one-clause functional explanation in that line, written as a complete sentence or clause with clear boundaries rather than a comma splice or a chain of colons: headcount as the number of employees against the work the team can complete, backups as saved copies of data, artificial intelligence as software that predicts or generates content from data, with its three questions stated as what customers might pay for, which staff work might improve and whether a rival product could replace yours.
- Say why the part exists and what its chapters do together, in under 400 authored words (each `[[…]]` chapter link counted as one word; title, byline and alt text excluded). The build expands the ten links to their full chapter titles, which adds roughly 75 rendered words; that rendered total is reported, not capped, because the chapter titles are owned by the chapters. The opening states the practical learning outcome rather than announcing an introduction, and does not repeat the previous part title.
- Walk the chapters in order, one line each, showing why that order. Name each chapter by its linked title rather than a number, so the list survives renumbering.
- State what the reader should be able to do by the end — and, where it matters, what the part will not give them.
- Hand off to the next part in the closing line.

## Non-goals

Summarising the chapters' arguments, which would make the part introduction a substitute for reading them. No new claims, no evidence of its own, no worked examples.

## Modalities

Article with one chapter-overview diagram. These are short orientation pieces; a TL;DR of a 400-word introduction would duplicate it, and a comic would imply an argument the piece does not make.

## Open questions

None for the agreed part structure. Introductions remain unnumbered; chapter reading positions follow the configuration, and existing permalinks remain stable.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- **2026-09-13: Added as unnumbered part openers.** The author asked for an introduction chapter per part. Unnumbered was chosen over numbered so that no existing chapter renumbers and every cross-reference and reading route keeps working.
- Length capped at ~400 words so an introduction cannot start competing with the chapters it introduces.

## Sources

The journal's current config.yaml and the configured chapter introductions. These pieces describe the book's own structure and make no external factual claims.

## Changelog

- 2026-09-25 (contents): [[have-your-numbers-ready]] added after [[adopt-outcome-thinking]] in the first move; the learning path now has seven chapters in four moves (2+3+1+1); Figure 1 regenerated (round 5), alt text and caption updated.
- 2026-09-24 (contents): [[adopt-outcome-thinking]] added as the first chapter, in a new first move “Agree what the work is for”; the learning path now has six chapters in four moves, alt text and caption updated, closing line begins with the new chapter; overview to be regenerated with six cards; kept under 400 words.
- 2026-09-24 (part order and contents): COMMIT is now Part IV (folder `part-4-intro`, permalink `part-4`). Chapters: set priorities, test revenue assumptions, clarify AI strategy (moved back in from the new SUSTAIN part as an investment-choice chapter), assess capability, manage funding delays (moved in from LEAD). Learning path in three moves (choose and justify, assess what delivery requires, revise when the money is late); overview regenerated three times during the day to match; opening recalls Parts II and III; closing hands off to Part V (SCALE) and Part VI (SUSTAIN).
- 2026-09-24 (Part IV SCALE): Three chapters ([[fix-decisions-before-hiring]], [[growth-into-design]], [[acquisition-adds-work-first]]) moved to the new Part IV. Learning path reduced to six chapters in three moves (the middle move is now the capability assessment alone), overview alt text, caption and figure regenerated, closing hand-off names Part IV then Part V. Permalink unchanged.
- 2026-09-23: In-depth review round 3 (P3-006 to P3-008). Shares are explained as units of ownership at the investor definition; the planning example opens directly with the customer-setup case; the headcount and artificial-intelligence guide lines are written with clear sentence boundaries. Word cap, permalink, chapter order, grouping and the overview diagram unchanged.
- 2026-09-23: In-depth review round 2 (P3-005, P3-002). Investor definition must not imply the company receives the money (funding the company or buying an existing owner's shares). Chapter lines explain headcount versus capacity, backups and artificial intelligence functionally, with the three AI questions stated in verbs; the overview diagram names the AI questions and carries a one-line key on what AI does (regenerated). Word cap, permalink, chapter order and grouping unchanged.
- 2026-09-23: In-depth review round 1 (P3-001 to P3-004). Plain-language criteria added: explain investor, thesis and the three planning questions at first use; make the planning example concrete (customer setup, sister companies of a corporate owner); recall Part II's decision authority as the bridge into commitments; describe each chapter through the question it answers; restate the 400-word cap as authored words with each chapter link counted once (the rendered titles add about 75 words); plain second-line labels, band labels and alt text on the overview diagram (regenerated). Permalink, chapter order and three-move grouping unchanged.
- 2026-09-22: Add one visual chapter framework at the author's request, showing the learning connections and the part's shared outcome. Generate an image through the Gemini API as explicitly requested, with alt text and a caption; retain the linked walkthrough and stable permalinks.
- 2026-09-16: The organization chapter’s line notes that it also tests an investor-proposed appointment.
- 2026-09-15: Widen the closing handoff to Part IV to “help from the investor or another source”; the three-move grouping and the level of detail of the learning path are preserved. Permalink unchanged.
- 2026-09-14: Group the nine chapters into three moves (choose and justify work; assess and change the delivery system; apply the reasoning to operating choices) and reflect the new order in which fix-decisions-before-hiring follows can-the-team-deliver. Permalink unchanged.
- 2026-09-14: Retitle the post from “PART III — Turning Investor Expectations into Commitments” to “PART III — Turning Investor Expectations Into Commitments”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Align the specification heading with the current part-introduction title.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Chapter walkthroughs changed from "**Chapter N** does X" to linked titles. Numbers were duplicated state that would silently rot if a chapter moved; the build renders link text from the target's title, so this stays correct automatically.
- 2026-09-13: Created.
