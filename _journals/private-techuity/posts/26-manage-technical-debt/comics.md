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

**Comic.** Larkspur is a fictional company that sells scheduling software, and an investor owns a large stake in it. Preparing the board's annual technology review, the investor's adviser asks two questions: how much technical debt does the company have, and would it not be simpler to rewrite the old parts? Seven pages show Larkspur answering with a register of five items, each with a carrying cost in three columns, what it costs to keep each month, what risk it carries and what it slows, and funding the first fix in tranches, separately approved stages of work, each released by a gate, an agreed check that the previous stage worked, with one dated item going first and one item deliberately carried.

The people: Morgan advises the investor, Alex leads technology, Priya leads product, Sam leads finance, and Ines is the chief executive, who can approve spending inside the limit the board has set. All are fictional, and every amount and date is invented for the example. On a phone the lettering is small: tap or click any page to open it at full size. Under each page, the caption ends with the words on its boards and cards, and the lines below repeat every speech bubble.

<!-- comic-page
{
  "id": "01-two-questions-one-wrong-answer",
  "title": "Two questions, and the wrong kind of answer",
  "asset": "assets/images/26-manage-technical-debt/comic-page-01-two-questions-one-wrong-answer.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Morgan",
    "Alex",
    "Priya"
  ],
  "strips": [
    {
      "scene": "Morgan, at the left, holds out one short note with two large lines of lettering, facing the reader. Alex, at the right, reads it. The note is the only prop in the strip.",
      "labels": [
        "HOW MUCH TECHNICAL DEBT?",
        "WHY NOT REWRITE?"
      ],
      "label_notes": "The two labels are the two lines of the note Morgan holds, one under the other.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "Two questions for the board's review: how much debt, and why not rewrite?"
        },
        {
          "who": "Alex",
          "text": "A count or a percentage would answer neither. Give me two weeks."
        }
      ]
    },
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps; the first two cards each have one single diagonal line struck through them and the third has a bold border. Alex, at the left, gestures up toward the third card with an open hand. Priya, at the right, nods. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "ISSUE COUNT",
        "PERCENT OF CODE",
        "CARRYING COST PER MONTH"
      ],
      "label_notes": "One label per card, in this left-to-right order; the first two are struck through, the third has the bold border.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Debt is the extra cost we carry each month because of how it's built."
        },
        {
          "who": "Priya",
          "text": "A carrying cost. The board already knows how to read one of those."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads divided into exactly three columns by two vertical lines; each column has a bold heading and one short line under it. Priya, at the left, and Alex, at the right, each gesture up at the board with an open hand. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "COST CARRIED",
        "RISK CARRIED",
        "SPEED LOST",
        "WORKAROUND HOURS, OLD HOSTING",
        "INCIDENTS, UNSUPPORTED, RETIRING",
        "LEAD TIME, DEALS LOST"
      ],
      "label_notes": "The first three labels are the three column headings, left to right; the last three are the single line under each heading, in the same order.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Three columns per item: what it costs, what it risks, what it slows."
        },
        {
          "who": "Priya",
          "text": "The third is the one a cost discussion leaves out. It's often the largest."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Morgan hands Alex a note asking how much technical debt and why not rewrite, and Alex says a count or a percentage answers neither; three cards read issue count and percent of code, both struck through, and carrying cost per month in bold, while Alex says debt is the extra cost carried each month because of how the software is built; a whiteboard shows three columns, cost carried with workaround hours and old hosting, risk carried with incidents, unsupported and retiring, and speed lost with lead time and deals lost.",
  "caption": "Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells scheduling software; an investor owns a large stake in it, and the board is the group of directors that oversees the company. Morgan advises the investor; Alex leads technology; Priya leads product.\n\nTechnical debt is the extra cost a company carries because its software was built, or has aged, in ways that make it slower, riskier or dearer to change than it needs to be; the word is a metaphor, not a loan. A carrying cost is what an item costs the company while it remains, in three columns: cost carried (euros per month), risk carried (service failures, unsupported parts, dated retirements) and speed lost (lead time, the working days from an agreed change to its delivery, and deals the product cannot take). The last two keep their own units and are read alongside the money, not added to it.\n\n*Words on the boards and cards.* Strip 1: “How much technical debt?”; “Why not rewrite?”. Strip 2: “Issue count”; “Percent of code”; “Carrying cost per month”. Strip 3: “Cost carried”; “Risk carried”; “Speed lost”; “Workaround hours, old hosting”; “Incidents, unsupported, retiring”; “Lead time, deals lost”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "cf1811eb116c10959040355d81fb856e8a0d14aeec2c15c78f9124f7897f8576"
  }
}
-->

![Comic page in three strips: Morgan hands Alex a note asking how much technical debt and why not rewrite, and Alex says a count or a percentage answers neither; three cards read issue count and percent of code, both struck through, and carrying cost per month in bold, while Alex says debt is the extra cost carried each month because of how the software is built; a whiteboard shows three columns, cost carried with workaround hours and old hosting, risk carried with incidents, unsupported and retiring, and speed lost with lead time and deals lost.](assets/images/26-manage-technical-debt/comic-page-01-two-questions-one-wrong-answer.jpeg)

**Page 1: Two questions, and the wrong kind of answer.** Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells scheduling software; an investor owns a large stake in it, and the board is the group of directors that oversees the company. Morgan advises the investor; Alex leads technology; Priya leads product.

Technical debt is the extra cost a company carries because its software was built, or has aged, in ways that make it slower, riskier or dearer to change than it needs to be; the word is a metaphor, not a loan. A carrying cost is what an item costs the company while it remains, in three columns: cost carried (euros per month), risk carried (service failures, unsupported parts, dated retirements) and speed lost (lead time, the working days from an agreed change to its delivery, and deals the product cannot take). The last two keep their own units and are read alongside the money, not added to it.

*Words on the boards and cards.* Strip 1: “How much technical debt?”; “Why not rewrite?”. Strip 2: “Issue count”; “Percent of code”; “Carrying cost per month”. Strip 3: “Cost carried”; “Risk carried”; “Speed lost”; “Workaround hours, old hosting”; “Incidents, unsupported, retiring”; “Lead time, deals lost”.

- *Strip 1.* **Morgan:** “Two questions for the board's review: how much debt, and why not rewrite?” **Alex:** “A count or a percentage would answer neither. Give me two weeks.”
- *Strip 2.* **Alex:** “Debt is the extra cost we carry each month because of how it's built.” **Priya:** “A carrying cost. The board already knows how to read one of those.”
- *Strip 3.* **Alex:** “Three columns per item: what it costs, what it risks, what it slows.” **Priya:** “The third is the one a cost discussion leaves out. It's often the largest.”

