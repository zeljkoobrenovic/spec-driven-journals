import re,sys,glob,os
root=sys.argv[1]
yaml=open(os.path.join(root,'config.yaml')).read()
posts=re.findall(r'- (\S+)/index.md',yaml)
DEF=re.compile(r'(\*\*[^*]{2,80}\*\*)[^.]{0,40}?\b(is|are|means|refers to|is the|was)\b')
for p in posts:
    f=os.path.join(root,'posts',p,'index.md')
    if not os.path.exists(f): continue
    t=open(f).read()
    pm=re.search(r'^permalink:\s*(\S+)',t,re.M).group(1)
    body=t.split('## Sources and Evidence')[0]
    # remove callouts
    out=[]
    seen=set()
    for para in body.split('\n'):
        if para.startswith('>') or para.startswith('#'): continue
        # split sentences
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*])',para):
            ok=False
            m=re.match(r'^\s*(?:[-*]\s+|\|\s*)?(?:An?\s+|The\s+)?\*\*([^*]{2,80})\*\*',s)
            if m and (re.search(r'\*\*\s*(\([^)]*\)\s*)?(is|are|means|refers|—|:|\|)',s[:len(m.group(0))+60]) or s.lstrip().startswith(('-','|'))): ok=True
            if not ok and re.search(r'\b(is|are|means)\b[^.]{0,30}\*\*',s[:80]) : ok=False
            if not ok and re.search(r'\bcalls? (this|it|that)[^.]{0,20}\*\*|\bthis book calls\b|\bthe book calls\b|\bthis chapter calls\b',s): ok=True
            if ok:
                k=s[:60]
                if k in seen: continue
                seen.add(k)
                out.append(s.strip()[:420])
    print('=====',pm,len(out))
    for o in out: print('  ',o)
