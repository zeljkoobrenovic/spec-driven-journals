---
timetoread: 9 min listen
---

## Why should I care?

**Ben:** Let me open with the obvious one. Your AI agent just produced a beautiful product-domain model — pages of customer groups, capabilities, bricks, roadmaps. Why isn't that the win? Why is there a whole closing article about what happens *after*?

**Ana:** Because polish is not trust. The first job of a product architecture model is not to be impressive — it is to be reviewable. An agent can produce a plausible model in an afternoon. The question that decides whether it's worth anything is: can a human challenge it? Can a reviewer tell which claims are sourced facts, which are assumptions, and which are the agent's educated guesses dressed up as facts?

**Ben:** And the answer is usually no?

**Ana:** Usually no, unless you build the discipline in. That's what this article closes the series with: evidence discipline, grounding, deterministic validation, and a publishing loop where the generated site is output, never source.

**Ben:** "Grounding" — that's the word from the opening article, right? Dreaming, exploring, grounding.

**Ana:** Exactly the frame from [[what-is-spec-driven-product-architecture]], and deliberately so. Dreaming defines the intended product architecture — vision, customer value, capabilities, bricks, teams, roadmap. Exploring reads reality: source code, cloud activity, delivery logs, finance, incidents, ownership, analytics. Grounding is the join between the two. The series opens by naming the three activities and closes by making the third one operational.

## Facts, assumptions, and everything between

**Ben:** Start with evidence then. What does "evidence discipline" actually mean when an agent is modeling a real company or market?

**Ana:** It means the model separates four kinds of statements: sourced facts, explicit assumptions, informed inferences, and open questions. The trouble is that product architecture naturally mixes public facts, internal knowledge, and architectural judgment. An agent may look at observed product behavior and infer a plausible product brick or capability. That inference might be good! But it must not be presented as a sourced fact.

**Ben:** Give me a concrete failure.

**Ana:** Metrics are the classic one. A company reports a platform-wide revenue number, and the model quietly rewrites it as a domain-specific revenue number. Or a market report uses a particular scope and year, and the model drops the scope. Each rewrite sounds more precise and is actually less true. The rule is: preserve the original scope, and if no public metric exists, use an assumption — but only a *visible* one.

**Ben:** Doesn't all this labeling slow the work down? You're asking the agent to footnote everything.

**Ana:** It's not about slowing the work down — it's about making later review possible at all. An unlabeled model can only be accepted or rejected wholesale. A labeled one can be challenged line by line.

## The grounding join

**Ben:** Okay, grounding. Connect it to something I can picture.

**Ana:** Every important concept in the model should either connect to evidence or be marked as an assumption. A capability connects to customer evidence or product analytics. A product brick connects to repositories, services, cloud assets, APIs, data assets, operational workflows. A team-ownership claim connects to activity, incident, financial, or accountability signals. In the rendered docs, a brick literally points to repository-analysis cards — source-code size, commits, cost signals.

**Ben:** And those cards decide the architecture?

**Ana:** No — that's the important nuance. The evidence doesn't decide anything. It gives reviewers concrete signals to challenge or support the model. Grounding does not remove judgment; it gives judgment a better substrate. This is where the approach connects to Grounded Architecture's data-led practice: build lightweight tools and maps over real data so architecture work can see what is actually happening.

**Ben:** What do you actually get for the effort?

**Ana:** Three things. It reveals concepts that are aspirational but not yet supported by reality — the dream that hasn't landed. It keeps the model current as systems, teams, costs, and activity patterns change. And it exposes trends: where investment is growing, where architecture is drifting, where ownership is unclear, where the product architecture is becoming more or less coherent.

**Ben:** Early models are mostly aspiration, though. If I ground a brand-new domain, won't half the concepts fail the test?

**Ana:** Then half the concepts get marked as assumptions, and that's a feature. The first version does not need to be perfect — it needs to be structurally coherent enough that the next session can improve it. What it must not do is hide which half is the bet.

