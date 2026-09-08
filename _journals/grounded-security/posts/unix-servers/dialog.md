---
timetoread: "7 min listen"
---

## Subtraction as a Security Strategy

**Ben:** Another hardening record. The Windows one at least had an architecture story — forests, trusts, domain controllers. This is `umask` and firewall rules. What's the executive content in per-server hygiene?

**Ana:** The content is that a Unix application server is the most concrete security problem you'll ever get, and the record refuses to let that concreteness get lost in generalities. The server's attack surface is exactly three lists: what runs, what listens, and what's writable. Everything in the record is about shrinking those lists and keeping them shrunk. The test at the end is almost aggressive in its simplicity — only what the application requires is running, reachable, writable, and privileged, and the server still does its job.

**Ben:** "Still does its job" is doing a lot of work in that sentence.

**Ana:** It's half the record, honestly, and we'll come back to it. But start with subtraction, because it's the strategy. A service that isn't running cannot be exploited — no patch, no policy, no monitoring needed. So the first moves are: inventory every running service, establish the purpose of each, disable what has none, prevent it from starting again at reboot, and — the underrated one — recheck periodically, because services come back. Every deploy, every package install is an opportunity for the surface to quietly grow.

**Ben:** Patching, though. "Keep the OS patched" was advice in 1998. What does the record add?

**Ana:** Two things people actually get wrong. First, cadence over heroics: the chapter says keep update intervals small so large, disruptive upgrades are less likely. Organizations that defer updates accumulate a debt only a risky big-bang upgrade can pay — which breaks things, which teaches them to defer longer. It's a doom loop, and small steps are the exit. Second, the software the package manager can't see. The hand-installed application with no advisory subscription is the one that stays vulnerable for years — so the record demands it be tracked separately, with subscriptions to its security advisories. That orphan is a named anti-pattern.

## The Filesystem Is the Blast Radius

**Ben:** The permissions section is the longest and looks the most pedestrian. Ownership checks, world-writable hunts, `umask`. Why is this the center of gravity?

**Ana:** Because most application compromises begin as the application account. Someone gets code execution as the web-server user — not as root. From that moment, what that account can read and write *is* the blast radius. The record's key line: application accounts cannot read data they do not require. Add the world-writable hunt, a restrictive `umask` so new files are born safe, and the SUID review — with special attention to privileged binaries outside normal system directories, which is a classic persistence trick — and a compromised application becomes a contained nuisance instead of a data breach.

**Ben:** And the regular search for unexpected permission changes?

**Ana:** That's what keeps it true after day one. `chmod 777` to fix a deployment problem at midnight is the temporary fix that becomes the permanent hole — "world-writable and working" is in the anti-pattern list for a reason. The search makes the regression visible instead of silent.

**Ben:** Host firewall. There's a network firewall already — [[network-security]] is a whole record. Why duplicate at the host?

**Ana:** Because defense assumes either layer can fail. The network firewall doesn't help against the compromised neighbor on the same segment. The host permits only the traffic its function requires, blocks the rest inbound, and restricts administrative services — SSH above all — to trusted networks. And the rules get maintained: obsolete entries removed, rules verified after application changes, and required traffic confirmed still working — there's the "still does its job" theme again.

**Ben:** File-integrity monitoring feels like a compliance checkbox. Every audit asks for it, every organization has it, nobody looks at it.

**Ana:** Which is exactly the failure mode the record targets. FIM is the control that pays out when everything else has already lost — the attacker is in, escalated, and modifies a binary or a config file, and the baseline comparison catches it. But it only works as a discipline: a *trusted* baseline, alerts on unexpected change, unexplained alerts investigated promptly, and integration into the monitoring people actually watch, per [[logging-and-monitoring]]. The anti-pattern is the muted integrity alert — a breach notification system with the ringer off.

## Containment, MAC, and the 2 a.m. Rollback

**Ben:** Isolation. The record says use `chroot`, containers, or jails — then immediately says `chroot` is not a security boundary. Which is it?

**Ana:** Both, and the honesty is the point. Isolation raises the attacker's cost: a minimal environment with few utilities, an application that isn't root, a filesystem that mostly isn't there. But `chroot` alone can be escaped, especially by root — so the record forbids treating it as a *complete* boundary. It's a layer, in an architecture that assumes any single layer fails. The real kernel-level containment is mandatory access control — SELinux, AppArmor, TrustedBSD, wherever the platform supports one.

**Ben:** Here's where I get to say it: the first thing every ops team does with SELinux is turn it off. `setenforce 0` is the most-typed troubleshooting command on Linux.

**Ana:** The record names that as an anti-pattern precisely because it's universal — disabled as a debugging step, never re-enabled, kernel-level protection traded for one afternoon's convenience. But notice the chapter doesn't demand enforcement on day one. It prescribes the workable path: permissive or audit mode during testing, watch the violations, fix the policy, then enforce — and re-review policies as the application changes, because a policy frozen while the app evolves either breaks things or stops meaning anything. MAC is what distinguishes "the account can't read the file" from "the *process* can't, even after it's subverted."

**Ben:** Now the part you deferred. Half the checklist is verification — the app still works, the server reboots clean, scan the ports, test the restrictions. Isn't that just... QA?

**Ana:** It's the difference between hardening that lasts and hardening that evaporates. A control that breaks the application gets rolled back at two in the morning — usually along with three neighboring controls, and none of them ever comes back. So verification is part of the control itself: test after the mount options, after the firewall change, after isolation; reboot and confirm services return. And when a restriction genuinely can't hold, the record prefers a recorded, approved exception over a silent regression. An exception register you can read beats a configuration that quietly lies.

**Ben:** And the review repeats.

**Ana:** Periodically, and after major application, OS, or infrastructure changes. "Hardened once" is the last anti-pattern — the server that passed at commissioning and drifted soft through every deploy since. The scope section is even honest about when this record itself changes shape: if the fleet goes immutable — images and containers — hardening moves into the build pipeline, and the record gets revisited.

**Ben:** All right. My concession: this isn't `umask` trivia — it's one idea applied everywhere. Shrink what runs, listens, and is writable down to what the application requires, prove the application survived, and re-prove it on a schedule.

**Ana:** That's the record. Two questions to ask of any server: what's listening that the application doesn't require, and what can the application account read that it doesn't need? The right answer to both is nothing — and the server still does its job.
