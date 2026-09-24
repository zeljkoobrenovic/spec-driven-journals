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

**Comic.** Larkspur is a fictional company that sells scheduling software, and an investor owns a large stake in it. Preparing the board's annual technology review, the investor's adviser asks two questions: how much technical debt does the company have, and would it not be simpler to rewrite the old parts? Seven pages show Larkspur answering with a register of five items, each with a monthly carrying cost in three columns, and funding the first fix in tranches released by measured gates, with one dated item going first and one item deliberately carried.

The people: Morgan advises the investor, Alex leads technology, Priya leads product, Sam leads finance, and Ines is the chief executive, who can approve spending inside the limit the board has set. All are fictional, and every amount and date is invented for the example.

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
          "text": "Debt is what the software costs us each month while it stays."
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
  "alt": "Comic page in three strips: Morgan hands Alex a note asking how much technical debt and why not rewrite, and Alex says a count or a percentage answers neither; three cards read issue count and percent of code, both struck through, and carrying cost per month in bold; a whiteboard shows three columns, cost carried with workaround hours and old hosting, risk carried with incidents, unsupported and retiring, and speed lost with lead time and deals lost.",
  "caption": "Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells scheduling software; an investor owns a large stake in it. Technical debt is the cost a company carries because its software was built, or has aged, in ways that make it slower, riskier or dearer to change than it needs to be. Morgan advises the investor; Alex leads technology; Priya leads product. A carrying cost is what an item costs the company each month while it remains, in three columns: cost carried, risk carried and speed lost.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "e570af06ef46e83d680c7cedbb965686e89e92728863950a30a1abed793887e0"
  }
}
-->

![Comic page in three strips: Morgan hands Alex a note asking how much technical debt and why not rewrite, and Alex says a count or a percentage answers neither; three cards read issue count and percent of code, both struck through, and carrying cost per month in bold; a whiteboard shows three columns, cost carried with workaround hours and old hosting, risk carried with incidents, unsupported and retiring, and speed lost with lead time and deals lost.](assets/images/26-manage-technical-debt/comic-page-01-two-questions-one-wrong-answer.jpeg)

**Page 1: Two questions, and the wrong kind of answer.** Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells scheduling software; an investor owns a large stake in it. Technical debt is the cost a company carries because its software was built, or has aged, in ways that make it slower, riskier or dearer to change than it needs to be. Morgan advises the investor; Alex leads technology; Priya leads product. A carrying cost is what an item costs the company each month while it remains, in three columns: cost carried, risk carried and speed lost.

- *Strip 1.* **Morgan:** “Two questions for the board's review: how much debt, and why not rewrite?” **Alex:** “A count or a percentage would answer neither. Give me two weeks.”
- *Strip 2.* **Alex:** “Debt is what the software costs us each month while it stays.” **Priya:** “A carrying cost. The board already knows how to read one of those.”
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
          "text": "Five items. A real register is rarely longer than ten."
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
          "text": "Item 4 was a deliberate shortcut, dated, owned by me. Not a failure."
        },
        {
          "who": "Alex",
          "text": "An undated one is. And a date nobody inside chose goes first."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly four large lines of lettering, one under the other. Sam, at the left, and Alex, at the right, stand clear of the board; Sam gestures up at it with an open hand. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "ABOUT €8,500 A MONTH",
        "2 INCIDENTS A QUARTER",
        "FAILOVER: 45 MINUTES",
        "€12,000 A MONTH NOT WON"
      ],
      "label_notes": "The four labels are the four lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Carried, the five cost about €8,500 a month of cash and time."
        },
        {
          "who": "Alex",
          "text": "And two prospects above 400 technicians we can't serve: revenue not won."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, and vendor model retiring; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, growth outran design tranches, ageing platform and retiring vendor by the date; a second whiteboard totals the register at about €8,500 a month, two incidents a quarter, a 45-minute failover and €12,000 a month not won.",
  "caption": "Larkspur's register has five items. The origin of each decides who owns it and what the remedy usually is; a deliberate shortcut recorded with a date and an owner is not a failure, an undated one is. Carried, the five cost about €8,500 a month of cash and cost-based engineering time, two customer-visible incidents a quarter and a 45-minute failover, and the scheduling engine's single-server design turns away customers above about 400 technicians, about €12,000 a month of revenue not won. Sam leads finance.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "7f623e1a1ade39b9d6e88cd9798c395963e3c35ab81208cf91e68789c721a508"
  }
}
-->

![Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, and vendor model retiring; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, growth outran design tranches, ageing platform and retiring vendor by the date; a second whiteboard totals the register at about €8,500 a month, two incidents a quarter, a 45-minute failover and €12,000 a month not won.](assets/images/26-manage-technical-debt/comic-page-02-five-items-four-origins.jpeg)

**Page 2: Five items, and where each came from.** Larkspur's register has five items. The origin of each decides who owns it and what the remedy usually is; a deliberate shortcut recorded with a date and an owner is not a failure, an undated one is. Carried, the five cost about €8,500 a month of cash and cost-based engineering time, two customer-visible incidents a quarter and a 45-minute failover, and the scheduling engine's single-server design turns away customers above about 400 technicians, about €12,000 a month of revenue not won. Sam leads finance.

- *Strip 1.* **Alex:** “Five items. A real register is rarely longer than ten.” **Priya:** “The vendor model retires on 31 March 2028. That one has a date.”
- *Strip 2.* **Priya:** “Item 4 was a deliberate shortcut, dated, owned by me. Not a failure.” **Alex:** “An undated one is. And a date nobody inside chose goes first.”
- *Strip 3.* **Sam:** “Carried, the five cost about €8,500 a month of cash and time.” **Alex:** “And two prospects above 400 technicians we can't serve: revenue not won.”

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
          "text": "For the engine: two prospects, oversized servers, a 45-minute failover against a two-second promise."
        },
        {
          "who": "Ines",
          "text": "Nothing here prices exactly. So judge the fix by the columns it moves."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: three cards read revenue protected or enabled, cost or risk removed, and a decision kept open; a before-and-after table lists incidents per quarter, failover time and lead time with empty cells, while Sam says nobody gets credit for a failure that never happened; four cards for the scheduling engine read two prospects €12,000 a month, €4,000 hosting above need, 45-minute failover, and core replacement kept open.",
  "caption": "A reduction project is presented the way the board reads any investment: the revenue it protects or enables, the cost or risk it removes and, only where a real dated decision is being kept open, the decision it preserves. None of the three can be priced exactly, so the work is judged on the register columns it moves, measured before and after. The board rarely sees the failures a fix prevented, because a prevented failure is invisible while the effort sits on this quarter's budget; the after column is the answer. Ines is the chief executive.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "7a66487b9b7018d75f93d31672f6bdd9a31f5ccfeb0d9fd4aa63b2597bc04abe"
  }
}
-->

![Comic page in three strips: three cards read revenue protected or enabled, cost or risk removed, and a decision kept open; a before-and-after table lists incidents per quarter, failover time and lead time with empty cells, while Sam says nobody gets credit for a failure that never happened; four cards for the scheduling engine read two prospects €12,000 a month, €4,000 hosting above need, 45-minute failover, and core replacement kept open.](assets/images/26-manage-technical-debt/comic-page-03-present-the-fix-by-what-it-buys.jpeg)

**Page 3: Present the fix by what it buys.** A reduction project is presented the way the board reads any investment: the revenue it protects or enables, the cost or risk it removes and, only where a real dated decision is being kept open, the decision it preserves. None of the three can be priced exactly, so the work is judged on the register columns it moves, measured before and after. The board rarely sees the failures a fix prevented, because a prevented failure is invisible while the effort sits on this quarter's budget; the after column is the answer. Ines is the chief executive.

