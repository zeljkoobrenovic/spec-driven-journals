# Rule table

Each schema field and each outcome check, the guide it came from, and the rule
in one line. Field paths are relative to the schema named in the first column:
**C** = `common.schema.json`, **J** = `journal-spec.schema.json`,
**P** = `post-spec.schema.json`, **R** = `check-report.schema.json`.

## Sources

### The six guides named in the brief

| Short name | Guide | Read from |
| --- | --- | --- |
| Flow | UNC Writing Center, *Flow* | <https://writingcenter.unc.edu/tips-and-tools/flow/> |
| Transitions | UNC Writing Center, *Transitions* | <https://writingcenter.unc.edu/tips-and-tools/transitions/> |
| Thesis | UNC Writing Center, *Thesis Statements* | <https://writingcenter.unc.edu/tips-and-tools/thesis-statements/> |
| Paragraphs | UNC Writing Center, *Paragraphs* | Lumen Learning copy: <https://courses.lumenlearning.com/sunycorning1020elec201819/chapter/paragraphs/> |
| Introductions | UNC Writing Center, *Introductions* | Lumen Learning copy: <https://courses.lumenlearning.com/sunycorning1020elec201819/chapter/introductions/> |
| Conclusions | UNC Writing Center, *Conclusions* | Lumen Learning copy: <https://courses.lumenlearning.com/suny-englishcomp1v2/chapter/conclusions/> |

The UNC site answered HTTP 403 to automated requests for *Paragraphs*,
*Introductions* and *Conclusions* (the other three loaded). Those three were
read from course copies that credit "The Writing Center, University of North
Carolina at Chapel Hill" under CC BY-NC-ND. The copies may be older than the
live pages; the category names used below (the five weak introductions, the
four weak conclusions, the 5-step paragraph process) should be confirmed
against the live pages if exact wording matters.

### Sources added to fill gaps

| Source | What it contributed |
| --- | --- |
| Ohio State University Writing Center, *Paragraphs* (first page, "Functions of Paragraphs"): <https://cstw.osu.edu/sites/default/files/2020-07/paragraphs_0.pdf> | Five values of the paragraph `function` enum that the UNC guide does not name as functions: `definition`, `description`, `comparison`, `cause_effect`, `refutation`; and confirmation that a paragraph may exist only to move the reader between parts (`transition`). |
| This repository: `_wiring/spec-template.md` and the *spec-driven-authoring* foundation record | The `status` lifecycle (`draft`, `accepted`, `drifted`, `superseded`), the spec-first rule, and the requirement that criteria be checkable. |
| This repository: `.claude/skills/sharpen-post/scripts/skeleton.py` | An existing reverse-outline tool (headings plus the first sentence of each paragraph); the check step reuses its paragraph numbering as the draft locator. |

### Extensions with no external source

Nine enum values are additions of this design. Each is marked `(extension)`
in the schema, and none is attributed to a guide.

| Value | Enum | Why it was added |
| --- | --- | --- |
| `prerequisite_order` | flow pattern | Books in this repository order chapters so that each supplies the vocabulary the next needs. Flow describes this at sentence level (known before new) but lists no pattern for whole units; the list is "including (but not limited to)". |
| `problem_solution`, `comparison`, `order_of_importance` | flow pattern | Decision records and trade-off chapters use them; Flow's list does not name them. |
| `elaboration`, `problem_solution` | relationship | A unit that unpacks a term the previous one only named, and a unit that resolves a problem the previous one left open, fit none of the ten Transitions categories cleanly. |
| `direct_statement` | hook type | Decision- and principle-shaped records open with a Status/Decision highlight, which is none of the five opening options in Introductions. |
| `context`, `recommendation` | function | Scene-setting paragraphs, and paragraphs that give the author's labelled judgement, recur in every journal here. |

`counterargument` in the `function` enum comes from the brief itself.

