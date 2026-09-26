<!-- comic-style
{
  "cast": "MORGAN: a thoughtful investor technology adviser with short dark hair and a green jacket, used in the fund scenarios. ALEX: a practical CTO, a brown-skinned man with short, tight dark curls close to his head and blue rolled-up sleeves. SAM: a CFO, a man with short brown hair, round glasses and an amber cardigan. PRIYA: a product leader with straight dark hair and plum sleeves. INES: a CEO with short grey hair and a navy jacket. All are fictional; none represents a person in a real case.",
  "style": "Clean editorial explainer comic pages, each one image of three stacked full-width strips: navy ink outlines, restrained green, blue and amber accents on warm ivory, generous space, expressive people and simple physical props. Dialogue, short labels and the supplied amounts are lettered in the artwork, exactly as scripted. Money bags, coins and banknotes are plain and undecorated; the euro sign appears only inside supplied text, and arrows, documents and screens carry plain lines, never lettering. No photorealism, logos, titles or unsupplied text. Keep the same character appearances throughout the journal.",
  "reference": "_research/comic-cast-20260913.jpeg",
  "identity": {
    "Morgan": "MORGAN is a light-skinned WOMAN with a short, straight, JET-BLACK bob cut level with her jaw and a straight fringe across her forehead (never brown hair, never a side parting), and a bright green jacket over a white top, first person in the reference; her face must match the reference sheet exactly.",
    "Alex": "ALEX is a medium-brown-skinned MAN with a masculine face, broad shoulders and a straight masculine build, SHORT tight dark curls close to his head (not a large afro), a blue rolled-sleeve shirt and blue jeans, second person in the reference; fill his face, neck and hands with the same brown skin color in every strip.",
    "Sam": "SAM is a light-skinned MAN with a masculine face and SHORT brown hair cropped above his ears (never a bob, never chin-length hair, never a woman), round glasses and an amber cardigan over a white shirt, third person in the reference.",
    "Priya": "PRIYA is a brown-skinned WOMAN with straight shoulder-length dark hair and a plum blouse, fourth person in the reference.",
    "Ines": "INES is a light-skinned OLDER WOMAN with a short GREY bob (grey hair, never dark) and a navy jacket, fifth person in the reference."
  },
  "short": {
    "Morgan": "a light-skinned woman with a jet-black jaw-length bob and fringe, in a bright green jacket",
    "Alex": "a brown-skinned man with short tight dark curls, in a blue rolled-sleeve shirt",
    "Sam": "a light-skinned man with short brown hair and round glasses, in an amber cardigan over a collared white shirt",
    "Priya": "a brown-skinned woman with straight shoulder-length dark hair, in a plum blouse",
    "Ines": "an older light-skinned woman with a short grey bob, in a navy jacket"
  }
}
-->

**Comic.** Larkspur is a fictional company that sells scheduling software and, since April 2027, an AI feature (artificial intelligence: software that uses a trained model) that sorts a customer’s inspection documents for €300 a month. Forty customers pay for it. Larkspur buys the model’s work from a vendor by the token, the pieces of text the model reads and writes, so the bill moves while the price stays fixed, and it has grown faster than the feature’s revenue for four months. Morgan, the technology adviser working for Larkspur’s investor, has asked for “the AI ROI” before the next board meeting: return on investment, the money an investment leaves after its costs, divided by those costs, for a stated period. Every figure is fictional.

<!-- comic-page
{
  "id": "01-a-number-with-a-unit",
  "title": "A number with a unit",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-01-a-number-with-a-unit.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Morgan",
    "Alex",
    "Priya"
  ],
  "strips": [
    {
      "scene": "Morgan, at the left, holds up one large card with both hands, facing the reader. Alex, at the right, holds his hands open.",
      "labels": [
        "WHAT IS OUR AI ROI?"
      ],
      "label_notes": "The label is the large card Morgan holds up.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "Before the board meets: what is our AI ROI?"
        },
        {
          "who": "Alex",
          "text": "A number with a unit, a period and a condition. Start with the unit."
        }
      ]
    },
    {
      "scene": "A pinboard with exactly three large index cards pinned side by side in one row with clear gaps between them, every word fully visible. Alex, at the left of the pinboard, gestures toward the first two cards with an open hand. Priya, at the right of the pinboard, points at the third card.",
      "labels": [
        "PER MILLION TOKENS",
        "PER MODEL CALL",
        "PER DOCUMENT ACCEPTED"
      ],
      "label_notes": "One label per index card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Tokens are the vendor's unit. A model call is one request and its answer."
        },
        {
          "who": "Priya",
          "text": "Ours is a document sorted and accepted. A rejected one costs tokens, earns nothing."
        }
      ]
    },
    {
      "scene": "A whiteboard with one large heading line and, under it, exactly three short lines of large, neat handwriting, each line fully visible. Priya, at the left of the whiteboard, gestures toward it with an open hand. Alex, at the right of the whiteboard, points at the heading. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "labels": [
        "COST PER DOCUMENT: UP 80%",
        "LONGER PROMPT",
        "MORE RETRIEVED CONTEXT",
        "RETRIES TO LARGER MODEL"
      ],
      "label_notes": "COST PER DOCUMENT: UP 80% is the heading; the other three are the three lines under it, top to bottom.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Each was a sound product decision, made between April and August."
        },
        {
          "who": "Alex",
          "text": "Together they raised model cost per document 80% at unchanged prices. Nobody checked."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Morgan holds a card asking what is our AI ROI; three cards compare per million tokens, per model call and per document accepted; a whiteboard shows cost per document up 80% from a longer prompt, more retrieved context and retries to a larger model.",
  "caption": "AI, artificial intelligence, is software that uses a trained model; ROI, return on investment, is the money an investment leaves after its costs, divided by those costs, for a stated period. AI services are metered in tokens, the pieces of text a model reads and writes; a model call is one request sent to the model and its answer. Neither is the company’s unit. Larkspur charges €300 a month for documents sorted so a planner can schedule without reading them, so its unit is a document sorted and accepted without correction; a rejected classification costs tokens and delivers nothing useful. What a document costs is not fixed: between April and August 2027 a longer prompt (the instructions sent with each document), more retrieved context (extra material sent along) and retries (repeat requests after a failed check) to a larger, costlier model raised the model cost per document by about 80% at unchanged vendor prices. That measure includes which model handled each request, so it is a cost, not a bare token count. Morgan advises the investor, who has put money into Larkspur expecting a return; Alex leads technology; Priya leads product.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "2427bf461ab5b8fd86d70175ea5340e6563aa6ab0c088509716151ceb9e7dbc0"
  }
}
-->

