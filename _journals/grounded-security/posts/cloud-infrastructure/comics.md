Why the provider secures the cloud while we secure what we put in it — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a provider crew and an office team point at each other across a bridge gap labeled security while a suitcase labeled our data falls through.](assets/images/cloud-infrastructure/comic-01-we-assumed-they-handled-it.jpeg)
**Panel 1:** *The hook: every postmortem that begins 'we assumed the provider handled that' is a responsibility-model failure — the control that belonged to nobody.*

![Comic panel: papers flutter out of a bucket labeled public next to a wide-open gate signed 0.0.0.0/0 welcome while Nadia sprints over.](assets/images/cloud-infrastructure/comic-02-the-open-bucket.jpeg)
**Panel 2:** *The problem: the public bucket and the open security group — cloud estates get breached by one unreviewed change, not exotic attacks; misconfiguration leads the threat model.*

![Comic panel: console clicks sprout crooked pipes on a messy cloud estate that no longer matches the blueprint labeled what the code says.](assets/images/cloud-infrastructure/comic-03-clickops-drift.jpeg)
**Panel 3:** *The wrong way: ClickOps drift — an estate shaped by years of unreviewed console changes is unreproducible, unauditable, and different from what the code says.*

![Comic panel: a contract scroll with a dividing line — provider shielding the cloud below, and data, identities, configs, workloads on the customer side above.](assets/images/cloud-infrastructure/comic-04-the-contract-read-right.jpeg)
**Panel 4:** *The principle: the shared responsibility model is a contract — the provider secures the cloud infrastructure; everything on our side — data, identities, configurations, workloads — has a named owner or it is unowned.*

![Comic panel: a code diff rides a conveyor through source control, code review, and security check stamps toward the cloud while a console shortcut chute is barred.](assets/images/cloud-infrastructure/comic-05-infrastructure-as-a-diff.jpeg)
**Panel 5:** *Practice: infrastructure is code — every change is a diff with an approver, a history, and pipeline security checks, so misconfiguration is caught before deployment, by machinery.*

![Comic panel: a lone key labeled root with an MFA double lock floats between the internet and the cloud estate, while a departing employee's key dissolves.](assets/images/cloud-infrastructure/comic-06-identity-is-the-perimeter.jpeg)
**Panel 6:** *Practice: identity is the perimeter — MFA on root and every administrator, centralized SSO, and access that dies the day someone leaves, not at the next quarterly review.*

![Comic panel: a developer hides a key in a library book labeled repository while a scanner robot moves it to a secrets vault with a rotation dial.](assets/images/cloud-infrastructure/comic-07-the-token-in-the-repo.jpeg)
**Panel 7:** *Practice: no secret ever lands in source code — repositories are scanned, secrets live in a dedicated service, rotation is routine, and an exposure response process exists before the exposure.*

![Comic panel: a detection pipe ends mid-air over an unread mailbox on one side; on the other Nadia's sample finding travels the pipe to a verified email.](assets/images/cloud-infrastructure/comic-08-the-alert-nobody-tested.jpeg)
**Panel 8:** *The cost: 'GuardDuty enabled' is not detection — build the pipe, generate a sample finding, and watch the notification arrive end to end, before the day it fires for real.*

![Comic panel: an auditor stays on a slab labeled compliance with last year's certificate while Vera and Nadia climb higher steps toward the present-day threat.](assets/images/cloud-infrastructure/comic-09-compliance-is-the-floor.jpeg)
**Panel 9:** *The closer: auditors certify the past; attackers work in the present — compliance is the baseline the program never falls below, and never the program itself.*