## Intent and audience

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `intent.outcome.know / believe / can_do` | Conclusions; Thesis | State what changes for the reader: a conclusion should "propel your reader to a new view of the subject", and a thesis must survive "So what?". |
| C `audience.who` | Introductions | "Decide how general or broad your opening should be": the opening is sized to a named reader. |
| C `audience.already_knows`, `does_not_know` | Flow | Readers process known information faster than new, so the spec lists what may be assumed and what must be introduced first. |
| C `acceptance_criterion` | Thesis; repository spec template | "If your thesis and the body of your essay do not seem to go together, one of them has to change": every intent carries criteria that can be checked against the prose. |
| C `acceptance_criterion.method = cold_reader` | Introductions | "Ask a friend to read your introduction and then tell you what he or she expects the paper will discuss". |
| C `acceptance_criterion.method = reverse_outline` | Flow; Transitions | Outline "what you actually wrote, rather than what you planned to write"; summarize each paragraph in a word or short phrase in the margin. |

## Thesis

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `thesis.question` | Thesis | "Do I answer the question?" A thesis answers a question; it is "an interpretation of a question or subject, not the subject itself". |
| C `thesis.claim` | Thesis | One sentence that takes a specific position; no vague words such as "good", "successful", "positive and negative ways". |
| C `thesis.disputed_by` | Thesis | "Have I taken a position that others might challenge or oppose?" If nobody could disagree, it is a summary. |
| C `thesis.so_what` | Thesis; Conclusions | "Does my thesis pass the 'So what?' test?" Connect the claim to a larger issue. |
| C `thesis.how_why` | Thesis | "Does my thesis pass the 'how and why?' test?" Give the reader the line of reasoning, not an open-ended statement. |
| C `thesis.supporting_claims` | Thesis | "Does my essay support my thesis specifically and without wandering?" The claims the children must establish are listed so support can be checked. |
| C `role.contribution`, `role.supports` | Paragraphs; Thesis | Every unit is "clearly related to the thesis": it names the parent claims it argues for. |
| P `introduction.thesis_statement` | Thesis; Conclusions | The thesis is stated near the beginning, never "for the very first time in the conclusion". |

## Flow

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `flow.pattern` | Flow | "How am I ordering ideas? Can I describe the pattern?" Name one primary pattern: chronological, grouping, large to small or the reverse, assertion-evidence-reasoning, IMRD. |
| C `flow.additional_patterns` | Flow | A draft has one primary pattern and may use additional patterns inside sections. |
| checks `flow_order_is_sound`, `flow_is_followable` | Flow | Flow is "easy to read smoothly from beginning to end": the declared order is tested on its own before drafting, and the reader's experience of it is tested on the prose. |
| C `flow.rationale` | Flow | "Why are the ideas presented in this order? Would they make more sense if I reorder them? What effect does the order of ideas have on my readers?" |
| C `opening.roadmap`, P `introduction.roadmap` | Flow; Introductions; Thesis | Signpost near the beginning; the introduction is "a road map for the rest of your paper". |
| P `paragraph.organization` | Paragraphs | Order a paragraph's sentences by narration, description, process, classification or illustration. |

## Transitions

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `transition.relationship` | Transitions | Pick the logical relationship first, then the words: similarity, exception/contrast, sequence/order, time, example, emphasis, place/position, cause and effect, additional support or evidence, conclusion/summary. |
| C `transition.carries_over` | Transitions; Flow | A transition "summarizes the content of a preceding sentence, paragraph, or section"; known information comes first. |
| C `transition.introduces` | Transitions; Flow | It then "helps the reader anticipate or comprehend the new information". |
| C `transition.form` | Transitions | Between sections, a transitional paragraph; between paragraphs, a phrase or sentence; within paragraphs, a word or short phrase. |
| C `transition.placement` | Transitions | At the end of the first unit, at the beginning of the second, or in both places. |
| `transition_in` on every non-first child | Transitions | Transitions "cannot substitute for good organization": the relationship must exist between the two units before words are chosen for it, so it is declared in the spec. |
| P `conclusion.hand_off` | Transitions | A section-level transition says what was covered and why it matters for what follows; it must agree with the next post's `transition_in`. |

