import re, os, json, sys
ROOT='/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/finance-systems-architecture'
cfg=open(ROOT+'/config.yaml').read()
posts=re.findall(r'^\s+- (\S+)/index\.md',cfg,re.M)
out=[]
for folder in posts:
    f=f'{ROOT}/posts/{folder}/index.md'
    if not os.path.exists(f) or folder in('bibliography',): continue
    t=open(f).read()
    pm=re.search(r'^permalink:\s*(\S+)',t,re.M).group(1)
    m=re.search(r'^## Sources and Evidence\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S)
    if not m: continue
    cat=''
    for line in m.group(1).split('\n'):
        s=line.strip()
        if re.match(r'^\*[^*].*\*$',s) or re.match(r'^\*\*.*\*\*$',s) or s.startswith('###'):
            cat=s.strip('*# '); continue
        if s.startswith(('- ','* ')):
            body=s[2:]
            urls=re.findall(r'\]\((https?://[^)\s]+)\)',body)
            out.append(dict(folder=folder,pm=pm,cat=cat,text=body,urls=urls))
json.dump(out,open(sys.argv[1],'w'),indent=1)
print(len(out), len({(e['urls'][0] if e['urls'] else e['text']) for e in out}))
from collections import Counter
print(Counter(e['cat'] for e in out))
print(sum(1 for e in out if not e['urls']))
