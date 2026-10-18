import json,re,sys
from urllib.parse import urlparse
d=json.load(open('raw.json'))
SKIP=re.compile(r'^(None specific|No regulat|No regulation|ASC 606 and IFRS 15, revenue|Sarbanes-Oxley Act section 404 and ICFR|The revenue standards|Research brief|Productscape digest|Book research|The generalized finance-domain)')
def norm(u):
    u=u.strip().rstrip('.,;')
    u=re.sub(r'^http://','https://',u)
    u=re.sub(r'#.*$','',u)
    u=u.replace('://www.','://')
    return u.rstrip('/').lower()
srcs={}
order=[]
for e in d:
    t=e['text']
    if SKIP.match(t): continue
    m=re.search(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',t)
    if m:
        title=m.group(1); url=m.group(2); key=norm(url)
        pre=t[:m.start()].strip(' *,"“'); post=t[m.end():]
        post=post.lstrip('*"” ')
    else:
        # book without url
        mm=re.match(r'(.*?)\s+—\s+(.*)',t)
        title=t.split(' — ')[0]; url=None; key='nourl:'+title[:60].lower(); pre='';post=''
    # split meta vs supports
    sup=''
    if ' — ' in post:
        meta,sup=post.split(' — ',1)
    else:
        mm=re.match(r'(.*?\.)\s+(\S.*)$',post)
        if mm and re.search(r'\d{4}|[A-Z]',mm.group(1)): meta,sup=mm.group(1),mm.group(2)
        else: meta,sup=post,''
    meta=meta.strip(' ,.;')
    if pre: meta=(pre.rstrip(',')+(', '+meta if meta else '')).strip()
    s=srcs.get(key)
    if not s:
        s=srcs[key]=dict(key=key,title=title,url=url,metas=[],sups=[],chapters=[],cats=[],extra=[])
        order.append(key)
    s['metas'].append(meta); s['sups'].append((e['pm'],sup.strip())); s['cats'].append(e['cat'])
    if e['pm'] not in s['chapters']: s['chapters'].append(e['pm'])
    others=re.findall(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',t)[1:]
    for ot,ou in others: s['extra'].append((ot,ou,norm(ou)))
json.dump([srcs[k] for k in order],open('srcs.json','w'),indent=1)
print(len(order))