<!-- comic-page
{
  "id": "02-five-items-four-origins",
  "title": "Five items, and where each came from",
  "asset": "assets/images/26-manage-technical-debt/comic-page-02-five-items-four-origins.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Alex",
    "Priya",
    "Sam"
  ],
  "strips": [
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly five index cards pinned side by side in one row with clear gaps, each card carrying its numeral and a short line. Alex, at the left, gestures up at the row with an open hand. Priya, at the right, points up at the fifth card. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "1 INVOICING TANGLES",
        "2 REPORTING STACK, UNSUPPORTED",
        "3 SCHEDULING ENGINE, ONE SERVER",
        "4 AI PROMPT IN CODE",
        "5 VENDOR MODEL RETIRING"
      ],
      "label_notes": "One label per card, in this left-to-right order, the numeral first on each card.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Five items: the board's shortlist. The full register behind it is longer."
        },
        {
          "who": "Priya",
          "text": "The vendor model retires on 31 March 2028. That one has a date."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly four lines of lettering, one under the other, each pairing an origin with its remedy. Priya, at the left, and Alex, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "DATED SHORTCUT: REVISIT ON DATE",
        "GROWTH OUTRAN DESIGN: TRANCHES",
        "AGEING PLATFORM: BY THE DATE",
        "RETIRING VENDOR: BY THE DATE"
      ],
      "label_notes": "The four labels are the four lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Item 4 was a dated shortcut, owned by me. Accountable, not necessarily wise."
        },
        {
          "who": "Alex",
          "text": "Undated shortcuts are failures of record. Outside dates are weighed against harm now."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly four large lines of lettering, one under the other. Sam, at the left, and Alex, at the right, stand clear of the board; Sam gestures up at it with an open hand. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "ABOUT €10,000 A MONTH",
        "2 INVOICE INCIDENTS A QUARTER",
        "FAILOVER: 45 MINUTES",
        "€12,000 A MONTH NOT WON"
      ],
      "label_notes": "The four labels are the four lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Carried, the five cost about €10,000 a month: €5,500 cash, €4,600 of our time."
        },
        {
          "who": "Alex",
          "text": "And two prospects above 400 technicians we can't serve: revenue not won."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, and vendor model retiring, and Alex calls them the board's shortlist over a longer register; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, growth outran design tranches, ageing platform and retiring vendor by the date, while Priya calls her dated shortcut accountable but not necessarily wise and Alex says undated shortcuts are failures of record and outside dates are weighed against harm now; a second whiteboard totals the register at about €10,000 a month, two invoice incidents a quarter, a 45-minute failover and €12,000 a month not won.",
  "caption": "Larkspur's register has five items; they are the board's shortlist, and a longer register sits behind them. Item 1 is the invoicing module, the software that prepares customer bills, whose code is still tangled so that parts cannot change alone. Item 2 is the reporting stack on a version its vendor no longer fixes security holes in. Item 3 is the scheduling engine, which runs each region on one server. Item 4 is the artificial intelligence (AI) sorting feature: the prompt, the instructions sent to the AI model that sorts customers' documents, is written into the program, so every change to it needs a software release. Item 5 is the vendor retiring the AI model that feature runs on.\n\nThe origin of each decides who owns it and what the remedy usually is. A deliberate shortcut recorded with a date and an owner is not a failure of record, though the record makes it accountable, not necessarily wise; an undated one is a failure. A tranche is a separately approved stage of work, so growth that outran a design is fixed in tranches. A date set from outside the company, by a vendor or a prospect, is weighed first: what missing it would cost against the harm undated items are doing now, so a close date with little time to spare goes first, and a distant date with little work behind it can wait.\n\nCarried, the five cost about €10,000 a month: €5,500 of cash paid to hosting providers, the companies whose servers run the software, and about €4,600 of the company's own engineering time, already on the payroll and valued at what it costs to employ the engineers. The invoicing tangles cause two customer-visible incidents a quarter, and the scheduling engine caused the year's last two incidents and takes 45 minutes to fail over, that is, to move its work to a replacement server. Its single-server design also turns away prospects, potential customers, above about 400 technicians: two this year, about €12,000 a month of revenue (sales income) not won. Sam leads finance.\n\n*Words on the boards and cards.* Strip 1: “1 Invoicing tangles”; “2 Reporting stack, unsupported”; “3 Scheduling engine, one server”; “4 AI prompt in code”; “5 Vendor model retiring”. Strip 2: “Dated shortcut: revisit on date”; “Growth outran design: tranches”; “Ageing platform: by the date”; “Retiring vendor: by the date”. Strip 3: “About €10,000 a month”; “2 invoice incidents a quarter”; “Failover: 45 minutes”; “€12,000 a month not won”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "60cdf57b2af4b5e0b44f4d75b667d6cd4ebe78e63bf7df588656a4e36bf11e1b"
  }
}
-->

![Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, and vendor model retiring, and Alex calls them the board's shortlist over a longer register; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, growth outran design tranches, ageing platform and retiring vendor by the date, while Priya calls her dated shortcut accountable but not necessarily wise and Alex says undated shortcuts are failures of record and outside dates are weighed against harm now; a second whiteboard totals the register at about €10,000 a month, two invoice incidents a quarter, a 45-minute failover and €12,000 a month not won.](assets/images/26-manage-technical-debt/comic-page-02-five-items-four-origins.jpeg)

**Page 2: Five items, and where each came from.** Larkspur's register has five items; they are the board's shortlist, and a longer register sits behind them. Item 1 is the invoicing module, the software that prepares customer bills, whose code is still tangled so that parts cannot change alone. Item 2 is the reporting stack on a version its vendor no longer fixes security holes in. Item 3 is the scheduling engine, which runs each region on one server. Item 4 is the artificial intelligence (AI) sorting feature: the prompt, the instructions sent to the AI model that sorts customers' documents, is written into the program, so every change to it needs a software release. Item 5 is the vendor retiring the AI model that feature runs on.

The origin of each decides who owns it and what the remedy usually is. A deliberate shortcut recorded with a date and an owner is not a failure of record, though the record makes it accountable, not necessarily wise; an undated one is a failure. A tranche is a separately approved stage of work, so growth that outran a design is fixed in tranches. A date set from outside the company, by a vendor or a prospect, is weighed first: what missing it would cost against the harm undated items are doing now, so a close date with little time to spare goes first, and a distant date with little work behind it can wait.

Carried, the five cost about €10,000 a month: €5,500 of cash paid to hosting providers, the companies whose servers run the software, and about €4,600 of the company's own engineering time, already on the payroll and valued at what it costs to employ the engineers. The invoicing tangles cause two customer-visible incidents a quarter, and the scheduling engine caused the year's last two incidents and takes 45 minutes to fail over, that is, to move its work to a replacement server. Its single-server design also turns away prospects, potential customers, above about 400 technicians: two this year, about €12,000 a month of revenue (sales income) not won. Sam leads finance.

*Words on the boards and cards.* Strip 1: “1 Invoicing tangles”; “2 Reporting stack, unsupported”; “3 Scheduling engine, one server”; “4 AI prompt in code”; “5 Vendor model retiring”. Strip 2: “Dated shortcut: revisit on date”; “Growth outran design: tranches”; “Ageing platform: by the date”; “Retiring vendor: by the date”. Strip 3: “About €10,000 a month”; “2 invoice incidents a quarter”; “Failover: 45 minutes”; “€12,000 a month not won”.

- *Strip 1.* **Alex:** “Five items: the board's shortlist. The full register behind it is longer.” **Priya:** “The vendor model retires on 31 March 2028. That one has a date.”
- *Strip 2.* **Priya:** “Item 4 was a dated shortcut, owned by me. Accountable, not necessarily wise.” **Alex:** “Undated shortcuts are failures of record. Outside dates are weighed against harm now.”
- *Strip 3.* **Sam:** “Carried, the five cost about €10,000 a month: €5,500 cash, €4,600 of our time.” **Alex:** “And two prospects above 400 technicians we can't serve: revenue not won.”

<!-- comic-page
{
  "id": "03-present-the-fix-by-what-it-buys",
  "title": "Present the fix by what it buys",
  "asset": "assets/images/26-manage-technical-debt/comic-page-03-present-the-fix-by-what-it-buys.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Alex",
    "Ines",
    "Sam"
  ],
  "strips": [
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps. Alex, at the left, gestures up at the cards with an open hand. Ines, at the right, listens with her arms folded. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "REVENUE PROTECTED OR ENABLED",
        "COST OR RISK REMOVED",
        "A DECISION KEPT OPEN"
      ],
      "label_notes": "One label per card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "The board reads a fix like any investment: protects, removes, or keeps open."
        },
        {
          "who": "Ines",
          "text": "Kept open only for a named decision with a date, never a general virtue."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads drawn as a small table: two column headings across the top and three row labels down the left side, with the six cells under the headings empty. Sam, at the left, and Alex, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "BEFORE",
        "AFTER",
        "INCIDENTS PER QUARTER",
        "FAILOVER TIME",
        "LEAD TIME"
      ],
      "label_notes": "BEFORE and AFTER are the two column headings; the other three are the row labels, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Nobody gets credit for a failure that never happened. The effort is this quarter's."
        },
        {
          "who": "Alex",
          "text": "So we measure before and after. That's a claim the board can check."
        }
      ]
    },
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly four index cards pinned side by side in one row with clear gaps. Alex, at the left, gestures up at the cards with an open hand. Ines, at the right, points up at the fourth card. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "2 PROSPECTS: €12,000 A MONTH",
        "€4,000 HOSTING ABOVE NEED",
        "45-MINUTE FAILOVER",
        "CORE REPLACEMENT: KEPT OPEN"
      ],
      "label_notes": "One label per card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "For the engine: two prospects, oversized servers, a 45-minute failover: a month's downtime allowance."
        },
        {
          "who": "Ines",
          "text": "Nothing here prices exactly. So judge the fix by the columns it moves."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: three cards read revenue protected or enabled, cost or risk removed, and a decision kept open; a before-and-after table lists incidents per quarter, failover time and lead time with empty cells, while Sam says nobody gets credit for a failure that never happened; four cards for the scheduling engine read two prospects €12,000 a month, €4,000 hosting above need, 45-minute failover, and core replacement kept open, and Alex calls the 45-minute failover a month's downtime allowance.",
  "caption": "A reduction project is presented the way the board reads any investment: the revenue it protects or enables (sales the product could make or keep), the cost or risk it removes and, only where a real dated decision is being kept open, the decision it preserves. None of the three can be priced exactly, so the work is judged on the register columns it moves, measured before and after.\n\nThe board rarely sees the failures a fix prevented, because a prevented failure is invisible while the effort sits on this quarter's budget; the after column is the answer.\n\nFor the engine, a failover, moving its work to a replacement server, takes 45 minutes; Larkspur promises its service is usable 99.9% of the month, which allows about 43 minutes of downtime, so one real failover would use the whole month's allowance. The two-second promise for confirming an appointment is a separate measure, response time, which this work does not change. Ines is the chief executive.\n\n*Words on the boards and cards.* Strip 1: “Revenue protected or enabled”; “Cost or risk removed”; “A decision kept open”. Strip 2: “Before”; “After”; “Incidents per quarter”; “Failover time”; “Lead time”. Strip 3: “2 prospects: €12,000 a month”; “€4,000 hosting above need”; “45-minute failover”; “Core replacement: kept open”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "e2e7ff80ef4d6379e3f6b74b1f465f611ef07d83ed7cda05b7b95f2a5a5d5dc5"
  }
}
-->