![Comic page in three strips: Morgan holds a card asking what is our AI ROI; three cards compare per million tokens, per model call and per document accepted; a whiteboard shows cost per document up 80% from a longer prompt, more retrieved context and retries to a larger model.](assets/images/30-ai-worth-its-cost/comic-page-01-a-number-with-a-unit.jpeg)

**Page 1: A number with a unit.** AI, artificial intelligence, is software that uses a trained model; ROI, return on investment, is the money an investment leaves after its costs, divided by those costs, for a stated period. AI services are metered in tokens, the pieces of text a model reads and writes; a model call is one request sent to the model and its answer. Neither is the company’s unit. Larkspur charges €300 a month for documents sorted so a planner can schedule without reading them, so its unit is a document sorted and accepted without correction; a rejected classification costs tokens and delivers nothing useful. What a document costs is not fixed: between April and August 2027 a longer prompt (the instructions sent with each document), more retrieved context (extra material sent along) and retries (repeat requests after a failed check) to a larger, costlier model raised the model cost per document by about 80% at unchanged vendor prices. That measure includes which model handled each request, so it is a cost, not a bare token count. Morgan advises the investor, who has put money into Larkspur expecting a return; Alex leads technology; Priya leads product.

- *Strip 1.* **Morgan:** “Before the board meets: what is our AI ROI?” **Alex:** “A number with a unit, a period and a condition. Start with the unit.”
- *Strip 2.* **Alex:** “Tokens are the vendor's unit. A model call is one request and its answer.” **Priya:** “Ours is a document sorted and accepted. A rejected one costs tokens, earns nothing.”
- *Strip 3.* **Priya:** “Each was a sound product decision, made between April and August.” **Alex:** “Together they raised model cost per document 80% at unchanged prices. Nobody checked.”

<!-- comic-page
{
  "id": "02-two-months-on-one-basis",
  "title": "Two months on one basis",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-02-two-months-on-one-basis.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Sam",
    "Alex",
    "Priya"
  ],
  "strips": [
    {
      "scene": "A whiteboard with three lines of large, neat handwriting, each line fully visible. Sam, at the left of the whiteboard, gestures toward it with an open hand. Alex, at the right of the whiteboard, reads down the lines. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "April 2027, monthly, all on one basis.",
      "labels": [
        "20 CUSTOMERS: €6,000 REVENUE",
        "SUPPLIER RUNNING COST: €2,600",
        "AFTER STAFF TIME: +€750"
      ],
      "label_notes": "The three labels are the three lines on the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Revenue, then supplier running cost, then engineers' and support time at salary cost."
        },
        {
          "who": "Alex",
          "text": "In April the feature still earned €750 after those costs."
        }
      ]
    },
    {
      "scene": "A second whiteboard with three lines of large, neat handwriting, each line fully visible, drawn identically to the first. Sam, at the left of the whiteboard, points at the third line from the side. Priya, at the right of the whiteboard, frowns at it. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "August 2027, same lines.",
      "labels": [
        "40 CUSTOMERS: €12,000 REVENUE",
        "SUPPLIER RUNNING COST: €7,424",
        "AFTER STAFF TIME: −€1,124"
      ],
      "label_notes": "The three labels are the three lines on the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Twice the customers, and after staff time August loses €1,124."
        },
        {
          "who": "Priya",
          "text": "Engineering time is not on the vendor's invoice. Nobody saw it."
        }
      ]
    },
    {
      "scene": "Alex, at the left, holds up two large cards, one in each hand, facing the reader, every word fully visible. Sam, at the right, holds up one smaller card with a single figure.",
      "labels": [
        "PER DOCUMENT: €0.30 TO €0.30",
        "PER CUSTOMER: €130 TO €186",
        "PRICE: €300"
      ],
      "label_notes": "PER DOCUMENT: €0.30 TO €0.30 is the card in Alex's left hand, at the left of the strip; PER CUSTOMER: €130 TO €186 is the card in his right hand; PRICE: €300 is the card Sam holds.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Supplier cost per accepted document is flat. Per customer it is up, against €300."
        },
        {
          "who": "Sam",
          "text": "Customers send more documents, and each one costs more tokens."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: an April whiteboard shows 20 customers, €6,000 revenue, €2,600 supplier running cost and €750 left after staff time; an August whiteboard shows 40 customers, €12,000 revenue, €7,424 supplier running cost and a €1,124 loss after staff time; Alex holds cards reading per document €0.30 to €0.30 and per customer €130 to €186, and Sam holds a card reading price €300.",
  "caption": "Sam leads finance. Supplier running cost is the vendor’s token charges plus upkeep (sampled review, test-set runs and hosting, the paid computing that runs the feature’s own parts), counted in the month the work was done whichever month the bill is paid. Engineering and support time are allocations of salaries already in the payroll, the wages paid whether or not the feature exists, valued at cost; a cash forecast, the plan of money expected to enter and leave the company, leaves them out because payroll is already in it, and a decision about keeping the feature counts them. On that basis April earned €750 and August lost €1,124. Supplier cost per accepted document stayed at about €0.30, because the largely fixed upkeep is spread over nearly three times as many documents, while supplier cost per customer rose from €130 to about €186 against the €300 price.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "47b96f603a046eee98832ef1055073b6b6defef23de465ab0ed3d640ff98947a"
  }
}
-->

![Comic page in three strips: an April whiteboard shows 20 customers, €6,000 revenue, €2,600 supplier running cost and €750 left after staff time; an August whiteboard shows 40 customers, €12,000 revenue, €7,424 supplier running cost and a €1,124 loss after staff time; Alex holds cards reading per document €0.30 to €0.30 and per customer €130 to €186, and Sam holds a card reading price €300.](assets/images/30-ai-worth-its-cost/comic-page-02-two-months-on-one-basis.jpeg)

**Page 2: Two months on one basis.** Sam leads finance. Supplier running cost is the vendor’s token charges plus upkeep (sampled review, test-set runs and hosting, the paid computing that runs the feature’s own parts), counted in the month the work was done whichever month the bill is paid. Engineering and support time are allocations of salaries already in the payroll, the wages paid whether or not the feature exists, valued at cost; a cash forecast, the plan of money expected to enter and leave the company, leaves them out because payroll is already in it, and a decision about keeping the feature counts them. On that basis April earned €750 and August lost €1,124. Supplier cost per accepted document stayed at about €0.30, because the largely fixed upkeep is spread over nearly three times as many documents, while supplier cost per customer rose from €130 to about €186 against the €300 price.

