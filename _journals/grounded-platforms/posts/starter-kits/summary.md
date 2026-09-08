---
timetoread: "2 min read"
---

When a platform team in my organization ships a starter kit, the finished capability has one shape: **a single portal action produces a working service** — repository, CI/CD pipeline, infrastructure claim, namespace, and catalog entry, with ownership recorded from minute one. The template is a versioned product, it is tested like software before anyone consumes it, and it is proven end to end — because an untested template makes every consuming team the test.

**What changes**

* **The skeleton is complete, and kept as code.** Starter kits live in a dedicated templates repository; the skeleton carries everything a real service needs on day one — container build file, CI/CD workflow, package manifest, README, source and configuration files. A generated service builds and deploys before the team writes a line of business logic.
* **The scaffold finishes the birth.** The portal template captures the real decisions (name, owner, database, port, repository location) and runs every step: fetch, conditional configuration, infrastructure-claim generation, repository publishing, namespace creation, catalog registration, and next-step links. No follow-up tickets.
* **Templates carry version metadata.** Platform metadata records the template name and version in every generated service — so upgrades are a query and a campaign, not archaeology.
* **Testing is behavioral, not structural.** Before publishing, a test project is generated and made to install, build, pass tests and linting, start, and answer its health endpoint. Every failure is fixed first; publishing runs through a validated script into the catalog.
* **Done means proven end to end.** Create a service through the portal, validate it locally, deploy it to the cluster, push a change, and watch the pipeline complete — once per template, honestly, before it is announced and again on material change.

**What it costs**

* Template maintenance is a standing product obligation — a stale template teaches teams to fork old repositories instead of riding the paved path.
* The behavioral test bar makes template changes slower to ship; that is the price of never using consuming teams as the test bed.
* The reference build covers one backend-service template; each new recurring service class (frontend, data pipeline, ML) is its own build to this same bar.

**What we are not doing**

* Not team onboarding — getting a team onto the platform is [[self-service-onboarding]]; this record starts a service once they are on.
* Not defining the pipeline or the claim model — those live in [[cicd-as-a-platform-service]] and [[self-service-infrastructure]]; the template wires them in.
* Not banning off-path services — the paved path has exits; off-path services still register in the catalog.

*The Article tab carries the rationale, the reference stack, and the anti-patterns; the Checklist tab carries the full build-and-publish checklist. Grounded in the* Platform Engineer's Handbook *Starter Kit Template chapter.*
