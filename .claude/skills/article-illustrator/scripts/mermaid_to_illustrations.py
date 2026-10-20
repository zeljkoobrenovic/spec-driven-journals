#!/usr/bin/env python3
"""Replace a post's mermaid diagrams with generated illustrations, in two steps.

Usage from the repository root:

    # 0. Build the site, then screenshot the rendered diagrams as layout references.
    python3.11 snapshot_mermaid.py <journal> <refs-dir>

    # 1. Stage: put an illustration-placeholder before every mermaid block. The
    #    prompt asks the model to restyle the reference image and lists the
    #    diagram's boxes, arrows and labels as a checklist; the mermaid block
    #    stays, so the page still renders. Sources are archived to JSON.
    python3 mermaid_to_illustrations.py stage <index.md> [...] --refs <refs-dir> --archive <file.json>

    # 2. Generate the images with generate_illustrations_nanobanana.py (no --replace),
    #    inspect every one against its diagram, then:
    python3 mermaid_to_illustrations.py finalize <index.md> [...]

finalize swaps each placeholder plus the mermaid block after it for a markdown
image, leaving the existing **Figure N:** caption in place, so figure numbers
and prose references do not change. A placeholder whose image file is missing
is left alone, with its mermaid block.
"""

import json
import re
import sys
from pathlib import Path

BLOCK = re.compile(r"^---begin mermaid---\n(?P<src>.*?)\n---end mermaid---\n", re.M | re.S)
STAGED = re.compile(
    r"^<!-- illustration-placeholder\n(?P<json>\{.*?\})\n-->\n(?P<block>---begin mermaid---\n.*?\n---end mermaid---\n)",
    re.M | re.S,
)
CAPTION = re.compile(r"\A\s*\*\*Figure (\d+):?\*\*\s*\*?(.*?)\*?\s*$", re.M)
ARROW = re.compile(r"\s*(?:<?[-=.]{2,}[>x]{1,2}|<?-[-.]*>{1,2}|-->>|->>|-[x)])\s*")
SKIP_LINE = re.compile(r"^\s*(classDef|class |style |linkStyle|%%|accTitle|accDescr)")

STYLE = (
    "Style: polished business explainer diagram for a book on marketplace platform architecture; "
    "flat vector, crisp outlines, minimal shading, light off-white background, disciplined blue, "
    "teal, green and orange accents, rounded boxes, small simple icons beside labels where they help, "
    "generous margins, clean alignment."
)
KINDS = {
    "flowchart": "boxes connected by arrows; arrow labels sit on their arrows; each subgraph is a labeled panel around its boxes",
    "graph": "boxes connected by arrows; arrow labels sit on their arrows; each subgraph is a labeled panel around its boxes",
    "sequenceDiagram": "a sequence diagram: participants as labeled columns with a small icon at the top, messages as horizontal arrows "
                       "in top-to-bottom order with their labels, notes as small callouts, alt/opt/loop/par blocks as framed regions with their label",
    "stateDiagram-v2": "a state diagram: states as rounded boxes, transitions as arrows labeled with their event, [*] as a filled start dot "
                       "or a ringed end dot, composite states as labeled panels; split CamelCase state names into words (UnderReview becomes Under review)",
}
DIRECTIONS = {"LR": "left to right", "RL": "right to left", "TB": "top to bottom", "TD": "top to bottom", "BT": "bottom to top"}
RULES = (
    "Text rules: print every label exactly as given, spelled correctly, with the same numbers, units, currencies and dates; "
    "replace <br/> with a line break; do not add any other words, numbers, legends, title, figure number or caption; "
    "never print Mermaid syntax (node ids, brackets, keywords such as subgraph or participant). "
    "No photorealism, no 3D render, no faces, no brand logos or trademarks."
)


def slug(text, words=6):
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    stop = {"the", "a", "an", "of", "and", "to", "in", "on", "for", "is", "its", "by", "with", "at", "as", "from"}
    return "-".join([t for t in tokens if t not in stop][:words]) or "diagram"


