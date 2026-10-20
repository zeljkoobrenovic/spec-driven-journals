import re,json
exec(open('an.py').read().split("cfg=open")[0])
BIB=ROOT+'/posts/bibliography/index.md'
bib=open(BIB).read()
cfg=open(ROOT+'/config.yaml').read()
folders=re.findall(r'^\s+- (\S+)/index\.md',cfg,re.M)
order=[]
for f in folders:
    t=open(f'{ROOT}/posts/{f}/index.md').read(); order.append(re.search(r'^permalink:\s*(\S+)',t,re.M).group(1))
# 1. URL / title fixes
rep=[
('[SAP S/4HANA maintenance to 2040; Business Suite 7 to 2027 and 2030](https://news.sap.com/africa/?p=140253)',
 '[SAP Extends Its Innovation Commitment for SAP S/4HANA, Provides Clarity and Choice on SAP Business Suite 7](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/)'),
('[SAP ERP, private edition, transition option](https://news.sap.com/?p=231556)',
 '[New Offering to Help Navigate Complex RISE with SAP Transformations](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/)'),
('[Transition option update](https://news.sap.com/?p=233946) — SAP News, October 2026.',
 '[Navigating Your RISE with SAP Journey: Updates for SAP ERP, Private Edition, Transition Option](https://news.sap.com/2025/08/rise-with-sap-journey-sap-erp-private-edition-transition-option-updates/) — SAP News, August 2025 (updated 13 October 2026).'),
('https://www.fisglobal.com:443/products/','https://www.fisglobal.com/products/'),
('https://s21.q4cdn.com/950027458/files/doc_news/The-Next-Generation-of-Workforce-Management-is-HereWorkday-Unveils-New-Agent-System-of-Record-02-11-2025-2025.pdf',
 'https://newsroom.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record'),
('https://gcom.pdo.aws.gartner.com/en/newsroom/','https://www.gartner.com/en/newsroom/'),
('— Gartner, 20 Aug 2026. Run reconstruction','— Gartner newsroom Q&A with Alex Levine, 20 Aug 2026; also reported by [CFOtech](https://cfotech.news/story/gartner-urges-cfos-to-pilot-finance-ai-with-governance). Run reconstruction'),
('The modelling language','The modeling language'),('safe harbours','safe harbors'),('licence transition','license transition'),('authorisation relay','authorization relay'),
]
for a,b in rep:
    assert bib.count(a)==1,a; bib=bib.replace(a,b)
# 2. insert new entries
new=open('new_entries.md').read().strip().split('\n')
r389=new[0]; uber=new[1:]
bib=bib.replace('\n\n## SAP\n','\n'+r389+'\n\n## SAP\n',1)
bib=bib.replace('\n## Sources by Chapter\n','\n## Public case studies: Uber\n\n'+'\n'.join(uber)+'\n\n## Sources by Chapter\n',1)
# 3. recompute cited
entries={}
for m in re.finditer(r'^- \*\*(R\d{3})\*\* · (.*)$',bib,re.M):
    rid,body=m.groups()
    entries[rid]=dict(body=body,urls=re.findall(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',body.split(' Cited in:')[0]))
url2r={}
for rid,e in entries.items():
    for t,u in e['urls']: url2r.setdefault(norm(u),rid)
harv=json.load(open('data.json'))['harv']
cited={}
for h in harv:
    rids=[url2r.get(norm(u)) or url2r.get(norm(u.replace('/br/blog','/blog'))) for t,u in h['urls']]
    if not h['urls']:
        rids=[r for r,e in entries.items() if not e['urls'] and h['text'].strip('* ')[:30].lower() in e['body'].lower()]
    for r in rids:
        if r: cited.setdefault(r,set()).add(h['pm'])
missing=[r for r in entries if r not in cited]
print('uncited',missing)
def cl(r): return ', '.join(f'[[{p}]]' for p in order if p in cited[r])
def fix(m):
    rid,body=m.groups()
    body=re.sub(r' Cited in: .*$','',body)
    return f'- **{rid}** · {body} Cited in: {cl(rid)}.'
bib=re.sub(r'^- \*\*(R\d{3})\*\* · (.*)$',fix,bib,flags=re.M)
# 4. sources by chapter
lines=[]
for p in order:
    rs=sorted(r for r in cited if p in cited[r])
    if rs: lines.append(f'- [[{p}]] ({len(rs)}): {", ".join(rs)}.')
head,sbc=bib.split('## Sources by Chapter\n',1)
intro=sbc.strip().split('\n\n')[0]
bib=head+'## Sources by Chapter\n\n'+intro+'\n\n'+'\n'.join(lines)+'\n'
open(BIB,'w').write(bib)
from collections import Counter
print(len(entries), Counter(re.findall(r'\*(Vendor documentation|Standard or regulation|Regulator or official|Practitioner|Book|Research|News)\.\* Cited',bib)))
print(len(lines),'chapters')
