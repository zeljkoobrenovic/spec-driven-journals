---
timetoread: "6 min read"
---
*The working tool behind this record. The Article tab carries the rationale and anti-patterns.*

## 1. First, try to solve locally

- [ ] Confirm the decision is reversible or tunable — most are
- [ ] For reversible decisions, optimize for speed: decide and iterate
- [ ] Ask: does this really matter? Will time and iteration get to a good endpoint either way?
- [ ] Ask: can the people doing the bulk of the work move forward on a path the dissenters could commit to, even if it isn't their first choice?
- [ ] If yes to either, resolve locally — do not escalate
- [ ] Recognize when a decision is a multi-constituency call that is important and not easily reversed — some debate time is warranted here
- [ ] If debate does not quickly produce a decision, kick off the unblocking process

## 2. Know when instigating is your duty

- [ ] Remember: unblocking is not bad — slow, unclear, or bad decisions are bad
- [ ] For meaningful, irreversible decisions, involve people responsible from "both sides" rather than let the decision hinder forward progress or move in the wrong direction
- [ ] Recognize the real cost of staying blocked: lost productivity and diminished happiness on both sides
- [ ] If you are blocked by an unresolved decision, treat instigating this process as your duty
- [ ] Commit to resolving the issue within five business days of kicking off the process
- [ ] If the block is a lack of data, commit instead to agreeing how to answer within five days of the data becoming available

## 3. Document the disagreement together

- [ ] Co-write one short document with the other party — half a page is enough
- [ ] Field: the problem to be solved, described as the goal of the joint enterprise, in the voice of the user
- [ ] Field: the options considered
- [ ] Field: the trade-offs both parties see between the options
- [ ] Within the trade-offs, highlight the ones that could not be resolved without further help
- [ ] If writing the document produces agreement on its own, stop here — no escalation needed

## 4. Escalate the document

- [ ] If the document does not resolve the disagreement, email it to your managers
- [ ] If the two authors report to different managers, send it to both managers
- [ ] Expect the managers to decide together, or to call a meeting if needed
- [ ] If escalating to a single manager, expect them to make the decision
- [ ] If escalating to multiple managers, expect them to decide together
- [ ] If the managers cannot agree, expect them to raise the issue with their own respective managers recursively — adding context to the doc as needed — until a decision is reached (or the stack overflows)

## 5. Keep it bilateral by default

- [ ] Default to co-authoring and co-escalating the document together
- [ ] If one party declines to unblock jointly, inform them you will do it alone
- [ ] Invite the other party once again to bring the matter up together before going alone
- [ ] Only after the reluctant party continues to refuse, unblock unilaterally, copying the other party throughout

## 6. Recognize a unilateral request when you see one

- [ ] Check: are you raising an issue with a manager that you know or suspect the other party disagrees with?
- [ ] Check: might their feedback be presented as a decision to that person or group without them present?
- [ ] If yes to both, treat it as a request to unblock unilaterally
- [ ] The other party should be present for the discussion whenever possible

## 7. Manager gate: the three questions before hearing a unilateral case

- [ ] Question 1 — Have you and your colleague tried to resolve this using constructive negotiation? If no, send them back to try that first.
- [ ] Question 2 — Have you tried the unblocking process and written the disagreement document with your colleague? If no, send them back to do that first.
- [ ] Question 3 — Did you tell your colleague that if they didn't use the unblocking process, you would bring the problem to the manager alone? If no, send them back to tell the colleague first.
- [ ] Only proceed once all three answers are yes
- [ ] Even with three yeses, message the missing colleague and ask them to attend
- [ ] Hold the line: it is not acceptable to refuse to unblock jointly — this is the cultural norm the gate exists to protect

## 8. Worked example fields (fictional Charlie/Alice case)

- [ ] Situation: Charlie (widget team) and Alice (storage team) report to different managers (Chun and Aiden), who share a manager (Bharath)
- [ ] Trigger: Charlie needs encryption at rest for new PII storage; Alice's team has it on their roadmap but not yet built; the two disagree on whether the widget team should build its own storage layer to hit a two-month launch deadline
- [ ] Step 1 — Charlie raises the disagreement with his manager, Chun, who asks whether constructive negotiation was tried; Charlie confirms it was, so Chun points him to the escalation process
- [ ] Step 2 — Charlie and Alice co-write the disagreement document, framing it around the shared question "what are we really trying to do?"

**Escalation document template (adapt per disagreement):**

| Field | Content |
| --- | --- |
| Title | Name the alignment decision, e.g. "\<Team\> alignment model" |
| Authors | Each author, with their team |
| Date | Date the document was written |
| Goal | The shared objective, stated in the user's voice, e.g. "Deploy a system that meets \<requirement\> in a timely fashion." |
| Decision sought | The precise question to be resolved, with the relevant deadline |
| Options considered | Each option, labeled A, B, C… |
| Trade-offs | Per option: the case for it and who contributed which points; flag where the authors could not agree |

- [ ] Step 3 — Charlie and Alice jointly email the document to both managers (Chun and Aiden)
- [ ] Step 4 — the managers meet, review the document, ask clarifying questions, and edit it for completeness
- [ ] Step 5 — if the managers still can't agree, they escalate the same document to their shared manager (Bharath), with both original authors copied — treat this as the exception, not the norm
- [ ] Step 6 — the deciding manager reviews the document, makes the call, and documents the rationale in reply to the escalation email
- [ ] Step 7 — everyone involved commits to following the resulting course

## 9. Close the loop

- [ ] Confirm the decision and rationale are written down, not just spoken
- [ ] Confirm both original parties have committed to the resulting course
- [ ] Confirm the resolution happened within the five-business-day window (or the data-driven equivalent)
- [ ] Note anything about the process itself worth improving before the next disagreement
