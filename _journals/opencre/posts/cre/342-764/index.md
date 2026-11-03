---
id: "CRE-342-764"
title: "Only store hashed authentication codes"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-342-764
excerpt: "CRE 342-764 · in Technical application security controls › Authentication › Authentication mechanism › MFA/OTP · 5 mappings to 5 standards and tools."
tags: ASVS, CWE, NIST 800-63, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [342-764](https://opencre.org/cre/342-764)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]] › [[cre-062-850]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.7.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v27-out-of-band-verifier) | Verify that the out of band verifier retains only a hashed version of the authentication code. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [256](https://cwe.mitre.org/data/definitions/256.html) | Plaintext Storage of a Password | curated |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.3.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.5.1 | PAN is rendered unreadable anywhere it is stored by using any of the following approaches: () One-way hashes based on strong cryptography of the entire PAN. () Truncation (hashing cannot be used to replace the truncated segment of PAN). – If hashed and truncated versions of the same PAN, or different truncation formats of the same PAN, are present in an environment, additional controls are in place such that the different versions cannot be correlated to reconstruct the original PAN. () Index tokens. () Strong cryptography with associated keymanagement processes and procedures. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext PAN cannot be read from storage media. (APPLICABILITY NOTES): It is a relatively trivial effort for a malicious individual to reconstruct original PAN data if they have access to both the truncated and hashed version of a PAN. This requirement applies to PANs stored in primary storage (databases, or flat files such as text files spreadsheets) as well as non-primary storage (backup, audit logs, exception, or troubleshooting logs) must all be protected. This requirement does not preclude the use of temporary files containing cleartext PAN while encrypting and decrypting PAN. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [342-764](https://opencre.org/cre/342-764). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