![Comic page in three strips: three cards read revenue protected or enabled, cost or risk removed, and a decision kept open; a before-and-after table lists incidents per quarter, failover time and lead time with empty cells, while Sam says nobody gets credit for a failure that never happened; four cards for the scheduling engine read two prospects €12,000 a month, €4,000 hosting above need, 45-minute failover, and core replacement kept open, and Alex calls the 45-minute failover a month's downtime allowance.](assets/images/26-manage-technical-debt/comic-page-03-present-the-fix-by-what-it-buys.jpeg)

**Page 3: Present the fix by what it buys.** A reduction project is presented the way the board reads any investment: the revenue it protects or enables (sales the product could make or keep), the cost or risk it removes and, only where a real dated decision is being kept open, the decision it preserves. None of the three can be priced exactly, so the work is judged on the register columns it moves, measured before and after.

The board rarely sees the failures a fix prevented, because a prevented failure is invisible while the effort sits on this quarter's budget; the after column is the answer.

For the engine, a failover, moving its work to a replacement server, takes 45 minutes; Larkspur promises its service is usable 99.9% of the month, which allows about 43 minutes of downtime, so one real failover would use the whole month's allowance. The two-second promise for confirming an appointment is a separate measure, response time, which this work does not change. Ines is the chief executive.

*Words on the boards and cards.* Strip 1: “Revenue protected or enabled”; “Cost or risk removed”; “A decision kept open”. Strip 2: “Before”; “After”; “Incidents per quarter”; “Failover time”; “Lead time”. Strip 3: “2 prospects: €12,000 a month”; “€4,000 hosting above need”; “45-minute failover”; “Core replacement: kept open”.

- *Strip 1.* **Alex:** “The board reads a fix like any investment: protects, removes, or keeps open.” **Ines:** “Kept open only for a named decision with a date, never a general virtue.”
- *Strip 2.* **Sam:** “Nobody gets credit for a failure that never happened. The effort is this quarter's.” **Alex:** “So we measure before and after. That's a claim the board can check.”
- *Strip 3.* **Alex:** “For the engine: two prospects, oversized servers, a 45-minute failover: a month's downtime allowance.” **Ines:** “Nothing here prices exactly. So judge the fix by the columns it moves.”

<!-- comic-page
{
  "id": "04-rewrite-tranches-or-live-with-it",
  "title": "Rewrite, tranches, or live with it",
  "asset": "assets/images/26-manage-technical-debt/comic-page-04-rewrite-tranches-or-live-with-it.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Alex",
    "Priya",
    "Sam"
  ],
  "strips": [
    {
      "scene": "On a table stand exactly three upright cards side by side with clear gaps, each with a heading and lines of lettering facing the reader; the first card has three lines, the second three lines, the third two lines. Alex, at the left of the table, and Priya, at the right of the table, each gesture toward the cards with an open hand held well above them; no hand, arm or bubble covers any card.",
      "labels": [
        "A: REWRITE THE ENGINE",
        "€300,000 TIME, €40,000 CASH",
        "BENEFIT AT MONTH 9",
        "B: TRANCHES WITH GATES",
        "TRANCHE 1: €50,000 TIME",
        "€8,000 CASH, BENEFIT MONTH 3",
        "C: LIVE WITH IT",
        "COST CONTINUES"
      ],
      "label_notes": "The first three labels are the three lines of card A, top to bottom; the next three are card B; the last two are card C.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Three ways to reduce item 3, on one basis: staff time, cash, benefit date."
        },
        {
          "who": "Priya",
          "text": "A rewrite buys nothing before month nine. Tranche 1 buys failover at three."
        }
      ]
    },
    {
      "scene": "A long horizontal timeline high on the wall, above everyone's heads, with exactly four tick marks in total, one tick directly under each of the four labels and no other tick anywhere. Above the line lies one long plain bar reaching exactly from the first tick to the fourth, with one small flag standing at its right end directly above the fourth tick. Below the line lie two shorter plain bars on one scale: the first runs exactly from the first tick to the second tick and ends in a small flag directly under the second tick, with a small closed barrier gate right beside that flag; the second starts at the second tick and ends exactly under the third tick, with a small flag standing directly under the third tick; no bar extends past its tick. Sam, at the left, and Alex, at the right, stand below the timeline and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "MONTH 0",
        "MONTH 3",
        "MONTH 7",
        "MONTH 9",
        "REWRITE",
        "TRANCHE 1: €58,000",
        "GATE",
        "TRANCHE 2: €80,000"
      ],
      "label_notes": "The four MONTH labels sit over the four ticks, left to right; REWRITE is lettered on the long upper bar; TRANCHE 1: €58,000 on the first lower bar, GATE beside the barrier at month 3, TRANCHE 2: €80,000 on the second lower bar, which ends at the MONTH 7 tick.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Rewrite: the old engine frozen nine months, then every risk arrives at the switch-over."
        },
        {
          "who": "Alex",
          "text": "Tranches: failover at month three, large customers at month seven, each measured first."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly four lines of lettering, one under the other, the first two lines about the rewrite and the last two about tranche 1. Sam, at the left, and Priya, at the right, stand clear of the board; Priya gestures up at the last two lines with an open hand. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "REWRITE, MONTH 5:",
        "€180,000 GONE, €160,000 TO DECIDE",
        "TRANCHE 1 DONE:",
        "€58,000 SPENT, FAILOVER IN HAND"
      ],
      "label_notes": "The four labels are the four lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Month five of a rewrite: €180,000 gone either way; only the €160,000 left counts."
        },
        {
          "who": "Priya",
          "text": "After tranche 1, €58,000 is spent and the benefit is already in hand."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: three cards compare A, rewrite the engine, €300,000 of staff time and €40,000 of cash with the benefit at month nine, B, tranches with gates, tranche 1 at €50,000 of time plus €8,000 of cash with failover at month three, and C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar ending in a single flag at month 9, against a tranche 1 bar labelled €58,000 ending in a flag at month 3 with a gate beside it, and a tranche 2 bar labelled €80,000 running from month 3 to a flag at month 7; a whiteboard reads rewrite month 5, €180,000 gone and €160,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.",
  "caption": "For the scheduling engine, a rewrite (replacing the system with a new one) takes nine months with the old engine frozen, still running but no longer changed, and every risk arriving at one switch-over; it costs about €300,000 of the company's own engineering time plus €40,000 of additional cash, about €340,000 in all.\n\nA tranche is a separately approved stage of the work; a gate is the check, agreed in advance, that must pass before the next tranche is funded. Tranche 1 splits the schedule computation so it can fail over: about €50,000 of time plus €8,000 of cash, benefit at month three. Tranche 2 gives the largest customers their own servers: about €70,000 of time plus €10,000 of cash, benefit at month seven, about €138,000 for both stages together; replacing the core stays a later decision. Living with it keeps the carrying cost.\n\nMoney already spent is gone the moment it is spent, whether or not any benefit has arrived, so it should not tip the next decision: five months into the rewrite about €180,000 is gone and nothing has been bought yet, and only the remaining €160,000 and the benefit still to come should decide whether to continue. After tranche 1 the remaining decision is only about tranche 2.\n\n*Words on the boards and cards.* Strip 1: “A: Rewrite the engine”; “€300,000 time, €40,000 cash”; “Benefit at month 9”; “B: Tranches with gates”; “Tranche 1: €50,000 time”; “€8,000 cash, benefit month 3”; “C: Live with it”; “Cost continues”. Strip 2: “Month 0”; “Month 3”; “Month 7”; “Month 9”; “Rewrite”; “Tranche 1: €58,000”; “Gate”; “Tranche 2: €80,000”. Strip 3: “Rewrite, month 5:”; “€180,000 gone, €160,000 to decide”; “Tranche 1 done:”; “€58,000 spent, failover in hand”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "51d4a1435b199eb45eecfedf22fec5d1686622fe0bcaf48dc98098aaabdff6d2"
  }
}
-->

![Comic page in three strips: three cards compare A, rewrite the engine, €300,000 of staff time and €40,000 of cash with the benefit at month nine, B, tranches with gates, tranche 1 at €50,000 of time plus €8,000 of cash with failover at month three, and C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar ending in a single flag at month 9, against a tranche 1 bar labelled €58,000 ending in a flag at month 3 with a gate beside it, and a tranche 2 bar labelled €80,000 running from month 3 to a flag at month 7; a whiteboard reads rewrite month 5, €180,000 gone and €160,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.](assets/images/26-manage-technical-debt/comic-page-04-rewrite-tranches-or-live-with-it.jpeg)