- *Strip 1.* *Narration:* April 2027, monthly, all on one basis. **Sam:** “Revenue, then supplier running cost, then engineers' and support time at salary cost.” **Alex:** “In April the feature still earned €750 after those costs.”
- *Strip 2.* *Narration:* August 2027, same lines. **Sam:** “Twice the customers, and after staff time August loses €1,124.” **Priya:** “Engineering time is not on the vendor's invoice. Nobody saw it.”
- *Strip 3.* **Alex:** “Supplier cost per accepted document is flat. Per customer it is up, against €300.” **Sam:** “Customers send more documents, and each one costs more tokens.”

<!-- comic-page
{
  "id": "03-why-the-bill-changed",
  "title": "Why the bill changed",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-03-why-the-bill-changed.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Alex",
    "Sam",
    "Priya"
  ],
  "strips": [
    {
      "scene": "A whiteboard with one heading line and, under it, exactly three lines of large, neat handwriting, each line fully visible. Alex, at the left of the whiteboard, gestures toward it with an open hand. Sam, at the right of the whiteboard, reads down the lines. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "Model charges, April to August.",
      "labels": [
        "€1,400 TO €5,824",
        "USAGE: +€2,644",
        "CONSTRUCTION: +€3,236",
        "RATES: −€1,456"
      ],
      "label_notes": "€1,400 TO €5,824 is the heading; the other three are the lines under it, top to bottom.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Three causes, applied in this order. Each has a different owner."
        },
        {
          "who": "Sam",
          "text": "Customers, product and engineering, the vendor. Different remedies too."
        }
      ]
    },
    {
      "scene": "Priya, at the left, holds up one large card with both hands, facing the reader. Sam, at the right, raises an eyebrow.",
      "labels": [
        "VENDOR PRICE CUT: 20%"
      ],
      "label_notes": "The label is the large card Priya holds up.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "The June price cut went to the board as good news."
        },
        {
          "who": "Priya",
          "text": "It offset under half the construction rise. Without it: about €7,300."
        }
      ]
    },
    {
      "scene": "A pinboard with exactly four large index cards pinned side by side in one row with clear gaps between them, every word fully visible. Alex, at the left of the pinboard, gestures toward the cards with an open hand. Sam, at the right of the pinboard, rests a hand on a fifth card pinned at the lower right, facing the reader.",
      "labels": [
        "SHORTER PROMPT",
        "CAPPED CONTEXT",
        "SMALLER MODEL, EASY DOCUMENTS",
        "CACHED CONTEXT",
        "COST PER DOCUMENT: −35%"
      ],
      "label_notes": "The first four labels are the four pinned cards, in this left-to-right order; COST PER DOCUMENT: −35% is the fifth card, pinned at the lower right beside Sam.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Two engineer-weeks, tested on the release-gate samples, quality unchanged."
        },
        {
          "who": "Sam",
          "text": "Do it before we commit, or we pay for tokens we'll stop using."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: a whiteboard splits the rise in model charges from €1,400 to €5,824 into usage plus €2,644, construction plus €3,236 and rates minus €1,456; Priya holds a card reading vendor price cut 20%; four cards list shorter prompt, capped context, smaller model for easy documents and cached context, and a fifth card beside Sam reads cost per document minus 35%.",
  "caption": "Usage is more customers sending more documents (9,000 became 26,000 a month); construction is how the feature is built, the prompts, context, retries and model size the company’s own engineers choose; rates are the vendor’s price per token. The three are applied in that order, usage, then construction, then rates, because the effects multiply and the order decides how much each is credited with. Computed from April’s cost per document, usage added €2,644 to the August bill, construction €3,236, and a 20% June price cut took €1,456 off, offsetting about 45% of the construction rise.\n\nAlex’s construction work is estimated to cut the model cost per document by about 35% at unchanged vendor prices and unchanged quality, in two engineer-weeks (one person’s full working week of effort each), tested on the release-gate samples, the document sets whose results were required before general release. Part of the saving is fewer tokens, from the shorter prompt and the capped context; part is cheaper tokens, from a smaller model for easy documents and from cached context (material that repeats between requests, kept so it is not processed again and billed at a reduced rate). A cheaper model can cut the bill with the token count unchanged, which is why the measure is cost, not tokens. The work is done before the vendor commitment is sized, so the same saving is not counted twice.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "8bc3cd4ea1a7f8206838274890e46b000ea76ef551d132f9f0cead5b1c6fd7d8"
  }
}
-->

![Comic page in three strips: a whiteboard splits the rise in model charges from €1,400 to €5,824 into usage plus €2,644, construction plus €3,236 and rates minus €1,456; Priya holds a card reading vendor price cut 20%; four cards list shorter prompt, capped context, smaller model for easy documents and cached context, and a fifth card beside Sam reads cost per document minus 35%.](assets/images/30-ai-worth-its-cost/comic-page-03-why-the-bill-changed.jpeg)

**Page 3: Why the bill changed.** Usage is more customers sending more documents (9,000 became 26,000 a month); construction is how the feature is built, the prompts, context, retries and model size the company’s own engineers choose; rates are the vendor’s price per token. The three are applied in that order, usage, then construction, then rates, because the effects multiply and the order decides how much each is credited with. Computed from April’s cost per document, usage added €2,644 to the August bill, construction €3,236, and a 20% June price cut took €1,456 off, offsetting about 45% of the construction rise.

Alex’s construction work is estimated to cut the model cost per document by about 35% at unchanged vendor prices and unchanged quality, in two engineer-weeks (one person’s full working week of effort each), tested on the release-gate samples, the document sets whose results were required before general release. Part of the saving is fewer tokens, from the shorter prompt and the capped context; part is cheaper tokens, from a smaller model for easy documents and from cached context (material that repeats between requests, kept so it is not processed again and billed at a reduced rate). A cheaper model can cut the bill with the token count unchanged, which is why the measure is cost, not tokens. The work is done before the vendor commitment is sized, so the same saving is not counted twice.

- *Strip 1.* *Narration:* Model charges, April to August. **Alex:** “Three causes, applied in this order. Each has a different owner.” **Sam:** “Customers, product and engineering, the vendor. Different remedies too.”
- *Strip 2.* **Sam:** “The June price cut went to the board as good news.” **Priya:** “It offset under half the construction rise. Without it: about €7,300.”
- *Strip 3.* **Alex:** “Two engineer-weeks, tested on the release-gate samples, quality unchanged.” **Sam:** “Do it before we commit, or we pay for tokens we'll stop using.”

