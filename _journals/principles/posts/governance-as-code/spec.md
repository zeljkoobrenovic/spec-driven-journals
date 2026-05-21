---
status: draft
revised: 2026-05-20
---

# Spec: Practice Principle — Governance as Code

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Encode engineering standards, policies, and review rules as
**executable artifacts** (CI checks, hooks, IaC guardrails, Claude
Code settings, CLAUDE.md fragments, Skills, MCP allowlists, PR
templates). Governance documented only in policy decks fails silently
and gets discovered during incidents. Governance encoded in the
platform fails loudly and gets fixed in PRs.

## Audience

- **Platform engineers** encoding governance.
- **Reviewers** relying on the encoded checks.
- **Architecture group** evaluating which rules are encodeable.

## Success criteria

- [ ] Reader can answer "can this be checked automatically? if yes,
      encode it".
- [ ] Reader knows governance-as-code complements human review, not
      replaces it.
- [ ] Reader sees [[ai-engineering-standards]] as the largest
      application of this principle.

## Non-goals

- Removing human review.
- Encoding every rule (some require judgement).

## Open questions

- How to detect rules that *should* be encoded but aren't.

## Decision log

- **2026-05-20** — Chose **encode-by-default** for checkable rules.
  Considered policy-as-text-with-manual-checks; rejected because
  manual checks degrade.
- **2026-05-20** — Kept **human review essential** for judgement.
  Considered fully-encoded gates; rejected because some standards
  genuinely require judgement.

## Sources

- **Internal**
  - [[ai-engineering-standards]] — the largest application.
  - [[ai-policy]] — paired policy + executable controls.
  - [[ai-output-must-be-governed]] — companion practice principle.
- **External**
  - Open Policy Agent (OPA), Conftest — informs the
    policy-as-code framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
