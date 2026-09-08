How policy becomes code — one source, three gates, and a message a developer can act on — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an engineer holds a thick policy binder while cluster monitors behind him show violations, and an executive asks which machine enforces it.](assets/images/policy-as-code/comic-01-the-compliance-pdf.jpeg)
**Panel 1:** *The hook: 'we have guardrails' — but a policy that lives in a document and a review meeting is a hope with a signature line.*

![Comic panel: a developer's release bounces off a closed admission gate stamped DENIED at 5 PM on Friday while the developer asks what policy.](assets/images/policy-as-code/comic-02-the-friday-bounce.jpeg)
**Panel 2:** *The problem: when developers first meet a policy at admission, you built a tollbooth, not a guardrail — the most expensive place to learn.*

![Comic panel: an engineer flips a lever to ENFORCE ALL and is buried under a flood of paper exemption requests as alarms flash.](assets/images/policy-as-code/comic-03-the-big-bang-deny.jpeg)
**Panel 3:** *The wrong way: the big-bang deny — every rule enforced on day one, and the organization learns that policy is an outage with a committee attached.*

![Comic panel: an executive presents a diagram of one policy folder feeding three gates labeled desk, PR, and admission.](assets/images/policy-as-code/comic-04-one-source-three-gates-v2.jpeg)
**Panel 4:** *The principle: one policy source, evaluated at three gates — the desk in seconds, the PR in minutes, admission as the backstop that cannot be bypassed.*

![Comic panel: split scene contrasting a cryptic policy-engine error with a clear message telling the developer to add a memory limit.](assets/images/policy-as-code/comic-05-the-message-is-the-interface.jpeg)
**Panel 5:** *How it plays out: a violation message is a user interface — one sentence naming the fix is the difference between a guardrail and a grievance.*

![Comic panel: an engineer walks a developer past signposts labeled watch, explain, and enforce, handing over a card labeled why.](assets/images/policy-as-code/comic-06-audit-before-enforce.jpeg)
**Panel 6:** *Enforcement is progressive: audit first, educate on the why, then enforce what genuinely matters — risk sets the pace, not the rollout plan.*

![Comic panel: an executive and an engineer review a wall dashboard of compliance charts, circling one bar to ask who is fixing it.](assets/images/policy-as-code/comic-07-the-dashboard.jpeg)
**Panel 7:** *Compliance you cannot see is compliance you do not have: continuous audit, violations by constraint and namespace, remediation tracked over time.*

![Comic panel: an engineer lifts a floorboard revealing a crowd of exemption tags growing underneath while an executive holds a review calendar.](assets/images/policy-as-code/comic-08-the-permanent-exemption.jpeg)
**Panel 8:** *What it costs: exceptions granted once and never revisited become the unofficial paved path around policy — review them, or the floor turns decorative.*

![Comic panel: an executive interviews an anthropomorphic policy scroll at a cluster gate, telling it to explain itself or step aside.](assets/images/policy-as-code/comic-09-the-explain-test.jpeg)
**Panel 9:** *The closer: every enforced policy has a documented reason and a named owner — a policy that cannot explain itself does not get to block a deployment.*