<!-- comic-page
{
  "id": "04-a-return-with-a-period",
  "title": "A return with a period",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-04-a-return-with-a-period.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Sam",
    "Morgan",
    "Ines"
  ],
  "strips": [
    {
      "scene": "A whiteboard with one heading line and, under it, exactly three lines of large, neat handwriting, each line fully visible. Sam, at the left of the whiteboard, gestures toward it with an open hand. Morgan, at the right of the whiteboard, reads down the lines. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "Return on investment: money left after costs, over costs, for a period.",
      "labels": [
        "APRIL TO SEPTEMBER 2027, PROJECTED",
        "REVENUE €57,000",
        "SUPPLIER RUNNING COST ABOUT €30,100",
        "€26,900 BEFORE STAFF COSTS: 90%"
      ],
      "label_notes": "APRIL TO SEPTEMBER 2027, PROJECTED is the heading; the other three are the lines under it, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Contribution: about 90% on supplier running cost, before staff costs. September estimated, quality held."
        },
        {
          "who": "Morgan",
          "text": "That is the feature as it runs. Has it paid for itself?"
        }
      ]
    },
    {
      "scene": "A second whiteboard with exactly four lines of large, neat handwriting, each line fully visible. Sam, at the left of the whiteboard, points at the third line from the side. Morgan, at the right of the whiteboard, nods. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "One-off trial and release costs, still unrecovered.",
      "labels": [
        "TRIAL: €45,000 + SIX ENGINEER-WEEKS",
        "RELEASE: TEN ENGINEER-WEEKS",
        "SHORT BEFORE STAFF TIME: €18,000",
        "SHORT WITH STAFF TIME: €79,000"
      ],
      "label_notes": "The four labels are the four lines on the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Not yet. About four more months at August's contribution recover that €18,000."
        },
        {
          "who": "Morgan",
          "text": "Staff time never, at August's figures. The board should hear both."
        }
      ]
    },
    {
      "scene": "A wall calendar strip hangs high on the wall, above everyone's heads, showing exactly two equal blocks side by side, each with a heading and one line under it. Ines, at the left, points up at the first block. Sam, at the right, points up at the second block. Nothing covers the lettering.",
      "labels": [
        "2027: HIRE MOVED TO OCTOBER",
        "€32,000 LESS €8,000: €24,000",
        "2028: LICENCES + UPKEEP, €8,600",
        "DEFERS NOTHING BY ITSELF"
      ],
      "label_notes": "2027: HIRE MOVED TO OCTOBER is the heading of the first block and €32,000 LESS €8,000: €24,000 its line; 2028: LICENCES + UPKEEP, €8,600 is the heading of the second block and DEFERS NOTHING BY ITSELF its line.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "Deferred hire, April to October: 300% on licences and upkeep, 220% with rollout time."
        },
        {
          "who": "Sam",
          "text": "A benefit of that year, projected until it closes. 2028 needs a new change."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: a whiteboard gives projected April to September 2027 revenue of €57,000, supplier running cost of about €30,100 and contribution of about €26,900, a 90% return before staff costs; a second whiteboard lists the €45,000 and six-engineer-week trial and the ten-engineer-week release, with the feature still €18,000 short before staff time and €79,000 short with staff time; a calendar contrasts 2027, the hire moved to October and €32,000 less €8,000 giving €24,000, with 2028, seven licences plus upkeep costing €8,600 a year and deferring nothing by themselves; Ines says 300% on licences and upkeep, 220% with rollout time.",
  "caption": "Return on investment is the money an investment leaves after its costs, divided by those costs, for a stated period. For April to September 2027, with September estimated at August’s level, the sorting feature earned €57,000 and cost about €30,100 in supplier running cost, leaving about €26,900 of contribution before payroll, roughly 90%, a projection until September closes, on the condition that accuracy stayed at or above 95%, no safety document was missed and review effort stayed below 1.5 hours a week per customer. Supplier bills count in the month of the work, so September’s bill, paid in October, is inside the figure: it is a contribution, not money in the bank.\n\nThat 90% is a return before staff costs: it counts only what is paid to suppliers, not the engineering and support time the feature consumes. Charging that time at salary cost, €27,700 over the same six months, leaves the period about €800 short (€26,902 less €27,700), before the one-off costs. Read without that qualification, 90% would pass for operating profitability.\n\nThe trial cost €45,000 and six engineer-weeks (one person’s full working week of effort each) and the release build ten more; with the operating months’ engineering and support time added, the feature is still about €18,000 short before staff time and about €79,000 short if staff time is charged at salary cost. August’s contribution of €4,576 a month, on the same basis, recovers the €18,000 in about four months.\n\nInes is the chief executive, who leads the company. The support assistant’s 2027 return is projected, not earned yet. A seventh support agent (a person answering tickets, customers’ recorded requests for help) was planned for April at an employment cost of €64,000 a year, salary plus employer charges; the start moved to October, so six months of that cost, €32,000, is not paid in 2027. Less €8,000 of licences (paid permission to use the software) and upkeep, that leaves about €24,000, or 300% of those recurring payments, provided the hire stays deferred, quality holds, tickets stay under about 1,400 a month and no paid cover is bought meanwhile.\n\nThe 300% leaves out one cost: about €2,000 of existing staff time spent rolling the assistant out and training the agents in 2027. Counted too, the costs are €10,000, €22,000 remains, and the return is 220%. The seventh agent works without the assistant during induction in 2027; in 2028 seven licences, €4,200, plus €4,400 of upkeep bring the tool to about €8,600 a year, and it defers nothing unless the company makes another change.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "46ce3b523d757857dc461dc47094c5270f027854a8116fa728347ce4d8df1bbc"
  }
}
-->

![Comic page in three strips: a whiteboard gives projected April to September 2027 revenue of €57,000, supplier running cost of about €30,100 and contribution of about €26,900, a 90% return before staff costs; a second whiteboard lists the €45,000 and six-engineer-week trial and the ten-engineer-week release, with the feature still €18,000 short before staff time and €79,000 short with staff time; a calendar contrasts 2027, the hire moved to October and €32,000 less €8,000 giving €24,000, with 2028, seven licences plus upkeep costing €8,600 a year and deferring nothing by themselves; Ines says 300% on licences and upkeep, 220% with rollout time.](assets/images/30-ai-worth-its-cost/comic-page-04-a-return-with-a-period.jpeg)

**Page 4: A return with a period.** Return on investment is the money an investment leaves after its costs, divided by those costs, for a stated period. For April to September 2027, with September estimated at August’s level, the sorting feature earned €57,000 and cost about €30,100 in supplier running cost, leaving about €26,900 of contribution before payroll, roughly 90%, a projection until September closes, on the condition that accuracy stayed at or above 95%, no safety document was missed and review effort stayed below 1.5 hours a week per customer. Supplier bills count in the month of the work, so September’s bill, paid in October, is inside the figure: it is a contribution, not money in the bank.