**Page 4: Rewrite, tranches, or live with it.** For the scheduling engine, a rewrite (replacing the system with a new one) takes nine months with the old engine frozen, still running but no longer changed, and every risk arriving at one switch-over; it costs about €300,000 of the company's own engineering time plus €40,000 of additional cash, about €340,000 in all.

A tranche is a separately approved stage of the work; a gate is the check, agreed in advance, that must pass before the next tranche is funded. Tranche 1 splits the schedule computation so it can fail over: about €50,000 of time plus €8,000 of cash, benefit at month three. Tranche 2 gives the largest customers their own servers: about €70,000 of time plus €10,000 of cash, benefit at month seven, about €138,000 for both stages together; replacing the core stays a later decision. Living with it keeps the carrying cost.

Money already spent is gone the moment it is spent, whether or not any benefit has arrived, so it should not tip the next decision: five months into the rewrite about €180,000 is gone and nothing has been bought yet, and only the remaining €160,000 and the benefit still to come should decide whether to continue. After tranche 1 the remaining decision is only about tranche 2.

*Words on the boards and cards.* Strip 1: “A: Rewrite the engine”; “€300,000 time, €40,000 cash”; “Benefit at month 9”; “B: Tranches with gates”; “Tranche 1: €50,000 time”; “€8,000 cash, benefit month 3”; “C: Live with it”; “Cost continues”. Strip 2: “Month 0”; “Month 3”; “Month 7”; “Month 9”; “Rewrite”; “Tranche 1: €58,000”; “Gate”; “Tranche 2: €80,000”. Strip 3: “Rewrite, month 5:”; “€180,000 gone, €160,000 to decide”; “Tranche 1 done:”; “€58,000 spent, failover in hand”.

- *Strip 1.* **Alex:** “Three ways to reduce item 3, on one basis: staff time, cash, benefit date.” **Priya:** “A rewrite buys nothing before month nine. Tranche 1 buys failover at three.”
- *Strip 2.* **Sam:** “Rewrite: the old engine frozen nine months, then every risk arrives at the switch-over.” **Alex:** “Tranches: failover at month three, large customers at month seven, each measured first.”
- *Strip 3.* **Sam:** “Month five of a rewrite: €180,000 gone either way; only the €160,000 left counts.” **Priya:** “After tranche 1, €58,000 is spent and the benefit is already in hand.”

<!-- comic-page
{
  "id": "05-the-dated-item-goes-first",
  "title": "A close date, weighed and put first",
  "asset": "assets/images/26-manage-technical-debt/comic-page-05-the-dated-item-goes-first.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Alex",
    "Priya",
    "Ines"
  ],
  "strips": [
    {
      "scene": "A long horizontal timeline high on the wall, above everyone's heads with exactly three labelled ticks, one tick directly under each label and no tick anywhere without a label over it. Priya, at the left, and Alex, at the right, stand below the timeline; Priya points up at the middle label. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "PATCHES ENDED 31 MAR 2027",
        "SECURITY REVIEW: BY MARCH 2028",
        "MODEL RETIRES 31 MAR 2028"
      ],
      "label_notes": "The three labels sit over the three ticks, left to right.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Our largest prospect's security review needs supported components by the end of March 2028."
        },
        {
          "who": "Alex",
          "text": "The reporting stack lost support in March, and it has no half-way state."
        }
      ]
    },
    {
      "scene": "On a table stands one upright card with a heading and two lines of lettering facing the reader; it is the only prop on the table. Alex, at the left of the table, gestures at the card with an open hand. Ines, at the right of the table, nods. Nothing covers the lettering.",
      "labels": [
        "REPORTING STACK MIGRATION",
        "6 ENGINEER-WEEKS, €5,000 CASH",
        "NOVEMBER–DECEMBER 2027"
      ],
      "label_notes": "The three labels are the heading and two lines of the card, top to bottom.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Small rewrite, benefit at the end: right only when no half-way step exists."
        },
        {
          "who": "Ines",
          "text": "It goes before item 3: the date is close and the work is small."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly three lines of lettering, one under the other. Priya, at the left, and Ines, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "DEADLINE RISK VS HARM NOW",
        "REST: MOST REMOVED PER EFFORT",
        "SUCCESSOR SAMPLES BY 29 OCTOBER"
      ],
      "label_notes": "The three labels are the three lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Same rule, longer fuse: Alex runs the samples on the successor by 29 October."
        },
        {
          "who": "Ines",
          "text": "Fail, and I sign nothing. We choose by 29 November, switch in February."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: a timeline marks patches ended 31 March 2027, security review by March 2028, and model retires 31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says it goes before item 3 because the date is close and the work is small; a whiteboard gives the sequencing rule, deadline risk versus harm now, the rest by most removed per effort, successor samples by 29 October, and Ines says that if they fail she signs nothing, a replacement is chosen by 29 November and the switch comes in February.",
  "caption": "A migration moves software from one platform or vendor to another. The reporting stack, the software that produces customer reports, sits on a framework version, the reusable software it is built on, whose vendor stopped fixing its security holes in March 2027, and the largest prospect's security review requires supported components by the end of March 2028. The supported version builds reports differently, so there is no useful half-way state: its migration is a small rewrite with the benefit at the end, the one shape in which that is right. It goes first, ahead of the scheduling engine whose carrying cost is larger, because its date is close and its work is small: six engineer-weeks, six weeks of one engineer's time or three weeks each for two, and €5,000 of cash.\n\nThe rule has two parts. An item whose outside date leaves little more time than the work needs, with a margin for overrun, is weighed first: what missing the date would cost against the harm undated items are doing now; items brought forward go in date order, and a distant date with little work behind it can wait behind an undated item doing harm now. The rest are ordered by the cost, risk and delay each stage of effort would remove, across all three columns.\n\nThe vendor's notice of 30 September 2027 retires the artificial intelligence (AI) model that sorts customers' documents on 31 March 2028, names its successor and gives Larkspur usable access to it the same day. It arrives before Larkspur has signed its planned commitment, an agreement to make fixed monthly payments to the vendor through 2028 in return for a discount, which Ines is due to sign in November. So the test comes first. Alex runs the successor on the release-gate samples, the documents the feature had to sort correctly before release, by 29 October, and Ines signs only if it passes. If it fails, nothing is signed and no fixed payment is owed, and Larkspur chooses by 29 November between another vendor's model tested on the same samples and the failed successor. Had access come later, every date would move with it, and the choice would still be made by 31 January 2028.\n\nThe old model stays available until 31 March, but the switch is planned for February, leaving March to put right anything that goes wrong; what customers get changes on that switch day. A model that passed the samples keeps sorting automatically. A model that was tested and failed can carry the review mode from the trial: the feature proposes a category and each customer's own planner confirms it, with no new Larkspur staff. The mode still needs a model, and it starts only where Priya has confirmed that the planner has the time and has agreed the changed service and fee; other customers' sorting is suspended from the switch day.\n\nIf no model was tested at all, there is nothing to switch to: sorting is suspended for every customer on 31 March, with the changed service agreed beforehand, and documents go back to sorting by hand. Sam prices the chosen model's usage against the AI budget the board approved; anything beyond it needs the board.\n\n*Words on the boards and cards.* Strip 1: “Patches ended 31 Mar 2027”; “Security review: by March 2028”; “Model retires 31 Mar 2028”. Strip 2: “Reporting stack migration”; “6 engineer-weeks, €5,000 cash”; “November–December 2027”. Strip 3: “Deadline risk vs harm now”; “Rest: most removed per effort”; “Successor samples by 29 October”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "eb437f75111025630b800a4aa51a6db584d1a4fd28f09ce43d104231f8f668d6"
  }
}
-->