- *Strip 1.* **Alex:** “The board reads a fix like any investment: protects, removes, or keeps open.” **Ines:** “Kept open only for a named decision with a date, never a general virtue.”
- *Strip 2.* **Sam:** “Nobody gets credit for a failure that never happened. The effort is this quarter's.” **Alex:** “So we measure before and after. That's a claim the board can check.”
- *Strip 3.* **Alex:** “For the engine: two prospects, oversized servers, a 45-minute failover against a two-second promise.” **Ines:** “Nothing here prices exactly. So judge the fix by the columns it moves.”

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
        "9 MONTHS, ABOUT €340,000",
        "BENEFIT AT MONTH 9",
        "B: TRANCHES WITH GATES",
        "TRANCHE 1: €58,000",
        "FAILOVER AT MONTH 3",
        "C: LIVE WITH IT",
        "COST CONTINUES"
      ],
      "label_notes": "The first three labels are the three lines of card A, top to bottom; the next three are card B; the last two are card C.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Three ways to reduce item 3, on one basis: effort, cash, benefit date."
        },
        {
          "who": "Priya",
          "text": "A rewrite gives nothing customer-visible before month nine. Tranche 1 gives failover at three."
        }
      ]
    },
    {
      "scene": "A long horizontal timeline high on the wall, above everyone's heads with exactly four tick marks in total, one tick directly under each of the four labels and no other tick anywhere. Above the line lies one long plain bar reaching from the first tick to the fourth, with one small flag standing at its right end. Below the line lie two shorter plain bars: one from the first tick to the second with a flag at its right end, then a small closed barrier gate, then one from the second tick to the third with a flag at its right end. Sam, at the left, and Alex, at the right, stand below the timeline and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "MONTH 0",
        "MONTH 3",
        "MONTH 7",
        "MONTH 9",
        "REWRITE",
        "TRANCHE 1",
        "GATE",
        "TRANCHE 2"
      ],
      "label_notes": "The four MONTH labels sit over the four ticks, left to right; REWRITE is lettered on the long upper bar; TRANCHE 1 on the first lower bar, GATE beside the barrier, TRANCHE 2 on the second lower bar.",
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
        "€170,000 GONE, €130,000 TO DECIDE",
        "TRANCHE 1 DONE:",
        "€58,000 SPENT, FAILOVER IN HAND"
      ],
      "label_notes": "The four labels are the four lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "Halfway through a rewrite, €170,000 is gone whether it finishes or stops."
        },
        {
          "who": "Priya",
          "text": "After tranche 1, €58,000 is spent and the benefit is already in hand."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: three cards compare A, rewrite the engine, nine months and about €340,000 with the benefit at month nine, B, tranches with gates, tranche 1 at €58,000 with failover at month three, and C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar ending in a single flag against two tranche bars with flags at months 3 and 7 and a gate between; a whiteboard reads rewrite month 5, €170,000 gone and €130,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.",
  "caption": "For the scheduling engine, a rewrite (replacing the system with a new one) costs about €340,000 over nine months with the old engine frozen and every risk arriving at one switch-over. A tranche plan funds the work in stages, each released by a measured gate: tranche 1 splits the schedule computation so it can fail over, about €58,000, benefit at month three; tranche 2 partitions the largest customers, benefit at month seven; replacing the core stays a later decision. Living with it keeps the carrying cost. Money already spent should not tip the decision; after tranche 1 the remaining decision is only about tranche 2.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "841aa9c9b9fb9b570ffc02d3b6e3a183060017fb6258df4f7cafba8797eb80a7"
  }
}
-->

![Comic page in three strips: three cards compare A, rewrite the engine, nine months and about €340,000 with the benefit at month nine, B, tranches with gates, tranche 1 at €58,000 with failover at month three, and C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar ending in a single flag against two tranche bars with flags at months 3 and 7 and a gate between; a whiteboard reads rewrite month 5, €170,000 gone and €130,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.](assets/images/26-manage-technical-debt/comic-page-04-rewrite-tranches-or-live-with-it.jpeg)

**Page 4: Rewrite, tranches, or live with it.** For the scheduling engine, a rewrite (replacing the system with a new one) costs about €340,000 over nine months with the old engine frozen and every risk arriving at one switch-over. A tranche plan funds the work in stages, each released by a measured gate: tranche 1 splits the schedule computation so it can fail over, about €58,000, benefit at month three; tranche 2 partitions the largest customers, benefit at month seven; replacing the core stays a later decision. Living with it keeps the carrying cost. Money already spent should not tip the decision; after tranche 1 the remaining decision is only about tranche 2.

