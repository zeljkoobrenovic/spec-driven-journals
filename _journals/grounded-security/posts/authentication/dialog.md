---
timetoread: "8 min listen"
---

## Why Identity Comes First

**Ben:** Straight question first. This record covers passwords, hashing, Kerberos tickets, MFA — a security textbook's worth of material. Why does an executive operating model need all of it in one record?

**Ana:** Because it's one system pretending to be many topics. The chapter this record distills ends with a single question: can you explain how least privilege, centralized IAM, strong passwords, secure protocols, and MFA work together as a layered defense? That's the record. Every one of those controls fails somewhere — passwords get phished, MFA gets fatigued, protocols get downgraded. The commitment is never that a control is unbreakable; it's that no single failure is sufficient. You can't state that commitment about passwords alone or MFA alone.

**Ben:** Layered defense is a poster in every security office. What makes it operational here?

**Ana:** The refusal it implies. The record refuses to let any control make the others optional. MFA doesn't excuse weak passwords. Hashing doesn't excuse weak passwords either — the checklist says explicitly that weak passwords stay vulnerable even when hashed. Centralized IAM doesn't excuse dormant accounts. The moment someone says "we have MFA, so the password policy can relax", the layering is gone and you're back to one control carrying the day.

**Ben:** Start with centralization, then. SSO, SCIM provisioning — that sounds like an IT convenience program wearing a security costume.

**Ana:** It's what makes discipline enforceable. A rule applied by hand in forty systems is applied in thirty of them. Centralize identity and password policy, lockout, conditional access, and deprovisioning become decisions made once, enforced everywhere. That holds in the cloud too — cloud IAM is chosen on requirements like conditional access and banned-password lists, not on the assumption that cloud solves access control by itself. And the automation is really an offboarding guarantee — the day someone joins, SCIM is a convenience; the day someone leaves, it's the difference between access ending at once and an account nobody remembers surviving for years. Dormant accounts are the attacker's favorite identity: valid, monitored by no one, missed by no one.

## Passwords and the Arithmetic

**Ben:** The password section bans complexity requirements in favor of length. Every compliance regime I've met wants the symbol and the capital letter. You're saying they're wrong?

**Ana:** The arithmetic is saying it. Brute-force difficulty grows with every character far faster than with any substitution trick. A long, dull passphrase beats `P@ssw0rd1!` by orders of magnitude — and the complexity rules actively produce the predictable substitutions dictionary attacks eat first. The record's standard is long, unique, and held in a vetted password manager. Uniqueness matters as much as length: breaches happen at other people's companies, and credential stuffing means every reused password is only as safe as the least secure site it was ever typed into.

**Ben:** "Vetted" password manager — meaning what? It's an app with a vault icon.

**Ana:** Meaning it's infrastructure, so it gets an infrastructure review: strong encryption of the stored passwords verified, MFA on the manager itself, automatic lockout, auditing and logging, protection against keylogging reviewed, software obtained directly from the vendor with installer integrity checked. The manager holds the keys to everything — it gets more scrutiny than any other tool, not less.

**Ben:** And the reset path. That's the part I rarely see in policies.

**Ana:** Because attackers read policies too. A login guarded by MFA means nothing if the recovery flow accepts a mother's maiden name from a public genealogy site. The record makes the reset path a first-class authentication surface: no weak knowledge-based questions, randomized answers stored in the manager where questions can't be avoided, MFA on the reset itself where possible. The weakest authentication path *is* your authentication posture.

## Storage, Algorithms, and Protocol Literacy

**Ben:** The record spends real space on hashing and salting. Isn't that a developer's concern, three levels below an operating model?

**Ana:** Storage discipline is the plan for the day the credential database is stolen — which is an executive concern, because it decides whether that day is an incident or a catastrophe. Plaintext is total loss. Fast general-purpose hashes are a weekend of GPU time. Unsalted hashes fall to precomputed rainbow tables. Salted, deliberately slow, NIST-aligned hashing is what makes the stolen database expensive to exploit. And the algorithm hygiene follows: MD5, SHA-1, DES/3DES retired, weak key sizes gone, post-quantum on the radar.

**Ben:** Then the protocol tour — NTLM, Kerberos, LDAP, RADIUS, OIDC, SAML, each with named attacks. Golden Tickets, Kerberoasting, signature wrapping. Why must an operating record carry that vocabulary?

**Ana:** Because legacy protocols carry their attacks with them, and you can't retire what you can't recognize. NTLM ships with pass-the-hash — that's why it's legacy. Kerberos ships with a whole named attack family. Plaintext LDAP hands credentials to anyone on the path. A team that can't describe the Kerberos ticket flow can't tell which of its failures matter. And the record adds the step most organizations skip: verify what a system *actually* speaks — in configuration, in logs, with packet analysis when needed. The architecture diagram is not evidence.

**Ben:** You'll find an SMBv1 dependency somewhere. Everyone does.

**Ana:** And then the record forces the honest move: disable it, or accept the risk in writing with an end date. What it forbids is the silent default — the whole estate inheriting pass-the-hash indefinitely so one legacy application can avoid an upgrade nobody scheduled.

## MFA Without the Magic

**Ben:** MFA. The record mandates it for privileged accounts, remote access, VPN, email. Fine — nobody argues anymore. But then it spends a whole section on MFA's weaknesses. Why undercut your own mandate?

**Ana:** Because the mandate only pays if it's honest. MFA is the cheapest large risk reduction available to us — and it does not eliminate phishing. Attackers adapted: push bombing until a tired user taps approve, hijacking enrollment, targeting reset flows, walking through the systems the rollout skipped. So the record buys MFA at its honest price: code-matching preferred over blind push approval, users trained to refuse unexpected prompts, enrollment and reset protected, and the exclusion list reviewed until it shrinks. Implementation quality determines what MFA is worth — the acronym determines nothing.

**Ben:** The exclusion list being the systems where MFA was postponed.

**Ana:** Which is exactly where the attacker goes. Inconsistent MFA is almost worse than none, because it buys confidence without buying coverage. One VPN concentrator without MFA and the whole rollout is a decoration.

**Ben:** And the infrastructure items — BMC and iLO interfaces, default credentials. Those feel bolted on.

**Ana:** They're the same lesson as the reset path. Attackers don't fight the strong control; they find the weak sibling. A hardened server whose management interface still answers with the vendor's default password on the office LAN is an unlocked side entrance. Default credentials die on arrival, and management interfaces live on restricted networks — which is where this record hands off to [[network-segmentation]].

**Ben:** All right. My crisp takeaway: authentication isn't a control, it's a stack — and the bar isn't "is any layer unbreakable" but "if this one layer fails, what still holds the line?"

**Ana:** That's the record. Ask it of every login, every reset path, and every management port — and if the answer is "nothing", that's the next thing we fix.
