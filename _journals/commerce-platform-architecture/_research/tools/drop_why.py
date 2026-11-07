"""Remove the '> **WHY IT MATTERS:** ...' callout (and the blank line after it) from pages. Usage: python3 drop_why.py <index.md> ..."""
import re, sys
for p in sys.argv[1:]:
    s = open(p).read()
    n = re.sub(r'(?m)^> \*\*WHY IT MATTERS:\*\*[^\n]*\n(?:>[^\n]*\n)*\n?', '', s)
    if n != s:
        open(p, 'w').write(n); print('dropped', p)
