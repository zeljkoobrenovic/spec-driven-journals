---
id: "CRE-802-056"
title: "Restrict excessive authentication"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-802-056
excerpt: "CRE 802-056 · in Technical application security controls › Authentication › Authentication mechanism · 18 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [802-056](https://opencre.org/cre/802-056)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v22-general-authenticator-security) | Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. Such controls include blocking the most common breached passwords, soft lockouts, rate limiting, CAPTCHA, ever increasing delays between attempts, IP address restrictions, or risk-based restrictions such as location, first login on a device, recent attempts to unlock the account, or similar. Verify that no more than 100 failed attempts per hour is possible on a single account. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [16](https://capec.mitre.org/data/definitions/16.html) | Dictionary-based Password Attack | automatic |
| [49](https://capec.mitre.org/data/definitions/49.html) | Password Brute Forcing | automatic |
| [560](https://capec.mitre.org/data/definitions/560.html) | Use of Known Domain Credentials | automatic |
| [565](https://capec.mitre.org/data/definitions/565.html) | Password Spraying | automatic |
| [600](https://capec.mitre.org/data/definitions/600.html) | Credential Stuffing | automatic |
| [652](https://capec.mitre.org/data/definitions/652.html) | Use of Known Kerberos Credentials | automatic |
| [653](https://capec.mitre.org/data/definitions/653.html) | Use of Known Operating System Credentials | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [307](https://cwe.mitre.org/data/definitions/307.html) | Improper Restriction of Excessive Authentication Attempts | curated |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |
|  | 5.1.4.2 | curated |
|  | 5.1.5.2 | curated |
|  | 5.2.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | curated |
|  | [TLS Cipher String Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html) | curated |
|  | [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHN-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/04-Authentication_Testing/03-Testing_for_Weak_Lock_Out_Mechanism.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.3.4 | Invalid authentication attempts are limited by: () Locking out the user ID after not more than 10 attempts. () Setting the lockout duration to a minimum of 30 minutes or until the user’s identity is confirmed. (CUSTOMIZED APPROACH OBJECTIVE): An authentication factor cannot be guessed in a brute force, online attack. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [802-056](https://opencre.org/cre/802-056). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
