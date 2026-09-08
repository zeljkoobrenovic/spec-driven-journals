---
timetoread: "7 min listen"
---

## Paper Versus Protection

**Ben:** Let me open with what every engineer in the room is thinking: policies are the part of security that produces binders instead of protection. Attackers do not read our acceptable-use policy. Why does this deserve a record?

**Ana:** Because policies are not aimed at attackers — they are aimed at the thousand daily decisions our own people make. Whether the contractor gets remote access, whether the database credentials go in the wiki, whether the old laptop goes in the bin with its disk. Without written boundaries, each of those is decided ad hoc by whoever faces it first, differently every time. The record's opening commitment is that every policy exists for a reason: a named security objective, consistent behavior across the organization, and support for the regulatory and audit requirements we actually carry.

**Ben:** But that's exactly how you get the 90-page Security Policy that nobody has ever read to the end.

**Ana:** Which is the first anti-pattern, and the record kills it structurally: separate, manageable documents rather than one omnibus. A policy someone can read in five minutes, scoped to one topic, findable when the question arises. And — this is the load-bearing split — the policy states *what must be achieved*, and leaves the implementation steps to procedures and standards. That single decision is what keeps policies short.

**Ben:** Expand on that split, because it sounds like an excuse for vagueness. "Achieve security" — very achievable, very meaningless.

**Ana:** The split isn't vague versus specific — it's outcome versus mechanism. "Authentication credentials must be protected in storage and in transit" is precise about the outcome and silent about the mechanism. The moment a policy names a product, a port, or a console path, it starts aging at the speed of that technology — and every tool swap suddenly requires executive re-approval of a mandate that didn't actually change. The mandate lives here; the mechanism lives in [[standards-and-procedures]], where it can be revised at engineering speed.

## The Words That Bind

**Ben:** The language section reads almost like a style guide. Must, will, shall, do — banned words: should, try, mostly. Is grammar really a security control?

**Ana:** In a policy, the grammar *is* the control. Every "should" is a decision delegated to whoever reads it under pressure — and pressure always argues for the convenient reading. "Passwords should be unique" means, operationally, "unless it's Friday." Must, will, shall give the employee a rule they can follow, the auditor a claim they can test, and a manager a line they can hold without negotiating each case. The precision of the language is the precision of the policy.

**Ben:** Real organizations run on exceptions, though. The legacy system that can't do MFA, the vendor who needs the weird access. Hard mandatory language just drives exceptions underground.

**Ana:** Only if you pretend they don't exist. The record does the opposite: permitted exceptions are clearly documented. A written exception is a decision — scoped, visible, attributable. The verbal exception is the anti-pattern: waivers granted in hallways and chat threads, each one a quiet amendment nobody approved and nobody remembers. Mandatory language plus documented exceptions is honest; soft language plus invisible exceptions is erosion.

**Ben:** Then the document metadata — version, effective date, revision history, owner, approver, executive sign-off. That's the bureaucratic part people skip.

**Ana:** Until the day it's the entire argument. Two versions of the password policy are circulating — the version block decides which one binds. A requirement gets challenged — the owner answers, and the approver's authority backs it. An unowned policy is a rumor. And management endorsement is not ceremony: a policy the executive layer never signed is a suggestion the executive layer never made, and in the first hard collision with a deadline it gets treated as exactly that. Two anti-patterns live here — the orphan document and the immortal draft, the one that's been cited for two years and formally approved never.

## Coverage and Findability

**Ben:** The coverage list is twenty-six items — removable media, wireless, ethics, equipment disposal. Does a two-hundred-person company really need twenty-six policies?

**Ana:** Maybe not — but it needs twenty-six *decisions*. The record's phrase is that a coverage gap is a silent permission: whatever has no policy is, in practice, allowed, or decided differently by each person who hits the question. Walking the list and consciously recording "we need this, we don't need that" converts silent gaps into decisions. And notice the unglamorous corners on that list — removable media, third-party responsibilities, equipment disposal. That's where incidents actually start, precisely because nobody wrote anything down.

**Ben:** Fine. Now the part that surprised me: physical copies. Paper, in 2026?

**Ana:** For critical policies, yes — and the reasoning is cold. The policies you need most urgently are the ones for outages and disasters, and those are exactly the moments your document platform may be down or ransomed. The incident-response policy locked inside the crashed document system is a punchline, not a control. Central storage under revision control is the daily answer; backup copies and paper for the critical few is the bad-day answer.

**Ben:** And findability generally — you've made it the record's headline test.

**Ana:** Because a policy nobody can find binds nobody. The test cuts in both directions: the current approved version must be one search away for the person it applies to — and the obsolete version must be gone from where people look, because a stale policy that's still findable is still being followed by somebody. That's why "remove or archive obsolete versions" is in the maintenance section and not a footnote. The secret policy — approved, filed, communicated to no one, making its debut in a disciplinary meeting — fails the same test from the other side.

## Keeping It Alive

**Ben:** Annual review of every policy. In practice that becomes a calendar ritual: open document, change the year, close document.

**Ana:** An unchanged policy that was genuinely reviewed is a legitimate outcome — the record says so explicitly. What it refuses is the un-review. The three questions I ask per policy are: is it still true, is its language still mandatory, and can the people it binds still find it? And reviews aren't only calendar-driven — significant business, technology, regulatory, or security changes trigger them too. A policy set reviewed "when we get to it" describes a company that no longer exists. That's the stale mandate anti-pattern: requirements referencing systems retired years ago.

**Ben:** And each revision goes back through approval?

**Ana:** Recorded and re-approved — that keeps the authority chain intact. What changed, who approved it, effective when. Governance isn't the write-once act; it's the maintained chain.

**Ben:** All right, here's my concession, with a condition. Policies earn their place if they stay short, mandatory, owned, and findable — the moment they bloat into procedure manuals or rot into archaeology, they're back to being binders.

**Ana:** That's not a condition — that's the record. Policy says what must be achieved, in language that binds, in documents that are owned, found, and alive. Everything else — the how — belongs one layer down. And the test never changes: anyone can find the current version that applies to them and understand it, and no one can find an obsolete one.
