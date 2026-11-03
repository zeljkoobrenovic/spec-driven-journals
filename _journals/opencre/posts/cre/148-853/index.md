---
id: "CRE-148-853"
title: "Setup and maintain a secure software development process"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-148-853
excerpt: "CRE 148-853 · in Governance processes for security › Security organizing processes › Program management › Program management for secure software development · 9 mappings to 2 standards and tools."
tags: NIST SSDF, PCI DSS
---
> **CRE**: [148-853](https://opencre.org/cre/148-853)
>
> **Part of**: [[cre-567-755]] › [[cre-563-088]] › [[cre-571-271]] › [[cre-261-010]]
>
> **Maps to**: [[standard-nist-ssdf]], [[standard-pci-dss]]

## Related CREs

- [[cre-616-305]]
- [[cre-862-452]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PO.1.1 | Identify and document all security requirements for the organization’s software development infrastructures and processes, and maintain the requirements over time. | curated |
| PO.3.1 | Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are to be integrated with each other. | curated |
| PO.3.2 | Follow recommended security practices to deploy, operate, and maintain tools and toolchains. | curated |
| PO.5.1 | Separate and protect each environment involved in software development. | curated |
| PO.5.2 | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc.) to perform development-related tasks using a risk-based approach. | curated |

More: [[standard-nist-ssdf]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.1 | Processes and mechanisms for developing and maintaining secure systems and software are defined and understood. | automatic |
| 6.2 | Bespoke and custom software are developed securely. | automatic |
| 6.2.1 | Bespoke and custom software are developed securely, as follows: () Based on industry standards and/or best practices for secure development. () In accordance with PCI DSS (for example, secure authentication and logging). () Incorporating consideration of information security issues during each stage of the software development lifecycle. (CUSTOMIZED APPROACH OBJECTIVE): Bespoke and custom software is developed in accordance with PCI DSS and secure development processes throughout the software lifecycle. (APPLICABILITY NOTES): This applies to all software developed for or by the entity for the entity’s own use. This includes both bespoke and custom software. This does not apply to third-party software. | automatic |
| 6.2.4 | Software engineering techniques or other methods are defined and in use by software development personnel to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software, including but not limited to the following: () Injection attacks, including SQL, LDAP, XPath, or other command, parameter, object, fault, or injection-type flaws. () Attacks on data and data structures, including attempts to manipulate buffers, pointers, input data, or shared data. () Attacks on cryptography usage, including attempts to exploit weak, insecure, or inappropriate cryptographic implementations, algorithms, cipher suites, or modes of operation. () Attacks on business logic, including attempts to abuse or bypass application features and functionalities through the manipulation of APIs, communication protocols and channels, clientside functionality, or other system/application functions and resources. This includes cross-site scripting (XSS) and cross-site request forgery (CSRF). () Attacks on access control mechanisms, including attempts to bypass or abuse identification, authentication, or authorization mechanisms, or attempts to exploit weaknesses in the implementation of such mechanisms. () Attacks via any “high-risk” vulnerabilities identified in the vulnerability identification process, as defined in Requirement 6.3.1. (CUSTOMIZED APPROACH OBJECTIVE): Bespoke and custom software cannot be exploited via common attacks and related vulnerabilities. (APPLICABILITY NOTES): This applies to all software developed for or by the entity for the entity’s own use. This includes both bespoke and custom software. This does not apply to third-party software. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [148-853](https://opencre.org/cre/148-853). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
