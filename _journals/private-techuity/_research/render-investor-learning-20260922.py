"""Render the investor-learning chapter's authored vector figures and comic.

Standard library only. Artwork is original SVG, with no external images or fonts.
The Northline cast is independent of the book's shared Larkspur example.

Revised 23 September 2026 (in-depth review round 1, INVNET-001/002/003/005):
the comic pages carry plain-language explanations for lay readers and page 5's
caption describes planning the one-month review after the visit.

Revised again on 23 September 2026 (round 2, INVNET-007): the comic pages are
laid out for phone reading. Each page is 600 units wide instead of 960, the two
speakers are stacked (Mira's bubble above Tomas's) instead of side by side, and
dialogue is set at 24 units, so at a 340-pixel phone width the dialogue shows at
about 13.6 pixels instead of 7.8. Dialogue, headings and labels are wrapped by
measured Arial widths (Pillow, when installed; use `python3.11`, which has it)
with a 12% allowance for the widest declared fallback font, so no line can
cross its bubble border. Without Pillow the script falls back to a per-character
estimate, which wraps differently, so the recorded SVGs come from python3.11.

Run `python3 render-investor-learning-20260922.py comics` to regenerate only the
five comic SVGs and comics.md without touching the replaced article figures,
logo, icon or the Part IV overview. `... comics --check` prints the wrapped
lines and their measured widths without writing anything. `... part-overview`
regenerates only the Part IV six-chapter overview (stacked single column since
23 September 2026, so it reads at phone width).
"""
from pathlib import Path
from html import escape
import json
import textwrap

JOURNAL = Path(__file__).resolve().parents[1]
SLUG = 'learn-through-investors-network'
POST = next(p.parent for p in (JOURNAL / 'posts').glob('*/index.md')
            if f'permalink: {SLUG}\n' in p.read_text())
ASSETS = POST / 'assets' / 'images' / SLUG
ASSETS.mkdir(parents=True, exist_ok=True)
IVORY = '#f6f1e6'
INK = '#24394a'
TEAL = '#337d79'
OCHRE = '#c58c32'
MUTED = '#556a72'
PALE = '#e2eeea'
WHITE = '#fffdf8'


def rect(x, y, w, h, fill=WHITE, stroke=INK, radius=16, cls=None):
    klass = f' class="{cls}"' if cls else ''
    return f'<rect{klass} x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def line(x1, y1, x2, y2, color=INK, width=3):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none" stroke-linecap="round"/>'