## Paragraphs and sections

| Field or check | Guide | Rule |
| --- | --- | --- |
| P `paragraph.controlling_idea` | Paragraphs | Each paragraph has one main idea, which "controls what happens in the rest of the paragraph" (step 1). |
| P `section.controlling_idea` | Paragraphs | The same unity rule one level up: a section establishes one idea. |
| P `paragraph.function`, `section.function` | Paragraphs (5-step process); OSU *Paragraphs*; the brief | A unit does one job: claim, explanation, evidence or example, analysis, and so on. |
| P `paragraph.evidence[].what` | Paragraphs | Step 3: give an example or other evidence for the idea. |
| P `paragraph.evidence[].shows` | Paragraphs | Step 4: "NONE of your examples should be left unexplained". |
| P `paragraph.advances_thesis`, `section.advances_thesis` | Paragraphs | Readers should see "a recurrent relationship between your thesis and the information in each paragraph". |
| P `paragraph.transition_in` | Paragraphs | Step 5: complete the idea or transition into the next paragraph; "transitions are needed within the paragraph" is a named problem. |

## Introduction

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `hook.type` | Introductions | "Open with something that will draw readers in": an intriguing example, a provocative quotation closely related to the argument, a puzzling scenario, a vivid and perhaps unexpected anecdote, a thought-provoking question. |
| C `hook.content` | Introductions | "Pay special attention to your first sentence": the spec holds the actual example or question, not a description of one. |
| P `introduction.bridge` | Introductions | Introductions "transport your readers from their own lives into the 'place' of your analysis". |
| C `opening`, P `introduction` authored from the thesis | Introductions | "Start by thinking about the question (or questions) you are trying to answer"; write the introduction once the argument is known ("Try writing your introduction last"). |

## Conclusion

| Field or check | Guide | Rule |
| --- | --- | --- |
| C `closing.synthesis`, P `conclusion.synthesis` | Conclusions | "Synthesize, don't summarize": show how the points fit together, do not repeat them. |
| C `closing.so_what`, P `conclusion.so_what` | Conclusions | Play the "So What" game: answer "Why should anybody care?" |
| C `closing.callback`, P `conclusion.callback` | Conclusions | "Return to the theme or themes in the introduction." |
| C `takeaway.type` | Conclusions | Leave the reader with a course of action, a solution, questions for further study, broader implications, or a provocative insight. |

## Record keeping

| Field or check | Guide | Rule |
| --- | --- | --- |
| `status`, `revised`, `changelog` | Repository spec template | A spec is `draft`, `accepted`, `drifted` or `superseded`; every change and status transition gets a dated line. |
| `non_goals` | Repository spec template; Thesis | Say what the unit deliberately leaves out, and where it is covered, so the prose supports its thesis "without wandering". |
| P `modalities` | Repository spec template | List the docs the spec drives beyond the main article. |
| `open_questions` | Repository spec template | Unresolved points stay until answered or moved to a follow-up record. |
| `decision_log` | Repository spec template | Record each shaping choice with the alternatives rejected. |
| `sources` | Repository spec template | Name what the spec was built from and what each source contributed. |

## Check catalogue

Checks are identified by the values of `check` in `common.schema.json`. The
first four run on the spec before any prose exists; the rest run on a draft.
Every standard check runs on every draft at its default severity; a spec lists
a check under `acceptance_criteria` only to change the severity, to add a
probe, or to add a `custom` criterion.