LINK = re.compile(r"\s*(<-->|-\.->|-\.-x|-\.-|--x|-->|---|==>)\s*(?:\|\s*\"?(.*?)\"?\s*\|)?\s*")
NODE = re.compile(r"^\s*([A-Za-z_][\w-]*)\s*(?:(\[\[|\[\(|\(\[|\(\(|\{\{|\[|\(|\{)\s*\"?(.*?)\"?\s*(\]\]|\)\]|\]\)|\)\)|\}\}|\]|\)|\}))?\s*(?::::\w+)?\s*$")
CLEAN = re.compile(r"<br\s*/?>", re.I)


def label(text):
    return CLEAN.sub(" / ", text).replace("#quot;", "'").strip()


def flowchart_spec(lines):
    """Nodes, panels and arrows of a flowchart, as an explicit list for the image model."""
    nodes, order, panels, stack, edges, panel_ids = {}, [], [], [], [], {}

    def node(token):
        m = NODE.match(token)
        if not m:
            raise ValueError(f"cannot parse node {token!r}")
        ident, shape, text = m.group(1), m.group(2), m.group(3)
        if ident not in nodes:
            nodes[ident] = {"label": ident, "panel": stack[-1] if stack else None, "decision": False}
            order.append(ident)
        if text:
            nodes[ident]["label"] = label(text)
            nodes[ident]["decision"] = shape == "{"
            if stack and not nodes[ident]["panel"]:
                nodes[ident]["panel"] = stack[-1]
        return ident

    for line in lines[1:]:
        t = line.strip()
        if t.startswith("subgraph"):
            m = re.match(r'subgraph\s+([\w-]+)?\s*(?:\[\s*"?(.*?)"?\s*\])?\s*$', t)
            name = label(m.group(2) or m.group(1)) if m else label(t[8:].strip(' "'))
            panels.append((name, stack[-1] if stack else None))
            if m and m.group(1):
                panel_ids[m.group(1)] = name
            stack.append(name)
            continue
        if t == "end":
            stack.pop()
            continue
        if t.startswith("direction "):
            continue
        parts = LINK.split(t)
        # parts: node, arrow, label, node, arrow, label, node ...
        groups = [[node(x.strip()) for x in re.split(r"\s+&\s+", parts[0])]]
        for i in range(1, len(parts), 3):
            arrow, text, right = parts[i], parts[i + 1], parts[i + 2]
            targets = [node(x.strip()) for x in re.split(r"\s+&\s+", right)]
            for a in groups[-1]:
                for b in targets:
                    edges.append((a, b, label(text or ""), arrow))
            groups.append(targets)
    out = []
    if panels:
        out.append("Panels (draw only these, each as a labeled frame; no other panels or headings):")
        out += [f'- "{n}"' + (f' (inside "{parent}")' if parent else "") for n, parent in panels]
    out.append("Boxes (draw each exactly once" + (", inside its panel" if panels else "") + "):")
    def name(i):
        return f'the "{panel_ids[i]}" panel' if i in panel_ids else f'"{nodes[i]["label"]}"'

    for i in order:
        if i in panel_ids:
            continue
        n = nodes[i]
        out.append(f'- "{n["label"]}"' + (" (a decision diamond)" if n["decision"] else "") +
                   (f' in panel "{n["panel"]}"' if n["panel"] else ""))
    out.append(f"Arrows (draw exactly these {len(edges)}, each pointing from the first item to the second; no others):")
    for a, b, text, arrow in edges:
        kind = {"-.->": ", dashed", "-.-": ", dashed line with no arrowhead", "---": ", plain line with no arrowhead",
                "<-->": ", arrowheads at both ends", "--x": ", ending in a cross instead of an arrowhead (blocked)",
                "-.-x": ", dashed, ending in a cross instead of an arrowhead (blocked)", "==>": ", thick"}.get(arrow, "")
        out.append(f'- {name(a)} → {name(b)}' + (f', labeled "{text}"' if text else "") + kind)
    return "\n".join(out)


