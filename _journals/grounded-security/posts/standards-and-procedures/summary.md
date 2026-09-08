---
timetoread: "2 min read"
---

Security documentation in my organization is a hierarchy with a division of labor: **policy explains why, standards define what, procedures identify who, when, and where, and work instructions explain how**. Standards speak in mandatory language and are specific enough to implement consistently; requirements are written once and referenced everywhere; procedures are written for their readers, not their authors; and every document carries a version, an owner, an approver, a purpose, a scope, and links to its neighbors. The test the whole layer is held to: a new employee can find the authoritative document and apply it correctly without asking anyone.

**What changes**

* **Every document gets a level.** The why/what/who-when-where/how separation is enforced, so each layer changes at its own speed — reasons stay stable while cipher suites and commands move — and related documents are explicitly linked.
* **Requirements become requirements.** Must, shall, and will replace should, try, and mostly wherever a requirement is mandatory; anything two competent engineers could implement two different ways gets rewritten until it is specific enough to apply consistently.
* **Duplication is engineered out.** Common requirements are documented once and referenced by the policies that need them, so a fleet-wide change is one reviewed edit instead of a search party across ten documents.
* **Procedures are written for the 2 a.m. reader.** Ordered steps, active voice, explicitly stated and verified assumptions, real commands and examples — with judgment explicitly allowed where prescription would be impractical — and review by people who understand both the technology and the audience.
* **Every document carries its contract.** Version information, owner, approver, purpose, scope with exclusions, clearly identified requirements, and related-document references; one approved repository where the authoritative version is unambiguous and superseded versions are archived; nothing published without SME review, recorded approval, and a next review date.

**What it costs**

* Authoring discipline up front: leveling, metadata, and the final quality review make writing a document slower than dumping knowledge into a wiki page.
* Standing maintenance: owners, review dates, and cross-reference upkeep are recurring work, not a one-time cleanup.
* Editorial friction: mandatory-language and specificity rules force arguments about what is actually required — arguments that were previously deferred to the reader.

**What we are not doing**

* Not writing four documents for every control — small scopes collapse levels deliberately, not accidentally.
* Not deciding which external regulations apply — that is [[compliance]]; this record makes the documentation able to face them.
* Not writing the why-layer — that is [[policies]]; and teaching people to follow the documents is [[user-education]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full documentation-quality checklist, from hierarchy to the final quality review. Grounded in the Standards and Procedures chapter of the* Defensive Security Handbook*.*
