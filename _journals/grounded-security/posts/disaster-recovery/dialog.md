---
timetoread: "8 min listen"
---

## Whose Numbers Are RPO and RTO

**Ben:** Let me open with the obvious: we do backups. Nightly, offsite, encrypted, green dashboard. Isn't disaster recovery a solved problem we're now wrapping in ceremony?

**Ana:** The green dashboard is where this record starts its argument. A backup job succeeding tells you a file was written. It doesn't tell you the file restores, that the restore fits inside the downtime the business can survive, or that anyone ever decided what that survivable downtime is. The record begins somewhere most DR programs skip: every critical system carries an RPO — how much data we can afford to lose — and an RTO — how long we can afford to be down — driven by business requirements, priced, and signed by business owners.

**Ben:** Why drag business owners into what's essentially an infrastructure design choice?

**Ana:** Because they're the only ones who can answer the two questions, and the only ones who can pay for the answers. An RTO set by IT alone is either gold-plated — recovery capacity nobody asked to fund — or fictional, a number never validated against cost. And the signature buys something else: priority. When everything is down at once, the recovery order must already be decided. The worst possible moment to negotiate which system matters most is during the disaster.

**Ben:** Fine. But then the record refuses to pick one recovery architecture. Backups, warm standby, high availability, alternate systems, repurposed systems — why the menu? Pick the best one.

**Ana:** Because "the best one" wastes money at both ends. High availability everywhere bankrupts the budget on systems that could tolerate a day down; tape everywhere leaves the revenue path dark for a week. Strategy is chosen per system against its signed targets. And each rung has an honesty clause. Tape offsite? Then transport time plus restore time plus procuring replacement hardware *is* your RTO, whatever the document says. Warm standby? It has to stay synchronized and geographically separate, with the DNS and routing switch documented. HA? Only counts if there's spare capacity left after the failure.

## Cloud Recovery and the Dependency Trap

**Ben:** The cloud section reads almost optimistic. Replicate to another region, infrastructure-as-code recreates everything. Hasn't the cloud basically solved DR?

**Ana:** It's made DR cheaper to have and easier to fake — the record says both. Yes: cross-region replication and IaC turn what used to need a second datacenter into configuration. But the checklist is deliberately suspicious: verify the IaC actually reproduces production, confirm resources scale when DR activates, test the recovery procedures regularly, and review the cost in both normal and disaster modes. A recovery region that has never been stood up is the untested backup with a better architecture diagram.

**Ben:** And the cost line? That seems oddly financial for a security record.

**Ana:** A DR plan the organization can't afford to run is a plan that gets quietly abandoned in month three. Cost transparency is a survival property of the plan itself.

**Ben:** Let's do dependencies. Every DR document I've seen has a dependency section nobody reads.

**Ana:** That unread section is usually where the plan dies. A system's real RTO is the RTO of its slowest dependency. Your flagship app restores in an hour — and then waits a day for the identity provider, because nobody checked that the directory service had a compatible target. The record maps them all: network, routing, DNS, authentication, databases, storage, third-party APIs. Then the rule with teeth: dependent services meet compatible targets, or you adjust the promise honestly. And dependencies go into the tests, because a dependency map that's never exercised is just a diagram.

**Ben:** The scenarios feel like tabletop theater, though. Ransomware, fire, flood, pandemic — do the labels change the plan?

**Ana:** They change it completely, which is the point of walking each one through systems, people, facilities, and communications with the business in the room. Ransomware attacks the backups themselves and can make your recovered environment re-infectable — it's not a hardware failure with extra steps. Site loss takes the runbooks and badge readers with it. A pandemic takes no systems and all of the hands. A plan written abstractly recovers an abstract disaster. The scenarios are how it becomes ours.

## Testing Without a Safety Net

**Ben:** Now the hard one. "Test without relying on systems that would be unavailable during the simulated disaster." That's expensive, disruptive, and frankly a bit performative. A scoped restore test in a sandbox tells me most of what I need. Why insist on the brutal version?

**Ana:** Because the convenient test is one of the record's named anti-patterns, and it's the most seductive one. The exercise that quietly uses production DNS, production identity, and the primary site's tooling proves exactly one thing: recovery works when nothing is wrong. The disaster removes your DNS, your identity provider, your wiki — and your wiki is where the runbook lives. The plan-on-the-dead-wiki failure is so common the record has a separate line for keeping DR procedures accessible when normal systems are down.

**Ben:** So every test is a full site-down simulation?

**Ana:** No — the record wants a portfolio: tabletops, scoped technical exercises, restore drills, up to fuller simulations. The honesty rule isn't "maximum pain," it's "don't let the test secretly lean on what the disaster removes." And the loop closes the same way every time: observe, document, debrief, corrective actions with owners and deadlines, retest major changes. A test that finds nothing was probably not a test.

**Ben:** And restores. Surely modern backup tools verify integrity automatically.

**Ana:** Verification tells you the bits match. A restore tells you the system comes back — schema, permissions, application behavior, within the RPO and RTO. The record's load-bearing line is blunt on purpose: a backup that has never been restored is a hope, not a plan. Years of green jobs have ended in empty archives at precisely the moment they were the last copy.

## Security During the Worst Week

**Ben:** Here's a real objection from the trenches. It's 3 a.m., the site is down, revenue is bleeding. Someone says: disable MFA on the recovery accounts, open the firewall, share the admin password — we'll clean it up after. Isn't that just pragmatic triage?

**Ana:** It's the anti-pattern the record calls the security holiday, and it's how an outage becomes a breach. Two facts make disaster week the worst week to drop controls. First, backup and standby environments hold the same crown jewels as production, usually with less scrutiny — an unencrypted backup store or an unpatched warm standby is the cheapest path to the data, and attackers know it. Second, adversaries deliberately exploit chaos; ransomware operators in particular count on recovery-mode sloppiness. So: production-comparable controls on backup data, encrypted and authenticated replication, patched and configuration-aligned recovery systems, least privilege maintained, emergency access documented — and revoked afterwards. A recovery that reopens the breach is not a recovery.

**Ben:** The failback section surprised me. Everyone plans the jump to the standby; you're saying the jump back needs equal ceremony?

**Ana:** Equal ceremony, because it's an equal outage risk. Failback done casually — primary not confirmed stable, data not synchronized, nobody authorized to approve, nothing verified after the switch — turns a survived disaster into a self-inflicted second one. And wrapped around all of it: communicate during every outage, regardless of size. Silence during small outages is how organizations rehearse silence for the big one.

**Ben:** All right, the concession. Disaster recovery isn't a backup product — it's a set of promises: loss and downtime bounds the business actually signed, strategies priced to meet them, dependencies that don't lie, and proof by restore and rehearsal rather than by dashboard.

**Ana:** With one addition: the promises decay. Systems change, dependencies shift, contacts go stale — which is why the fifteenth section is ongoing review, tied back to business continuity. The question I'd leave any team with is the record's own test: has every backup been proven by a restore, and every RTO by a test that didn't lean on what the disaster would take? If not, you don't have a plan yet. You have a hope with a table of contents.