That 90% is a return before staff costs: it counts only what is paid to suppliers, not the engineering and support time the feature consumes. Charging that time at salary cost, €27,700 over the same six months, leaves the period about €800 short (€26,902 less €27,700), before the one-off costs. Read without that qualification, 90% would pass for operating profitability.

The trial cost €45,000 and six engineer-weeks (one person’s full working week of effort each) and the release build ten more; with the operating months’ engineering and support time added, the feature is still about €18,000 short before staff time and about €79,000 short if staff time is charged at salary cost. August’s contribution of €4,576 a month, on the same basis, recovers the €18,000 in about four months.

Ines is the chief executive, who leads the company. The support assistant’s 2027 return is projected, not earned yet. A seventh support agent (a person answering tickets, customers’ recorded requests for help) was planned for April at an employment cost of €64,000 a year, salary plus employer charges; the start moved to October, so six months of that cost, €32,000, is not paid in 2027. Less €8,000 of licences (paid permission to use the software) and upkeep, that leaves about €24,000, or 300% of those recurring payments, provided the hire stays deferred, quality holds, tickets stay under about 1,400 a month and no paid cover is bought meanwhile.

The 300% leaves out one cost: about €2,000 of existing staff time spent rolling the assistant out and training the agents in 2027. Counted too, the costs are €10,000, €22,000 remains, and the return is 220%. The seventh agent works without the assistant during induction in 2027; in 2028 seven licences, €4,200, plus €4,400 of upkeep bring the tool to about €8,600 a year, and it defers nothing unless the company makes another change.

- *Strip 1.* *Narration:* Return on investment: money left after costs, over costs, for a period. **Sam:** “Contribution: about 90% on supplier running cost, before staff costs. September estimated, quality held.” **Morgan:** “That is the feature as it runs. Has it paid for itself?”
- *Strip 2.* *Narration:* One-off trial and release costs, still unrecovered. **Sam:** “Not yet. About four more months at August's contribution recover that €18,000.” **Morgan:** “Staff time never, at August's figures. The board should hear both.”
- *Strip 3.* **Ines:** “Deferred hire, April to October: 300% on licences and upkeep, 220% with rollout time.” **Sam:** “A benefit of that year, projected until it closes. 2028 needs a new change.”

<!-- comic-page
{
  "id": "05-size-the-commitment-to-the-range",
  "title": "Size the commitment to the range",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-05-size-the-commitment-to-the-range.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Priya",
    "Sam",
    "Ines",
    "Alex"
  ],
  "strips": [
    {
      "scene": "High on the wall, above everyone's heads, runs a horizontal scale with a bracket marking a range in its middle, a label above the bracket, and a single mark to the left of the bracket with its own label. Priya, at the left, points up at the bracket. Sam, at the right, points up at the mark to its left. Nothing covers the lettering.",
      "narration": "2028 model charges at list prices, after the construction work.",
      "labels": [
        "2028 RANGE: €3,300 TO €7,600",
        "STRESS CASE: €2,000"
      ],
      "label_notes": "2028 RANGE: €3,300 TO €7,600 is the label above the bracket; STRESS CASE: €2,000 is the label on the single mark to the left of the bracket.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "The board's forecast: 35 to 80 customers, 650 documents each. €5,200 expected."
        },
        {
          "who": "Sam",
          "text": "€2,000 is a stress case, a harsh test, not a forecast."
        }
      ]
    },
    {
      "scene": "A wall calendar strip hangs high on the wall, showing one long solid block with a heading and, after it, a dashed empty outline with its own label. Ines, at the left, points up at the solid block. Sam, at the right, looks up at the dashed outline. Nothing covers the lettering.",
      "labels": [
        "2028: CASH PROVISION APPROVED",
        "2029 ONWARD: NO USAGE FUNDED"
      ],
      "label_notes": "2028: CASH PROVISION APPROVED is the heading on the solid block; 2029 ONWARD: NO USAGE FUNDED is the label on the dashed outline.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "A year or less sits inside my standing permission to sign."
        },
        {
          "who": "Sam",
          "text": "Only 2028 usage is funded; its payments run into early 2029. Nothing longer."
        }
      ]
    },
    {
      "scene": "A whiteboard divided by one vertical line into two columns, each column with a heading line and exactly two short lines of large, neat handwriting under it, every line fully visible. Alex, at the left of the whiteboard, gestures toward the left column with an open hand. Sam, at the right of the whiteboard, points at the right column from the side. Everyone stands to the side of the board, clear of it; no head, hand, marker or speech bubble covers any of its lettering.",
      "narration": "Fixed monthly payment, 25% off the usage it covers, the rest at list.",
      "labels": [
        "C: €2,400 FLOOR",
        "SAVES €800 ACROSS RANGE",
        "€400 WORSE UNDER STRESS",
        "B: €3,900 FLOOR",
        "SAVES €1,300 EXPECTED",
        "€600 WORSE AT LOW END"
      ],
      "label_notes": "C: €2,400 FLOOR is the heading of the left column, with SAVES €800 ACROSS RANGE and €400 WORSE UNDER STRESS as its two lines; B: €3,900 FLOOR is the heading of the right column, with SAVES €1,300 EXPECTED and €600 WORSE AT LOW END as its two lines.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "C saves €800 at every point in the range, €400 more under stress."
        },
        {
          "who": "Sam",
          "text": "B saves €1,300 at expected demand but costs more when customers leave. Take C."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: a scale shows the 2028 range of €3,300 to €7,600 of monthly model charges with a €2,000 stress case beside it; a calendar shows a 2028 cash provision approved and no usage funded from 2029; a whiteboard compares Option C, a €2,400 floor that saves €800 across the range and is €400 worse under stress, with Option B, a €3,900 floor that saves €1,300 at expected demand and is €600 worse at the low end.",
  "caption": "The vendor offers a committed-spend agreement for 2028: a fixed monthly payment for twelve months, 25% less per token on the usage that payment covers, usage above it at list price, the vendor’s standard price; the fixed payment is owed whether the usage arrives or not. The 25% and the amounts are assumptions for the example.\n\nDemand is what the feature’s usage would cost at list prices after the construction work: the board’s forecast of 35 to 80 customers at 650 documents each, at about 14.6 cents a document, gives about €3,300 to €7,600 a month, €5,200 expected, with €2,000 as a stress case, a deliberately harsh test rather than a forecast.\n\nInes has standing permission, continuing authority from the board, to sign contracts of a year or less, and the board has approved a 2028 cash provision, money set aside in the plan for these payments. No usage beyond December 2028 is funded, so nothing longer is on the table. Usage above the allowance is invoiced on the first day of the next month and due 45 days later, so November’s is due by 15 January 2029 and December’s by 15 February 2029. The provision reserves those payments up to 15 February; that is money for 2028 work, not a further year of usage.\n\nOption B commits €3,900 to cover €5,200 of usage; Option C commits €2,400 to cover €3,200. C saves €800 a month everywhere in the range and costs €400 more in the stress case; B saves €1,300 at expected demand and above but costs €600 more at the low end and €1,900 more under stress, with its floor exactly where the feature is losing customers. Larkspur chooses C, sized at the low end of a range the board has funded.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "ad2a1231979586dc8bf9f1d9d161639106fb65c1d3aa4e697a49b5fce07158a0"
  }
}
-->

