---
timetoread: "2 min read"
---

In my organization, identity is the first control plane — and **no single authentication control is ever asked to carry the day alone**. Identity is centralized under least privilege, passwords are long, unique, and managed, credentials are stored as salted modern hashes, protocols are known and verified, and MFA guards the doors that matter most. The test the whole stack is held to: least privilege, centralized IAM, strong passwords, secure protocols, and MFA working together as a layered defense.

**What changes**

* **Identity becomes centralized and self-pruning.** SSO cuts password sprawl, SCIM-style automation provisions and deprovisions accounts with the people they belong to, dormant and obsolete accounts are removed, and access for departing employees and vendors ends the day they leave — not the day someone remembers.
* **Password policy shifts from complexity theater to length and uniqueness.** Long passphrases in a vetted, MFA-protected password manager replace short clever passwords; sharing and reuse are forbidden outright, because credential stuffing means every reused password is only as safe as the weakest site it ever touched. Reset paths lose their weak security questions.
* **Credential storage assumes the breach.** Passwords are stored only as salted hashes under modern, deliberately slow algorithms with NIST-aligned work factors; MD5, SHA-1, DES/3DES, and plaintext protocols are retired, and default credentials — including on BMC/iLO/IPMI management interfaces — die on arrival.
* **Protocols are verified, not assumed.** Teams can explain NTLM, Kerberos, LDAP, RADIUS, OIDC, and SAML with their attack families — pass-the-hash, Golden Tickets, Kerberoasting, assertion theft — and confirm in configuration and logs which protocol a system actually speaks. New deployments choose protocols through requirements and threat modeling.
* **MFA is mandatory where it matters and honest about its limits.** Privileged accounts, remote access, VPN, and email first, extended to vendors and consultants; push bombing is trained against, code-matching is preferred over blind approval, enrollment and reset are protected, and the exclusion list is reviewed until it shrinks.

**What it costs**

* Centralizing identity and retiring legacy protocols is real migration work — the immortal legacy app must finally be dealt with or its risk accepted in writing.
* Password managers, MFA rollout, and protocol audits take budget and sustained attention; the exclusion review recurs — it is standing work, not a project.
* Some day-one friction for users and administrators, accepted deliberately: the reset path and the management port get the same rigor as the login page.

**What we are not doing**

* Not mandating an identity vendor, password manager, or MFA product — commitments hold at the capability level.
* Not hardening the network devices and segments these controls run on — that is [[network-security]] and [[network-segmentation]].
* Not treating MFA as the end of phishing — narrowing it here, handling it in [[phishing-response]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist, protocol by protocol, with the chapter's Final Review. Grounded in the Authentication chapter of the* Defensive Security Handbook*.*
