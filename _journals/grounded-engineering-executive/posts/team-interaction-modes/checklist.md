---
timetoread: "4 min read"
---
*The working checklist behind this principle. The Article tab carries the rationale, implications, and anti-patterns. Use this checklist for each team-to-team relationship.*

## Define the Interaction Clearly

- [ ] Identify the teams involved.
- [ ] Identify each team's topology: stream-aligned, enabling, complicated-subsystem, or platform.
- [ ] Decide the intended interaction mode: **Collaboration**, **X-as-a-Service**, or **Facilitating**.
- [ ] Make the interaction explicit so teams know what behavior is expected.
- [ ] Define who owns what responsibilities.
- [ ] Define the expected communication channels and cadence.
- [ ] Avoid requiring every team to communicate with every other team.
- [ ] Revisit the interaction mode as technology, organization size, market needs, or team experience changes.

## Collaboration Mode Checklist

- Use **Collaboration** when teams need close joint work, rapid discovery, innovation, or learning.

- [ ] There is significant uncertainty or novelty.
- [ ] The teams need to discover new approaches, patterns, or boundaries.
- [ ] The work benefits from high adaptability.
- [ ] Both teams have useful expertise to combine.
- [ ] The teams can work with high interaction and mutual respect.
- [ ] Responsibility is intentionally shared for the outcome of the collaboration.
- [ ] The collaboration is time-boxed or clearly limited.
- [ ] The team is collaborating with **at most one other team at a time**.
- [ ] The teams understand that boundaries may blur temporarily.
- [ ] The expected benefit justifies the higher cognitive load.
- [ ] There is a plan to reduce collaboration once boundaries or APIs become clearer.

### Watch for

- [ ] Collaboration continuing too long.
- [ ] Too much shared responsibility with unclear ownership.
- [ ] Excessive meetings or context-sharing overhead.
- [ ] A sign that team boundaries may be wrong.

## X-as-a-Service Checklist

- Use **X-as-a-Service** when one team provides a component, API, platform, tool, or capability that another team can consume with minimal collaboration.

- [ ] The service boundary is clear and well chosen.
- [ ] One team clearly provides the service.
- [ ] Another team clearly consumes the service.
- [ ] Day-to-day collaboration is minimal.
- [ ] The consuming team can use the service without needing deep implementation knowledge.
- [ ] The providing team manages the service like a product.
- [ ] The service has clear documentation.
- [ ] The service is easy to test, deploy, use, and debug.
- [ ] The developer experience is strong.
- [ ] Versioning and backward compatibility are considered.
- [ ] There is a roadmap or communication plan for future changes.
- [ ] Requests from consuming teams are considered but not automatically built.
- [ ] The service helps reduce cognitive load for consuming teams.

### Watch for

- [ ] Consumers need frequent help to use the service.
- [ ] The API or boundary is unclear.
- [ ] The service slows delivery instead of improving flow.
- [ ] Innovation across the boundary becomes too slow.
- [ ] The provider team lacks product or service management capabilities.

## Facilitating Mode Checklist

- Use **Facilitating** when one team helps another team improve, learn, unblock itself, or adopt new practices.

- [ ] One team needs help closing a capability gap.
- [ ] The facilitating team has relevant expertise.
- [ ] The goal is to make the helped team self-sufficient.
- [ ] The facilitating team is not taking ownership of the other team's main work.
- [ ] The interaction is focused on coaching, mentoring, enabling, or removing impediments.
- [ ] The facilitating team can detect gaps across multiple teams.
- [ ] The facilitating team works with only a small number of teams at the same time.
- [ ] Both teams understand the purpose and temporary nature of the facilitation.
- [ ] The helped team is open to learning and changing practices.

### Watch for

- [ ] The facilitating team becoming a permanent dependency.
- [ ] The helped team resisting assistance.
- [ ] The interaction feeling unclear, awkward, or unfamiliar.
- [ ] The facilitator doing the work instead of enabling the team.

## Match Modes to Team Types

### Stream-aligned teams

- [ ] Typically use **Collaboration** with other teams when discovery is needed.
- [ ] Typically consume capabilities through **X-as-a-Service**.
- [ ] Occasionally receive **Facilitation** to improve capabilities.

### Enabling teams

- [ ] Typically use **Facilitating** mode.
- [ ] Occasionally use **Collaboration** to jointly discover or shape practices.

### Complicated-subsystem teams

- [ ] Typically provide capabilities through **X-as-a-Service**.
- [ ] Occasionally use **Collaboration** when discovery or boundary refinement is needed.

### Platform teams

- [ ] Typically provide the platform through **X-as-a-Service**.
- [ ] Occasionally use **Collaboration** to discover or refine platform capabilities.

## Team Behavior Checklist

### Collaboration behavior

- [ ] Teams interact frequently.
- [ ] Teams show mutual respect.
- [ ] Teams are willing to share responsibility.
- [ ] Teams use practices such as pairing, mobbing, workshops, or whiteboarding when useful.
- [ ] Teams avoid blame when boundaries are unclear.

### X-as-a-Service behavior

- [ ] The provider team focuses on the user and developer experiences.
- [ ] The consumer team gives clear feedback.
- [ ] The provider team treats the service as a product.
- [ ] The interaction is low-friction and predictable.

### Facilitating behavior

- [ ] The facilitating team helps without taking over.
- [ ] The receiving team is open to being helped.
- [ ] The goal is capability growth, not permanent dependency.
- [ ] Both teams agree on what "self-sufficient" looks like.

## Evolution and Improvement Checklist

- [ ] Use collaboration temporarily to discover better service boundaries.
- [ ] Move from collaboration to X-as-a-Service once the boundary is stable.
- [ ] Use facilitating teams to support new structures during a Reverse Conway maneuver.
- [ ] Temporarily change interaction modes to build empathy and experience.
- [ ] Treat awkward interactions as signals of missing capabilities or misplaced boundaries.
- [ ] Ask whether the current mode is helping flow or creating friction.
- [ ] Review whether the interaction mode still fits the current architecture.
- [ ] Review whether the team boundaries still make sense.
- [ ] Use techniques like event storming or context mapping to clarify boundaries.

## Final Review

- [ ] Every important team interaction has an explicit mode.
- [ ] Teams know whether they are collaborating, consuming/providing a service, or facilitating.
- [ ] Responsibilities are clear.
- [ ] Boundaries are clear enough for the current stage of work.
- [ ] Communication is intentional, not accidental.
- [ ] The interaction mode supports fast flow.
- [ ] The organization is ready to evolve team structures and interaction modes when needed.
