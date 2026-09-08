---
timetoread: "2 min read"
---

The provider secures the cloud; my organization secures what it puts in the cloud — **the data, the identities, the configurations, and the workloads**. That split is a contract read correctly for every service model, and the rest follows: misconfiguration treated as the leading cloud risk, identity treated as the perimeter, infrastructure changed only through reviewed code, the old hygiene disciplines carried into the cloud undiminished, and no alert trusted until it has fired on a test. The closing rule: compliance is the baseline of the program, never the end of it.

**What changes**

* **Responsibility becomes explicit per service model.** SaaS, PaaS, and IaaS each split differently between provider and customer; the shared responsibility model is reviewed for AWS, Azure, and GCP, and everything on our side of the line gets a named owner.
* **Misconfiguration gets structural answers.** Continuous automated configuration monitoring — AWS Config, Azure Policy/Defender for Cloud, or Google Security Command Center as the worked examples — least privilege as the default posture, and infrastructure as code in source control, behind code review, with security checks in the CI/CD pipelines.
* **Identity becomes the perimeter.** MFA on root and administrator accounts and extended broadly, centralized identity and SSO, access removed the day someone leaves, no secrets in source code, repositories scanned, a dedicated secrets service with regular rotation, and a response process for exposed credentials.
* **IAM tightens to least-privilege RBAC.** Roles scoped to job function, permissions reviewed regularly, unused privileges removed, and unexpected privilege escalation raising an alert, not a retrospective.
* **Hygiene and architecture stay disciplined.** Inventory, patching, continuous vulnerability scanning, backups with tested restoration, DR planning, encryption, secured network boundaries, and log collection under CIS Controls or NIST CSF; architecture built on established patterns, tiering, and segmentation, checked against the provider Well-Architected frameworks and reassessed as workloads change.
* **Detection gets proven, not just enabled.** Alerts centralized in a SIEM, cloud incident-response procedures written, and every alert test-fired end to end — the GuardDuty exercise (GuardDuty → EventBridge → SNS, sample findings generated, email verified) is the worked example.

**What it costs**

* IaC-only changes and pipeline gates slow the first week and repay it every week after — console speed is how estates drift into unauditable shapes.
* Configuration monitoring, permission reviews, rotation, and alert testing are standing work, not projects.
* Reading the responsibility model per service takes real effort — assuming the provider covers it costs a postmortem.

**What we are not doing**

* Not mandating a provider — AWS, Azure, and GCP tools are the worked examples; the commitments are capability-level.
* Not covering the data layer in depth — cloud databases are held to [[databases]].
* Not building the identity model or the SIEM pipeline here — those are [[authentication]] and [[logging-and-monitoring]].
* Not treating the audit as the goal — compliance is the floor, per [[compliance]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist, the GuardDuty exercise, and the final security review. Grounded in the Cloud Infrastructure chapter of the* Defensive Security Handbook *(Brotherston, Berlin, and Reyor).*
