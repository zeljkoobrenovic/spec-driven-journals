---
id: "STD-NIST-SSDF"
title: "NIST SSDF"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: standard-nist-ssdf
excerpt: "Standard · 44 sections mapped to 28 CREs (46 curated, 0 automatic links)."
tags: standard, mapping
---
> **Standard**: NIST SSDF
>
> **Coverage**: 44 sections linked to 28 CREs — 46 curated and 0 automatic links.

## Where It Lands in the CRE Tree

| Top-level area | CREs |
| --- | --- |
| [[cre-616-305]] | 16 |
| [[cre-567-755]] | 7 |
| [[cre-636-660]] | 3 |
| [[cre-862-452]] | 2 |

## Sections and Their CREs

Each row is one section of NIST SSDF and the common requirements OpenCRE links it to. Links marked *(auto)* were derived automatically.

| ID | Section | CREs |
| --- | --- | --- |
|  | code, executable code, and configuration-as-code – based on the principle of least privilege so that only authorized personnel, tools, services, etc. have access. | [[cre-080-466]] |
|  | should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing and, if so, which types of testing should be used. | [[cre-570-487]] |
| PO.1.1 | Identify and document all security requirements for the organization’s software development infrastructures and processes, and maintain the requirements over time. | [[cre-148-853]] |
| PO.1.2 | Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time. | [[cre-004-517]] |
| PO.1.3 | Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software. (Formerly PW.3.1) | [[cre-613-285]] |
| PO.2.1 | Create new roles and alter responsibilities for existing roles as needed to encompass all parts of the SDLC. Periodically review and maintain the defined roles and responsibilities, updating them as needed. | [[cre-013-021]] |
| PO.2.2 | Provide role-based training for all personnel with responsibilities that contribute to secure development. Periodically review personnel proficiency and role-based training, and update the training as needed. | [[cre-244-750]] |
| PO.2.3 | Obtain upper management or authorizing official commitment to secure development, and convey that commitment to all with development-related roles and responsibilities. | [[cre-251-446]] |
| PO.3.1 | Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are to be integrated with each other. | [[cre-148-853]] |
| PO.3.2 | Follow recommended security practices to deploy, operate, and maintain tools and toolchains. | [[cre-148-853]] |
| PO.3.3 | Configure tools to generate artifacts of their support of secure software development practices as defined by the organization. | [[cre-464-513]]<br>[[cre-745-356]] |
| PO.4.1 | Define criteria for software security checks and track throughout the SDLC. | [[cre-433-442]] |
| PO.4.2 | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. | [[cre-433-442]] |
| PO.5.1 | Separate and protect each environment involved in software development. | [[cre-148-853]] |
| PO.5.2 | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc.) to perform development-related tasks using a risk-based approach. | [[cre-148-853]] |
| PS.1.1 | Store all forms of code – including source | [[cre-080-466]] |
| PS.2.1 | Make software integrity verification information available to software acquirers. | [[cre-307-507]] |
| PS.3.1 | Securely archive the necessary files and supporting data (e.g., integrity verification information, provenance data) to be retained for each software release. | [[cre-461-680]] |
| PS.3.2 | Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials (SBOM)). | [[cre-863-521]] |
| PW.1.1 | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. | [[cre-068-102]] |
| PW.1.2 | Track and maintain the software’s security requirements, risks, and design decisions. | [[cre-820-877]] |
| PW.1.3 | Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management, identity management, access control, and vulnerability management systems) instead of creating proprietary implementations of security features and services. | [[cre-344-611]] |
| PW.2.1 | Have 1) a qualified person (or people) who were not involved with the design and/or 2) automated processes instantiated in the toolchain review the software design to confirm and enforce that it meets all of the security requirements and satisfactorily addresses the identified risk information. | [[cre-626-250]] |
| PW.4.1 | Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open- source, and other third-party developers for use by the organization’s software. | [[cre-613-285]] |
| PW.4.2 | Create and maintain well-secured software components in-house following SDLC processes to meet common internal software development needs that cannot be better met by third-party software components. | [[cre-417-342]] |
| PW.4.4 | Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements, as defined by the organization, throughout their life cycles | [[cre-613-285]] |
| PW.5.1 | Follow all secure coding practices that are appropriate to the development languages and environment to meet the organization’s requirements | [[cre-636-660]] |
| PW.6.1 | Use compiler, interpreter, and build tools that offer features to improve executable security. | [[cre-314-131]] |
| PW.6.2 | Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations. | [[cre-314-131]] |
| PW.7.1 | Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a fully automated way or in conjunction with a person) should be used, as defined by the organization. | [[cre-411-684]] |
| PW.7.2 | Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended remediations in the development team’s workflow or issue tracking system. | [[cre-411-684]] |
| PW.8.1 | Determine whether executable code testing | [[cre-570-487]] |
| PW.8.2 | Scope the testing, design the tests, perform the testing, and document the results, including recording and triaging all discovered issues and recommended remediations in the development team’s workflow or issue tracking system. | [[cre-088-377]] |
| PW.9.1 | Define a secure baseline by determining how to configure each setting that has an effect on security or a security-related setting so that the default settings are secure and do not weaken the security functions provided by the platform, network infrastructure, or services. | [[cre-180-488]] |
| PW.9.2 | Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators. | [[cre-180-488]] |
| RV.1.1 | Gather information from software acquirers, users, and public sources on potential vulnerabilities in the software and third-party components that the software uses, and investigate all credible reports. | [[cre-613-286]]<br>[[cre-732-148]] |
| RV.1.2 | Review, analyze, and/or test the software’s code to identify or confirm the presence of previously undetected vulnerabilities. | [[cre-433-442]] |
| RV.1.3 | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities, and processes needed to support that policy. | [[cre-463-577]] |
| RV.2.1 | Analyze each vulnerability to gather sufficient information about risk to plan its remediation or other risk response. | [[cre-732-148]] |
| RV.2.2 | Plan and implement risk responses for vulnerabilities. | [[cre-732-148]] |
| RV.3.1 | Analyze identified vulnerabilities to determine their root causes. | [[cre-732-148]] |
| RV.3.2 | Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently. | [[cre-732-148]] |
| RV.3.3 | Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and proactively fix them rather than waiting for external reports. | [[cre-732-148]] |
| RV.3.4 | Review the SDLC process, and update it if appropriate to prevent (or reduce the likelihood of) the root cause recurring in updates to the software or in new software that is created. | [[cre-635-851]] |

## Source

Generated from the OpenCRE catalogue. Browse NIST SSDF on [opencre.org](https://opencre.org/node/standard/NIST%20SSDF).
