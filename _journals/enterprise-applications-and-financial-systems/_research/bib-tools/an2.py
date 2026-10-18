import re,json
exec(open('an.py').read().split("cfg=open")[0])
d=json.load(open('data.json')); harv=d['harv']; entries=d['entries']
url2r={}; title2r={}
for rid,e in entries.items():
    for t,u in e['urls']: url2r.setdefault(norm(u),rid); title2r.setdefault(t.lower().strip(' "“”'),rid)
MANUAL=json.load(open('manual.json')) if __import__('os').path.exists('manual.json') else {}
newcited={}; unmatched=[]; urlchanges=[]
for h in harv:
    rids=[]
    for t,u in h['urls']:
        rid=url2r.get(norm(u)) or MANUAL.get(u)
        if not rid:
            rid=title2r.get(t.lower().strip(' "“”'))
            if rid: urlchanges.append((rid,t,u))
        if rid: rids.append(rid)
        else: unmatched.append((h['pm'],t,u))
    if not h['urls']:
        for r,e in entries.items():
            if not e['urls'] and h['text'].strip('* ')[:30].lower() in e['body'].lower(): rids.append(r)
        if not rids: unmatched.append((h['pm'],h['text'][:120],None))
    for rid in rids:
        l=newcited.setdefault(rid,[])
        if h['pm'] not in l: l.append(h['pm'])
print('URL CHANGES'); [print(x) for x in sorted(set(map(tuple,urlchanges)))]
print('UNMATCHED',len(unmatched))
for x in unmatched: print('--',x)
print('CITED DIFFS')
for rid,e in entries.items():
    a=set(e['cited']); b=set(newcited.get(rid,[]))
    if a!=b: print(rid,'old-only',a-b,'new-only',b-a)
json.dump(dict(newcited=newcited,unmatched=unmatched,urlchanges=urlchanges),open('res.json','w'),indent=1)
