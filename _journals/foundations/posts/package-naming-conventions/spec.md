---
status: draft
revised: 2026-05-21
---

# Spec: Package Naming Conventions Across Ecosystems

> Backfilled after the post. Third leaf of the naming/tagging trio with
> [[github-naming-tagging]] and [[aws-naming-tagging]]. The same logical
> name travels from a git repo to AWS resources to published packages.

## Intent

Define one logical package name per artefact
(`<domain>-<system>-<component>`) and a deterministic mapping into each
ecosystem Organization uses: JVM (Maven/Gradle), npm, Python (PyPI / internal
index), .NET (NuGet), and OCI container images. The record should make
publishing decisions mechanical and keep nothing internal from leaking to
public registries by accident.

## Audience

- **Library authors** picking package names and registries.
- **Service teams** publishing OCI images.
- **Platform / build engineers** wiring CI to publish to internal vs public
  registries.
- **Consumers** trying to predict where a given artefact lives.
- **AI agents** generating new modules and needing to pick names.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can map a logical name to the correct shape in each of the
      five ecosystems without guessing.
- [ ] Reader knows the default is internal-only and that public publication
      needs an explicit ADR.
- [ ] Reader can connect a published package back to its GitHub repo (same
      `<domain>-<system>-<component>` triple).
- [ ] Reader understands SemVer is for libraries and date-based tags are
      for service container images.
- [ ] Reader recognises the shared vocabulary with
      [[github-naming-tagging]] and [[aws-naming-tagging]].

## Non-goals

- Dictating internal code structure beyond root namespaces/packages.
- Defining what *should* be published vs kept internal — that is a separate
  per-artefact decision.
- Changing how versions are computed by CI (only how they are shaped on the
  outside).
- Listing every ecosystem Organization might ever use — the five named are the
  ones in active use.

## Open questions

- Whether the JVM `groupId` should always be the full
  `io.organization.<domain>.<system>` or whether short forms (drop `<system>`
  for org-wide libraries) are acceptable.
- How to handle the .NET PascalCase mapping when a `<domain>` or `<system>`
  contains digits or hyphens.
- Whether OCI image tags should ever combine SemVer + date (immutable
  semver, mutable date) or stay disjoint.
- The Python distribution-name / import-name split confuses tooling
  occasionally — worth a small follow-up on best-practice imports.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Made every ecosystem map to **the same logical name**
  (`<domain>-<system>-<component>`). Considered letting each ecosystem
  pick its own; rejected because the value is precisely the
  cross-ecosystem traceability — a `pip install`, a Maven coordinate,
  and an OCI image should resolve to the same artefact by string match.
- **2026-05-20** — Defaulted to **internal-only publication**. Considered
  public-by-default; rejected because most artefacts have no business
  being on a public registry, and an explicit opt-in via ADR keeps the
  decision in the open.
- **2026-05-20** — Used **SemVer for libraries**, **date-based tags for
  service container images**. Mirrors the choice in
  [[github-naming-tagging]]; same rationale (compatibility vs release
  ordering).
- **2026-05-20** — Adopted **scoped npm packages** (`@organization/...`).
  Considered unscoped names; rejected because unscoped names collide
  with the public registry and signal that the package belongs to the
  org, not to whoever happened to publish it.
- **2026-05-20** — Used **`io.organization` reverse-DNS** for JVM. Considered
  `com.organization`; chose `io.` to align with modern OSS conventions and
  avoid implying corporate-package semantics.

## Sources

- **Internal**
  - [[github-naming-tagging]] — companion record providing the logical
    name vocabulary and SemVer/date-tag conventions.
  - [[aws-naming-tagging]] — companion record; together with this
    record completes the GitHub/AWS/packages naming trio.
- **External**
  - SemVer 2.0 — the versioning scheme for libraries.
  - OCI Image Spec — informs the container image reference shape.
  - Maven Central groupId conventions (reverse-DNS) — informs the JVM
    coordinate shape.
  - npm scoped packages documentation — informs the `@organization/...`
    convention.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