- *Strip 1.* **Alex:** “Three ways to reduce item 3, on one basis: effort, cash, benefit date.” **Priya:** “A rewrite gives nothing customer-visible before month nine. Tranche 1 gives failover at three.”
- *Strip 2.* **Sam:** “Rewrite: the old engine frozen nine months, then every risk arrives at the switch-over.” **Alex:** “Tranches: failover at month three, large customers at month seven, each measured first.”
- *Strip 3.* **Sam:** “Halfway through a rewrite, €170,000 is gone whether it finishes or stops.” **Priya:** “After tranche 1, €58,000 is spent and the benefit is already in hand.”

<!-- comic-page
{
  "id": "05-the-dated-item-goes-first",
  "title": "A hard date outranks a large number",
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
        "SECURITY REVIEW: Q1 2028",
        "MODEL RETIRES 31 MAR 2028"
      ],
      "label_notes": "The three labels sit over the three ticks, left to right.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Our largest prospect's security review needs supported components by the first quarter of 2028."
        },
        {
          "who": "Alex",
          "text": "The reporting stack has been unsupported since March. There is no half-way state."
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
          "text": "A small rewrite, benefit at the end: the one case where that's right."
        },
        {
          "who": "Ines",
          "text": "It goes before item 3. A hard date outranks a large number."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with exactly three lines of lettering, one under the other. Priya, at the left, and Ines, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "DATED ITEMS: BY THE DATE",
        "THE REST: BY CARRYING COST",
        "SUCCESSOR MODEL TEST: JANUARY 2028"
      ],
      "label_notes": "The three labels are the three lines of the whiteboard, top to bottom.",
      "bubbles": [
        {
          "who": "Priya",
          "text": "Same rule, longer fuse: the successor model is tested in January."
        },
        {
          "who": "Ines",
          "text": "Three months before the retirement, so the decision window isn't spent finding the problem."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: a timeline marks patches ended 31 March 2027, security review in the first quarter of 2028, and model retires 31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says a hard date outranks a large number; a whiteboard gives the sequencing rule, dated items by the date, the rest by carrying cost, successor model test January 2028.",
  "caption": "A migration moves software from one platform or vendor to another. The reporting stack's framework has been unsupported since March 2027 and the largest prospect's security review requires supported components by the first quarter of 2028; there is no half-way state, so its migration is a small rewrite with the benefit at the end, the one situation in which that shape is right. It goes first, ahead of the scheduling engine whose carrying cost is larger. An engineer-week is one person working one week. The successor to the retiring vendor model is tested in January 2028, three months before the retirement date.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "254c49419ee7cdc822c32cb38b35c6cd2d81d3dd6a1c311fd192efb1c53c4332"
  }
}
-->

![Comic page in three strips: a timeline marks patches ended 31 March 2027, security review in the first quarter of 2028, and model retires 31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says a hard date outranks a large number; a whiteboard gives the sequencing rule, dated items by the date, the rest by carrying cost, successor model test January 2028.](assets/images/26-manage-technical-debt/comic-page-05-the-dated-item-goes-first.jpeg)

**Page 5: A hard date outranks a large number.** A migration moves software from one platform or vendor to another. The reporting stack's framework has been unsupported since March 2027 and the largest prospect's security review requires supported components by the first quarter of 2028; there is no half-way state, so its migration is a small rewrite with the benefit at the end, the one situation in which that shape is right. It goes first, ahead of the scheduling engine whose carrying cost is larger. An engineer-week is one person working one week. The successor to the retiring vendor model is tested in January 2028, three months before the retirement date.

