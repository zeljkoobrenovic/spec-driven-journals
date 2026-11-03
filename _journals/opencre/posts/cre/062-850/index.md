---
id: "CRE-062-850"
title: "MFA/OTP"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-062-850
excerpt: "CRE 062-850 · in Technical application security controls › Authentication › Authentication mechanism · 21 sub-requirements."
tags: 
---
> **CRE**: [062-850](https://opencre.org/cre/062-850)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]]

## Where It Sits

---begin mermaid---
graph LR
  n270568["Authentication mechanism"] --> n062850["MFA/OTP"]
  n062850 --> n525361["Authenticate by OTP token entry or user-initi…"]
  n062850 --> n076470["Biometric authenticators only as secondary fa…"]
  n062850 --> n102811["Communicate out of band multi factor authenti…"]
  n062850 --> n681823["Defined lifetime of time-based one-time password"]
  n062850 --> n354753["Do not offer weak (clear text) multi-factor a…"]
  n062850 --> n440361["Ensure that physical single factor OTP genera…"]
  n062850 --> n816631["Ensure timely expiration of out of band authe…"]
  n062850 --> n622835["Generate initial passwords with sufficient se…"]
  n062850 --> n346640["Generate multi-factor lookup secrets with suf…"]
  n062850 --> n646227["Log and reject re-use of valid time-based OTP…"]
  n062850 --> n524446["Mandate using multi factor authentication"]
  n062850 --> n342764["Only store hashed authentication codes"]
  n062850 --> n354752["Prioritize strong multi-factor authenticators…"]
  n062850 --> n553413["Support subscriber-provided authentication de…"]
  n062850 --> n841757["Use approved cryptographic algorithms in gene…"]
  n062850 --> n101217["Use lookup secrets only once"]
  n062850 --> more062850["… 5 more"]
  style n062850 stroke-width:3px
---end mermaid---

## Contains

- [[cre-525-361]]
- [[cre-076-470]]
- [[cre-102-811]]
- [[cre-681-823]]
- [[cre-354-753]]
- [[cre-440-361]]
- [[cre-816-631]]
- [[cre-622-835]]
- [[cre-346-640]]
- [[cre-646-227]]
- [[cre-524-446]]
- [[cre-342-764]]
- [[cre-354-752]]
- [[cre-553-413]]
- [[cre-841-757]]
- [[cre-101-217]]
- [[cre-168-186]]
- [[cre-206-254]]
- [[cre-543-428]]
- [[cre-404-126]]
- [[cre-513-845]]

## Related CREs

- [[cre-170-772]]
- [[cre-270-634]]
- [[cre-201-246]]

## Mapped Standards and Tools

OpenCRE has no direct standard links on this requirement; see the requirements it contains.

## Source

Generated from the OpenCRE catalogue entry [062-850](https://opencre.org/cre/062-850). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