## What a validator can and cannot prove

**Ben:** Now the validators. I'm suspicious of any claim that a script can validate strategy.

**Ana:** Good — because it can't, and the article is blunt about it. Validation cannot tell whether the product strategy is good. It can tell whether the source model is *broken*. A scoped validator checks JSON parsing, duplicate IDs, brick ownership, team dependencies, staffing consistency. Mechanical drift, not strategic quality.

**Ben:** Then why bother making it a gate?

**Ana:** Because it changes the authoring standard for agents. An agent shouldn't only produce text that sounds plausible — it should leave behind source that can be parsed and checked. Structured JSON, stable lowercase IDs, schema recognition, consistent references. Mechanical validation is the floor. But a model with no floor isn't worth a human's review time.

**Ben:** So what stays with the humans?

**Ana:** All the questions that matter most. Whether the selected domain is the right boundary. Whether customer groups are strategically meaningful. Whether jobs to be done reflect real customer progress. Whether KPIs measure the right things. Whether a brick is a good ownership boundary, whether a team topology is politically and operationally realistic, whether the roadmap sequence fits business constraints. No validator will ever answer those. The structured model exists to make that human review easier — not unnecessary.

## Output, not source

**Ben:** The publishing part sounds almost too obvious to need a rule. Generate a docs site from the source. Where's the trap?

**Ana:** The trap is the day a stakeholder spots a wrong sentence on a rendered page and someone fixes it *on the page*. The site looks better; the model that future agents and generators depend on is now wrong, and the next generation run silently reverts the fix or forks the truth. The generated site turns the model into pages product leaders and engineers can scan — that's its whole value. But it is output, not source.

**Ben:** So the loop is...

**Ana:** Author or edit source files, validate, generate documentation, review the rendered pages, and return to source when the rendered story exposes gaps. Five steps, always in that order. That's the same source-first rule the series established in [[product-domain-as-source-of-truth]] — publishing is where it pays off or breaks.

## Your first session

**Ben:** Say I'm convinced and I have a Monday morning free. What does a good first modeling session look like?

**Ana:** Deliberately structured, ten steps. Choose a clear domain and a lowercase slug. Gather source links and internal context. Have the agent inspect the repository guidance, mature comparable domains, generators, templates, and skills — [[modeling-diverse-domains]] is the pattern library for that step. Have it propose the domain scope *before* creating files. Then create the source files, populate customers, jobs, KPIs, strategy, delivery, capabilities, bricks, teams, objectives, roadmap, evidence, and business context to a useful first depth. Validate. Generate documentation only when the source is coherent enough to review. Review the pages, return fixes to source, and record assumptions and gaps for the next session.

**Ben:** How do I know the draft is any good? "Coherent enough" is doing a lot of work in that sentence.

**Ana:** My favorite test in the whole article: a draft domain is useful when it supports *informed disagreement*. If reviewers can say "this customer group is missing," "this KPI is not measurable," "this brick is too broad for one team," "this release depends on a team that is not modeled" — those are good review comments. They mean the model is concrete enough to challenge. A model nobody can disagree with is a model nobody can review.

## What we're not claiming

**Ben:** Close it out. What is this article explicitly *not*?

**Ana:** It's not full validator documentation, it's not instructions for running every generator group, and it's not a taxonomy of external evidence sources. It's the closing frame: grounding connects dreaming and exploring, evidence stays separated from assumptions, validation catches mechanical drift, publishing keeps review shared, and humans keep the judgment.

**Ben:** And the payoff, in one breath?

**Ana:** Not a prettier documentation site — a living product-domain model that humans and AI agents keep improving together. Source-first, grounded, validated, published. Every session builds on the last, and the repository becomes a structured memory for product architecture work. That's the real promise of the series: not automatic strategy, but a better substrate for judgment.

**Ben:** Structured memory beats impressive fiction. I'll take it. *(laughs)*
