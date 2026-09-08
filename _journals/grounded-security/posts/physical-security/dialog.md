---
timetoread: "7 min listen"
---

## Why Doors Are in a Security Journal

**Ben:** Straight question. This journal has records on Active Directory, cloud, IDS. Why is an engineering executive writing about door locks and visitor badges?

**Ana:** Because physical access is root access. Nearly every technical record in this journal assumes the attacker is remote. Someone standing at the machine doesn't need an exploit — they can boot from their own media, pull a drive, plug into an open network jack, or photograph the papers on a desk. An estate with hardened servers and an unlocked server room is hardened on paper. That's why this record opens the Hardening the Estate section: it's the layer with no dashboard, so it's the layer that gets forgotten.

**Ben:** But most of the checklist reads like office etiquette. Lock your screen, clear your desk, keep the printer tray clean. Is that really security?

**Ana:** It's exactly security — those are the physical equivalents of closing open ports. The document on the desk, the page in the printer discard box, the live network jack in the empty meeting room: each one is an interface someone can read or connect to without authenticating. The record just applies the discipline we take for granted digitally. And it's layered deliberately: highly sensitive areas get more than one control, because the chapter's closing rule is defense-in-depth — never rely on a single physical control.

**Ben:** Isn't a good badge system a single control that mostly works?

**Ana:** Mostly, until it doesn't — and the record is explicit about how it doesn't. Badges get cloned; the chapter says so flatly and tells you to assume it. Keypads wear down until the four shiny buttons reveal the code. Walls stop at the suspended ceiling and someone goes over the top. So sensitive areas combine badge access with another factor, keypads get inspected, ceiling routes get evaluated, and the controls themselves get tested — physical security goes into penetration tests, same as everything else in [[osint-purple-teaming]].

## Revocation and the Badge That Never Dies

**Ben:** The maintenance section feels bureaucratic. Audit keypads, recover badges, change codes. Where's the risk?

**Ana:** In the asymmetry. Granting access is easy — any organization can issue badges. Revocation is the discipline that separates the secure ones. Every departure that doesn't same-day recover the badge, remove the permissions, and change the shared codes leaves a standing credential nobody is watching. A former employee's live badge is worse than a weak password: no one is monitoring for its use, and it looks legitimate on every log.

**Ben:** And the shared PIN on the server room?

**Ana:** That's the purest version of the problem. A shared secret has no offboarding — you can't revoke it from one person, you can only change it for everyone, which means in practice it never changes. That's why the record bans shared PINs from highly sensitive areas outright. It's also why role changes trigger access reviews: access accumulates silently unless something forces the question.

**Ben:** Cameras, then. Every office has them. What does the record add?

**Ana:** The word *correlate*. A badge log proves a badge entered at 02:13; it doesn't prove who carried it. The record wants cameras positioned to capture faces and to pair a face with a badge event — that's what turns a log line into evidence. And it wants footage actually reviewed when something looks wrong, correlated with badge-access logs inside the [[incident-response]] process. A camera at the wrong angle, reachable from a chair, never reviewed — that's a prop, not a control.

## People, Politeness, and Pretexts

**Ben:** Here's my real skepticism. Tailgating training, don't-hold-the-door rules — everyone nods in the session and holds the door the next morning. Human controls don't hold.

**Ana:** They don't hold *by default*, which is different. The chapter's sharpest line is that politeness should not override security procedures — because politeness is precisely what the attacks exploit. Tailgating, the confident person in the branded polo with a fake work order, the promotional USB drive: all of them weaponize decent people defaulting to helpfulness. Training works when it reframes verification as professionalism rather than rudeness, and when it recurs — signs, reminders, awareness cycles — because this control decays fastest of all. The full curriculum lives in [[user-education]]; pretexting is just phishing in person, the same reflex [[phishing-response]] builds.

**Ben:** And when the person at the door is legitimate — the printer technician, the delivery?

**Ana:** Then verification costs them two minutes and nothing else. Identity checked, work order confirmed as expected and authorized, unusual requests escalated to a manager, unexpected devices verified before anything gets connected. Nobody gets into a restricted area solely for looking knowledgeable or appropriately dressed. Visitors sign in and out, get escorted, and need employee approval before touching equipment; contractors show verified photo ID, are vetted, and work within access limited to their job. Badges make status visible: visitor badges look different, expire with the visit, and get disabled promptly when lost or unreturned.

**Ben:** The USB drop still feels like movie-plot stuff.

**Ana:** It's one of the oldest working attacks there is, which is why the record doesn't rely on willpower alone. Training says treat found and promotional media as untrusted — and then endpoint controls restrict or disable removable-media ports where practical. Layers again: the human control backed by a technical one.

## Media and the Program

**Ben:** The media section — couriers, movement records, classification labels. Isn't that a lot of ceremony for USB sticks?

**Ana:** It's chain of custody for data that walks. A locked datacenter means little if the backup tapes and removable drives leave the building untracked. Labeled by classification, locked when not in use, approval before removal, secure courier in transit, every movement recorded, storage locations inspected periodically. It leans on [[asset-management]] — you can't track media you don't know exists.

**Ben:** Last objection. In most companies this whole area falls between two stools — facilities owns doors, security owns firewalls, nobody owns the gap.

**Ana:** The record names that as an anti-pattern — the orphaned program — and closes it structurally: physical security is coordinated between information security and facilities with a named owner, reviewed periodically, tested in assessments, with new threats identified and gaps corrected on a clock. It's a program, not a fit-out.

**Ben:** So the concession is this: physical security isn't about better locks — it's about layers plus revocation plus people who verify. And the test is that no single failure — a held door, a cloned badge, a good story — gets anyone to the sensitive stuff.

**Ana:** That's the record in one line. One failed control should be an inconvenience for the attacker, never a breach.
