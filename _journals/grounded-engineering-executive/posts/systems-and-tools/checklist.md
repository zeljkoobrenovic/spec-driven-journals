---
timetoread: "8 min read"
---
*The working checklist behind this principle — the full fifteen-tool inventory from* An Elegant Puzzle. *The Article tab carries the rationale, implications, and anti-patterns.*

## 1. Use Systems Thinking for Management Problems

- [ ] Identify the **stocks** in the system: accumulated quantities such as managers, trained managers, pull requests, incidents, technical debt, or available time.
- [ ] Identify the **flows** that change those stocks: hiring, training, departures, coding, review, deployment, recovery, debugging.
- [ ] Label every flow as a **rate**, not a quantity.
- [ ] Look for **feedback loops** where downstream outcomes affect upstream work.
- [ ] Separate **causal relationships** from mere correlations.
- [ ] Identify which stock or flow is currently the real constraint.
- [ ] Avoid optimizing a rate that does not matter because its downstream stock is already empty or blocked.
- [ ] Use the model to test hypotheses before committing to work.

## 2. Manage Product Work Through Exploration, Selection, and Validation

### Problem discovery

- [ ] Explore users' pain points: what problems do they actually experience?
- [ ] Explore users' purpose: what are users trying to accomplish?
- [ ] Benchmark against similar companies or industries.
- [ ] Look for hidden cohorts with unusual or surprising needs.
- [ ] Identify areas where your company has unusual strengths.
- [ ] Identify competitive moats or advantages.
- [ ] Look for compounding leverage: work that becomes more valuable over time.

### Problem selection

- [ ] Ask what is needed to **survive the current round**.
- [ ] Ask what is needed to **survive the next round**.
- [ ] Ask what would help you eventually **win rounds**, not only survive them.
- [ ] Consider different time frames: six months, two years, five years.
- [ ] Consider industry trends and where they are heading.
- [ ] Estimate return on investment, especially for quick or easy wins.
- [ ] Identify experiments that will make future selection easier.

### Solution validation

- [ ] Write a customer letter or launch announcement before building.
- [ ] Identify prior art and how peers have approached the problem.
- [ ] Find reference users who are willing to be early users.
- [ ] Prefer experiments over analysis when validation is cheap.
- [ ] Find the fastest path to learning whether the solution works.
- [ ] Test switching costs for users moving to the solution.
- [ ] Avoid building the whole solution merely to validate it.

## 3. Create Strategies and Visions

### Strategy

- [ ] Define the specific challenge the strategy addresses.
- [ ] Write a diagnosis that clearly explains the challenge.
- [ ] Identify constraints and trade-offs.
- [ ] Define guiding policies for addressing the challenge.
- [ ] Translate policies into concrete actions.
- [ ] Keep the strategy practical, specific, and detailed.
- [ ] Write as many strategies as are useful, but avoid unnecessary documents.

### Vision

- [ ] Define the future state where today's trade-offs are no longer mutually exclusive.
- [ ] Write a short vision statement.
- [ ] Define the value proposition for users and the company.
- [ ] Identify capabilities needed to deliver the value proposition.
- [ ] Name current constraints that the future state resolves.
- [ ] Name future constraints that may appear.
- [ ] Link relevant plans, metrics, and reference materials.
- [ ] Synthesize the vision into a short narrative.
- [ ] Test the document with others and iterate.
- [ ] Refresh the vision periodically.
- [ ] Use present tense.
- [ ] Write simply.
- [ ] Prefer one unified vision for each complete area.

## 4. Define Useful Metrics and Goals

- [ ] Ensure every goal has a **target state**.
- [ ] Include a **baseline** showing where you are today.
- [ ] Include a **trend** showing current velocity.
- [ ] Include a **time frame** for the change.
- [ ] Check whether someone unfamiliar with the area can judge the goal's difficulty.
- [ ] Check whether success can be evaluated afterward.
- [ ] Distinguish **investment goals** from **baseline goals**.
- [ ] Pair investment goals with counterbalancing baseline metrics.
- [ ] Keep investment goals few enough to drive planning discussions.
- [ ] Carry baseline goals across planning cycles where useful.
- [ ] Treat some baselines as contracts, especially when tied to SLOs.

## 5. Use Metrics to Guide Broad Organizational Change

- [ ] Start by exploring the data in a usable format.
- [ ] Dive into the largest contributors or drivers.
- [ ] Attribute each metric to the teams that can affect it.
- [ ] Build context around each team's performance.
- [ ] Benchmark teams against relevant peers.
- [ ] Nudge teams with contextual information, not just dashboards.
- [ ] Agree on baseline metrics with key teams.
- [ ] Review performance monthly or quarterly.
- [ ] Advocate for prioritization when teams lack agreed-upon baselines.
- [ ] Minimize top-down orchestration where self-correction is possible.

## 6. Run Technical Migrations Well

### Decide whether migration is needed