![Comic page in three strips: a scale shows the 2028 range of €3,300 to €7,600 of monthly model charges with a €2,000 stress case beside it; a calendar shows a 2028 cash provision approved and no usage funded from 2029; a whiteboard compares Option C, a €2,400 floor that saves €800 across the range and is €400 worse under stress, with Option B, a €3,900 floor that saves €1,300 at expected demand and is €600 worse at the low end.](assets/images/30-ai-worth-its-cost/comic-page-05-size-the-commitment-to-the-range.jpeg)

**Page 5: Size the commitment to the range.** The vendor offers a committed-spend agreement for 2028: a fixed monthly payment for twelve months, 25% less per token on the usage that payment covers, usage above it at list price, the vendor’s standard price; the fixed payment is owed whether the usage arrives or not. The 25% and the amounts are assumptions for the example.

Demand is what the feature’s usage would cost at list prices after the construction work: the board’s forecast of 35 to 80 customers at 650 documents each, at about 14.6 cents a document, gives about €3,300 to €7,600 a month, €5,200 expected, with €2,000 as a stress case, a deliberately harsh test rather than a forecast.

Ines has standing permission, continuing authority from the board, to sign contracts of a year or less, and the board has approved a 2028 cash provision, money set aside in the plan for these payments. No usage beyond December 2028 is funded, so nothing longer is on the table. Usage above the allowance is invoiced on the first day of the next month and due 45 days later, so November’s is due by 15 January 2029 and December’s by 15 February 2029. The provision reserves those payments up to 15 February; that is money for 2028 work, not a further year of usage.

Option B commits €3,900 to cover €5,200 of usage; Option C commits €2,400 to cover €3,200. C saves €800 a month everywhere in the range and costs €400 more in the stress case; B saves €1,300 at expected demand and above but costs €600 more at the low end and €1,900 more under stress, with its floor exactly where the feature is losing customers. Larkspur chooses C, sized at the low end of a range the board has funded.

- *Strip 1.* *Narration:* 2028 model charges at list prices, after the construction work. **Priya:** “The board's forecast: 35 to 80 customers, 650 documents each. €5,200 expected.” **Sam:** “€2,000 is a stress case, a harsh test, not a forecast.”
- *Strip 2.* **Ines:** “A year or less sits inside my standing permission to sign.” **Sam:** “Only 2028 usage is funded; its payments run into early 2029. Nothing longer.”
- *Strip 3.* *Narration:* Fixed monthly payment, 25% off the usage it covers, the rest at list. **Alex:** “C saves €800 at every point in the range, €400 more under stress.” **Sam:** “B saves €1,300 at expected demand but costs more when customers leave. Take C.”