def text(x, y, words, size=26, color=INK, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="{FONT_STACK}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(words)}</text>'


def wrapped(x, y, words, width=30, size=26, color=INK, leading=None, weight=400, anchor='start'):
    leading = leading or size * 1.32
    rows = textwrap.wrap(words, width=width, break_long_words=False)
    return ''.join(text(x, y + i * leading, row, size, color, weight, anchor) for i, row in enumerate(rows))


FONT_STACK = "Arial, 'Liberation Sans', Helvetica, 'DejaVu Sans', sans-serif"
_ARIAL = {400: '/System/Library/Fonts/Supplemental/Arial.ttf', 700: '/System/Library/Fonts/Supplemental/Arial Bold.ttf'}
# DejaVu Sans, the widest font in FONT_STACK, sets text roughly a tenth wider than Arial;
# every measured line keeps this much spare room so a fallback rendering still fits.
FALLBACK_ALLOWANCE = 1.12


def measure(words, size, weight=400):
    """Width of `words` in Arial at `size`: Pillow's font metrics when available, else an estimate."""
    try:
        from PIL import ImageFont
        return ImageFont.truetype(_ARIAL[weight], size).getlength(words)
    except Exception:
        return len(words) * size * (0.56 if weight == 700 else 0.52)


def fit_lines(words, size, max_width, weight=400):
    """Greedy wrap by measured width, leaving FALLBACK_ALLOWANCE inside max_width."""
    limit = max_width / FALLBACK_ALLOWANCE
    lines, current = [], ''
    for word in words.split():
        candidate = f'{current} {word}'.strip()
        if current and measure(candidate, size, weight) > limit:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    for row in lines:
        if measure(row, size, weight) > limit:
            raise ValueError(('line too wide for its box', row, size, max_width))
    return lines


def lines_text(x, y, lines, size, color=INK, leading=None, weight=400, anchor='start'):
    leading = leading or size * 1.32
    return ''.join(text(x, y + i * leading, row, size, color, weight, anchor) for i, row in enumerate(lines))


def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{TEAL}" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'


def svg(width, height, title, desc, body):
    # width/height give the SVG an intrinsic size; without them an <img> with
    # `max-width:100%; height:auto` collapses to a dot in Chromium (found 23 Sept 2026).
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{TEAL}"/></marker></defs>
<rect width="{width}" height="{height}" fill="{IVORY}"/>{body}</svg>\n'''


def write(name, width, height, title, desc, body):
    (ASSETS / name).write_text(svg(width, height, title, desc, body))


def person(cx, cy, who, scale=1):
    # Head centered at y=0; torso and feet extend to y=123.
    if who == 'Mira':
        skin, shirt = '#a96449', '#86566f'
        hair = '<path d="M-31 5 Q-42-49 0-40 Q42-43 34 37 L23 37 L22-10 Q0-8-22-20 L-24 37 L-35 37 Z" fill="#29343e"/>'
    else:
        skin, shirt = '#e6b28a', TEAL
        hair = '<path d="M-30-6 Q-37-42-13-38 Q7-52 21-34 Q39-33 31-6 L20-17 L5-20 L-11-17 Z" fill="#3a3d42"/>'
    face = f'<ellipse cx="0" cy="0" rx="27" ry="32" fill="{skin}" stroke="{INK}" stroke-width="2"/>'
    if who == 'Mira':
        face = hair + face + '<path d="M-28-7 Q-27-39 0-36 Q28-38 29-10 Q3-11-18-24 Z" fill="#29343e"/>'
    else:
        face += hair + f'<g fill="none" stroke="{INK}" stroke-width="2"><rect x="-23" y="-8" width="19" height="13" rx="5"/><rect x="4" y="-8" width="19" height="13" rx="5"/><path d="M-4-2 H4"/></g>'
    face += f'<path d="M-9 15 Q0 21 10 14" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
    body = f'<path d="M-15 29 L15 29 L42 51 L29 95 L-28 95 L-42 51 Z" fill="{shirt}" stroke="{INK}" stroke-width="2"/>'
    body += f'<path d="M-29 51 L-45 81 L-65 66 M29 51 L45 80 L62 65" stroke="{shirt}" stroke-width="15" stroke-linecap="round" fill="none"/>'
    body += f'<circle cx="-65" cy="66" r="8" fill="{skin}"/><circle cx="62" cy="65" r="8" fill="{skin}"/>'
    body += f'<path d="M-15 95 L-18 120 M15 95 L18 120" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>'
    return f'<g transform="translate({cx} {cy}) scale({scale})">{body}{face}</g>'


def figures():
    b = text(55, 65, 'FROM ACCESS TO LEARNING', 22, TEAL, 700)
    b += text(55, 113, 'Bring people and experience into view', 35, INK, 700)
    for x, title, detail in [(55, 'Investor connections', 'Introductions, convening and continuity'), (555, 'People and practice', 'Encounters beyond your everyday work')]:
        b += rect(x, 163, 390, 135, PALE)
        b += text(x + 25, 207, title, 28, INK, 700)
        b += wrapped(x + 25, 248, detail, 28, 25)
    b += arrow(454, 228, 541, 228)
    b += arrow(750, 313, 750, 351)
    b += rect(55, 366, 890, 106)
    b += text(500, 407, 'REFLECT WITH YOUR COMPANY', 25, TEAL, 700, 'middle')
    b += text(500, 446, 'What did we see? What might matter here?', 28, INK, 400, 'middle')
    outcomes = [(55, 'Better questions', 'Revisit an assumption'), (365, 'Useful relationships', 'Keep a conversation alive'), (675, 'A local experiment', 'Test what could transfer')]
    for x, title, detail in outcomes:
        b += arrow(x + 135, 481, x + 135, 521)
        b += rect(x, 536, 270, 124, '#f3e6cf', OCHRE)
        b += wrapped(x + 135, 577, title, 22, 25, INK, 33, 700, 'middle')
        b += wrapped(x + 135, 623, detail, 24, 21, MUTED, 25, 400, 'middle')
    b += text(500, 714, 'Each can lead to more learning. Outcomes are not automatic.', 23, MUTED, 400, 'middle')
    write('learning-paths.svg', 1000, 754, 'From access to learning', 'Connections lead to encounters and reflection, with possible outcomes of better questions, continuing relationships or local experiments.', b)

    b = text(55, 63, 'NORTHLINE · A FICTIONAL EXAMPLE', 21, TEAL, 700)
    b += text(55, 112, 'Carry the context home', 38, INK, 700)
    cards = [(55, 158, '1  OBSERVED', 'People review suggestions inside their inventory screen.', PALE),
             (520, 158, '2  HOST’S EXPLANATION', 'Reliable records and easy corrections help the workflow.', WHITE),
             (55, 375, '3  OUR CIRCUMSTANCES', 'Our customers have uneven product records.', WHITE),
             (520, 375, '4  NEXT ENQUIRY', 'What information and control would our customers need?', '#f3e6cf')]
    for x, y, title, words, fill in cards:
        b += rect(x, y, 425, 184, fill)
        b += text(x + 24, y + 43, title, 22, TEAL, 700)
        b += wrapped(x + 24, y + 87, words, 26, 28)
    b += text(500, 620, 'A useful observation still needs interpretation and local enquiry.', 23, MUTED, 400, 'middle')
    write('bring-context-home.svg', 1000, 664, 'Carry the context home', 'Four cards distinguish observation, a host explanation, Northline’s different conditions and its next question.', b)

    b = '<circle cx="784" cy="165" r="88" fill="#ead3a6"/>'
    b += '<path d="M80 450 Q245 225 450 315 T925 190" fill="none" stroke="#aecac1" stroke-width="38" stroke-linecap="round"/>'
    for x, y in [(150, 130), (390, 85), (625, 310)]:
        b += rect(x, y, 165, 135, WHITE, TEAL, 13)
        b += line(x + 25, y + 38, x + 130, y + 38, OCHRE, 7)
        for row in range(3): b += line(x + 25, y + 68 + row * 18, x + 108 - row * 13, y + 68 + row * 18, '#9aacae', 5)
    b += '<path d="M280 485 Q390 423 500 469 Q610 423 720 485 L720 540 Q610 487 500 526 Q390 487 280 540 Z" fill="#fffdf8" stroke="#24394a" stroke-width="4"/>'
    b += line(500, 469, 500, 526, TEAL, 4)
    b += person(210, 360, 'Mira', .72) + person(815, 330, 'Tomas', .72)
    write('logo.svg', 1000, 590, 'Learning through connections', 'Two leaders connect an open book with unfamiliar examples and shared experience.', b)
    icon = '<path d="M24 79 Q44 64 64 74 Q84 64 104 79 V104 Q84 90 64 100 Q44 90 24 104 Z" fill="#fffdf8" stroke="#24394a" stroke-width="4"/>'
    icon += line(64, 73, 64, 101, TEAL, 3)
    icon += line(38, 35, 64, 62, TEAL, 4) + line(90, 35, 64, 62, TEAL, 4)
    icon += '<circle cx="35" cy="31" r="13" fill="#337d79"/><circle cx="93" cy="31" r="13" fill="#c58c32"/>'
    target = POST / 'assets' / 'icons' / f'{SLUG}.svg'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(svg(128, 128, 'Shared learning', 'Connections feeding an open book.', icon))


PAGES = [
    ('01-choose-the-experience', 'Choose the experience', 'Mira leads product and Tomas leads engineering at fictional Northline, whose software helps small wholesalers track their stock. They compare ways to learn how customers would use AI reorder suggestions: recommendations of what to buy again and how much.', [
        ('Start with a question worth exploring', 'What helps a customer trust an AI reorder suggestion?', 'We need to see how people use it during an ordinary working day.', 'Our question / Trust in use'),
        ('Different formats offer different access', 'The investor offers a tour, a seminar or introductions to people using similar systems.', 'The regional hosts will show their everyday work steps and discuss exceptions.', 'Compare access / Tour, seminar, visit'),
        ('Choose the access and keep a fallback', 'Let us take the two-day regional visit.', 'If that access falls through, use the seminar and a follow-up call.', 'Chosen / Two-day visit')]),
    ('02-make-room', 'Make room for learning', 'The chief executive approves up to €1,200 from Northline’s existing learning budget and six person-days, one person’s working day each: two travel and visit days plus one preparation and follow-through day for each of the two leaders. Existing paid time is reassigned; the investor charges no programme fee.', [
        ('Make the money visible', 'The investor arranges introductions without a programme fee.', 'Our chief executive approves up to €1,200 for travel and accommodation.', 'Learning budget / €1,200 cap'),
        ('Count preparation and follow-through', 'We each need two days for travel and visits, plus one for preparation and follow-through.', 'That is six person-days in total, approved by our chief executive.', 'Two people / Three days each'),
        ('Identify the work that moves', 'Our review of a potential supplier moves back one week.', 'Customer delivery dates stay the same. We have made time to learn.', 'Supplier review / One week later')]),
    ('03-separate-observation', 'Separate observation from explanation', 'At a host company, the visitors see people checking suggestions inside the screen they already use to manage stock. They record what they observed separately from the host’s explanation and from their own interpretation.', [
        ('Observe the actual workflow', 'People check suggested orders inside the screen they use to manage stock.', 'The AI suggestion is one step in their everyday work.', 'Observed / Review in workflow'),
        ('Keep the host’s explanation attributed', 'The host says reliable product records and easy corrections matter.', 'That is their explanation. We have not independently tested it.', 'Host says / Data and control'),
        ('Carry the conditions with the idea', 'Which of those conditions would matter for our customers?', 'Let us bring that question back to the team.', 'Local relevance / Still to investigate')]),
    ('04-bring-the-team-in', 'Bring the team into the learning', 'Northline’s support lead points out that the product records of Northline’s customers vary widely: some keep complete product codes and stock counts, others do not. Mira adds a question to already scheduled customer interviews. A brief case note can preserve the context for colleagues and later conversations.', [
        ('Listen to people who did not travel', 'Our support lead says our customers’ product records vary widely.', 'Then the host’s circumstances differ from our customers’.', 'Our context / Uneven customer records'),
        ('Reframe the next enquiry', 'What information and control would our customers need?', 'Ask in the customer interviews already planned.', 'Next enquiry / Customer interviews'),
        ('Make experience available to others', 'Let us write down the question, observations and missing context.', 'A shared resource gives the next person a useful starting point.', 'Case note / Context included')]),
    ('05-keep-learning', 'Keep the conversation alive', 'Back from the visit, Tomas agrees to ask the host about handling poor product records, and the team plans a learning review one month later: what did the customer interviews clarify, and does the host’s experience still help? No feature has been authorized and no saving established. A small trial version (a prototype), further enquiry or leaving the idea alone remain possible next decisions.', [
        ('Keep the relationship useful', 'Will you ask the host about handling poor product records?', 'Yes. I will offer to share what we learn, if our team agrees.', 'Peer relationship / Give and receive'),
        ('Review what the learning changed', 'At our review next month, what should we examine?', 'What the interviews clarified and which questions still deserve attention.', 'Review in one month / What to examine?'),
        ('Let evidence shape the next decision', 'We have a more grounded question and someone to keep talking with.', 'The next step may be a prototype, more enquiry or leaving the idea alone.', 'Better question / Continuing contact')])
]


# Comic page geometry (SVG user units). The page is narrow and the two speakers are
# stacked so that the dialogue stays readable when a phone shows the page 340px wide.
PAGE_W = 600
MARGIN = 24
CARD_X, CARD_W = 20, PAGE_W - 40
INNER_X, INNER_W = CARD_X + 16, CARD_W - 32
DIALOGUE, LEAD, PAD_X, PAD_Y = 24, 30, 16, 14
FIGURE_W = 80                                   # room reserved beside a bubble for the speaker
BUBBLE_W = INNER_W - FIGURE_W - 10              # 438
DIALOGUE_W = BUBBLE_W - 2 * PAD_X               # 406
ROW_H = 126                                     # a speaker figure with its name label
LABEL_W = 320


def speaker_row(y, who, words):
    """One speaker: figure on the outer side, bubble beside it with the tail toward the head."""
    lines = fit_lines(words, DIALOGUE, DIALOGUE_W)
    if len(lines) > 3:
        raise ValueError(('dialogue exceeds three lines', who, words))
    bubble_h = len(lines) * LEAD + 2 * PAD_Y
    if who == 'Mira':
        fx, bx = INNER_X + FIGURE_W / 2, INNER_X + FIGURE_W + 10
        tail = f'<path d="M{bx + 1} {y + 26} l-14 8 l14 8" fill="{IVORY}" stroke="{INK}" stroke-width="2"/>'
        color = '#86566f'
    else:
        fx, bx = INNER_X + INNER_W - FIGURE_W / 2, INNER_X
        tail = f'<path d="M{bx + BUBBLE_W - 1} {y + 26} l14 8 l-14 8" fill="{IVORY}" stroke="{INK}" stroke-width="2"/>'
        color = TEAL
    b = rect(bx, y, BUBBLE_W, bubble_h, IVORY, INK, 14, 'bubble') + tail
    b += lines_text(bx + PAD_X, y + PAD_Y + 19, lines, DIALOGUE, INK, LEAD)
    b += person(fx, y + 36, who, .55)
    b += text(fx, y + 120, who, 15, color, 700, 'middle')
    return b, max(bubble_h, ROW_H)


def comic_page(number, title, strips):
    b = text(MARGIN, 34, 'NORTHLINE · A FICTIONAL LEARNING VISIT', 15, TEAL, 700)
    title_lines = fit_lines(title, 28, PAGE_W - 2 * MARGIN, 700)
    b += lines_text(MARGIN, 72, title_lines, 28, INK, 34, 700)
    y = 72 + (len(title_lines) - 1) * 34 + 26
    for narration, mira, tomas, label in strips:
        card_top = y
        heading = fit_lines(narration, 20, INNER_W, 700)
        y += 30
        b += lines_text(INNER_X, y, heading, 20, TEAL, 26, 700)
        y += (len(heading) - 1) * 26 + 16
        for who, words in (('Mira', mira), ('Tomas', tomas)):
            row, row_h = speaker_row(y, who, words)
            b += row
            y += row_h + 8
        a, c = label.split(' / ')
        fit_lines(a, 20, LABEL_W - 24, 700)
        fit_lines(c, 18, LABEL_W - 24)
        b += rect((PAGE_W - LABEL_W) / 2, y, LABEL_W, 62, PALE, TEAL, 10, 'label')
        b += text(PAGE_W / 2, y + 26, a, 20, TEAL, 700, 'middle')
        b += text(PAGE_W / 2, y + 50, c, 18, INK, 400, 'middle')
        y += 62 + 16
        b = rect(CARD_X, card_top, CARD_W, y - card_top, WHITE, '#b4c4c0', 14, 'card') + b
        y += 14
    height = y + 30
    b += text(PAGE_W - MARGIN, height - 14, f'{number} / 5', 16, MUTED, 400, 'end')
    return b, height


def comics(check=False):
    intro = '**Comic.** Mira, Northline’s product leader, and Tomas, its engineering leader, choose a learning visit arranged by their investor and examine what they can bring home. An investor puts money into a business expecting a financial return, and it often knows people across the businesses it has funded. Northline is fictional: it makes inventory software, which tracks the goods a business holds in stock, for small wholesalers, businesses that buy goods in quantity and sell them on to shops. The team is considering reorder suggestions from artificial intelligence (AI), software that learns from past sales and stock levels to recommend what to buy again and how much. This example is independent of the book’s Larkspur budget and calendar; every amount and time allowance below is illustrative.\n\n'
    docs = [intro]
    for number, (identifier, title, caption, strips) in enumerate(PAGES, 1):
        if check:
            print(f'--- page {number}: {title}')
            for narration, mira, tomas, label in strips:
                for who, words in (('Mira', mira), ('Tomas', tomas)):
                    for row in fit_lines(words, DIALOGUE, DIALOGUE_W):
                        print(f'  {who:5} {measure(row, DIALOGUE):6.1f}/{DIALOGUE_W / FALLBACK_ALLOWANCE:.0f}  {row}')
            continue
        body, height = comic_page(number, title, strips)
        transcript = [f'- *Strip {n}.* **Mira:** “{mira}” **Tomas:** “{tomas}”' for n, (_, mira, tomas, _) in enumerate(strips, 1)]
        record_strips = [{'scene': narration, 'labels': label.split(' / '), 'bubbles': [{'who': 'Mira', 'text': mira}, {'who': 'Tomas', 'text': tomas}]}
                         for narration, mira, tomas, label in strips]
        filename = f'comic-page-{identifier}.svg'
        alt = f'Three-strip comic: {title.lower()}. ' + ' '.join(s[0] + '.' for s in strips)
        write(filename, PAGE_W, height, title, alt, body)
        from math import gcd
        g = gcd(PAGE_W, height)
        record = {'id': identifier, 'title': title, 'asset': f'assets/images/{SLUG}/{filename}', 'aspect_ratio': f'{PAGE_W // g}:{height // g}', 'cast': ['Mira', 'Tomas'], 'strips': record_strips, 'alt': alt, 'caption': caption, 'status': 'generated', 'generation': {'tool': 'locally authored SVG', 'source': '_research/render-investor-learning-20260922.py'}}
        docs.append('<!-- comic-page\n' + json.dumps(record, ensure_ascii=False, indent=2) + '\n-->\n\n')
        docs.append(f'![{alt}]({record["asset"]})\n\n**Page {number}: {title}.** {caption}\n\n' + '\n'.join(transcript) + '\n\n')
        if number == 4:
            docs.append('The author’s [CTO Starter Kit](https://ctostarter.com/start/index.html) collects guidance for chief technology officers (CTOs), the executives responsible for a company’s technology. Its [repository](https://github.com/zeljkoobrenovic/cto-starter-kit) of public project files shows one way to organize guidance and routes to peers. An investor community could adapt that approach; no investor adoption is claimed.\n\n')
    if check:
        return
    docs.append('Use the [learning brief in Tool 14](toolkit.html#tool-14) to carry questions, observations, context and follow-through between conversations. The article also examines seminars, summits, conferences and continuing peer communities, with documented examples and their sources.\n')
    (POST / 'comics.md').write_text(''.join(docs))


def part_overview():
    """Part IV chapter overview: one stacked column so it stays readable inline on a phone.

    Revised 23 September 2026 (Part IV in-depth review round 1, PART4-001/003): the
    earlier three-column 1000-unit layout showed its 24-unit descriptions at about
    8 pixels when the image was 342 pixels wide. The column is 600 units wide, so the
    same description size shows at about 13.7 pixels and headings at about 16.
    Box descriptions say what each chapter does in ordinary words; the last box no
    longer describes operating partners as "the wider function".

    Revised again on 23 September 2026 (round 2, PART4-001): the "Choose help" and
    "Set the terms" boxes say what is missing (work your team cannot yet do) and
    what changes hands (who takes the work over afterwards) instead of "one gap"
    and "the handover", so the diagram reads on its own.
    """
    W, BOX_X, BOX_W, BOX_H, GAP = 600, 40, 520, 122, 40
    HEAD, DESC = 28, 24
    boxes = [('Plan support', 'Agree how the investor and company will work together'),
             ('Learn together', 'Use the investor’s network and peers to learn'),
             ('Choose help', 'Compare sources of help for work your team cannot yet do'),
             ('Set the terms', 'Agree the work, its cost and who takes it over afterwards'),
             ('Clarify the adviser', 'Know what the investor’s adviser is asked to do'),
             ('Operating partners', 'Meet the investor’s specialists who help its companies')]
    b = text(BOX_X, 52, 'COLLABORATE', 22, TEAL, 700)
    b += lines_text(BOX_X, 96, ['Use the investor', 'relationship well'], 32, INK, 40, 700)  # balanced two-line title
    y = 150
    for i, (title, desc) in enumerate(boxes):
        b += rect(BOX_X, y, BOX_W, BOX_H, PALE if i == 1 else WHITE)
        b += lines_text(BOX_X + 20, y + 42, fit_lines(title, HEAD, BOX_W - 40, 700), HEAD, INK, 34, 700)
        b += lines_text(BOX_X + 20, y + 80, fit_lines(desc, DESC, BOX_W - 40), DESC, MUTED, 30)
        if i < len(boxes) - 1:
            b += arrow(W // 2, y + BOX_H + 6, W // 2, y + BOX_H + GAP - 8)
        y += BOX_H + GAP
    footer = fit_lines('Learning and support, with company judgment and responsibility.', 24, BOX_W)
    b += lines_text(W // 2, y + 14, footer, 24, INK, 32, 400, 'middle')
    height = y + 14 + 32 * len(footer) + 10
    out = JOURNAL / 'posts/part-3-intro/assets/images/part-3-intro/chapter-overview-six.svg'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg(W, height, 'Six choices for useful collaboration',
                       'Six chapters stacked in reading order: plan support, learn together, choose help for work your team cannot yet do, set the terms including who takes the work over afterwards, clarify the adviser and meet the operating partners; learning and support come with company judgment and responsibility.', b))
    return out, height


if __name__ == '__main__':
    import sys
    if 'part-overview' in sys.argv[1:]:
        out, height = part_overview()
        print(f'Wrote Part IV overview (600 x {height}): {out}')
    elif 'comics' in sys.argv[1:]:
        comics(check='--check' in sys.argv[1:])
        if '--check' not in sys.argv[1:]:
            print(f'Wrote five comic pages and comics.md: {POST}')
    else:
        figures()
        comics()
        part_overview()
        print(f'Wrote chapter figures, logo, icon, five comic pages and Part IV overview: {POST}')
