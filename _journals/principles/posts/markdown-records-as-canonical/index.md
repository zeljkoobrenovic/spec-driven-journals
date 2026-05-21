---
id: "ORG-PRIN-MARKDOWN-RECORDS-AS-CANONICAL"
status: draft:gray
title: "Practice Principle: Markdown Records as Canonical"
date: 2026-05-16
author: Organization Tech Strategy
permalink: markdown-records-as-canonical
timetoread: 12 min
excerpt: "The canonical record of an Organization technical decision, strategy, or durable discussion is a markdown file in git. Slack threads, Google Docs, meeting notes, and wiki pages may support discussion, but the markdown record is the artifact other people will cite, search, link, and learn from in two years. Canonicality is what makes records trustworthy across time. Without it, the same decision is remembered in three different versions and acted on differently."
tags: practices, documentation, adr, markdown, git, knowledge-management
logo: "assets/images/markdown-records-as-canonical/logo.jpeg"
logo_credit: "Inspired by Organization's Markdown Records foundational decision"
icon: "assets/icons/markdown-records-as-canonical.png"
---

> **Status**: DRAFT
>
> **Principle**: The canonical record of any durable technical artifact at Organization - decision, strategy, discussion document, principle, foundational practice - is a **markdown file in git**, published as a static site. Conversations may happen in Slack, Google Docs, pull requests, or meetings. The markdown record is what other people will read, cite, link, and learn from later. Where the markdown record and any other artifact disagree, the markdown record wins.

## Statement

Organization commits to:

* **Markdown** as the format for durable technical writing.
* **Git** as the storage and history mechanism.
* **A small static site generator** for publication.
* **A MADR-inspired structure** for decision records.
* **The markdown record as the source of truth.** Other artifacts support it but do not replace it.

This applies to architecture decisions, technical strategies, discussion documents, engineering principles, operating-model decisions, and similar foundational engineering records.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Markdown records are canonical. | All Organization writing is markdown. |
| Conversation happens elsewhere; record lives in git. | Slack and Docs are forbidden. |
| The markdown file is the source of truth. | The markdown file is immutable. |
| Records have a stable structure. | Every record follows the same template. |
| Static-site publication. | A complex documentation product. |

The principle is about *durability* and *trust over time*, not about banning conversational tools.

## How to Apply This Principle

Use this principle to:

* Explain why durable technical reasoning needs a canonical artifact.
* Decide when a Slack thread, deck, PR discussion, or Google Doc must be folded back into markdown.
* Recognise metadata, status, and permalink stability as part of trust.
* Use markdown records as context for humans and AI tools.

## Rationale

A technical decision's long-term value lives in the artifact, not in the conversation that produced it. The conversation evaporates: Slack threads scroll out of view, Google Docs lose owners, wikis drift, meeting notes are forgotten. The artifact, if it is kept somewhere durable, remains readable, searchable, citable, and reviewable years later.

Markdown in git has practical properties that make this work:

* Plain text. Diff-friendly. Reviewable in pull requests.
* Versioned. History tells you what changed and when.
* Portable. No proprietary editor required.
* AI-friendly. Claude Code and similar tools can read and write it directly.
* Cheap to publish. A static site generator turns it into a readable, durable web artifact.

Organization's foundational decision on markdown records makes this concrete. The repository hosting this content is itself an instance of the principle.

## Implications

* **Decision records are markdown files in git.** Not Confluence pages, Google Docs, slide decks, or Notion entries.
* **Front matter is small and stable.** A consistent metadata header keeps records comparable.
* **The structure is MADR-inspired.** Decision, context, drivers, options, consequences, revisiting.
* **Publication is via a small static site.** Generated HTML, served through GitHub Pages or an Okta-protected CDN proxy.
* **Conversation tools are explicitly secondary.** Slack threads, Google Docs, and pull-request reviews are support; the markdown file is canonical.
* **When conflict appears, the markdown record wins.** A decision is what the markdown says, not what someone remembers.
* **Records are reviewed and updated, not orphaned.** Records with no owner are flagged the same way unowned capabilities are.

## Canonicality Test

A technical record is canonical only if readers can rely on it without asking around.