- *Strip 1.* **Priya:** “Our largest prospect's security review needs supported components by the first quarter of 2028.” **Alex:** “The reporting stack has been unsupported since March. There is no half-way state.”
- *Strip 2.* **Alex:** “A small rewrite, benefit at the end: the one case where that's right.” **Ines:** “It goes before item 3. A hard date outranks a large number.”
- *Strip 3.* **Priya:** “Same rule, longer fuse: the successor model is tested in January.” **Ines:** “Three months before the retirement, so the decision window isn't spent finding the problem.”

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
      "scene": "One decision sheet is pinned flat high on the wall, above everyone's heads, its heading and four lines of lettering facing the reader; it is the only lettered object. Below it Ines sits at a desk signing a plain page that carries only ruled lines. Alex stands at the right of the desk. No head, hand, pen or bubble covers the lettering.",
      "labels": [
        "DECISION: STACK NOV–DEC 2027",
        "THEN ENGINE TRANCHE 1",
        "JAN–MAR 2028, €8,000 CASH",
        "REJECTED: REWRITE, €340,000"
      ],
      "label_notes": "The four labels are the four lines of the sheet, top to bottom.",
      "bubbles": [
        {
          "who": "Ines",
          "text": "Item 2 is within my delegation. Tranche 1 goes in the 2028 plan."
        },
        {
          "who": "Alex",
          "text": "The board sees tranche 2 only with tranche 1's measured result."
        }
      ]
    },
    {
      "scene": "A whiteboard high on the wall, above everyone's heads with a two-line heading and exactly four lines of lettering under it, one under the other. Alex, at the left, and Sam, at the right, stand clear of the board and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "GATE FOR TRANCHE 2",
        "BY 31 MARCH 2028",
        "FAILOVER UNDER 5 MINUTES",
        "HOSTING DOWN €1,500 A MONTH",
        "NO INCIDENT FROM THE SPLIT",
        "LEAD TIME NO WORSE"
      ],
      "label_notes": "The first two labels are the two heading lines; the other four are the four lines under them, top to bottom.",
      "bubbles": [
        {
          "who": "Alex",
          "text": "Failover from 45 minutes to under five. All four met, tranche 2 starts April."
        },
        {
          "who": "Sam",
          "text": "An incident from the split: wait one clean quarter. Failover missed: review the design."
        }
      ]
    },
    {
      "scene": "A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps. Sam, at the left, gestures up at the first card with an open hand. Alex, at the right, points up at the third card. No head, hand, marker or bubble covers the lettering.",
      "labels": [
        "PORTAL REDESIGN WAITS ONE QUARTER",
        "TRANCHE 1 ENGINEERS: NAMED",
        "INVOICING SPECIALISTS: NOT INVOLVED"
      ],
      "label_notes": "One label per card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Sam",
          "text": "The engineer-weeks come from the portal redesign, which waits one quarter."
        },
        {
          "who": "Alex",
          "text": "And the two invoicing specialists are in none of this work."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1, January to March 2028 with €8,000 cash, rejected rewrite at €340,000; a whiteboard states the gate for tranche 2 by 31 March 2028, failover under five minutes, hosting down €1,500 a month, no incident from the split, lead time no worse; three cards read portal redesign waits one quarter, tranche 1 engineers named, invoicing specialists not involved.",
  "caption": "Ines authorizes the reporting-stack migration and the January model test within her delegation; tranche 1 of the engine, €8,000 of cash and two named engineers for a quarter, is requested in the 2028 plan the board approves, and tranche 2 is a separate line the board sees only with tranche 1's measured result. A rewrite would have been a board decision on its own, at €340,000. The gate names a reduction in each column and what happens when it is met, missed or falls between. The customer portal redesign is the work that waits, and it is told so.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "6607a354d4175d82dfd02715a026b6b41e53b7c83b835dc18a6fd1f516fc7d09"
  }
}
-->

![Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1, January to March 2028 with €8,000 cash, rejected rewrite at €340,000; a whiteboard states the gate for tranche 2 by 31 March 2028, failover under five minutes, hosting down €1,500 a month, no incident from the split, lead time no worse; three cards read portal redesign waits one quarter, tranche 1 engineers named, invoicing specialists not involved.](assets/images/26-manage-technical-debt/comic-page-06-the-decision-and-the-gate.jpeg)

**Page 6: The decision, and the gate for tranche 2.** Ines authorizes the reporting-stack migration and the January model test within her delegation; tranche 1 of the engine, €8,000 of cash and two named engineers for a quarter, is requested in the 2028 plan the board approves, and tranche 2 is a separate line the board sees only with tranche 1's measured result. A rewrite would have been a board decision on its own, at €340,000. The gate names a reduction in each column and what happens when it is met, missed or falls between. The customer portal redesign is the work that waits, and it is told so.