def state_spec(lines):
    """States and transitions of a state diagram, as an explicit list."""
    names, order, edges, notes = {}, [], [], []

    def state(ident, where):
        if ident == "[*]":
            return "(the start dot)" if where == "from" else "(the end dot)"
        if ident not in names:
            names[ident] = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", ident).capitalize() if ident.isidentifier() else ident
            order.append(ident)
        return ident

    for line in lines[1:]:
        t = line.strip()
        m = re.match(r'state\s+"(.*?)"\s+as\s+(\w+)', t)
        if m:
            names[m.group(2)] = label(m.group(1)); order.append(m.group(2)); continue
        m = re.match(r"(\S+)\s*-->\s*(\S+?)\s*(?::\s*(.*))?$", t)
        if m:
            edges.append((state(m.group(1), "from"), state(m.group(2), "to"), label(m.group(3) or "")))
            continue
        m = re.match(r"note\s+(?:left|right)\s+of\s+(\w+)\s*:\s*(.*)", t)
        if m:
            notes.append((m.group(1), label(m.group(2)))); continue
        if t.startswith(("direction", "}", "state ")) or not t:
            continue
        m = re.match(r"(\w+)\s*:\s*(.*)", t)
        if m:
            state(m.group(1), "")
            names[m.group(1)] = label(m.group(2)); continue
        raise ValueError(f"cannot parse state line {t!r}")
    out = ["States (draw each exactly once, as a rounded box with this name):"]
    out += [f'- "{names[i]}"' for i in dict.fromkeys(order)]
    out.append(f"Transitions (draw exactly these {len(edges)} arrows; the start dot is one small filled circle and the end dot "
               "one ringed circle, both drawn without any text beside them):")
    for a, b, text in edges:
        out.append(f'- {names.get(a, a) if a in names else a} → {names.get(b, b) if b in names else b}'
                   + (f', labeled "{text}"' if text else ""))
    for who, text in notes:
        out.append(f'Note beside "{names.get(who, who)}": "{text}"')
    return "\n".join(out)


def describe(src):
    lines = [l for l in src.splitlines() if l.strip() and not SKIP_LINE.match(l)]
    head = lines[0].split()
    kind = head[0]
    direction = DIRECTIONS.get(head[1], "") if len(head) > 1 else ""
    try:
        if kind in ("flowchart", "graph"):
            return kind, direction, flowchart_spec(lines)
        if kind == "stateDiagram-v2":
            return kind, direction, state_spec(lines)
    except (ValueError, IndexError, AttributeError) as exc:
        print(f"  note: falling back to raw source ({exc})")
    body = "\n".join(ARROW.sub(" → ", l) for l in lines)
    return kind, direction, body.replace("-->", "→")


RATIOS = {"1:1": 1, "4:3": 4 / 3, "3:2": 1.5, "16:9": 16 / 9, "21:9": 21 / 9, "3:4": 0.75, "2:3": 2 / 3, "9:16": 9 / 16}


def png_ratio(png):
    """Nearest supported aspect ratio for a PNG, read from its header."""
    data = png.read_bytes()[16:24]
    w, h = int.from_bytes(data[:4], "big"), int.from_bytes(data[4:], "big")
    return min(RATIOS, key=lambda r: abs(RATIOS[r] - w / h))


