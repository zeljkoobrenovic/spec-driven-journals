Why platform security is a chain proven by breaking it — not a list of green checkboxes — in eight panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an engineer shows a wall of green checkmarks labeled secure while an executive inspects a single chain link.](assets/images/platform-security/comic-01-secure-says-who.jpeg)
**Panel 1:** *The hook: 'the platform is secure' is either a claim or a chain of verified controls — the executive asks which link was tested.*

![Comic panel: a burglar assembles puzzle pieces labeled stolen token, CI credential, and admin role while two engineers watch alarmed.](assets/images/platform-security/comic-02-the-incident-assembles.jpeg)
**Panel 2:** *The problem: a stolen token, a leaked CI credential, and an over-permissive role are the same incident waiting to assemble itself.*

![Comic panel: a cobwebbed robot arm holds a giant key labeled cluster-admin with a note saying temporary since 2019.](assets/images/platform-security/comic-03-the-convenience-admin.jpeg)
**Panel 3:** *The wrong way: the convenience admin and the immortal token — the platform's real posture is whatever the oldest credential can still do.*

![Comic panel: an executive presents a six-link chain labeled identity, least privilege, machine id, admission, network, evidence.](assets/images/platform-security/comic-04-six-links.jpeg)
**Panel 4:** *The principle: six links, in order — human identity, least-privilege authorization, machine identity, admission control, network and transport, evidence.*

![Comic panel: an engineer rolls a noncompliant crate at a robot gatekeeper who stamps it rejected, while an executive checks a clipboard.](assets/images/platform-security/comic-05-the-negative-test.jpeg)
**Panel 5:** *How it plays out: nothing counts as done until someone tried to break it — the noncompliant deployment must be rejected, the forbidden action must fail.*

![Comic panel: one giant robot holding keys to five doors contrasted with five small robots each holding a short-lived token at one door.](assets/images/platform-security/comic-06-one-robot-per-pipeline.jpeg)
**Panel 6:** *Machine identity: one narrowly scoped service account per pipeline with short-lived tokens — when the shared robot leaks, the blast radius is everything.*

![Comic panel: an executive times an engineer who revokes a burned credential and traces an audit trail from login to token to API call.](assets/images/platform-security/comic-07-the-stopwatch-drill.jpeg)
**Panel 7:** *What it takes: the drill — simulate the leak, revoke, verify dead, trace login to token to API call in the audit logs, fix, and re-test on a schedule.*

![Comic panel: two framed padlocks, one pristine and never tested, one battle-scarred having rejected attacks; the executive points at the scarred one.](assets/images/platform-security/comic-08-hope-is-not-a-control.jpeg)
**Panel 8:** *The closer: a control that has never rejected anything is a hope, not a control.*