| Check | Runs on | Method | Default severity | Guide | Rule |
| --- | --- | --- | --- | --- | --- |
| `thesis_passes_tests` | spec | rubric | blocker | Thesis | The claim answers its question, can be disputed, is specific, and its `so_what` and `how_why` are not restatements of the claim. |
| `flow_order_is_sound` | spec | rubric | major | Flow | A reader given only the ordered ideas and the declared pattern confirms the order follows the pattern, that each item relies only on earlier ones, and that the stated reason says what would break if it changed ("Can I describe the pattern? Would they make more sense if I reorder them?"). |
| `children_cover_parent_thesis` | spec | deterministic | blocker | Thesis | Every supporting claim has a child that supports it (no gaps); every arguing child supports a claim (no orphans); no child cites an unknown claim. |
| `role_matches_journal_spec` | spec | deterministic | blocker | Thesis | The post spec's intent outcome, thesis and role equal the journal spec's entry for that post. |
| `intro_predicts_content` | draft | cold reader | major | Introductions | A reader shown only the introduction predicts the sections, the kind of evidence and the tone. |
| `reverse_outline_matches_spec` | draft | reverse outline | blocker | Flow; Transitions; Paragraphs | One-phrase summaries of the draft's paragraphs, written without the spec, match the spec's controlling ideas in the spec's order. |
| `one_controlling_idea_per_paragraph` | draft | reverse outline | major | Paragraphs | No draft paragraph needs two summaries ("the paragraph has more than one controlling idea"). |
| `paragraph_traces_to_thesis` | draft | rubric | major | Paragraphs | Each paragraph can be tied to a supporting claim of the post thesis; a paragraph that cannot is cut or moved. |
| `evidence_is_explained` | draft | rubric | major | Paragraphs | Every example, figure, table and quotation is followed by a sentence saying what it shows. |
| `transition_expresses_declared_relationship` | draft | rubric | major | Transitions | At each boundary the prose expresses the declared relationship and picks up the declared known information. |
| `known_before_new` | draft | rubric | major | Flow | No term is used before the audience knows it; sentences that open a paragraph start from something already introduced. |
| `flow_is_followable` | draft | cold reader | major | Flow | A reader of the prose alone can say what principle orders the sections and why each comes where it does, and reports no place where they lost the thread ("Readers should not have to stop, double back, reread, or work hard to find connections between ideas"). |
| `no_weak_introduction_pattern` | draft | rubric | major | Introductions | The introduction is none of: placeholder, restated question, Webster's Dictionary, "dawn of man", book report. |
| `no_weak_conclusion_pattern` | draft | rubric | major | Conclusions | The conclusion is none of: "That's My Story and I'm Sticking to It", "Sherlock Holmes", "America the Beautiful", "Grab Bag"; it does not open with "in conclusion", introduce a new idea or subtopic, end on a rephrased thesis alone, or hold evidence that belongs in the body. |
| `conclusion_synthesizes_and_answers_so_what` | draft | rubric | major | Conclusions | The conclusion states something no single section states, and says why it matters. |
| `conclusion_calls_back_to_introduction` | draft | rubric | major | Conclusions | The conclusion returns to the element of the introduction named in `callback.to`. |

**Corroboration.** `known_before_new` and `flow_is_followable` are open-ended:
they have no fixed list of things to find, and a fresh reader reports a
different small point on each pass. A failed result of either is major only
when a second, independent reader reported the same point (the result carries
`corroborated_by`); otherwise it is recorded as minor and does not block. The
draft-time flow check is therefore run with two readers. A spec that names one
of these checks in an acceptance criterion keeps the severity it states.

The six checks the brief requires map to: `intro_predicts_content`;
`reverse_outline_matches_spec`; `one_controlling_idea_per_paragraph` with
`paragraph_traces_to_thesis`; `transition_expresses_declared_relationship`;
`no_weak_introduction_pattern` with `no_weak_conclusion_pattern`; and
`children_cover_parent_thesis`.

"Sentimental, emotional appeals" appears twice in Conclusions (as a strategy to
avoid and as the "America the Beautiful" type); the enum has one value for it.