def stage(path, archive, refs=None):
    text = path.read_text(encoding="utf-8")
    folder = path.parent.name
    out, pos, used = [], 0, set()
    for k, m in enumerate(BLOCK.finditer(text), 1):
        if text[:m.start()].endswith("-->\n"):
            continue  # already staged
        cap = CAPTION.match(text[m.end():m.end() + 1200])
        if not cap:
            print(f"SKIP {path}: mermaid block at offset {m.start()} has no Figure caption after it")
            continue
        number, caption = int(cap.group(1)), cap.group(2).strip()
        kind, direction, body = describe(m.group("src"))
        ident = f"fig{number:02d}-{slug(caption)}"
        while ident in used:
            ident += "-b"
        used.add(ident)
        tall = kind == "sequenceDiagram" or (direction in ("top to bottom", "bottom to top") and body.count("\n") > 14)
        ref = (refs / folder / f"{k}.png").resolve() if refs else None
        if ref and not ref.exists():
            print(f"  note: no reference image {ref}; prompting from text only")
            ref = None
        listed = not body.lstrip().startswith(kind)
        if ref:
            prompt = " ".join([
                "The attached image is a correct but plain rendering of a diagram. Redraw it as one polished, professional illustration.",
                f"It must show: {caption}",
                "Keep its structure exactly: the same boxes, panels, arrows, arrow directions, dashed or solid lines and labels, "
                "in the same relative positions, with the same text spelled identically. Do not add, remove, merge or duplicate any box, "
                "panel, arrow or label. Improve only the visual style; you may add a small icon inside a box.",
                "Checklist of what the attached diagram contains:" if listed else "Its source, for reference:",
                "\n" + body + "\n",
                STYLE, RULES,
            ])
        else:
            prompt = " ".join([
                "Redraw the diagram below as one clear, professional illustration.",
                f"It must show: {caption}",
                f"Draw it as {KINDS.get(kind, KINDS['flowchart'])}" + (f", laid out {direction}." if direction else "."),
                ("Content: draw exactly what is listed below and nothing else; text in quotes is the exact label to print."
                 if listed else
                 "Content, in Mermaid notation with arrows written as →: reproduce every participant, message, note and block, "
                 "in the same order; text after a colon or in quotes is the exact label to print."),
                "\n" + body + "\n",
                STYLE, RULES,
            ])
        item = {
            "id": ident,
            "status": "pending",
            "asset": f"assets/images/{folder}/{ident}.jpeg",
            "aspect_ratio": png_ratio(ref) if ref else ("4:3" if tall else "16:9"),
            "image_size": "2K",
            "placement": f"replaces the mermaid diagram of Figure {number}",
            "visual_goal": caption,
            "prompt": prompt.replace("-->", "→"),
            **({"reference_image": str(ref)} if ref else {}),
            "alt": "Diagram: " + re.split(r"(?<=[.;:])\s", caption, maxsplit=1)[0].rstrip(".;:"),
            "caption": caption,
        }
        archive.append({"post": folder, "figure": number, "id": ident, "asset": item["asset"], "mermaid": m.group("src")})
        out.append(text[pos:m.start()])
        out.append("<!-- illustration-placeholder\n" + json.dumps(item, indent=2, ensure_ascii=False) + "\n-->\n")
        pos = m.start()
    out.append(text[pos:])
    path.write_text("".join(out), encoding="utf-8")


def finalize(path):
    text = path.read_text(encoding="utf-8")
    done = 0

    def swap(m):
        nonlocal done
        item = json.loads(m.group("json"))
        if not (path.parent / item["asset"]).exists():
            print(f"KEEP {path.parent.name}/{item['id']}: no image yet")
            return m.group(0)
        done += 1
        return f"![{item['alt']}]({item['asset']})\n"

    new = STAGED.sub(swap, text)
    # The caption must follow its image directly.
    new = re.sub(r"(^!\[[^\n]*\]\([^)\n]*\)\n)\n+(\*\*Figure \d+)", r"\1\2", new, flags=re.M)
    path.write_text(new, encoding="utf-8")
    print(f"{path.parent.name}: {done} diagram(s) replaced")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("stage", "finalize"):
        sys.exit(__doc__)
    args = sys.argv[2:]
    archive_path = refs = None
    if "--refs" in args:
        i = args.index("--refs")
        refs = Path(args[i + 1])
        args = args[:i] + args[i + 2:]
    if "--archive" in args:
        i = args.index("--archive")
        archive_path = Path(args[i + 1])
        args = args[:i] + args[i + 2:]
    if sys.argv[1] == "stage":
        archive = json.loads(archive_path.read_text()) if archive_path and archive_path.exists() else []
        for p in args:
            stage(Path(p), archive, refs)
        if archive_path:
            archive_path.write_text(json.dumps(archive, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"staged; archive holds {len(archive)} diagram(s)")
    else:
        for p in args:
            finalize(Path(p))


if __name__ == "__main__":
    main()
