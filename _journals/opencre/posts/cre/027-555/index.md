---
id: "CRE-027-555"
title: "Enforce user passwords are of sufficient minimum length"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-027-555
excerpt: "CRE 027-555 · in Technical application security controls › Authentication › Credentials directives · 20 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [027-555](https://opencre.org/cre/027-555)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-455-885]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v21-password-security) | Verify that user set passwords are at least 12 characters in length (after multiple spaces are combined). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [16](https://capec.mitre.org/data/definitions/16.html) | Dictionary-based Password Attack | automatic |
| [49](https://capec.mitre.org/data/definitions/49.html) | Password Brute Forcing | automatic |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |
| [70](https://capec.mitre.org/data/definitions/70.html) | Try Common or Default Usernames and Passwords | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [509](https://capec.mitre.org/data/definitions/509.html) | Kerberoasting | automatic |
| [555](https://capec.mitre.org/data/definitions/555.html) | Remote Services with Stolen Credentials | automatic |
| [561](https://capec.mitre.org/data/definitions/561.html) | Windows Admin Shares with Stolen Credentials | automatic |
| [565](https://capec.mitre.org/data/definitions/565.html) | Password Spraying | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [521](https://cwe.mitre.org/data/definitions/521.html) | Weak Password Requirements | curated |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C6](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c6-implement-digital-identity.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.3.6 | If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they meet the following minimum level of complexity: () A minimum length of 12 characters (or IF the system does not support 12 characters, a minimum length of eight characters). () Contain both numeric and alphabetic characters. (CUSTOMIZED APPROACH OBJECTIVE): A guessed password/passphrase cannot be verified by either an online or offline brute force attack. (APPLICABILITY NOTES): This requirement is not intended to apply to: () User accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). () Application or system accounts, which are governed by requirements in section 8.6. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until 31 March 2025, passwords must be a minimum length of seven characters in accordance with PCI DSS v3.2.1 Requirement 8.2.3. | automatic |
| 8.3.9 | If passwords/passphrases are used as the only authentication factor for user access (i.e., in any single-factor authentication implementation) then either: () Passwords/passphrases are changed at least once every 90 days, OR () The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly. (CUSTOMIZED APPROACH OBJECTIVE): An undetected compromised password/passphrase cannot be used indefinitely. (APPLICABILITY NOTES): This requirement applies to in-scope system components that are not in the CDE because these components are not subject to MFA requirements. This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). This requirement does not apply to service providers’ customer accounts but does apply to accounts for service provider personnel. | automatic |
| 8.3.10 | Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access to cardholder data (i.e., in any singlefactor authentication implementation), then guidance is provided to customer users including: () Guidance for customers to change their user passwords/passphrases periodically. () Guidance as to when, and under what circumstances, passwords/passphrases are to be changed. (CUSTOMIZED APPROACH OBJECTIVE): Passwords/passphrases for service providers’ customers cannot be used indefinitely. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information. This requirement for service providers will be superseded by Requirement 8.3.10.1 once 8.3.10.1 becomes effective. | automatic |
| 8.3.10.1 | Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access (i.e., in any single-factor authentication implementation) then either: () Passwords/passphrases are changed at least once every 90 days, OR () The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly. (CUSTOMIZED APPROACH OBJECTIVE): Passwords/passphrases for service providers’ customers cannot be used indefinitely. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until this requirement is effective on 31 March 2025, service providers may meet either Requirement 8.3.10 or 8.3.10.1. | automatic |
| 8.6.2 | Passwords/passphrases for any application and system accounts that can be used for interactive login are not hard coded in scripts, configuration/property files, or bespoke and custom source code. (CUSTOMIZED APPROACH OBJECTIVE): Passwords/passphrases used by application and system accounts cannot be used by unauthorized personnel. (APPLICABILITY NOTES): Stored passwords/passphrases are required to be encrypted in accordance with PCI DSS Requirement 8.3.2. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 8.6.3 | Passwords/passphrases for any application and system accounts are protected against misuse as follows: () Passwords/passphrases are changed periodically (at the frequency defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1) and upon suspicion or confirmation of compromise. () Passwords/passphrases are constructed with sufficient complexity appropriate for how frequently the entity changes the passwords/passphrases. (CUSTOMIZED APPROACH OBJECTIVE): Passwords/passphrases used by application and system accounts cannot be used indefinitely and are structured to resist brute-force and guessing attacks. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [027-555](https://opencre.org/cre/027-555). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
