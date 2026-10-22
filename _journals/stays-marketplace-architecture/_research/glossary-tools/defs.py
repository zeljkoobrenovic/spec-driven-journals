import re,sys,glob
ROOT='/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/posts/'
for folder in sys.argv[1:]:
    t=open(glob.glob(ROOT+folder+'*/index.md')[0]).read()
    t=t.split('## Sources and Evidence')[0]
    print('#####',folder)
    seen=set()
    # split into sentences
    for para in t.split('\n'):
        if para.startswith(('>','|','**Figure','---','![')) : continue
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*])',para):
            for m in re.finditer(r'\*\*([^*]{3,60})\*\*',s):
                term=m.group(1).strip().rstrip('.:')
                k=term.lower()
                if k in seen: continue
                # definitional heuristics
                if re.search(r'\b(is|are|means|mean|=|:|—|,)\b|—|:',s[m.end():m.end()+40]) or s.startswith('**'):
                    seen.add(k)
                    print('-',s.strip()[:330])
