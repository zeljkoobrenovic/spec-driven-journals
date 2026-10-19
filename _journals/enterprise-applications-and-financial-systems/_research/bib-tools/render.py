import json,re,sys
D=json.load(open('srcs4.json'))
TOPICS=["Enterprise architecture practice","Integration, data and ledger engineering","Accounting, controls and regulation","SAP","Workday","Oracle","BlackLine and close automation","OneStream and EPM","Payments","Satellite platforms","AI and automation","Modernization, governance and strategy","Public case studies"]
PAYSUB=["Payments fundamentals and regulation","Adyen","Stripe","Orchestration and multi-provider routing"]
def paysub(s):
    t=(s['title']+' '+(s['url'] or '')).lower()
    if re.search(r'spreedly|hyperswitch|more psps|/orchestration',t): return 3
    if 'adyen' in t: return 1
    if 'stripe' in t: return 2
    return 0
chap=D['chapters']  # folder,pm,title
corder={pm:i for i,(f,pm,t) in enumerate(chap)}
srcs=D['srcs']
from urllib.parse import unquote
def nrm(u):
    u=unquote(u.strip()).lower(); u=re.sub(r'^http://','https://',u); u=re.sub(r'#.*$','',u); u=u.replace('://www.','://'); return u.rstrip('/')
byk={s['key']:s for s in srcs}
for s in srcs:
    keep=[]
    for a,b in s['extra']:
        t=byk.get(nrm(b))
        if t and t is not s:
            for c in s['chapters']:
                if c not in t['chapters']: t['chapters'].append(c)
        else: keep.append((a,b))
    s['extra']=keep
for s in srcs:
    if s['title']=="Hyrum's Law": s['meta']='Hyrum Wright'; s['sups']=['every observable behavior of an interface will be depended on']
    if 'OWNED' in s['title']: s['sups']=[s['sups'][0].rstrip('. ')+'; see [Manage Technical Debt: Present the Fix by What It Buys](https://ownedbyinvestors.com/manage-technical-debt)']
for s in srcs:
    s['chapters'].sort(key=lambda p:corder.get(p,999))
    s['sub']=paysub(s) if s['topic']==8 else 0
    s['first']=corder.get(s['chapters'][0],999)
srcs.sort(key=lambda s:(s['topic'],s['sub'],s['first']))
for i,s in enumerate(srcs): s['id']='R%03d'%(i+1)
def clause(s):
    sup=next((x for x in s['sups'] if x),'')
    sup=sup.strip()
    if len(sup)>260:
        cut=sup[:260]; j=max(cut.rfind('; '),cut.rfind('. '))
        sup=(cut[:j] if j>80 else cut.rsplit(' ',1)[0])
    sup=sup.rstrip(' .;,')
    if sup: sup=sup[0].upper()+sup[1:]+'.'
    return sup
def entry(s):
    meta=s['meta'].strip().rstrip('.')
    head=f"[{s['title']}]({s['url']})" if s['url'] else f"{s['title'].strip('*')}" if not s['title'].startswith('*') else s['title']
    if not s['url'] and s['title'].startswith(('Željko','Hector')): head=s['title']
    parts=[f"- **{s['id']}** · {head}" + (f" — {meta}." if meta else '.')]
    c=clause(s)
    if c: parts.append(c)
    if s['extra']:
        parts.append('Also: '+', '.join(f'[{a}]({b})' for a,b in s['extra'])+'.')
    parts.append(f"*{s['type']}.*")
    parts.append('Cited in: '+', '.join(f'[[{p}]]' for p in s['chapters'])+'.')
    out=' '.join(parts).replace('..','.').replace('this chapter','the citing chapter').replace('This chapter','The citing chapter')
    return out
body=[]
def rng(ids):
    return f"{ids[0]}–{ids[-1]}" if len(ids)>1 else ids[0]
# topic index
TOPDESC=json.load(open('topdesc.json'))
body.append('## Topic Index\n')
body.append('Identifiers run in topic order, so each topic is one contiguous block. A source cited by chapters in several topics sits under the topic it serves best; its **Cited in** line lists every chapter that uses it.\n')
for i,T in enumerate(TOPICS):
    ids=[s['id'] for s in srcs if s['topic']==i]
    desc,start=TOPDESC[T]
    body.append(f"**{T} ({rng(ids)}, {len(ids)} sources).** {desc} Start with {start}.\n")
for i,T in enumerate(TOPICS):
    body.append(f"## {T}\n")
    if i==8:
        for j,ST in enumerate(PAYSUB):
            body.append(f"### {ST}\n")
            body += [entry(s) for s in srcs if s['topic']==8 and s['sub']==j]
            body.append('')
    else:
        body += [entry(s) for s in srcs if s['topic']==i]
        body.append('')
body.append('## Sources by Chapter\n')
body.append('Each line lists the identifiers a chapter cites in its **Sources and Evidence** section, in identifier order. The preface essays, part introductions and reference pages that cite no external source are omitted.\n')
for f,pm,t in chap:
    ids=sorted(s['id'] for s in srcs if pm in s['chapters'])
    if ids: body.append(f"- [[{pm}]] ({len(ids)}): "+', '.join(ids)+'.')
body.append('')
open('body.md','w').write('\n'.join(body))
json.dump(srcs,open('final.json','w'),indent=1)
print(len(srcs))
