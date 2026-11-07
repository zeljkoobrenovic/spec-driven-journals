"""Merge the WHY THE BUSINESS CARES and WHY ARCHITECTS SHOULD CARE callouts into one WHY IT MATTERS callout,
and move KEY POINTS directly after the IN THIS ... YOU WILL opener. Usage: python3 merge_why.py <index.md> ..."""
import re, sys
for path in sys.argv[1:]:
    s = open(path).read()
    orig = s
    m_open = re.search(r'> \*\*IN THIS (?:CHAPTER|SECTION|PART|APPENDIX), YOU WILL:\*\*[^\n]*\n', s)
    m_biz = re.search(r'> \*\*WHY THE BUSINESS CARES:\*\* ?([^\n]*)\n', s)
    m_arc = re.search(r'> \*\*WHY ARCHITECTS SHOULD CARE:\*\* ?([^\n]*)\n', s)
    m_kp = re.search(r'> \*\*KEY POINTS:\*\*\n(?:>[^\n]*\n)+', s)
    if not (m_open and m_kp):
        print('skip (no opener/key points)', path); continue
    if m_biz and m_arc:
        merged = '> **WHY IT MATTERS:** ' + m_biz.group(1).strip() + ' ' + m_arc.group(1).strip() + '\n'
        # remove both callouts (and the blank line after each)
        for m in sorted([m_biz, m_arc], key=lambda m: -m.start()):
            end = m.end()
            if s[end:end+1] == '\n': end += 1
            s = s[:m.start()] + s[end:]
    else:
        merged = None
    # re-locate opener and key points after removals
    m_open = re.search(r'> \*\*IN THIS (?:CHAPTER|SECTION|PART|APPENDIX), YOU WILL:\*\*[^\n]*\n', s)
    m_kp = re.search(r'> \*\*KEY POINTS:\*\*\n(?:>[^\n]*\n)+', s)
    kp = m_kp.group(0)
    end = m_kp.end()
    if s[end:end+1] == '\n': end += 1
    s = s[:m_kp.start()] + s[end:]
    m_open = re.search(r'> \*\*IN THIS (?:CHAPTER|SECTION|PART|APPENDIX), YOU WILL:\*\*[^\n]*\n', s)
    insert = kp + '\n' + (merged + '\n' if merged else '')
    s = s[:m_open.end()] + '\n' + insert + s[m_open.end():].lstrip('\n')
    if s != orig:
        open(path, 'w').write(s); print('merged', path)
    else:
        print('unchanged', path)
