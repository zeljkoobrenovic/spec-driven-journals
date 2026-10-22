import re,sys,os
root=sys.argv[1]
yaml=open(os.path.join(root,'config.yaml')).read()
posts=re.findall(r'- (\S+)/index.md',yaml)
skip={'meet-axleby','toolkit','domain-coverage','introduction','where-vehicle-platforms-go-wrong'}
P=re.compile(r'(?:^|[\s(])(?:[Aa]n?\s+|[Tt]he\s+)?\*\*([^*]{2,70})\*\*\s*(?:\([^)]{1,60}\)\s*|,[^,]{1,60},\s*)?(is|are|means|refers to|describes|names)\b')
for p in posts:
    f=os.path.join(root,'posts',p,'index.md')
    if not os.path.exists(f): continue
    t=open(f).read()
    pm=re.search(r'^permalink:\s*(\S+)',t,re.M).group(1)
    if pm in skip: continue
    body=t.split('## Sources and Evidence')[0]
    out=[];seen=set()
    for para in body.split('\n'):
        if para.startswith(('>','#','|')): continue
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*])',para):
            for m in P.finditer(s):
                term=m.group(1).strip().rstrip('.')
                if len(term.split())>8 or term.lower() in seen: continue
                seen.add(term.lower())
                i=s.find('**'+m.group(1))
                out.append(f'[{term}] '+s[max(0,i-40):i+330].strip())
    print('=====',pm,len(out))
    for o in out: print(' ',o)
