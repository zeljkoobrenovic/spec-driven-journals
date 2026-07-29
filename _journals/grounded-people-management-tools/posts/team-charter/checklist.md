---
timetoread: "8 min read"
---
*The working tool behind this record. The Article tab carries the rationale and anti-patterns.*

## 1. Mission

- [ ] Write one to two sentences stating what the team does
- [ ] State it plainly enough that it forecloses multiple interpretations
- [ ] Confirm it covers the full scope of the team's responsibility, not just its best-known part

**Worked example (dashboard account-security team):** "Provide best-in-class security to all of our users and their accounts on the dashboard. This encompasses both authentication and authorization, including dashboard roles and permissioning."

## 2. Vision

- [ ] State the future the team is building toward
- [ ] Name what "success" looks like for the people the team serves
- [ ] Name what the team accepts it will never fully solve
- [ ] Name the "table-stakes" commitments the team delivers regardless of trade-offs

**Worked example:** "We aim to build strong trust internally and externally in our ability to provide best-in-class security for all of our users, from enterprises to small users, while avoiding overhead for our users and support team. Account takeovers will no longer be an active problem (neither as a terrible user experience nor as a financial loss). While we won't ever be able to get them to zero, we and our customers should have full faith that when they occur (e.g., through an internal bad actor on the customer side), we did everything within creative reasonability to prevent them. We will also deliver 'table-stakes' security features such that we fly through user security–related discussions with new enterprise customers."

## 3. Customers

- [ ] List who the team is responsible for, as concrete bullets
- [ ] Name what the team protects or provides on their behalf
- [ ] Avoid vague catch-alls ("our users") in favor of named groups

**Worked example:**
- We're responsible for the account security of every user and account, ensuring that their accounts and the sensitive data therein remain theirs alone.
- We protect the interests of all merchant accounts by enabling them to control who in their business can access what, and by protecting them from rogue actions.

## 4. Metrics

- [ ] List each metric the team is accountable to
- [ ] For each metric, state what it measures
- [ ] For each metric, state a target value — no metric without a number

| Metric | Measuring | Target value |
| --- | --- | --- |
| Number of accounts that experienced a takeover in a given month | User experience, risk of unhappy customer leak, support burden | [X] |
| Account takeover losses | Direct financial loss and loss of margin due to account security issues | [X] |
| Percentage of all dashboard users who have adopted two-factor authentication | Protection of entire user base from account takeovers | [X] |

- [ ] Reject any draft metric that ships without a target value

## 5. Strategic importance

- [ ] State why this team's work matters beyond its own scorecard
- [ ] Connect the team's work to company-level trust, risk, or growth
- [ ] Name any competitive or sales impact

**Worked example:** "Aside from the financial benefits of reducing losses, having better account security will improve the user experience and build user trust. Strong foundations here will help prevent attacks, bad user experiences, and losses, since we will become a target if we are not world-class. A strong track record will also increase the appeal of our products to enterprise users, open up new sales conversations, and accelerate existing ones."

## 6. Major risks

- [ ] List the team's major risks as short, named bullets
- [ ] Include distraction risk (lower-priority work pulling focus)
- [ ] Include catastrophic risk (major incidents)
- [ ] Include attrition-style risk (accumulating small asks, tech debt)

**Worked example:**
- Team gets pulled into lower-priority work by audit or compliance activities
- Major security breach
- Major new attack vectors
- Death by a thousand cuts of one-off enterprise requests
- Tech debt

## 7. Provided interfaces

- [ ] List what the team provides that other teams build on
- [ ] Keep the list short — if it needs twenty bullets, the boundary is wrong
- [ ] Make this list visible to teams that consume it

**Worked example:**
- Login code
- 2FA infrastructure
- Session infrastructure
- Login/email challenge
- Dashboard auditing models
- Account recovery/password reset flow

## 8. Dependent interfaces

- [ ] List what the team depends on from other teams
- [ ] Name the owning team or system for each dependency, not just the capability
- [ ] Treat every entry as a declared risk, not a footnote

**Worked example:**
- User registration UI
- Verificator (interface for SMS 2FA)
- User email system and team

## 9. Organizational foundations self-test

Fill in the same five rows for an individual report, for one team, and for the division. For each cell, ask: is this information documented anywhere in your division, and is it easy to find? If you're having trouble filling out this template, imagine how your teams and reports must feel.

| | Individual | Team | Division |
| --- | --- | --- | --- |
| **Mission** | | | |
| **Objectives (with owner / DRI)** | | | |
| **Key metrics** | | | |
| **Accountability mechanisms** | | | |
| **Operating cadence** | | | |

- [ ] Complete the Individual column for at least one direct report, from documentation alone
- [ ] Complete the Team column for at least one team, from documentation alone
- [ ] Complete the Division column, from documentation alone
- [ ] Flag any cell you could only fill in from memory, not from a findable document

## 10. Publish and maintain

- [ ] Publish the charter and the foundations table on the team's internal homepage
- [ ] Publish the same detail — top objectives and metrics with targets for the year — on the division's internal homepage, or at the top of the internal dashboard if separate
- [ ] Re-check that the published version still matches reality at each quarterly review
- [ ] Update the charter when mission, customers, metrics, or interfaces change — do not let the document go stale while the team's real work moves on
