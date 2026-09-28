#!/usr/bin/env python3
"""Record the 28 Sept 2026 summary rewrite in a post's spec.md: add one Success-criteria bullet
(which supersedes older summary-specific coverage requirements), bump `revised:` and add a Changelog line.
Usage: python3 spec-note-summary-20260928.py <post-folder> [...]. Idempotent."""
import re, sys
from pathlib import Path
J = Path(__file__).resolve().parents[1]
CRIT = ('- **Summary (2026-09-28, supersedes earlier summary-specific coverage requirements above):** the TL;DR is a '
        'fluent, conversational read of 300–500 words that follows one logical line — the question, the key insight, '
        'one worked example, the decision or practice, and a transition to the next chapter. It covers the key points '
        'and examples, not every detail of the article; terms are explained in plain words only where the summary '
        'needs them. Its overview figure is detailed enough that a reader grasps the key concepts from it alone.')
LOG = ('- 2026-09-28: Summary rewritten as a fluent, conversational read of the key points and one worked example, '
       'with needless words removed and a more detailed overview figure; added the Summary criterion, which '
       'supersedes earlier summary-specific coverage requirements.')
for post in sys.argv[1:]:
    p = J / 'posts' / post / 'spec.md'
    t = p.read_text()
    if '2026-09-28, supersedes earlier summary' in t:
        print('[skip]', post); continue
    t = re.sub(r'^revised: .*$', 'revised: 2026-09-28', t, count=1, flags=re.M)
    m = re.search(r'^## Success criteria\n(.*?)(?=^## )', t, flags=re.M | re.S)
    assert m, post
    body = m.group(1).rstrip('\n') + '\n' + CRIT + '\n\n'
    t = t[:m.start(1)] + body + t[m.end(1):]
    m = re.search(r'^## Changelog\n\n?', t, flags=re.M)
    assert m, post
    t = t[:m.end()] + LOG + '\n' + t[m.end():]
    p.write_text(t)
    print('[spec]', post)
