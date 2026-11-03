---
id: "CRE-138-448"
title: "Inform users for authentication renewal"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-138-448
excerpt: "CRE 138-448 · in Technical application security controls › Secure user management · 88 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, ZAP Rule
---
> **CRE**: [138-448](https://opencre.org/cre/138-448)
>
> **Part of**: [[cre-636-660]] › [[cre-586-842]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-zap-rule]]

## Related CREs

- [[cre-270-568]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.3.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v23-authenticator-lifecycle) | Verify that renewal instructions are sent with sufficient time to renew time bound authenticators. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [2](https://capec.mitre.org/data/definitions/2.html) | Inducing Account Lockout | automatic |
| [22](https://capec.mitre.org/data/definitions/22.html) | Exploiting Trust in Client | automatic |
| [57](https://capec.mitre.org/data/definitions/57.html) | Utilizing REST's Trust in the System Resource to Obtain Sensitive Data | automatic |
| [94](https://capec.mitre.org/data/definitions/94.html) | Adversary in the Middle (AiTM) | automatic |
| [114](https://capec.mitre.org/data/definitions/114.html) | Authentication Abuse | automatic |
| [115](https://capec.mitre.org/data/definitions/115.html) | Authentication Bypass | automatic |
| [151](https://capec.mitre.org/data/definitions/151.html) | Identity Spoofing | automatic |
| [194](https://capec.mitre.org/data/definitions/194.html) | Fake the Source of Data | automatic |
| [593](https://capec.mitre.org/data/definitions/593.html) | Session Hijacking | automatic |
| [633](https://capec.mitre.org/data/definitions/633.html) | Token Impersonation | automatic |
| [650](https://capec.mitre.org/data/definitions/650.html) | Upload a Web Shell to a Web Server | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [287](https://cwe.mitre.org/data/definitions/287.html) | Improper Authentication | curated |
| [13](https://cwe.mitre.org/data/definitions/13.html) | ASP.NET Misconfiguration: Password in Configuration File | automatic |
| [41](https://cwe.mitre.org/data/definitions/41.html) | Improper Resolution of Path Equivalence | automatic |
| [42](https://cwe.mitre.org/data/definitions/42.html) | Path Equivalence: 'filename.' (Trailing Dot) | automatic |
| [43](https://cwe.mitre.org/data/definitions/43.html) | Path Equivalence: 'filename....' (Multiple Trailing Dot) | automatic |
| [44](https://cwe.mitre.org/data/definitions/44.html) | Path Equivalence: 'file.name' (Internal Dot) | automatic |
| [45](https://cwe.mitre.org/data/definitions/45.html) | Path Equivalence: 'file...name' (Multiple Internal Dot) | automatic |
| [46](https://cwe.mitre.org/data/definitions/46.html) | Path Equivalence: 'filename ' (Trailing Space) | automatic |
| [47](https://cwe.mitre.org/data/definitions/47.html) | Path Equivalence: ' filename' (Leading Space) | automatic |
| [48](https://cwe.mitre.org/data/definitions/48.html) | Path Equivalence: 'file name' (Internal Whitespace) | automatic |
| [49](https://cwe.mitre.org/data/definitions/49.html) | Path Equivalence: 'filename/' (Trailing Slash) | automatic |
| [50](https://cwe.mitre.org/data/definitions/50.html) | Path Equivalence: '//multiple/leading/slash' | automatic |
| [51](https://cwe.mitre.org/data/definitions/51.html) | Path Equivalence: '/multiple//internal/slash' | automatic |
| [52](https://cwe.mitre.org/data/definitions/52.html) | Path Equivalence: '/multiple/trailing/slash//' | automatic |
| [53](https://cwe.mitre.org/data/definitions/53.html) | Path Equivalence: '\multiple\\internal\backslash' | automatic |
| [54](https://cwe.mitre.org/data/definitions/54.html) | Path Equivalence: 'filedir\' (Trailing Backslash) | automatic |
| [55](https://cwe.mitre.org/data/definitions/55.html) | Path Equivalence: '/./' (Single Dot Directory) | automatic |
| [56](https://cwe.mitre.org/data/definitions/56.html) | Path Equivalence: 'filedir*' (Wildcard) | automatic |
| [57](https://cwe.mitre.org/data/definitions/57.html) | Path Equivalence: 'fakedir/../realdir/filename' | automatic |
| [58](https://cwe.mitre.org/data/definitions/58.html) | Path Equivalence: Windows 8.3 Filename | automatic |
| [256](https://cwe.mitre.org/data/definitions/256.html) | Plaintext Storage of a Password | automatic |
| [257](https://cwe.mitre.org/data/definitions/257.html) | Storing Passwords in a Recoverable Format | automatic |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |
| [259](https://cwe.mitre.org/data/definitions/259.html) | Use of Hard-coded Password | automatic |
| [260](https://cwe.mitre.org/data/definitions/260.html) | Password in Configuration File | automatic |
| [261](https://cwe.mitre.org/data/definitions/261.html) | Weak Encoding for Password | automatic |
| [262](https://cwe.mitre.org/data/definitions/262.html) | Not Using Password Aging | automatic |
| [263](https://cwe.mitre.org/data/definitions/263.html) | Password Aging with Long Expiration | automatic |
| [288](https://cwe.mitre.org/data/definitions/288.html) | Authentication Bypass Using an Alternate Path or Channel | automatic |
| [289](https://cwe.mitre.org/data/definitions/289.html) | Authentication Bypass by Alternate Name | automatic |
| [290](https://cwe.mitre.org/data/definitions/290.html) | Authentication Bypass by Spoofing | automatic |
| [291](https://cwe.mitre.org/data/definitions/291.html) | Reliance on IP Address for Authentication | automatic |
| [293](https://cwe.mitre.org/data/definitions/293.html) | Using Referer Field for Authentication | automatic |
| [294](https://cwe.mitre.org/data/definitions/294.html) | Authentication Bypass by Capture-replay | automatic |
| [295](https://cwe.mitre.org/data/definitions/295.html) | Improper Certificate Validation | automatic |
| [296](https://cwe.mitre.org/data/definitions/296.html) | Improper Following of a Certificate's Chain of Trust | automatic |
| [297](https://cwe.mitre.org/data/definitions/297.html) | Improper Validation of Certificate with Host Mismatch | automatic |
| [298](https://cwe.mitre.org/data/definitions/298.html) | Improper Validation of Certificate Expiration | automatic |
| [299](https://cwe.mitre.org/data/definitions/299.html) | Improper Check for Certificate Revocation | automatic |
| [301](https://cwe.mitre.org/data/definitions/301.html) | Reflection Attack in an Authentication Protocol | automatic |
| [302](https://cwe.mitre.org/data/definitions/302.html) | Authentication Bypass by Assumed-Immutable Data | automatic |
| [303](https://cwe.mitre.org/data/definitions/303.html) | Incorrect Implementation of Authentication Algorithm | automatic |
| [304](https://cwe.mitre.org/data/definitions/304.html) | Missing Critical Step in Authentication | automatic |
| [305](https://cwe.mitre.org/data/definitions/305.html) | Authentication Bypass by Primary Weakness | automatic |
| [306](https://cwe.mitre.org/data/definitions/306.html) | Missing Authentication for Critical Function | automatic |
| [307](https://cwe.mitre.org/data/definitions/307.html) | Improper Restriction of Excessive Authentication Attempts | automatic |
| [308](https://cwe.mitre.org/data/definitions/308.html) | Use of Single-factor Authentication | automatic |
| [309](https://cwe.mitre.org/data/definitions/309.html) | Use of Password System for Primary Authentication | automatic |
| [321](https://cwe.mitre.org/data/definitions/321.html) | Use of Hard-coded Cryptographic Key | automatic |
| [322](https://cwe.mitre.org/data/definitions/322.html) | Key Exchange without Entity Authentication | automatic |
| [350](https://cwe.mitre.org/data/definitions/350.html) | Reliance on Reverse DNS Resolution for a Security-Critical Action | automatic |
| [370](https://cwe.mitre.org/data/definitions/370.html) | Missing Check for Certificate Revocation after Initial Check | automatic |
| [425](https://cwe.mitre.org/data/definitions/425.html) | Direct Request ('Forced Browsing') | automatic |
| [521](https://cwe.mitre.org/data/definitions/521.html) | Weak Password Requirements | automatic |
| [522](https://cwe.mitre.org/data/definitions/522.html) | Insufficiently Protected Credentials | automatic |
| [523](https://cwe.mitre.org/data/definitions/523.html) | Unprotected Transport of Credentials | automatic |
| [549](https://cwe.mitre.org/data/definitions/549.html) | Missing Password Field Masking | automatic |
| [555](https://cwe.mitre.org/data/definitions/555.html) | J2EE Misconfiguration: Plaintext Password in Configuration File | automatic |
| [593](https://cwe.mitre.org/data/definitions/593.html) | Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created | automatic |
| [599](https://cwe.mitre.org/data/definitions/599.html) | Missing Validation of OpenSSL Certificate | automatic |
| [603](https://cwe.mitre.org/data/definitions/603.html) | Use of Client-Side Authentication | automatic |
| [620](https://cwe.mitre.org/data/definitions/620.html) | Unverified Password Change | automatic |
| [640](https://cwe.mitre.org/data/definitions/640.html) | Weak Password Recovery Mechanism for Forgotten Password | automatic |
| [645](https://cwe.mitre.org/data/definitions/645.html) | Overly Restrictive Account Lockout Mechanism | automatic |
| [798](https://cwe.mitre.org/data/definitions/798.html) | Use of Hard-coded Credentials | automatic |
| [804](https://cwe.mitre.org/data/definitions/804.html) | Guessable CAPTCHA | automatic |
| [836](https://cwe.mitre.org/data/definitions/836.html) | Use of Password Hash Instead of Password for Authentication | automatic |
| [1299](https://cwe.mitre.org/data/definitions/1299.html) | Missing Protection Mechanism for Alternate Hardware Interface | automatic |
| [1390](https://cwe.mitre.org/data/definitions/1390.html) | Weak Authentication | automatic |
| [1391](https://cwe.mitre.org/data/definitions/1391.html) | Use of Weak Credentials | automatic |
| [1392](https://cwe.mitre.org/data/definitions/1392.html) | Use of Default Credentials | automatic |
| [1393](https://cwe.mitre.org/data/definitions/1393.html) | Use of Default Password | automatic |
| [1394](https://cwe.mitre.org/data/definitions/1394.html) | Use of Default Cryptographic Key | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 6.1.4 | curated |

More: [[standard-nist-800-63]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10101](https://github.com/zaproxy/zap-extensions/blob/main/addOns/accessControl/src/main/java/org/zaproxy/zap/extension/accessControl/ExtensionAccessControl.java) | Access Control Issue - Improper Authentication | automatic |
| [10105-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java) | Authentication Credentials Captured | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [138-448](https://opencre.org/cre/138-448). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
