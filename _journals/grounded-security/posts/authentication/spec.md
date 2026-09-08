---
status: accepted
revised: 2026-08-22
---

# Spec: Authentication

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Identity and Network section: fix the bar for how identity is proven
in my organization. The post turns the Authentication chapter of the
*Defensive Security Handbook* into an operating record: identity managed
centrally under least privilege — SSO against password sprawl, SCIM-style
automated provisioning and deprovisioning, obsolete accounts removed and
access disabled promptly on departure; passwords long, unique, and held in a
vetted password manager, never shared and never reused, with credential
stuffing assumed; credentials stored only as salted hashes under modern
password-hashing functions, with MD5, SHA-1, DES/3DES, and weak key sizes
retired; the authenticating infrastructure hardened — no default credentials,
management interfaces (BMC/iLO/IPMI) segmented, SMB signed and SMBv1 disabled;
authentication protocols (NTLM, Kerberos, LDAP, RADIUS, OIDC, SAML) known
with their attacks, verified in actual use, and chosen deliberately with
threat modeling; and MFA required for privileged accounts, remote access,
VPN, and email — deployed consistently and treated honestly as a control
with known weaknesses, not a spell. The load-bearing test: least privilege,
centralized IAM, strong passwords, secure protocols, and MFA work together
as a layered defense — no single control carries the day alone.

## Audience

Engineering and platform teams in my organization who run identity providers,
directories, and anything with a login (so they know the bar their
authentication surfaces are held to); security engineers auditing credential
storage and protocol usage; peer executives who want to see what "layered
identity defense" concretely commits us to. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the layered-defense shape
      end to end and closes with the chapter's own test: least privilege,
      centralized IAM, strong passwords, secure protocols, and MFA working
      together, no single control alone.
- [x] **IAM discipline survives** — least privilege, centralized
      authentication and account management, SSO against password sprawl,
      SCIM-style automated provisioning and deprovisioning, obsolete and
      unused accounts removed, access disabled promptly when employees or
      vendors leave, no reliance on a single control.
- [x] **Password discipline survives** — long unique passphrases over short
      complex passwords, no sharing (help desk included), no reuse,
      credential stuffing assumed, plaintext storage forbidden; password
      managers vetted for encryption, MFA, lockout, auditing, and
      vendor-direct installation; reset paths protected — no weak
      knowledge-based questions, randomized answers stored in the manager,
      MFA on reset where possible.
- [x] **Cryptographic hygiene survives** — the encryption / hashing /
      salting distinction; unique random salts per password; modern
      password-hashing and key-derivation functions with NIST-aligned work
      factors; MD5, SHA-1, DES/3DES, and weak RSA/DSA key sizes retired;
      post-quantum awareness.
- [x] **Infrastructure hardening survives** — default credentials changed
      immediately, BMC/iLO/IPMI protected and segmented onto restricted
      networks, SMB signing and encryption with SMBv1 disabled and guest
      authentication off, fine-grained password policies applied to the
      right groups without needless complexity, cloud IAM selected on
      requirements rather than assumed.
- [x] **Protocol literacy survives** — NTLM's challenge-response flow and
      pass-the-hash; the Kerberos ticket flow (KDC, AS, TGS, TGT, service
      ticket) and pass-the-ticket, Golden and Silver Ticket, Kerberoasting,
      AS-REP roasting; LDAP binds over LDAPS/TLS; RADIUS AAA with EAP
      mechanisms; OIDC and SAML with their token and assertion attacks;
      plaintext protocols (Telnet, FTP, SNMPv2, HTTP, old SMB) disabled;
      the protocol a system *actually* uses verified in configuration and
      logs; protocol choice made deliberately with threat modeling before
      production.
- [x] **MFA discipline survives** — required for privileged accounts,
      remote access, VPN, email, and portals, extended to vendors and
      consultants; MFA fatigue and push bombing recognized, code-matching
      preferred over blind approval, enrollment and reset processes
      protected, excluded systems reviewed, consistency across the
      organization; the chapter's Final Review reproduced in the checklist.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Authentication chapter checklist.

## Non-goals

- Not [[network-security]] — segmenting management interfaces appears here
  as an authentication protection; hardening the network devices themselves
  lives there.
- Not [[network-segmentation]] — the design of restricted networks and
  VLANs that authentication surfaces sit on lives there.
- Not [[windows-infrastructure]] — Kerberos, NTLM, and SMB hardening appear
  here as authentication concerns; the broader Active Directory and Windows
  estate discipline lives there.
- Not [[user-education]] — training users to refuse password requests and
  unexpected MFA prompts is committed to here; the education program that
  delivers it lives there.
- Not [[phishing-response]] — this record states that MFA does not eliminate
  phishing; what happens when credentials are phished anyway lives there.
- Not a product mandate — no identity provider, password manager, or MFA
  vendor is prescribed; the commitments hold at the capability level.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the visual layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Authentication chapter checklist of the
  *Defensive Security Handbook* (Brotherston, Berlin, Reyor), read through a
  practitioner-executive lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 15 _ Authentication.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the Final Review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Authentication chapter
    checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