<!-- comic-page
{
  "id": "06-the-contract-and-the-stop-rules",
  "title": "The contract and the stop rules",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-06-the-contract-and-the-stop-rules.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Ines",
    "Sam",
    "Alex",
    "Priya"
  ],
  "strips": [
    {
      "scene": "Ines, at the left, sits at a desk holding up an unsigned contract so that its heading reads upright for the reader; it carries a heading and exactly two short lines above an empty signature line, and a capped pen lies on the desk beside her hand, not in it. Sam sits at the same desk, at the right, with a checklist on a clipboard that carries only plain tick boxes.",
      "labels": [
        "COMMITTED SPEND: 2028",
        "€2,400 MONTHLY, €28,800 IN ALL",
        "SIGNATURE: NOVEMBER 2027"
      ],
      "label_notes": "COMMITTED SPEND: 2028 is the heading of the contract; the other two are its two lines, top to bottom.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "Approved in September, on one condition. I sign in November, after October's measured bill."
        },
        {
          "who": "Sam",
          "text": "Owed whether we use it or not. No early exit, except one we negotiated."
        }
      ]
    },
    {
      "scene": "A pinboard with exactly three large index cards pinned side by side in one row with clear gaps between them, every word fully visible. Sam, at the left of the pinboard, gestures toward the cards with an open hand. Alex, at the right of the pinboard, points at the first card.",
      "labels": [
        "MODEL RETIREMENT: SIX MONTHS' NOTICE",
        "PRICE CHANGE: 30 DAYS' NOTICE",
        "DATA TERMS: CONFIRMED IN WRITING"
      ],
      "label_notes": "One label per index card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "A price rise means €2,400 buys fewer tokens; transfer needs the vendor's consent."
        },
        {
          "who": "Alex",
          "text": "Successor fails our samples? We give notice; fixed payments stop on the retirement date."
        }
      ]
    },
    {
      "scene": "A pinboard with exactly six large index cards pinned in two rows of three with clear gaps between them, every word fully visible. Priya, at the left of the pinboard, gestures toward the cards with an open hand. Ines, at the right of the pinboard, nods.",
      "labels": [
        "COST PER CUSTOMER OVER €150",
        "ACCURACY UNDER 95%",
        "ANY SAFETY DOCUMENT MISSED",
        "REVIEW 1.5 HOURS PER CUSTOMER-WEEK",
        "VENDOR PRICE UP 30%",
        "RENEWALS UNDER 80%"
      ],
      "label_notes": "One label per index card: the first three on the top row left to right, the last three on the bottom row left to right.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Rules decided now: reprice, review-aid mode or suspend, remeasure, sixty-day decision, reprice test."
        },
        {
          "who": "Ines",
          "text": "So the October meeting applies a rule instead of inventing one."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Ines holds an unsigned contract headed committed spend 2028, €2,400 monthly and €28,800 in all, signature November 2027, while Sam holds a checklist; three cards name the model-retirement clause with six months’ notice, the price-change clause with 30 days’ notice, and data terms confirmed in writing; six cards give the stop rules, cost per customer over €150, accuracy under 95%, any safety document missed, review 1.5 hours per customer-week, vendor price up 30% and renewals under 80%.",
  "caption": "The September review approves Option C on one condition: the construction saving must show on the release-gate samples and in October’s bill. Ines, who has standing permission to sign contracts of a year or less, signs in November once Sam has both. The obligation is then the operating company’s, the business that signed it: it runs from 1 January to 31 December 2028 with no automatic renewal, cannot be cancelled early even if the feature is withdrawn, and cannot be transferred without the vendor’s written consent. Sam checks the three clauses AI vendors add.\n\nThe vendor may retire the model with six months’ notice. Larkspur negotiated three rights: usable access to the successor with that notice or within thirty days of it; the right to test it on its release-gate samples (the document sets whose results were required before release); and the right to end the commitment on the retirement date, either because the samples fail or because usable access has not arrived sixty days before the retirement date. That is the one exception to non-cancellation.\n\nTwo deadlines matter. The testing window is the sixty days after access, in which the samples are run and a failure notified. The access deadline is sixty days before the retirement date: with no access by then, Larkspur gives its notice that day. For a notice on 1 February 2028 and retirement on 1 August, the access deadline is 2 June. Either way, the last fixed payment is July’s; nothing fixed is owed from August.\n\nWhat runs after the retirement date depends on the result. A successor that passes in time keeps the commitment running at its discounted price. Once the commitment has ended, everything is at flexible list prices, and ending it is a right, not a replacement model: sorting continues only on a model that has passed the samples; a model that ran the samples and failed can carry review-aid mode, a planner confirming each classification, for customers who confirm the planner time; if no model was measured, sorting is suspended and the service change agreed with each customer.\n\nList prices may change with thirty days’ notice: the fixed €2,400 does not change, but a higher price means it covers fewer tokens and more usage is charged at list, while a lower price means it covers more. The terms on how long customer documents are kept and whether they train the vendor’s models stay as in the trial, in writing.\n\nThe stop rules are set before the review so the October meeting applies one instead of inventing one. Running cost per customer above €150 for two months means construction first, then a reprice. Accuracy below 95% on the ordinary sample or any missed document in the separate safety sample means review-aid mode that day, if the customer confirms a planner has the time; otherwise sorting is suspended and the service change is agreed with the customer.\n\nReview effort at or above 1.5 hours a week for one customer means construction first, then remeasuring the time saved against that customer’s sorting by hand and agreeing a revised scope or price, or withdrawing the feature for them, since a higher fee alone would not give the customer back its time. A 30% price rise means a decision within sixty days of its notice, with the fixed payment still owed; a successor that fails the samples, or has no access by the access deadline, means a decision by the end of the testing window or on that deadline. Fewer than 80% renewing at €300 means a reprice test.\n\nA loss of up to €1,000 a month is tolerated until 31 March 2028 while customers with the feature renew the main product at least ten percentage points more often, for example 85% against 75%, in comparable groups of at least twenty. That is a provisional comparison, not proof that the feature causes renewals, and the rule expires regardless.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "87e994b7741f9f979306f1169e610fef9ba96a9c869e25ad3ac8170b6da0f7d6"
  }
}
-->

![Comic page in three strips: Ines holds an unsigned contract headed committed spend 2028, €2,400 monthly and €28,800 in all, signature November 2027, while Sam holds a checklist; three cards name the model-retirement clause with six months’ notice, the price-change clause with 30 days’ notice, and data terms confirmed in writing; six cards give the stop rules, cost per customer over €150, accuracy under 95%, any safety document missed, review 1.5 hours per customer-week, vendor price up 30% and renewals under 80%.](assets/images/30-ai-worth-its-cost/comic-page-06-the-contract-and-the-stop-rules.jpeg)

**Page 6: The contract and the stop rules.** The September review approves Option C on one condition: the construction saving must show on the release-gate samples and in October’s bill. Ines, who has standing permission to sign contracts of a year or less, signs in November once Sam has both. The obligation is then the operating company’s, the business that signed it: it runs from 1 January to 31 December 2028 with no automatic renewal, cannot be cancelled early even if the feature is withdrawn, and cannot be transferred without the vendor’s written consent. Sam checks the three clauses AI vendors add.

The vendor may retire the model with six months’ notice. Larkspur negotiated three rights: usable access to the successor with that notice or within thirty days of it; the right to test it on its release-gate samples (the document sets whose results were required before release); and the right to end the commitment on the retirement date, either because the samples fail or because usable access has not arrived sixty days before the retirement date. That is the one exception to non-cancellation.

Two deadlines matter. The testing window is the sixty days after access, in which the samples are run and a failure notified. The access deadline is sixty days before the retirement date: with no access by then, Larkspur gives its notice that day. For a notice on 1 February 2028 and retirement on 1 August, the access deadline is 2 June. Either way, the last fixed payment is July’s; nothing fixed is owed from August.

What runs after the retirement date depends on the result. A successor that passes in time keeps the commitment running at its discounted price. Once the commitment has ended, everything is at flexible list prices, and ending it is a right, not a replacement model: sorting continues only on a model that has passed the samples; a model that ran the samples and failed can carry review-aid mode, a planner confirming each classification, for customers who confirm the planner time; if no model was measured, sorting is suspended and the service change agreed with each customer.

List prices may change with thirty days’ notice: the fixed €2,400 does not change, but a higher price means it covers fewer tokens and more usage is charged at list, while a lower price means it covers more. The terms on how long customer documents are kept and whether they train the vendor’s models stay as in the trial, in writing.

The stop rules are set before the review so the October meeting applies one instead of inventing one. Running cost per customer above €150 for two months means construction first, then a reprice. Accuracy below 95% on the ordinary sample or any missed document in the separate safety sample means review-aid mode that day, if the customer confirms a planner has the time; otherwise sorting is suspended and the service change is agreed with the customer.

Review effort at or above 1.5 hours a week for one customer means construction first, then remeasuring the time saved against that customer’s sorting by hand and agreeing a revised scope or price, or withdrawing the feature for them, since a higher fee alone would not give the customer back its time. A 30% price rise means a decision within sixty days of its notice, with the fixed payment still owed; a successor that fails the samples, or has no access by the access deadline, means a decision by the end of the testing window or on that deadline. Fewer than 80% renewing at €300 means a reprice test.

A loss of up to €1,000 a month is tolerated until 31 March 2028 while customers with the feature renew the main product at least ten percentage points more often, for example 85% against 75%, in comparable groups of at least twenty. That is a provisional comparison, not proof that the feature causes renewals, and the rule expires regardless.