- [ ] Confirm the migration is the best path to reduce technical debt.
- [ ] Confirm the migration creates technical leverage or capacity.
- [ ] Recognize that large migrations often trade short-term contribution for long-term capacity.
- [ ] Avoid pretending technical debt can be solved only through isolated teamwork.

### De-risk

- [ ] Write a design document.
- [ ] Test the design with teams likely to have the hardest migration.
- [ ] Iterate with edge cases and atypical patterns.
- [ ] Test against the next six to twelve months of roadmap.
- [ ] Embed with one or two challenging teams before broader rollout.
- [ ] Get endorsement from a team that completed the migration.

### Enable

- [ ] Build self-service tooling where possible.
- [ ] Make the migration incremental and reversible.
- [ ] Document the process clearly.
- [ ] Test documentation with real teams.
- [ ] Prefer programmatic migration for the easy 90%.
- [ ] Improve tools and docs before scaling the migration.

### Finish

- [ ] Stop the bleeding by ensuring new work uses the new approach.
- [ ] Avoid generating tracking tickets too early.
- [ ] Add visibility into migration status for teams and management.
- [ ] Push status to teams that need to migrate.
- [ ] Reserve recognition for successful completion, not only starting.
- [ ] Drive to 100% adoption when deprecating the legacy system.

## 7. Plan an Engineering Reorg

### Validate that a reorg is the right tool

- [ ] Confirm the problem is structural.
- [ ] Make sure you are not avoiding a people-management issue.
- [ ] Confirm the problem already exists.
- [ ] Check whether the conditions are temporary.
- [ ] Avoid reorgs that merely work around broken relationships.

### Project headcount

- [ ] Estimate an optimistic number based on what is barely possible.
- [ ] Estimate a natural-size number for each team and role if they were fully staffed.
- [ ] Estimate a realistic number based on historical hiring rates.
- [ ] Merge these into one planning number.
- [ ] Avoid overfitting the design to today's exact individuals.

### Set manager-to-engineer ratio

- [ ] Decide whether managers are expected to do hands-on technical work.
- [ ] Use a lower ratio if managers do substantial technical work.
- [ ] Otherwise target roughly five to eight engineers per manager.
- [ ] Pick a ratio deliberately, probably in the six-to-eight range.

### Define teams and groups

- [ ] Write a crisp mission statement for each team.
- [ ] Check whether each team would be exciting to join and manage.
- [ ] Put teams that need to work together close to each other.
- [ ] Define clear interfaces for each team.
- [ ] List ownership areas for each team.
- [ ] Create a gapless ownership map.
- [ ] Avoid implicit holes of ownership.
- [ ] Prepare compelling candidate pitches for each team.
- [ ] Check whether the design over-optimizes for individuals.

### Staff the structure

- [ ] Identify people ready to fill roles now.
- [ ] Identify people who can grow into roles in time.
- [ ] Identify possible internal transfers.
- [ ] Identify external hires needed.
- [ ] Prefer people who already know the culture.
- [ ] Maintain a spreadsheet of every person, current team, and future team.
- [ ] Make sure nobody is accidentally omitted.

### Commit and roll out

- [ ] Confirm the changes are meaningfully net positive.
- [ ] Check whether the structure will last at least six months.
- [ ] Name the problems discovered during design.
- [ ] Identify what might trigger the next reorg.
- [ ] Identify who will be most impacted.
- [ ] Explain the reasoning behind the reorganization.
- [ ] Document how each person and team will be impacted.
- [ ] Provide availability and empathy for impacted individuals.
- [ ] Speak privately with those most heavily impacted first.
- [ ] Prepare managers and key individuals to explain the reasoning.
- [ ] Send written documentation.
- [ ] Be available for discussion.
- [ ] Prefer small-group discussion over large all-hands when emotions are high.
- [ ] Double down on skip-level one-on-ones.

## 8. Identify Your Leadership Controls

- [ ] Decide where you need to engage and where you should hang back.
- [ ] Choose controls appropriate to the team size and the leader-relationship.
- [ ] Use metrics to align on outcomes while preserving flexibility.
- [ ] Use visions to align on long-term direction.
- [ ] Use strategies to align on constraints and approaches.
- [ ] Use organization design to align wider sub-organizations.
- [ ] Use headcount and transfers as a prioritization mechanism.
- [ ] Use roadmaps to align on problem selection and solution validation.
- [ ] Use performance reviews to coordinate culture and recognition.
- [ ] Agree on the required degree of alignment for each control:
  - [ ] "I'll do it."
  - [ ] Preview.
  - [ ] Review.
  - [ ] Notes.
  - [ ] No surprises.
  - [ ] Let me know.
- [ ] Establish clear interfaces with the leaders you support.
- [ ] Use inability to delegate as a signal that you may be micromanaging.

## 9. Build Career Narratives

- [ ] Avoid reducing career development to promotion ladders.
- [ ] Help people identify broad long-term goals.
- [ ] Identify gaps between current capabilities and future aspirations.
- [ ] Translate goals into projects, research, relationships, and skills.
- [ ] Use the manager's business context to find opportunities.
- [ ] Ask the individual to participate actively rather than outsource the thinking.
- [ ] Refresh the narrative quarterly or periodically.
- [ ] Prioritize goals for the next three to six months.
- [ ] Focus on disproportionate opportunities, not only contested career-path steps.