Use this test:

* Is there one stable markdown file that states the current decision or principle?
* Does the file have stable metadata, including ID, status, owner, date, and permalink?
* Are supporting conversations linked from the record rather than replacing it?
* If Slack, Jira, a deck, and the markdown disagree, would everyone know the markdown wins?
* Is the status current: proposed, accepted, deprecated, superseded, or archived?
* Is there a clear owner who can update the record when reality changes?

If people need folklore to interpret the record, the record is not yet canonical. Improve the markdown until it can stand on its own.

## What This Means for Teams

For service teams:

* Capture significant technical decisions as markdown ADRs in the appropriate journal.
* Use pull requests to review and refine; merge the canonical version when the decision is made.
* Link to the markdown record from Slack, Jira, and other tools, not the other way around.

For architects and senior engineers:

* Write your reasoning down. The slide deck is for presentation; the markdown is for memory.
* When advising a team, point them at existing records first.

For tech leads:

* Make ADR writing a normal part of delivery, not a separate step.
* Resist the urge to make "the deck" the artifact; the deck rots, the markdown does not.

For AI tooling:

* Treat markdown records as primary context. CLAUDE.md, Skills, and subagents should read from and link to them.

## Anti-Patterns

* **Slack-as-record.** A "decision" lives in a Slack thread and is referenced by date.
* **Doc-as-record.** A Google Doc with twenty comments is treated as authoritative even after the discussion ended.
* **Deck-as-record.** The slides someone presented become the de facto reference; the slides go stale within months.
* **Wiki sprawl.** A confusing Confluence tree where the same decision appears in three places, none authoritative.
* **Markdown drift.** A markdown record exists but the canonical state is "what we actually do, which is not in the record".
* **Pull-request graveyard.** The reasoning is in PR comments that nobody reads after merge.
* **Permalink churn.** A record's URL changes every time the title is edited.

## Examples

Aligned with the principle:

* This principles journal. Each principle is a markdown file in git, published as a static site, with stable permalinks and an ownership story.
* The Architecture Advisory Forum decision lives in `_journals/foundations/posts/architecture-advisory-forum/index.md`; the AAF meeting itself is a conversation supporting that record.
* The AI tooling decision is a markdown ADR; the original strategy slides are an input to it, not the canonical version.

Out of alignment with the principle:

* A Confluence page captioned "Final architecture decision" updated quietly by anyone who has edit access.
* A Slack pin labelled "this is how we do it" that nobody can locate two months later.
* A "v3" Google Doc with no link to "v2" and no shared definition of which one is current.

## Discussion Prompts

Use these prompts in documentation reviews:

* Which decision do people still explain from memory because the markdown record is missing or weak?
* Where do supporting artifacts disagree with the canonical record?
* What record should be updated before the next team or AI assistant relies on it?

## Related Principles

* [[advice-in-public]] - conversations make decisions better; markdown makes them durable.
* [[decisions-stay-with-teams]] - team-owned decisions need a team-owned record.
* [[governance-as-code]] - some governance is enforced in records (front-matter standards, permalink stability).
* [[capabilities-follow-ownership]] - records, like capabilities, have owners and lifecycles.

## Scope and Revisiting

This principle applies to Organization's high-quality, long-lived technical writing: ADRs, technical strategies, discussion documents, engineering principles, foundational engineering records, and operating-model decisions.

It does not apply to:

* Short-lived team chat.
* Ephemeral planning notes.
* Product documentation aimed at users.
* Service-local READMEs that belong with service code.
* Operational runbooks that have a separate ownership and publication path.
* Anything genuinely throwaway.

The principle should be revisited if:

* The static-site generator stops scaling for real needs (cross-linking, search, navigation, contributor experience).
* Access-control requirements outgrow what the protected static-hosting path can support.
* A future toolchain becomes meaningfully cheaper while preserving markdown, git history, reviewability, and portability.

## Authoritative References

* MADR, [Markdown Architectural Decision Records](https://adr.github.io/madr/).
* CommonMark, [Specification](https://commonmark.org/).
* Organization Foundations, Markdown Records as the Default Format ([[markdown-records]]).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
