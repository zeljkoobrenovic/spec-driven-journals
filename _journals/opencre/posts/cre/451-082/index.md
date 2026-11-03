---
id: "CRE-451-082"
title: "File execution"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-451-082
excerpt: "CRE 451-082 · in Technical application security controls › Input and output protection › File handling · 6 sub-requirements."
tags: 
---
> **CRE**: [451-082](https://opencre.org/cre/451-082)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]]

## Where It Sits

---begin mermaid---
graph LR
  n130550["File handling"] --> n451082["File execution"]
  n451082 --> n683722["Block direct execution of file metadata from…"]
  n451082 --> n737086["Ignore/at least validate  filename metadata f…"]
  n451082 --> n742056["Ignore/at least validate  filename metadata f…"]
  n451082 --> n421513["Ignore/at least validate filenames from untru…"]
  n451082 --> n777470["Ignore/block execution logic from untrusted s…"]
  n451082 --> n675168["Sanitize filename metadata from untrusted ori…"]
  style n451082 stroke-width:3px
---end mermaid---

## Contains

- [[cre-683-722]]
- [[cre-737-086]]
- [[cre-742-056]]
- [[cre-421-513]]
- [[cre-777-470]]
- [[cre-675-168]]

## Mapped Standards and Tools

OpenCRE has no direct standard links on this requirement; see the requirements it contains.

## Source

Generated from the OpenCRE catalogue entry [451-082](https://opencre.org/cre/451-082). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
