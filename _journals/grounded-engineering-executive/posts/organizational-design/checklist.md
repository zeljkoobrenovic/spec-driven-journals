---
timetoread: "4 min read"
---
*The working checklist behind this principle. The Article tab carries the rationale, implications, and anti-patterns.*

## Choose the Right Lever

- [ ] Is this a quick, cheap problem? Use **process design**.
- [ ] Is this a long-term problem that will take time to solve well? Evolve **culture**.
- [ ] Are process and culture both relevant? Use **organizational design** to bridge them.

## Size Teams Deliberately

### Manager load

- [ ] Each engineering manager supports roughly **6–8 engineers**.
- [ ] Managers with fewer than 4 engineers are not stuck as accidental tech leads.
- [ ] Managers with more than 8–9 engineers are not merely acting as coaches/firefighters.
- [ ] Managers-of-managers support roughly **4–6 managers**.
- [ ] Managers-of-managers with fewer than 4 managers are in an active ramping/transition phase, not a permanent state.

### Team size

- [ ] Each team is large enough to operate independently.
- [ ] On-call teams have around **8 engineers** for a sustainable 24/7 rotation.
- [ ] Teams with fewer than 4 people are treated as temporary exceptions.
- [ ] Empty teams are not created.
- [ ] New teams are created by growing an existing team to 8–10 people, then splitting into two teams of 4–5.
- [ ] Managers are not left supporting more than 8 individuals for long periods.

## Diagnose Each Team's State

- For each team, mark its current state:

- [ ] **Falling behind**: backlog grows every week.
- [ ] **Treading water**: critical work gets done, but no debt repayment or major new work starts.
- [ ] **Repaying debt**: technical debt is being reduced, and compounding benefits are beginning.
- [ ] **Innovating**: debt is low, morale is high, and most work satisfies new user needs.

## Apply the Right System Fix

### If the team is falling behind

- [ ] Add people until the team can tread water.
- [ ] Avoid stealing people from other fragile teams.
- [ ] Set expectations with users and stakeholders.
- [ ] Celebrate easy wins and maintain optimism.

### If the team is treading water

- [ ] Reduce work in progress.
- [ ] Consolidate effort so more work gets finished.
- [ ] Limit concurrent projects.
- [ ] Help individuals shift from personal productivity to team-level throughput.

### If the team is repaying debt

- [ ] Add time, not necessarily people.
- [ ] Protect space for debt repayment.
- [ ] Keep users and stakeholders informed so debt work remains visible.
- [ ] Prevent the team from slipping back into backlog growth.

### If the team is innovating

- [ ] Maintain slack.
- [ ] Avoid overloading the team just because it appears healthy.
- [ ] Ensure innovation work is valued by stakeholders.
- [ ] Preserve quality, learning, and long-term adaptability.

## Consolidate Investment

- [ ] Prioritize one constrained team at a time.
- [ ] Do not spread limited resources thinly across many teams.
- [ ] Staff one team until it reaches the next healthier state, then move to another.
- [ ] Allow teams to alternate between growth periods and consolidation periods.
- [ ] Avoid disrupting a team's gelling process with constant staffing changes.

## Avoid Harmful Global Optimization

- [ ] Do not casually move people out of high-performing teams.
- [ ] Treat high-performing teams as scarce and valuable.
- [ ] Account for re-gelling costs when moving people.
- [ ] Avoid moving teams below the size needed for on-call or core responsibilities.
- [ ] Preserve slack in teams that have earned it.
- [ ] Prefer shifting scope to teams over moving people between teams.
- [ ] Use temporary rotations when help is needed elsewhere.

## Manage Hypergrowth Carefully

### Hiring and training

- [ ] Check whether hiring is slowing down the existing team.
- [ ] Track how much time trained engineers spend interviewing.
- [ ] Track how much time trained engineers spend onboarding new hires.
- [ ] Give interviewers periodic breaks when they exceed about three interviews per week.
- [ ] Avoid growing faster than training systems can absorb.

### Organizational scaling

- [ ] Add a new management layer for each additional order of magnitude of engineers.
- [ ] Add teams for roughly every 8–10 engineers.
- [ ] Watch for increased load on deployment tools, incident response, planning, and coordination.
- [ ] Recognize that systems often survive only one order of magnitude of growth without redesign.

### Entropy control

- [ ] Ensure some projects finish.
- [ ] Concentrate on hiring and growth rather than spreading it evenly across the board.
- [ ] Funnel interruptions into a smaller area.
- [ ] Automate repetitive interruptions.
- [ ] Create useful documentation and documentation search.
- [ ] Build ownership registries so people know who owns what.
- [ ] Avoid unnecessary rewrites.
- [ ] Keep interfaces stable during system rewrites.
- [ ] Treat gatekeeping as an implementation bug, not a stability feature.

## Manage Organizational Risk

- [ ] Identify sources of organizational debt.
- [ ] Track risks such as toxic culture, painful processes, struggling leaders, or inequitable mechanisms.
- [ ] Pick a few areas to improve deliberately.
- [ ] Agree with your manager on what constitutes reasonable progress.
- [ ] Give yourself permission to handle some lower-priority risks poorly.
- [ ] Stabilize one team or area before moving focus elsewhere.
- [ ] Delegate only risks that are realistically solvable.
- [ ] Keep ownership of risks that are unlikely to go well.

## Build Succession Plans

### Identify what you do

- [ ] Review your calendar and list your recurring meeting roles.
- [ ] List your calendar roles outside meetings, such as planning or candidate closing.
- [ ] Review the past six months of recurring processes.
- [ ] Document your role in each recurring process.
- [ ] List where your reports depend on your skills, authorization, advice, or organizational knowledge.
- [ ] Audit inbound chats and emails for recurring requests.
- [ ] Review your to-do list for work you keep postponing.
- [ ] Identify external relationships important to your role.

### Close the gaps

- [ ] Identify people who could already take over each responsibility.
- [ ] Cross off responsibilities that already have a clear owner.
- [ ] For remaining items, identify people who could eventually take them over.
- [ ] Separate easy gaps from risky gaps.
- [ ] Close easy gaps first with documentation or a quick handoff.
- [ ] Choose one or two risky gaps to actively reduce.
- [ ] Add the plan to your personal goals.
- [ ] Repeat the succession exercise at least once a year.