- *Strip 1.* **Ines:** “Approved in September, on one condition. I sign in November, after October's measured bill.” **Sam:** “Owed whether we use it or not. No early exit, except one we negotiated.”
- *Strip 2.* **Sam:** “A price rise means €2,400 buys fewer tokens; transfer needs the vendor's consent.” **Alex:** “Successor fails our samples? We give notice; fixed payments stop on the retirement date.”
- *Strip 3.* **Priya:** “Rules decided now: reprice, review-aid mode or suspend, remeasure, sixty-day decision, reprice test.” **Ines:** “So the October meeting applies a rule instead of inventing one.”

<!-- comic-page
{
  "id": "07-three-questions-three-answers",
  "title": "Three questions, three answers",
  "asset": "assets/images/30-ai-worth-its-cost/comic-page-07-three-questions-three-answers.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Morgan",
    "Sam",
    "Alex",
    "Ines"
  ],
  "strips": [
    {
      "scene": "Morgan, at the left, holds up one large card with both hands, facing the reader. Sam, at the right, holds up a smaller card with a single line, facing the reader.",
      "labels": [
        "WHAT IS OUR AI ROI?",
        "FEATURE 90%: APR–SEP 2027",
        "ASSISTANT 300%: 2027"
      ],
      "label_notes": "WHAT IS OUR AI ROI? is the large card Morgan holds; FEATURE 90%: APR–SEP 2027 and ASSISTANT 300%: 2027 are the two lines, top to bottom, of the card Sam holds.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "So: what is our AI ROI?"
        },
        {
          "who": "Sam",
          "text": "Projected, quality holding. Feature before staff costs; assistant before rollout time, hire deferred April–October."
        }
      ]
    },
    {
      "scene": "Morgan, at the left, holds up one large card with both hands, facing the reader. Alex, at the right, holds up a smaller card with a single line, facing the reader.",
      "labels": [
        "BILL OUTGROWS REVENUE. WHY?",
        "USAGE, CONSTRUCTION, RATES"
      ],
      "label_notes": "BILL OUTGROWS REVENUE. WHY? is the large card Morgan holds; USAGE, CONSTRUCTION, RATES is the card Alex holds.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Documents nearly tripled, construction added 80% per document, a price cut offset part."
        },
        {
          "who": "Morgan",
          "text": "The construction share is yours to fix, and measured before you commit."
        }
      ]
    },
    {
      "scene": "Morgan, at the left, holds up one large card with both hands, facing the reader. Ines, at the right, holds up a smaller card with a single line, facing the reader.",
      "labels": [
        "SHOULD WE COMMIT MORE?",
        "ONE YEAR, LOW END"
      ],
      "label_notes": "SHOULD WE COMMIT MORE? is the large card Morgan holds; ONE YEAR, LOW END is the card Ines holds.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "One year, sized at the low end: €800 a month saved across the range."
        },
        {
          "who": "Morgan",
          "text": "And the obligation travels with the company if ownership changes."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Morgan asks what is our AI ROI and Sam holds a card reading feature 90%, April to September 2027, and assistant 300%, 2027, saying both are projected with quality holding, the feature’s before staff costs and the assistant’s before rollout time with the hire deferred from April to October; Morgan asks why the bill outgrows revenue and Alex answers usage, construction, rates; Morgan asks should we commit more and Ines answers one year, at the low end.",
  "caption": "Each answer points at the method rather than at one number, and both return figures are projections at the September review.\n\nWhat is our AI ROI? The feature’s running return is about 90% on supplier running cost for April to September 2027, before staff costs, September estimated, with accuracy and review conditions holding. Charging staff time leaves the six months about €800 short, and the one-off trial and release costs are still about €18,000 short before staff time, about €79,000 with it. The support assistant’s 300% for 2027 is a return on its licences and upkeep, 220% once the €2,000 of rollout time is counted. It rests on a hire deferred from April to October, a benefit of that year only, confirmed when the year closes and only if the hire stays deferred and quality holds.\n\nWhy is the bill outgrowing revenue? Customers doubled and documents nearly tripled, construction raised the model cost per document by 80% at unchanged prices, and a 20% price cut offset under half of that.\n\nShould we commit more? The one-year commitment, sized at the low end of the funded range after the construction work, saves €800 a month across the range and costs €400 a month more in the stress case. A committed contract is an obligation of the operating company, the business that signed it, and travels with it if ownership changes.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "7e38f2c515d01be199354f0569a61e4dcbeb9fb5f9cfc52a250218daa0265463"
  }
}
-->

![Comic page in three strips: Morgan asks what is our AI ROI and Sam holds a card reading feature 90%, April to September 2027, and assistant 300%, 2027, saying both are projected with quality holding, the feature’s before staff costs and the assistant’s before rollout time with the hire deferred from April to October; Morgan asks why the bill outgrows revenue and Alex answers usage, construction, rates; Morgan asks should we commit more and Ines answers one year, at the low end.](assets/images/30-ai-worth-its-cost/comic-page-07-three-questions-three-answers.jpeg)

**Page 7: Three questions, three answers.** Each answer points at the method rather than at one number, and both return figures are projections at the September review.

What is our AI ROI? The feature’s running return is about 90% on supplier running cost for April to September 2027, before staff costs, September estimated, with accuracy and review conditions holding. Charging staff time leaves the six months about €800 short, and the one-off trial and release costs are still about €18,000 short before staff time, about €79,000 with it. The support assistant’s 300% for 2027 is a return on its licences and upkeep, 220% once the €2,000 of rollout time is counted. It rests on a hire deferred from April to October, a benefit of that year only, confirmed when the year closes and only if the hire stays deferred and quality holds.

Why is the bill outgrowing revenue? Customers doubled and documents nearly tripled, construction raised the model cost per document by 80% at unchanged prices, and a 20% price cut offset under half of that.

Should we commit more? The one-year commitment, sized at the low end of the funded range after the construction work, saves €800 a month across the range and costs €400 a month more in the stress case. A committed contract is an obligation of the operating company, the business that signed it, and travels with it if ownership changes.

- *Strip 1.* **Morgan:** “So: what is our AI ROI?” **Sam:** “Projected, quality holding. Feature before staff costs; assistant before rollout time, hire deferred April–October.”
- *Strip 2.* **Alex:** “Documents nearly tripled, construction added 80% per document, a price cut offset part.” **Morgan:** “The construction share is yours to fix, and measured before you commit.”
- *Strip 3.* **Ines:** “One year, sized at the low end: €800 a month saved across the range.” **Morgan:** “And the obligation travels with the company if ownership changes.”
