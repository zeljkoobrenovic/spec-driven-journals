Why an internal platform is three planes and two tests — in eight panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a sleek one-button platform box in front of a curtain barely hiding a tangled leaking mass of pipes.](assets/images/implementing-platforms/comic-01-hidden-complexity-returns.jpeg)
**Panel 1:** *The hook: a platform that hides complexity without a way back hasn't reduced cognitive load — it has deferred it to the worst moment.*

![Comic panel: a developer presses a self-service kiosk button while a cutaway shows an engineer inside clicking manually among tickets.](assets/images/implementing-platforms/comic-02-the-ticket-platform.jpeg)
**Panel 2:** *The problem: if every request becomes a ticket and a human, it is not a platform — it is ClickOps with a facade.*

![Comic panel: a developer unrolls an endless scroll of configuration fields while an executive taps it disapprovingly.](assets/images/implementing-platforms/comic-03-forty-parameter-template.jpeg)
**Panel 3:** *The wrong way: the forty-parameter template — all the indirection of a platform, none of the cognitive-load reduction.*

![Comic panel: a three-story cutaway building with management, control, and services floors, explained by two characters.](assets/images/implementing-platforms/comic-04-three-planes.jpeg)
**Panel 4:** *The principle: an internal platform is three planes — a self-service management plane, a reconciling control plane, and a services plane that does the work.*

![Comic panel: a circular observe-analyze-act loop mechanism nudging a drifted server block back into alignment.](assets/images/implementing-platforms/comic-05-reconciliation-engine.jpeg)
**Panel 5:** *How it runs: reconciliation is the engine — a platform that provisions but does not reconcile is only right on day one.*

![Comic panel: a developer beside a broken resource follows a glowing thread up to a specification document held above.](assets/images/implementing-platforms/comic-06-the-thread-back.jpeg)
**Panel 6:** *How it runs: traceability is the price of abstraction — every generated resource keeps a thread back to the spec that produced it.*

![Comic panel: a noisy tenant shakes a shared building while a burst storm rains arrows on a small control room.](assets/images/implementing-platforms/comic-07-tenancy-and-bursts.jpeg)
**Panel 7:** *The cost: tenancy is a conscious decision and scale fails in bursts — test the control plane before adoption performs the test for you.*

![Comic panel: an executive shows a notebook with two checked boxes, less load and traceable, beside a tidy platform box.](assets/images/implementing-platforms/comic-08-two-tests.jpeg)
**Panel 8:** *The closer: every abstraction earns its keep by two tests — it genuinely reduces cognitive load, and a failure can be traced back through it.*