![Comic page in three strips: a timeline marks patches ended 31 March 2027, security review by March 2028, and model retires 31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says it goes before item 3 because the date is close and the work is small; a whiteboard gives the sequencing rule, deadline risk versus harm now, the rest by most removed per effort, successor samples by 29 October, and Ines says that if they fail she signs nothing, a replacement is chosen by 29 November and the switch comes in February.](assets/images/26-manage-technical-debt/comic-page-05-the-dated-item-goes-first.jpeg)

**Page 5: A close date, weighed and put first.** A migration moves software from one platform or vendor to another. The reporting stack, the software that produces customer reports, sits on a framework version, the reusable software it is built on, whose vendor stopped fixing its security holes in March 2027, and the largest prospect's security review requires supported components by the end of March 2028. The supported version builds reports differently, so there is no useful half-way state: its migration is a small rewrite with the benefit at the end, the one shape in which that is right. It goes first, ahead of the scheduling engine whose carrying cost is larger, because its date is close and its work is small: six engineer-weeks, six weeks of one engineer's time or three weeks each for two, and €5,000 of cash.

The rule has two parts. An item whose outside date leaves little more time than the work needs, with a margin for overrun, is weighed first: what missing the date would cost against the harm undated items are doing now; items brought forward go in date order, and a distant date with little work behind it can wait behind an undated item doing harm now. The rest are ordered by the cost, risk and delay each stage of effort would remove, across all three columns.

The vendor's notice of 30 September 2027 retires the artificial intelligence (AI) model that sorts customers' documents on 31 March 2028, names its successor and gives Larkspur usable access to it the same day. It arrives before Larkspur has signed its planned commitment, an agreement to make fixed monthly payments to the vendor through 2028 in return for a discount, which Ines is due to sign in November. So the test comes first. Alex runs the successor on the release-gate samples, the documents the feature had to sort correctly before release, by 29 October, and Ines signs only if it passes. If it fails, nothing is signed and no fixed payment is owed, and Larkspur chooses by 29 November between another vendor's model tested on the same samples and the failed successor. Had access come later, every date would move with it, and the choice would still be made by 31 January 2028.

The old model stays available until 31 March, but the switch is planned for February, leaving March to put right anything that goes wrong; what customers get changes on that switch day. A model that passed the samples keeps sorting automatically. A model that was tested and failed can carry the review mode from the trial: the feature proposes a category and each customer's own planner confirms it, with no new Larkspur staff. The mode still needs a model, and it starts only where Priya has confirmed that the planner has the time and has agreed the changed service and fee; other customers' sorting is suspended from the switch day.

If no model was tested at all, there is nothing to switch to: sorting is suspended for every customer on 31 March, with the changed service agreed beforehand, and documents go back to sorting by hand. Sam prices the chosen model's usage against the AI budget the board approved; anything beyond it needs the board.

*Words on the boards and cards.* Strip 1: “Patches ended 31 Mar 2027”; “Security review: by March 2028”; “Model retires 31 Mar 2028”. Strip 2: “Reporting stack migration”; “6 engineer-weeks, €5,000 cash”; “November–December 2027”. Strip 3: “Deadline risk vs harm now”; “Rest: most removed per effort”; “Successor samples by 29 October”.

- *Strip 1.* **Priya:** “Our largest prospect's security review needs supported components by the end of March 2028.” **Alex:** “The reporting stack lost support in March, and it has no half-way state.”
- *Strip 2.* **Alex:** “Small rewrite, benefit at the end: right only when no half-way step exists.” **Ines:** “It goes before item 3: the date is close and the work is small.”
- *Strip 3.* **Priya:** “Same rule, longer fuse: Alex runs the samples on the successor by 29 October.” **Ines:** “Fail, and I sign nothing. We choose by 29 November, switch in February.”

