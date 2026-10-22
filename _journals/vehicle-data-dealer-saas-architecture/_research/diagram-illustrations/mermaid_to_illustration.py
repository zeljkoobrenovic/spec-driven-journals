"""Replace a page's mermaid diagrams (and their captions) with illustration placeholders.

Usage: python3 mermaid_to_illustration.py <abs index.md> <figures.json>
       python3 mermaid_to_illustration.py --update <abs index.md> <figures.json>
         (rewrites prompt/alt/visual_goal/aspect of still-pending placeholders by id,
          after you improve a prompt for a regeneration)

figures.json is a list, in document order, with one entry per mermaid block:
  {"id": "kebab-id", "prompt": "...scene and labels...", "alt": "...",
   "visual_goal": "...", "aspect_ratio": "16:9"}            # aspect optional
The existing caption text is kept verbatim as the placeholder caption.
The shared style suffix is appended to every prompt.
"""
import json
import pathlib
import re
import sys

STYLE = (
    " Style: polished business explainer diagram drawn as an illustration, flat vector style, crisp outlines, "
    "minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins, "
    "clear visual hierarchy and arrows that are easy to follow. Every label must be spelled exactly as given in "
    "quotes above; draw no other words, no extra labels, no numbers that were not given. No photorealism, no 3D "
    "render, no dense text, no title text. Draw no logos, emblems, badges or brand marks anywhere and no car-maker, "
    "vendor, portal or marketplace names; cars are generic unbranded hatchbacks, sedans or vans with no grille badge "
    "and no readable number plate unless a plate label is given; show dealer management systems, portals, registers, "
    "data suppliers and payment providers as generic unbranded components; never draw payment cards or card-network "
    "symbols. People, if shown, are unlabeled generic figures; never write a label under a person."
)

CAPTION = re.compile(r"^\*\*Figure \d+:\*\* \*(.*)\*\s*$")


def main(index_path: str, spec_path: str) -> None:
    path = pathlib.Path(index_path)
    slug = path.parent.name
    figures = json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8"))
    lines = path.read_text(encoding="utf-8").split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        if lines[i] != "---begin mermaid---":
            out.append(lines[i])
            i += 1
            continue
        end = lines.index("---end mermaid---", i)
        j = end + 1
        if lines[j] == "":
            j += 1
        m = CAPTION.match(lines[j])
        if not m:
            sys.exit(f"{path}: no caption after mermaid block at line {i + 1}")
        if n >= len(figures):
            sys.exit(f"{path}: more mermaid blocks than figure entries")
        f = figures[n]
        n += 1
        ph = {
            "id": f["id"],
            "status": "pending",
            "asset": f"assets/images/{slug}/{f['id']}.jpeg",
            "aspect_ratio": f.get("aspect_ratio", "16:9"),
            "placement": "replaces the mermaid diagram at this position",
            "visual_goal": f["visual_goal"],
            "prompt": f["prompt"].rstrip() + STYLE,
            "alt": f["alt"],
            "caption": m.group(1),
        }
        body = json.dumps(ph, ensure_ascii=False, indent=2)
        if "-->" in body:
            sys.exit(f"{path}: '-->' inside placeholder {f['id']}")
        out.append("<!-- illustration-placeholder")
        out.extend(body.split("\n"))
        out.append("-->")
        i = j + 1
    if n != len(figures):
        sys.exit(f"{path}: {n} mermaid blocks but {len(figures)} figure entries")
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"{path.parent.name}: replaced {n} mermaid blocks with placeholders")


PH = re.compile(r"<!-- illustration-placeholder\n(.*?)\n-->", re.S)


def update(index_path: str, spec_path: str) -> None:
    path = pathlib.Path(index_path)
    figures = {f["id"]: f for f in json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8"))}
    done = []

    def repl(m):
        ph = json.loads(m.group(1))
        f = figures.get(ph["id"])
        if not f:
            return m.group(0)
        ph.update(prompt=f["prompt"].rstrip() + STYLE, alt=f["alt"], visual_goal=f["visual_goal"],
                  aspect_ratio=f.get("aspect_ratio", "16:9"))
        done.append(ph["id"])
        return "<!-- illustration-placeholder\n" + json.dumps(ph, ensure_ascii=False, indent=2) + "\n-->"

    path.write_text(PH.sub(repl, path.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"{path.parent.name}: updated {done}")


if __name__ == "__main__":
    if sys.argv[1] == "--update":
        update(sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1], sys.argv[2])
