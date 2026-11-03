---
status: accepted
revised: 2026-10-28
---

# Spec: Part VII — CONTROL: Security, Privacy and Human Oversight

## Intent

Orient the reader to Part VII as one line of reasoning: drop Part VI's assumption that the agent is trying to do the right thing; a threat model drawn per session type finds the context-window boundary and the sessions holding the lethal trifecta; because injection cannot be filtered away, untrusted text may shape output but never authority, and sinks accept arguments by provenance; a sink check reaches only as far as the identity behind it, so authority is delegated, scoped and attributable; where no rule bounds a sink, a human approves through a record bound to the action, and approvers are measured; enforcement points outside the model carry every rule and an evidence log proves they ran. Carry the Ostrell thread (Poisoned Ticket, threat model v2, injection and identity redesigns, Rubber Stamp and the credit-gate redesign, the October 2027 audit) and the hand-offs from Part VI and to Part VIII.

## Audience

Chief architects, security architects, platform leads and risk owners deciding how agent authority is bounded, overseen and audited.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and FAILURE PATTERNS THIS PART ADDRESSES with exact pattern names (Ambient Authority, The Lethal Trifecta, The Rubber Stamp) linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one chain across the five chapters, not as a list of summaries.
- [ ] Says once that Ostrell is fictional; numbers match the chapters and ledger (6 days; 4 of 9 session types; 14 of 61 paths; 9,400 accounts to 1; 4,812 / 99.3% / 6 seconds / 3.1%; 1.1%; about two hours vs two and a half days).
- [ ] Names the questions the reader will be able to answer.
- [ ] Hands off from Part VI (the agent assumed to be trying to do right) and to Part VIII (how much control each action class needs, decided by evidence).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: each chapter as a `[[permalink]]` with what it decides and its Ostrell case, in config order.
- [ ] About 500–900 words of prose; no new citations.

## Non-goals

Teaching trust boundaries, the trifecta, injection patterns, token exchange, approval-gate design, policy languages or evidence-log mechanics (the five chapters own them); the Across Domains comparison; any external factual claim.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on this book's Part VI and Part VIII introductions: callouts, a short lead stating the chain, one diagram, an Ostrell paragraph, a paragraph per chapter.
- 2026-10-28: Failure patterns: Ambient Authority, The Lethal Trifecta and The Rubber Stamp, the three the style guide assigns to Part VII; Autonomy by Default and Context Soup are left to the chapters.
- 2026-10-28: The Poisoned Ticket opens the Ostrell thread because the first three chapters return to it; the October 2027 audit closes it because it shows the part's last step, proof.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[agent-threat-model]], [[prompt-injection-defense]], [[agent-identity-and-least-privilege]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
