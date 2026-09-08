Why the platform's own foundation is code — repositories, secrets, membership, and releases — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an engineer unrolls a grand platform blueprint while an executive points at the bare ground beneath them.](assets/images/groundwork/comic-01-groundwork-first.jpeg)
**Panel 1:** *The hook: before my platform builds anything for anyone else, it lays its own groundwork — and the groundwork is code.*

![Comic panel: repositories float away as untethered balloons while an engineer clicks a giant web console.](assets/images/groundwork/comic-02-the-clickops-foundation.jpeg)
**Panel 2:** *The problem: the ClickOps foundation — repositories and policies clicked into existence by whoever had admin that day, invisible to review, drifting from day one.*

![Comic panel: an engineer drops a golden key into a commit box while a copier labeled History prints endless copies of the key.](assets/images/groundwork/comic-03-the-credential-that-made-it-in.jpeg)
**Panel 3:** *The wrong way: the credential that made it in 'temporarily' — history is forever, and there is no mostly-clean history.*

![Comic panel: a single config file feeds a conveyor through preview, review, and apply arches, producing shielded repository buildings.](assets/images/groundwork/comic-04-one-file-is-the-truth.jpeg)
**Panel 4:** *The principle: one configuration file is the source of truth — repositories are provisioned by IaC through preview, review, apply, with delete protection proven.*

![Comic panel: an engineer runs a scripted loop feeding real keys into a vault while a framed cardboard example key hangs nearby.](assets/images/groundwork/comic-05-the-vault-flow.jpeg)
**Panel 5:** *How it plays out: example files are committed, real values are gitignored, and credentials enter the vault through a scripted flow — authenticate, unlock, upsert, sync, lock.*

![Comic panel: a new engineer enters through a green diff doorway while a leaver's badge dissolves under a stamped red diff.](assets/images/groundwork/comic-06-onboarding-is-a-diff.jpeg)
**Panel 6:** *How it plays out: onboarding is a diff, offboarding is a diff — membership lives in configuration, applied and verified through the same pipeline.*

![Comic panel: an admin's unsigned commit bounces off a branch gate while a wax-sealed signed commit passes through.](assets/images/groundwork/comic-07-administrators-included.jpeg)
**Panel 7:** *How it plays out: branch protection binds administrators, and signed commits are required on every branch — both the rejection and the success are verified.*

![Comic panel: pushes flow through a validation checkpoint while a tagged cart waits at an approval gate and a rollback lever is tested.](assets/images/groundwork/comic-08-the-tag-and-the-gate.jpeg)
**Panel 8:** *What it costs: every release is a named, gated, auditable act — and the rollback lever gets pulled regularly, because an untested rollback is a hope.*

![Comic panel: a second engineer rebuilds the entire foundation pop-up-book style from a single repository box.](assets/images/groundwork/comic-09-the-second-engineer-test.jpeg)
**Panel 9:** *The closer: the groundwork test — a second platform engineer can reproduce the entire foundation from the repository alone.*