## 10. Communicate with Media or Public Audiences

- [ ] Answer the question you want to be asked.
- [ ] Reframe difficult questions into ones you can answer constructively.
- [ ] Stay positive.
- [ ] Avoid being pulled into negative framing.
- [ ] Speak in threes.
- [ ] Repeat the same three concise points as your refrain.

## 11. Use Model, Document, Share

- [ ] Model the practice locally with your own team first.
- [ ] Measure team health and throughput before changing the process.
- [ ] Iterate until you are confident the approach works.
- [ ] Document the problem, learning process, and adoption details.
- [ ] Make the document specific enough for another team to adopt.
- [ ] Ask others to review the documentation for clarity.
- [ ] Share the approach and your rollout experience.
- [ ] Do not lobby for change prematurely.
- [ ] Avoid using this approach to circumvent organizational authority.
- [ ] Use it when slow adoption of a great approach is better than fast adoption of a good-enough one.

## 12. Design Centralized Decision-Making Groups

### Decide whether to centralize

- [ ] Identify the consistency problem you are trying to solve.
- [ ] Decide whether the group should be **authoritative** or **advisory**.
- [ ] Understand which positive freedoms the group creates.
- [ ] Understand which negative freedoms the group removes.
- [ ] Avoid centralizing merely because inconsistency feels uncomfortable.

### Design the group

- [ ] Define the group's influence.
- [ ] Define how teams interact with the group.
- [ ] Choose a size small enough to operate effectively.
- [ ] Decide expected time commitment.
- [ ] Decide whether members should identify primarily with the group.
- [ ] Define a structured selection process.
- [ ] Define term length.
- [ ] Decide whether terms are fixed or permanent.
- [ ] Decide how representative the group must be.
- [ ] Include the right functions, teams, tenures, and perspectives.

### Watch failure modes

- [ ] Avoid **domineering** groups that reduce both positive and negative freedoms.
- [ ] Avoid **bottlenecked** groups that try to do too much.
- [ ] Avoid **status-oriented** groups whose value becomes recognition rather than contribution.
- [ ] Avoid **inert** groups that do little.
- [ ] Embed a manager who is responsible for iterating on the group's format.

## 13. Present to Senior Leadership

- [ ] Start with the conclusion.
- [ ] Tie the topic to business value.
- [ ] Explain why anyone should care in one or two sentences.
- [ ] Establish historical narrative: how things are going, how you got here, and what is planned next.
- [ ] Make an explicit ask.
- [ ] Provide a data-driven diagnosis.
- [ ] Show enough raw data for others to follow your analysis.
- [ ] State decision-making principles.
- [ ] Explain how principles lead to the proposed actions.
- [ ] Explain what is next and when it will be done.
- [ ] Return to the explicit ask at the end.
- [ ] Prepare for detours.
- [ ] Answer directly.
- [ ] Go deep enough in the data to handle unexpected questions.
- [ ] Discuss details when needed, but avoid getting trapped in irrelevant detail.
- [ ] Prepare a lot; practice a little.
- [ ] Make the goal of the meeting clear.

## 14. Manage Time Deliberately

- [ ] Run a quarterly time retrospective.
- [ ] Categorize the past three months of calendar time.
- [ ] Use the retrospective to adjust next quarter's allocation.
- [ ] Prioritize long-term success over short-term quality when trade-offs are necessary.
- [ ] Finish small, leveraged things.
- [ ] Stop doing work that should be dropped, recategorized, or delegated.
- [ ] Size work backward from available time.
- [ ] Decide how many hours can be spent, then fit the work to that limit.
- [ ] Delegate work "in the system," not only individual tasks.
- [ ] Build systems that allow others to handle the work.
- [ ] Trust the systems you build.
- [ ] Stop handling exceptions forever.
- [ ] Decouple meeting attendance from productivity.
- [ ] Do not assume attendance equals value.
- [ ] Hire before you are overwhelmed.
- [ ] Calendar-block focused work.
- [ ] Add several two-hour focus blocks each week.
- [ ] Get administrative support when complexity justifies it.

## 15. Build Communities of Learning

- [ ] Prefer facilitation over lecturing.
- [ ] Keep presentations brief.
- [ ] Leave most time for discussion.
- [ ] Use small breakout groups.
- [ ] Give each group a clear discussion prompt.
- [ ] Regroup and share learning from each breakout.
- [ ] Choose topics people already know about or encounter in daily work.
- [ ] Encourage senior or tenured people to attend.
- [ ] Provide optional pre-reads for people who dislike public first exposure.
- [ ] Start with a short check-in when useful.
- [ ] Ask each person for their name, team, and one sentence about what is on their mind.
- [ ] Keep the format lightweight and repeatable.
- [ ] Design the group so participants learn from each other, not only from the facilitator.
