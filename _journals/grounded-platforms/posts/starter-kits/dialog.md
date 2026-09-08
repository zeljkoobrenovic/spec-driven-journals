---
timetoread: "8 min listen"
---

## The First Hour

**Ben:** Blunt version first. Every portal demo I have ever seen ends with "and now you scaffold a service from a template." It always works in the demo. Why does an operating model need a whole record for the easy part?

**Ana:** Because the demo is precisely the problem this record exists to see through. The demo shows a template generating files. The record's bar is a template producing a *working service*: one portal action, and out comes a repository with a complete skeleton, a CI/CD pipeline already wired in, an infrastructure claim, a namespace to run in, and a catalog entry that says who owns it. Most "starter kits" in the wild fail somewhere between generating files and that sentence.

**Ben:** And why does that gap matter so much? A team can wire the rest by hand in a day.

**Ana:** Because a team starting a new service makes its platform decision in the first hour, not in the architecture review. If the paved path is a wiki page of copy-paste steps — the record calls that the wiki scaffold — every service is hand-assembled, subtly different, and drifting from the platform from day one. This is [[four-pillars]] pillar one and pillar three meeting in one artifact: a curated opinion, consumed self-service. The starter kit is where the paved-path claim either becomes real or gets quietly disproved.

**Ben:** The record also insists the template does more than create the repository. Isn't namespace creation and catalog registration just ceremony?

**Ana:** There is a named anti-pattern for skipping it: scaffold and vanish. The template creates a repository and stops — and namespace, infrastructure claim, pipeline wiring, and catalog registration become the team's four follow-up tickets. The scaffold relocated the work instead of removing it. That is why the template's steps run all the way through: fetch the skeleton, apply conditional configuration — a database only if one was chosen — generate the claim, publish the repository, create the namespace, register the service, and end with useful next-step links. The service exists everywhere it needs to exist, with ownership recorded from minute one.

## The Template Is a Product

**Ben:** The versioning obsession surprised me. Platform metadata in the manifest, template name and version recorded in every generated service. That smells like bureaucracy for a bunch of boilerplate.

**Ana:** Run the clock forward. The template generates its tenth service, then its fortieth, and then the template improves — a new pipeline, a patched base image, a fixed vulnerable dependency. Now the only question that matters is: *which services carry the old one?* Without recorded template name and version, the answer is archaeology. With metadata stamped at generation time, upgrades become a query and a campaign. The record's phrase for the failure is the unversioned template — a one-way door that looks like a product.

**Ben:** So the concrete executive test is —

**Ana:** The platform team can list, from metadata alone, every service generated from each template version. If they cannot, the starter kit is a demo, not a capability.

**Ben:** Let me push on parameters, then. If the template is a product, product thinking says give users choices. Framework, database, message broker, port, replicas —

**Ana:** And the record pushes back with the kitchen-sink template: one template, forty parameters, every framework option — curation abdicated into a form. The team's first platform experience becomes a questionnaire it cannot answer. The reference template asks only what a team actually decides: service information, owning team, database options, service port, repository location. Everything else is the platform's opinion. That is what curation means.

## Tested Like Software

**Ben:** Now the testing section, which is where I think the record over-reaches. It demands a generated test project that installs, builds, passes unit tests, passes linting, starts up, and answers its health endpoint — before every publish. For a template. Isn't structural validation enough?

**Ana:** Structural validation is necessary and nowhere near sufficient — a template can be syntactically perfect and generate a service that does not compile. The bar is behavioral because the template's output is software, so its test must be running software. Generate a test project and make it live: dependencies install, build passes, tests pass, linting passes, the application starts, the health endpoint responds. And fix all failures before publishing — that clause is in the source checklist verbatim.

**Ben:** The cost is real, though. That makes every template change slower to ship.

**Ana:** Accepted, and named as a cost. Because the alternative is worse than no template: the untested template ships its defect to every team that trusts the paved path, at the exact moment they were most willing to trust it. The first team to scaffold discovers the build failure, and every team after them. An untested template makes every consuming team the test — that is the record's most quotable line for a reason.

**Ben:** Publishing is also scripted, I noticed. Portal URL, token, repository variables, a publishing script, validation gates.

**Ana:** Because the templates repository is the source of truth, and the portal catalog is a publish target — not an editing surface. A publish is: script runs, validation succeeds, template registered in the catalog, visible in the portal. Same discipline as any other software release.

## The End-to-End Proof

**Ben:** The final verification reads almost ceremonial: create a service through the portal, clone it, build it locally, deploy it to the cluster, push a change, watch the pipeline go green. If every step was already tested, why prove the whole chain?

**Ana:** Because the chain crosses seams that no isolated test touches — portal to repository, repository to pipeline, claim to infrastructure, deployment to catalog — and seams break silently. The record's name for skipping this is the demo-day template: verified to generate files, never to deploy. Works beautifully in the portal, dies at the cluster. The proof runs once per template, honestly, before it is announced — and again on material change. Not on every scaffold; the record is explicit about that.

**Ben:** And the consumer-side validation — clone, install, build, test, lint, container build, claim exists, catalog metadata valid, local development works. That is a lot of confirming.

**Ana:** It is an afternoon of confirming, once, versus every future team silently absorbing whichever step would have failed. The executive version of the whole record fits in one sentence: portal click to deployed service with a green pipeline, measured in minutes, without a ticket, without the platform team touching anything.

**Ben:** One trap left. Teams that skip the portal entirely and copy last quarter's generated repo. I have watched that happen everywhere.

**Ana:** Fork-and-forget — and the record treats it as a signal, not a crime. Teams fork old repositories when the template is stale or slow, which means the template stopped being a product. That is a named revisit trigger, and it is why template maintenance is a standing obligation under [[platform-as-a-product]], not a one-time build. The measurement side — whether the path is actually fast and actually used — lives in [[devex-evaluation]].

## What This Record Is Not

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** Three fences. It is not team onboarding — getting a team onto the platform, with tenancy, access, and quotas, is [[self-service-onboarding]]; this record starts a service once the team is already on. It is not the pipeline or the infrastructure model — those live in [[cicd-as-a-platform-service]] and [[self-service-infrastructure]]; the template wires them in and the final proof watches them run. And it is not a ban on off-path services — the paved path has exits, and off-path services still register in the catalog. Also worth saying: Backstage, GitHub, Crossplane are the reference stack, the worked example. The commitments hold at capability level and survive a tool swap.

**Ben:** So the whole record in one breath.

**Ana:** One portal action produces a working service — repository, pipeline, claim, namespace, catalog entry. The template is versioned, tested like software, and proven end to end before anyone consumes it.

**Ben:** And if the template is not tested?

**Ana:** Then it still gets tested — by every team that trusts it. The only choice is who pays.