- *Strip 1.* **Ines:** “Item 2 is within my delegation. Tranche 1 goes in the 2028 plan.” **Alex:** “The board sees tranche 2 only with tranche 1's measured result.”
- *Strip 2.* **Alex:** “Failover from 45 minutes to under five. All four met, tranche 2 starts April.” **Sam:** “An incident from the split: wait one clean quarter. Failover missed: review the design.”
- *Strip 3.* **Sam:** “The engineer-weeks come from the portal redesign, which waits one quarter.” **Alex:** “And the two invoicing specialists are in none of this work.”

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
        "5 ITEMS, ABOUT €8,500 MONTHLY",
        "2 INCIDENTS A QUARTER",
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
          "text": "Five items: about €8,500 a month, two incidents a quarter, €12,000 not won."
        }
      ]
    },
    {
      "scene": "On a table stand exactly two upright cards side by side with a clear gap, their lettering facing the reader; they are the only props on the table. Morgan, at the left of the table, looks at the cards. Alex, at the right of the table, gestures at the second card with an open hand. Nothing covers the lettering.",
      "labels": [
        "REWRITE: €340,000, MONTH 9",
        "TRANCHE 1: €58,000, MONTH 3"
      ],
      "label_notes": "One label per card, in this left-to-right order.",
      "bubbles": [
        {
          "who": "Morgan",
          "text": "And why not just rewrite it?"
        },
        {
          "who": "Alex",
          "text": "Nine frozen months, €340,000 counted only at the end. Tranche 1: failover by March."
        }
      ]
    }
  ],
  "alt": "Comic page in three strips: Ines holds a card reading carried, invoicing tangles, about €3,000 a month, review every quarter, and says some debt is worth carrying; Morgan asks how much technical debt Larkspur has and Alex answers with three cards, five items about €8,500 a month, two incidents a quarter, €12,000 a month not won; Morgan asks why not rewrite and two cards compare rewrite €340,000 at month nine with tranche 1 €58,000 at month three.",
  "caption": "Some debt is worth carrying, and saying so is honest. The invoicing module's remaining tangles cost about €3,000 a month and two incidents a quarter, and removing them would take the two specialists the company can least spare; the item is carried with a written reason and a review date, which makes it a decision rather than neglect. Morgan's two questions are answered from the register and the tranche plan: five items on three columns, and a first tranche that buys failover by March for about €58,000 against a €340,000 rewrite whose benefit arrives at month nine.",
  "status": "generated",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference": "_research/comic-cast-20260913.jpeg",
    "sha256": "e9e6e286973b4d843677e132bc6470871083a536d72f408a0e061b97861865d4"
  }
}
-->

![Comic page in three strips: Ines holds a card reading carried, invoicing tangles, about €3,000 a month, review every quarter, and says some debt is worth carrying; Morgan asks how much technical debt Larkspur has and Alex answers with three cards, five items about €8,500 a month, two incidents a quarter, €12,000 a month not won; Morgan asks why not rewrite and two cards compare rewrite €340,000 at month nine with tranche 1 €58,000 at month three.](assets/images/26-manage-technical-debt/comic-page-07-carried-on-purpose.jpeg)

**Page 7: Carried on purpose, and the investor's answers.** Some debt is worth carrying, and saying so is honest. The invoicing module's remaining tangles cost about €3,000 a month and two incidents a quarter, and removing them would take the two specialists the company can least spare; the item is carried with a written reason and a review date, which makes it a decision rather than neglect. Morgan's two questions are answered from the register and the tranche plan: five items on three columns, and a first tranche that buys failover by March for about €58,000 against a €340,000 rewrite whose benefit arrives at month nine.

- *Strip 1.* **Ines:** “Some debt is worth carrying. Item 1 stays, at this cost, until this date.” **Alex:** “Written reason, review date. A third incident in a quarter reopens it.”
- *Strip 2.* **Morgan:** “So: how much technical debt do you have?” **Alex:** “Five items: about €8,500 a month, two incidents a quarter, €12,000 not won.”
- *Strip 3.* **Morgan:** “And why not just rewrite it?” **Alex:** “Nine frozen months, €340,000 counted only at the end. Tranche 1: failover by March.”
