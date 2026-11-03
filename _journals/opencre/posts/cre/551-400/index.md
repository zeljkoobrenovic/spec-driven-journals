---
id: "CRE-551-400"
title: "Allow user revocation of Oauth tokens"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-551-400
excerpt: "CRE 551-400 · in Technical application security controls › Session management › Re-authentication from federation or assertion · 18 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Cheat Sheets
---
> **CRE**: [551-400](https://opencre.org/cre/551-400)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-258-115]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]]

## Related CREs

- [[cre-724-770]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.5.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v35-token-based-session-management) | Verify the application allows users to revoke OAuth tokens that form trust relationships with linked applications. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [21](https://capec.mitre.org/data/definitions/21.html) | Exploitation of Trusted Identifiers | automatic |
| [22](https://capec.mitre.org/data/definitions/22.html) | Exploiting Trust in Client | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [94](https://capec.mitre.org/data/definitions/94.html) | Adversary in the Middle (AiTM) | automatic |
| [459](https://capec.mitre.org/data/definitions/459.html) | Creating a Rogue Certification Authority Certificate | automatic |
| [461](https://capec.mitre.org/data/definitions/461.html) | Web Services API Signature Forgery Leveraging Hash Function Extension Weakness | automatic |
| [473](https://capec.mitre.org/data/definitions/473.html) | Signature Spoof | automatic |
| [476](https://capec.mitre.org/data/definitions/476.html) | Signature Spoofing by Misrepresentation | automatic |
| [667](https://capec.mitre.org/data/definitions/667.html) | Bluetooth Impersonation AttackS (BIAS) | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [290](https://cwe.mitre.org/data/definitions/290.html) | Authentication Bypass by Spoofing | curated |
| [291](https://cwe.mitre.org/data/definitions/291.html) | Reliance on IP Address for Authentication | automatic |
| [293](https://cwe.mitre.org/data/definitions/293.html) | Using Referer Field for Authentication | automatic |
| [350](https://cwe.mitre.org/data/definitions/350.html) | Reliance on Reverse DNS Resolution for a Security-Critical Action | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 7.1.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [JSON Web Token for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) | curated |
|  | [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [551-400](https://opencre.org/cre/551-400). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
