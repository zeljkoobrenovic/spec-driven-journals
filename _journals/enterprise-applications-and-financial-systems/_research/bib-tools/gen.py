import json,re,sys,os
from urllib.parse import urlparse, unquote
ROOT='/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/enterprise-applications-and-financial-systems'
cfg=open(ROOT+'/config.yaml').read()
folders=re.findall(r'^\s+- (\S+)/index\.md',cfg,re.M)
chapters=[]  # (folder, permalink, title)
for f in folders:
    p=f'{ROOT}/posts/{f}/index.md'
    if f=='bibliography' or not os.path.exists(p): continue
    t=open(p).read()
    pm=re.search(r'^permalink:\s*(\S+)',t,re.M).group(1)
    ti=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
    chapters.append((f,pm,ti,t))
SKIP=re.compile(r'^(None specific|No regulat|ASC 606 and IFRS 15, revenue|Sarbanes-Oxley Act section 404 and ICFR|The revenue standards|Research brief|Productscape digest|Book research|The generalized finance-domain)')
def norm(u):
    u=unquote(u.strip().rstrip('.,;')).lower()
    u=re.sub(r'^http://','https://',u); u=re.sub(r'#.*$','',u); u=u.replace('://www.','://')
    u=re.sub(r'/(eng)$','',u); u=re.sub(r'\.htm$','',u); u=u.replace('stripe.com/br/','stripe.com/')
    return u.rstrip('/')
LINK=re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
def parse(t):
    m=LINK.search(t)
    if not m:
        parts=t.split(' — ',1)
        return dict(title=parts[0].strip(),url=None,key='nourl:'+re.sub(r'\W+','',parts[0].lower())[:50],meta='',sup=parts[1] if len(parts)>1 else '',extra=[])
    title=m.group(1).strip('*"“” '); url=m.group(2)
    pre=t[:m.start()].strip(' *,"“”')
    tail=t[m.end():]
    extra=[(a,b) for a,b in LINK.findall(tail)]
    # remove extra links ("and [x](u)", ", [x](u)")
    lead=re.compile(r'^\s*\*?(,|and|,\s*and)?\s*'+LINK.pattern+r'\*?')
    while lead.match(tail): tail=lead.sub('',tail,count=1)
    tail=LINK.sub(lambda m:m.group(1),tail)
    tail=tail.lstrip('*"”) ').strip()
    meta=sup=''
    if tail.startswith('—'):
        tail=tail[1:].strip()
        if '; ' in tail: meta,sup=tail.split('; ',1)
        elif ': ' in tail: meta,sup=tail.split(': ',1)
        else: meta=tail
    else:
        tail=tail.lstrip(', ').strip()
        if ' — ' in tail: meta,sup=tail.split(' — ',1)
        elif ': ' in tail and len(tail.split(': ',1)[0])<90: meta,sup=tail.split(': ',1)
        else:
            mm=re.match(r'(.*?(?:\d{4}|O\'Reilly|martinfowler\.com|Workday|Oracle|Stripe|Adyen|SAP|[a-z]{2,}))\.\s+(\S.*)$',tail)
            if mm: meta,sup=mm.group(1),mm.group(2)
            else: meta=tail
    meta=meta.strip(' ,.;'); sup=sup.strip()
    if pre: meta=pre+(', '+meta if meta else '')
    return dict(title=title,url=url,key=norm(url),meta=meta,sup=sup,extra=extra)
srcs={};order=[]
for f,pm,ti,t in chapters:
    m=re.search(r'^## Sources and Evidence\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S)
    if not m: continue
    cat=''
    for line in m.group(1).split('\n'):
        s=line.strip()
        if re.match(r'^\*[^*\[].*\*$',s) or re.match(r'^\*\*[^\[].*\*\*$',s): cat=s.strip('*'); continue
        if not s.startswith(('- ','* ')): continue
        body=s[2:]
        if SKIP.match(body): continue
        e=parse(body)
        k=e['key']
        if k not in srcs:
            e.update(chapters=[],cats=[],sups=[]); srcs[k]=e; order.append(k)
        S=srcs[k]
        if pm not in S['chapters']: S['chapters'].append(pm)
        S['cats'].append(cat); S['sups'].append(e['sup'])
        for x in e['extra']:
            if norm(x[1]) not in [norm(y[1]) for y in S['extra']] and norm(x[1])!=k: S['extra'].append(x)
json.dump(dict(chapters=[(a,b,c) for a,b,c,_ in chapters],srcs=[srcs[k] for k in order]),open('srcs2.json','w'),indent=1)
print(len(order))
