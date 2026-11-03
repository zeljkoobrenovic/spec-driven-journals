---
id: "CRE-524-446"
title: "Mandate using multi factor authentication"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-524-446
excerpt: "CRE 524-446 · in Technical application security controls › Authentication › Authentication mechanism › MFA/OTP · 25 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [524-446](https://opencre.org/cre/524-446)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]] › [[cre-062-850]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.2.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v22-general-authenticator-security) | Verify replay resistance through the mandated use of One-time Passwords (OTP) devices, cryptographic authenticators, or lookup codes. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [16](https://capec.mitre.org/data/definitions/16.html) | Dictionary-based Password Attack | automatic |
| [49](https://capec.mitre.org/data/definitions/49.html) | Password Brute Forcing | automatic |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |
| [70](https://capec.mitre.org/data/definitions/70.html) | Try Common or Default Usernames and Passwords | automatic |
| [509](https://capec.mitre.org/data/definitions/509.html) | Kerberoasting | automatic |
| [555](https://capec.mitre.org/data/definitions/555.html) | Remote Services with Stolen Credentials | automatic |
| [560](https://capec.mitre.org/data/definitions/560.html) | Use of Known Domain Credentials | automatic |
| [561](https://capec.mitre.org/data/definitions/561.html) | Windows Admin Shares with Stolen Credentials | automatic |
| [565](https://capec.mitre.org/data/definitions/565.html) | Password Spraying | automatic |
| [600](https://capec.mitre.org/data/definitions/600.html) | Credential Stuffing | automatic |
| [644](https://capec.mitre.org/data/definitions/644.html) | Use of Captured Hashes (Pass The Hash) | automatic |
| [645](https://capec.mitre.org/data/definitions/645.html) | Use of Captured Tickets (Pass The Ticket) | automatic |
| [652](https://capec.mitre.org/data/definitions/652.html) | Use of Known Kerberos Credentials | automatic |
| [653](https://capec.mitre.org/data/definitions/653.html) | Use of Known Operating System Credentials | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [308](https://cwe.mitre.org/data/definitions/308.html) | Use of Single-factor Authentication | curated |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.2.8 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | curated |
|  | [TLS Cipher String Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html) | curated |
|  | [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.3.1 | All user access to system components for users and administrators is authenticated via at least one of the following authentication factors: () Something you know, such as a password or passphrase. () Something you have, such as a token device or smart card. () Something you are, such as a biometric element. (CUSTOMIZED APPROACH OBJECTIVE): An account cannot be accessed except with a combination of user identity and an authentication factor. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). This requirement does not supersede multi-factor authentication (MFA) requirements but applies to those in-scope systems not otherwise subject to MFA requirements. A digital certificate is a valid option for “something you have” if it is unique for a particular user. | automatic |
| 8.3.11 | Where authentication factors such as physical or logical security tokens, smart cards, or certificates are used: () Factors are assigned to an individual user and not shared among multiple users. () Physical and/or logical controls ensure only the intended user can use that factor to gain access. (CUSTOMIZED APPROACH OBJECTIVE): An authentication factor cannot be used by anyone other than the user to which it is assigned. | automatic |
| 8.4 | Multi-factor authentication (MFA) is implemented to secure access into the CDE. | automatic |
| 8.5 | Multi-factor authentication (MFA) systems are configured to prevent misuse. | automatic |
| 8.6 | Use of application and system accounts and associated authentication factors is strictly managed. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [524-446](https://opencre.org/cre/524-446). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
