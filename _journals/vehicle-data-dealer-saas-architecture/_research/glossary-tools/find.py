import re,sys,glob
pairs=[l.split('|') for l in sys.stdin.read().strip().split('\n')]
for d,term in pairs:
    f=glob.glob(d+'*/index.md')[0]
    t=open(f).read().split('## Sources and Evidence')[0]
    sents=[s for para in t.split('\n') if not para.startswith(('>','#')) for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*])',para)]
    hits=[s for s in sents if re.search(r'\*\*[^*]*'+re.escape(term)+r'[^*]*\*\*',s,re.I)]
    if not hits: hits=[s for s in sents if term.lower() in s.lower()]
    print('##',term,'@',d,len(hits))
    for h in hits[:2]: print('   ',h.strip()[:450])
