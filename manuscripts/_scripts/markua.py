"""Small, dependency-free helpers shared by the journal exporter and validator."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator


class ExportError(ValueError):
    """An input cannot be exported without losing content or breaking a link."""


def within(root: Path, relative: str) -> Path:
    """Resolve a relative file name without permitting traversal or symlink escapes."""
    path = (root / relative).resolve()
    if Path(relative).is_absolute() or not path.is_relative_to(root.resolve()):
        raise ExportError(f"Path escapes {root}: {relative}")
    return path


def map_prose(text: str, transform: Callable[[str], str], *, inline: bool = True) -> str:
    """Apply a transformation outside fenced code blocks and inline code spans."""
    saved: list[str] = []

    def save(value: str) -> str:
        saved.append(value)
        return f"\x00LITERAL{len(saved) - 1}\x00"

    lines = text.splitlines(keepends=True)
    masked: list[str] = []
    i = 0
    while i < len(lines):
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", lines[i])
        if not opening:
            masked.append(lines[i])
            i += 1
            continue
        fence = opening[1]
        start = i
        i += 1
        while i < len(lines):
            closing = re.fullmatch(r" {0,3}" + re.escape(fence[0]) +
                                   "{" + str(len(fence)) + r",}[ \t]*\n?", lines[i])
            i += 1
            if closing:
                break
        masked.append(save("".join(lines[start:i])) + "\n")
    prose = "".join(masked)
    if inline:
        prose = re.sub(r"(`+)(?!`)(.*?)(?<!`)\1(?!`)",
                       lambda match: save(match[0]), prose, flags=re.S)
    result = transform(prose)
    # A fenced block already contains its terminating newline.
    result = re.sub(r"\x00LITERAL(\d+)\x00\n?", lambda match:
                    saved[int(match[1])] + ("\n" if match[0].endswith("\n")
                    and not saved[int(match[1])].endswith("\n") else ""), result)
    return result


@dataclass
class Link:
    start: int
    end: int
    image: bool
    label: str
    destination: str
    suffix: str

    def render(self, destination: str) -> str:
        return f"{'!' if self.image else ''}[{self.label}]({destination}{self.suffix})"


def links(text: str) -> Iterator[Link]:
    """Read inline Markdown links, including balanced URL parentheses and titles."""
    opening = re.compile(r"(?<![\\!])(!?)\[((?:\\.|[^\[\]\n]|\[[^\]\n]*\])*)\]\(")
    pos = 0
    while match := opening.search(text, pos):
        cursor = match.end()
        while cursor < len(text) and text[cursor] in " \t":
            cursor += 1
        start = cursor
        if cursor < len(text) and text[cursor] == "<":
            end = text.find(">", cursor + 1)
            if end < 0:
                pos = cursor
                continue
            destination = text[cursor + 1:end]
            cursor = end + 1
        else:
            depth = 0
            while cursor < len(text):
                char = text[cursor]
                if char == "\\":
                    cursor += 2
                    continue
                if depth == 0 and (char == ")" or char.isspace()):
                    break
                if char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                cursor += 1
            destination = text[start:cursor]
        suffix_start = cursor
        while cursor < len(text) and text[cursor] in " \t":
            cursor += 1
        if cursor < len(text) and text[cursor] in "\"'":
            quote = text[cursor]
            cursor += 1
            while cursor < len(text) and text[cursor] != quote:
                cursor += 2 if text[cursor] == "\\" else 1
            cursor += 1
            while cursor < len(text) and text[cursor] in " \t":
                cursor += 1
        if cursor < len(text) and text[cursor] == ")":
            yield Link(match.start(), cursor + 1, bool(match[1]), match[2],
                       destination, text[suffix_start:cursor])
            pos = cursor + 1
        else:
            pos = match.end()


def rewrite_links(text: str, transform: Callable[[Link], str]) -> str:
    output: list[str] = []
    previous = 0
    for link in links(text):
        output.extend((text[previous:link.start], transform(link)))
        previous = link.end
    output.append(text[previous:])
    return "".join(output)