<!-- comic-page
{
  "id": "06-the-decision-and-the-gate",
  "title": "The decision, and the gate for tranche 2",
  "asset": "assets/images/26-manage-technical-debt/comic-page-06-the-decision-and-the-gate.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Ines",
    "Alex",
    "Sam"
  ],
  "strips": [
    {
      "scene": "One decision sheet is pinned flat high on the wall, above everyone's heads, its heading and five lines of lettering facing the reader; it is the only lettered object. Below it Ines sits at a desk signing a plain page that carries only ruled lines. Alex stands at the right of the desk. No head, hand, pen or bubble covers the lettering.",
      "labels": [
        "DECISION: STACK NOV–DEC 2027",
        "THEN ENGINE TRANCHE 1, JAN–MAR",
        "€50,000 TIME + €8,000 CASH",
        "REJECTED: REWRITE",
        "€300,000 TIME + €40,000 CASH"
      ],
      "label_notes": "The five labels are the five lines of the sheet, top to bottom; the third line prices tranche 1 and the fifth prices the rejected rewrite.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "Item 2 is within my delegation. Tranche 1 goes in the 2028 plan."
        },
        {
          "who": "Alex",
          "text": "Tranche 2 is a conditional line, released only on the gate's evidence."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with a two-line heading and exactly four lines of lettering under it, one under the other. Alex, at the left, and Sam, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "GATE FOR TRANCHE 2",
        "READ 31 MARCH 2028",
        "FAILOVER UNDER 5 MINUTES",
        "HOSTING DOWN €1,500 A MONTH",
        "NO INCIDENT FROM THE SPLIT",
        "LEAD TIME NO WORSE"
      ],
      "label_notes": "The first two labels are the two heading lines; the other four are the four lines under them, top to bottom.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Live by 29 February, one month observed. All four pass together, or none."
        },
        {
          "who": "Sam",
          "text": "Any miss blocks tranche 2 until every condition is read again and passes."
        }
      ]
    },
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps; the first card carries two lines of lettering, the other two one line each. Sam, at the left, gestures up at the first card with an open hand. Alex, at the right, points up at the third card. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "PORTAL REDESIGN: APRIL–JUNE",
        "AUGUST–OCTOBER IF TRANCHE 2",
        "TRANCHE 1 ENGINEERS: NAMED",
        "INVOICING SPECIALISTS: NOT INVOLVED"
      ],
      "label_notes": "The first two labels are the two lines of the first card; the third and fourth labels are the second and third cards.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Portal engineers: migration, then tranche 1. Redesign in April, or August if tranche 2."
        },
        {
          "who": "Alex",
          "text": "And the two invoicing specialists are in none of this work."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1 January to March at €50,000 of time plus €8,000 of cash, rejected rewrite at €300,000 of time plus €40,000 of cash, and Alex says tranche 2 is a conditional line released only on the gate's evidence; a whiteboard states the gate for tranche 2, read 31 March 2028, failover under five minutes, hosting down €1,500 a month, no incident from the split, lead time no worse, while Alex says the split is live by 29 February with one month observed and all four must pass together; three cards read portal redesign April to June, August to October if tranche 2, tranche 1 engineers named, invoicing specialists not involved, and Sam says the redesign starts in April, or August if tranche 2 runs.",
  "caption": "Ines, the chief executive, may approve spending inside the plan the board has adopted and below a limit the board set; that is her delegation. She authorizes the reporting-stack migration and the October model test under it. Tranche 1 of the engine, about €50,000 of the company's own engineering time plus €8,000 of cash and two named engineers for a quarter, is requested in the 2028 plan the board approves in January; tranche 2 is requested in the same plan as a conditional line that Ines may release only against the gate's evidence, which the board sees in April.\n\nThe rejected rewrite is priced on the same basis, about €300,000 of engineering time plus €40,000 of cash; it would have been outside any approved plan, so a board decision on its own.\n\nThe split goes live by 29 February 2028, March is one month of live operation, and the gate is read on 31 March. Four conditions must all pass at that reading: a failover rehearsed in under five minutes; the March hosting bill at least €1,500 a month below the bill before the split; no incident caused by the split; and lead time, the working days from an agreed change to its delivery, no worse than before, a safeguard rather than a gain. Any unmet condition blocks tranche 2 until every condition is re-read and passes; an incident means fixing its cause and observing one further clean month.\n\nThe two engineers named for the customer portal redesign, the rebuild of the website customers use, spend six engineer-weeks on the migration in November and December, then build tranche 1 from January to March.\n\nThe redesign was planned for January to March. If the work stops after tranche 1, it moves to April to June. If tranche 2 starts in April, it moves to August to October. It moves later still if approval or the gate slips, and its owner is told so.\n\n*Words on the boards and cards.* Strip 1: “Decision: stack Nov–Dec 2027”; “Then engine tranche 1, Jan–Mar”; “€50,000 time + €8,000 cash”; “Rejected: rewrite”; “€300,000 time + €40,000 cash”. Strip 2: “Gate for tranche 2”; “Read 31 March 2028”; “Failover under 5 minutes”; “Hosting down €1,500 a month”; “No incident from the split”; “Lead time no worse”. Strip 3: “Portal redesign: April–June”; “August–October if tranche 2”; “Tranche 1 engineers: named”; “Invoicing specialists: not involved”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "daca6733c09a755a00cdbc6a201be873b72557840b35a959d9674087039df0b4"
  }
}
-->

![Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1 January to March at €50,000 of time plus €8,000 of cash, rejected rewrite at €300,000 of time plus €40,000 of cash, and Alex says tranche 2 is a conditional line released only on the gate's evidence; a whiteboard states the gate for tranche 2, read 31 March 2028, failover under five minutes, hosting down €1,500 a month, no incident from the split, lead time no worse, while Alex says the split is live by 29 February with one month observed and all four must pass together; three cards read portal redesign April to June, August to October if tranche 2, tranche 1 engineers named, invoicing specialists not involved, and Sam says the redesign starts in April, or August if tranche 2 runs.](assets/images/26-manage-technical-debt/comic-page-06-the-decision-and-the-gate.jpeg)

**Page 6: The decision, and the gate for tranche 2.** Ines, the chief executive, may approve spending inside the plan the board has adopted and below a limit the board set; that is her delegation. She authorizes the reporting-stack migration and the October model test under it. Tranche 1 of the engine, about €50,000 of the company's own engineering time plus €8,000 of cash and two named engineers for a quarter, is requested in the 2028 plan the board approves in January; tranche 2 is requested in the same plan as a conditional line that Ines may release only against the gate's evidence, which the board sees in April.

The rejected rewrite is priced on the same basis, about €300,000 of engineering time plus €40,000 of cash; it would have been outside any approved plan, so a board decision on its own.

The split goes live by 29 February 2028, March is one month of live operation, and the gate is read on 31 March. Four conditions must all pass at that reading: a failover rehearsed in under five minutes; the March hosting bill at least €1,500 a month below the bill before the split; no incident caused by the split; and lead time, the working days from an agreed change to its delivery, no worse than before, a safeguard rather than a gain. Any unmet condition blocks tranche 2 until every condition is re-read and passes; an incident means fixing its cause and observing one further clean month.

The two engineers named for the customer portal redesign, the rebuild of the website customers use, spend six engineer-weeks on the migration in November and December, then build tranche 1 from January to March.

The redesign was planned for January to March. If the work stops after tranche 1, it moves to April to June. If tranche 2 starts in April, it moves to August to October. It moves later still if approval or the gate slips, and its owner is told so.

*Words on the boards and cards.* Strip 1: “Decision: stack Nov–Dec 2027”; “Then engine tranche 1, Jan–Mar”; “€50,000 time + €8,000 cash”; “Rejected: rewrite”; “€300,000 time + €40,000 cash”. Strip 2: “Gate for tranche 2”; “Read 31 March 2028”; “Failover under 5 minutes”; “Hosting down €1,500 a month”; “No incident from the split”; “Lead time no worse”. Strip 3: “Portal redesign: April–June”; “August–October if tranche 2”; “Tranche 1 engineers: named”; “Invoicing specialists: not involved”.

- *Strip 1.* **Ines:** “Item 2 is within my delegation. Tranche 1 goes in the 2028 plan.” **Alex:** “Tranche 2 is a conditional line, released only on the gate's evidence.”
- *Strip 2.* **Alex:** “Live by 29 February, one month observed. All four pass together, or none.” **Sam:** “Any miss blocks tranche 2 until every condition is read again and passes.”
- *Strip 3.* **Sam:** “Portal engineers: migration, then tranche 1. Redesign in April, or August if tranche 2.” **Alex:** “And the two invoicing specialists are in none of this work.”

<!-- comic-page
{
  "id": "07-carried-on-purpose",
  "title": "Carried on purpose, and the investor's answers",
  "asset": "assets/images/26-manage-technical-debt/comic-page-07-carried-on-purpose.jpeg",
  "aspect_ratio": "3:4",
  "cast": [
    "Ines",
    "Alex",
    "Morgan"
  ],
  "strips": [
    {
      "scene": "Ines, at the left, holds up one card so that its three lines of lettering read upright for the reader; it is the only prop in the strip. Alex, at the right, nods. Nothing covers the lettering.",
      "labels": [
        "CARRIED: INVOICING TANGLES",
        "ABOUT €3,000 A MONTH",
        "REVIEW EVERY QUARTER"
      ],
      "label_notes": "The three labels are the three lines of the card, top to bottom.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "Some debt is worth carrying. Item 1 stays, at this cost, until this date."
        },
        {
          "who": "Alex",
          "text": "Written reason, review date. A third incident in a quarter reopens it."
        }
      ]
    },
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps. Morgan, at the left, looks up at the cards. Alex, at the right, gestures up at them with an open hand. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "5 ITEMS, ABOUT €10,000 MONTHLY",
        "INCIDENTS: INVOICING AND ENGINE",
        "€12,000 A MONTH NOT WON"
      ],
      "label_notes": "One label per card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "So: how much technical debt do you have?"
        },
        {
          "who": "Alex",
          "text": "Five items: about €10,000 a month, incidents from two of them, €12,000 not won."
        }
      ]
    },
    {
      "scene": "On a table stand exactly two upright cards side by side with a clear gap, each with a heading and one line of lettering facing the reader; they are the only props on the table. Morgan, at the left of the table, looks at the cards. Alex, at the right of the table, gestures at the second card with an open hand. Nothing covers the lettering.",
      "labels": [
        "REWRITE, BENEFIT MONTH 9",
        "€300,000 TIME + €40,000 CASH",
        "TRANCHE 1, BENEFIT MONTH 3",
        "€50,000 TIME + €8,000 CASH"
      ],
      "label_notes": "The first two labels are the heading and line of the left card; the last two are the heading and line of the right card.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "And why not just rewrite it?"
        },
        {
          "who": "Alex",
          "text": "Nine frozen months and nothing bought until month nine. Tranche 1: failover by March."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Ines holds a card reading carried, invoicing tangles, about €3,000 a month, review every quarter, and says some debt is worth carrying; Morgan asks how much technical debt Larkspur has and Alex answers with three cards, five items about €10,000 monthly, incidents from invoicing and engine, €12,000 a month not won; Morgan asks why not rewrite and two cards compare the rewrite, benefit at month nine, €300,000 of time plus €40,000 of cash, with tranche 1, benefit at month three, €50,000 of time plus €8,000 of cash.",
  "caption": "Some debt is worth carrying, and saying so is honest. The invoicing module's remaining tangles cost about €3,000 a month of the company's own engineering time and two incidents a quarter, and removing them would take the two specialists the company can least spare; the item is carried with a written reason and a review date, which makes it a decision rather than neglect.\n\nMorgan's two questions are answered from the register and the tranche plan: five items on three columns, about €10,000 a month of which €5,500 is cash, incidents from the invoicing module and the engine, €12,000 a month of revenue not won; and a first tranche that buys failover by March for about €50,000 of staff time and €8,000 of cash, against a rewrite of about €300,000 of staff time and €40,000 of cash whose benefit arrives only at month nine.\n\n*Words on the boards and cards.* Strip 1: “Carried: invoicing tangles”; “About €3,000 a month”; “Review every quarter”. Strip 2: “5 items, about €10,000 monthly”; “Incidents: invoicing and engine”; “€12,000 a month not won”. Strip 3: “Rewrite, benefit month 9”; “€300,000 time + €40,000 cash”; “Tranche 1, benefit month 3”; “€50,000 time + €8,000 cash”.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "a4c9cbbbe20f186fb86b257c0c23c41f59093810541f571f1671bf95600dc635"
  }
}
-->

![Comic page in three strips: Ines holds a card reading carried, invoicing tangles, about €3,000 a month, review every quarter, and says some debt is worth carrying; Morgan asks how much technical debt Larkspur has and Alex answers with three cards, five items about €10,000 monthly, incidents from invoicing and engine, €12,000 a month not won; Morgan asks why not rewrite and two cards compare the rewrite, benefit at month nine, €300,000 of time plus €40,000 of cash, with tranche 1, benefit at month three, €50,000 of time plus €8,000 of cash.](assets/images/26-manage-technical-debt/comic-page-07-carried-on-purpose.jpeg)

**Page 7: Carried on purpose, and the investor's answers.** Some debt is worth carrying, and saying so is honest. The invoicing module's remaining tangles cost about €3,000 a month of the company's own engineering time and two incidents a quarter, and removing them would take the two specialists the company can least spare; the item is carried with a written reason and a review date, which makes it a decision rather than neglect.

Morgan's two questions are answered from the register and the tranche plan: five items on three columns, about €10,000 a month of which €5,500 is cash, incidents from the invoicing module and the engine, €12,000 a month of revenue not won; and a first tranche that buys failover by March for about €50,000 of staff time and €8,000 of cash, against a rewrite of about €300,000 of staff time and €40,000 of cash whose benefit arrives only at month nine.

*Words on the boards and cards.* Strip 1: “Carried: invoicing tangles”; “About €3,000 a month”; “Review every quarter”. Strip 2: “5 items, about €10,000 monthly”; “Incidents: invoicing and engine”; “€12,000 a month not won”. Strip 3: “Rewrite, benefit month 9”; “€300,000 time + €40,000 cash”; “Tranche 1, benefit month 3”; “€50,000 time + €8,000 cash”.

- *Strip 1.* **Ines:** “Some debt is worth carrying. Item 1 stays, at this cost, until this date.” **Alex:** “Written reason, review date. A third incident in a quarter reopens it.”
- *Strip 2.* **Morgan:** “So: how much technical debt do you have?” **Alex:** “Five items: about €10,000 a month, incidents from two of them, €12,000 not won.”
- *Strip 3.* **Morgan:** “And why not just rewrite it?” **Alex:** “Nine frozen months and nothing bought until month nine. Tranche 1: failover by March.”
