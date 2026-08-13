---
timetoread: "4 min read"
---
*The working checklist behind this record. The Article tab carries the rationale and anti-patterns.*

## 1. Strategic Foundation

- [ ] Define why a platform strategy is needed
- [ ] Connect the platform strategy to the organization's business strategy
- [ ] Account for the organization's unique assets, constraints, and competitive environment
- [ ] Avoid copying another organization's platform strategy without adapting it
- [ ] Treat business strategy and technology strategy as a two-way relationship
- [ ] Focus on increasing the organization's rate of change, not merely reaching a fixed target state

## 2. Context, Objectives, Mechanisms & Design Decisions

- [ ] Context: explain why the organization is pursuing a platform strategy
- [ ] Objectives: identify and prioritize the most important business outcomes
- [ ] Mechanisms: explain how platform capabilities will produce those outcomes
- [ ] Design decisions: document the important implementation trade-offs
- [ ] Make the connection between context → objectives → mechanisms → design decisions explicit
- [ ] Avoid replacing mechanisms with buzzwords such as "DevOps" or "microservices"
- [ ] Make technical decisions understandable to business and technology stakeholders

*The source recommends these four connected layers specifically to avoid the "IT hourglass" problem in strategy documents.*

## 3. Transformation & Ways of Working

- [ ] Identify which existing ways of working must change
- [ ] Distinguish transformation from simply upgrading or optimizing technology
- [ ] Determine which old constraints the platform can remove
- [ ] Translate new technical capabilities into improved user experiences or business value
- [ ] Look for opportunities to achieve both speed and quality through automation
- [ ] Look for opportunities to achieve both speed and compliance
- [ ] Challenge the assumption that innovation and harmonization must be opposites

*Upgrading technology without changing how the organization works is described as optimization rather than transformation.*

## 4. Platform Design

- [ ] Define clear, reusable components and their relationships
- [ ] Separate commodity capabilities from true differentiators
- [ ] Use common interfaces and standards where they enable reuse
- [ ] Hide unnecessary underlying complexity from platform users
- [ ] Keep onboarding and consumption friction low
- [ ] Allow users enough freedom to build solutions you did not anticipate
- [ ] Avoid designing an all-encompassing "IT pyramid" that attempts to predict every use case
- [ ] Continuously review platform boundaries as technologies and user needs evolve
- [ ] Treat the way users interact with the platform as seriously as the functionality inside it

*Platforms should not anticipate every use case; standardization underneath should enable diversity and innovation above.*

## 5. Governance & Autonomy

- [ ] Centralize reusable expertise where it creates economies of scale
- [ ] Decentralize platform usage and innovation to individual teams
- [ ] Separate operational control from user control
- [ ] Use automation and shared-responsibility models as governance mechanisms
- [ ] Provide guardrails without creating excessive approval or ticket-based friction
- [ ] Be willing to relinquish some central control so users can innovate

*Platforms can combine central governance with decentralized usage and innovation.*

## 6. Map the Platform Landscape

- [ ] Identify the user or customer needs that anchor the platform
- [ ] Map the components required to meet those needs
- [ ] Determine which components are genesis, custom-built, product, or commodity
- [ ] Identify components likely to be commoditized over time
- [ ] Identify opportunities for componentization and reuse
- [ ] Use a Wardley Map or similar model to understand platform evolution
- [ ] Monitor platform usage for signals that certain capabilities should become shared platform services

*Wardley Maps are used in the text to examine component evolution and the effects of commoditization and componentization.*

## 7. Roadmap & Execution

- [ ] Define the point: where the organization wants to go
- [ ] Define the path: how it intends to get there
- [ ] Understand the terrain: risks, uncertainty, and environmental changes
- [ ] Ensure the roadmap begins from the organization's actual current state
- [ ] Avoid assuming only a "happy path"
- [ ] Identify important future decision points
- [ ] Identify alternative paths that may be taken
- [ ] Specify what data will be needed to make future decisions
- [ ] Allow tactics to change while preserving the overall strategic direction

*A strategic roadmap should anticipate decision points, possible paths, and the information needed to choose between them rather than pretending execution will be linear.*

## 8. Strategy Communication

- [ ] Emphasize the most important ideas rather than attempting to document everything
- [ ] Explicitly state what is not included in the strategy
- [ ] Use simple conceptual models where they reduce complexity
- [ ] Write for a broad human audience, not only technical specialists
- [ ] Ensure objectives, mechanisms, and technical choices form a coherent story
- [ ] Keep the document concise enough that decision-makers can understand its central argument

## 9. ACED Quality Check

Before approving the strategy, confirm that you have ACED it:

- [ ] Alignment — does the platform strategy support the IT and business strategies?
- [ ] Clarity — can a broad audience easily understand the strategy?
- [ ] Evolution — can the strategy evolve as opportunities, priorities, and constraints change?
- [ ] Decisions — does the strategy make actual choices and trade-offs rather than merely listing wishes?

*The source presents Alignment, Clarity, Evolution, and Decisions (ACED) as a simple final checklist for evaluating a strategy document or slide deck.*

## Final Go/No-Go Check

- [ ] We can clearly explain why the platform is needed
- [ ] We know the measurable business outcomes it should enable
- [ ] We can explain how the proposed mechanisms lead to those outcomes
- [ ] Major design trade-offs have been made explicitly
- [ ] The platform changes ways of working rather than merely introducing new technology
- [ ] Standardization enables rather than suppresses innovation
- [ ] Users have sufficient autonomy within appropriate guardrails
- [ ] The roadmap accounts for uncertainty and alternative paths
- [ ] Platform evolution will be driven by usage data and feedback
- [ ] The strategy passes the ACED test
