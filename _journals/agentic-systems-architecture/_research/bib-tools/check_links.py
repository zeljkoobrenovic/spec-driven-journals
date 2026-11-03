# Optional step after render.py: fetch every URL on posts/bibliography/index.md and append problems to review.txt.
# Run with:  sh run.sh --links   (needs network; takes a minute or two)
# Flags: LINK DEAD (HTTP 404/410 or DNS failure), LINK ERROR (other HTTP errors or timeouts; often bot blocking,
# so check by hand), ARXIV TITLE (the arXiv page's title shares too few words with the cited title: possibly
# a wrong or invented identifier). A clean link is not proof that the page supports the claim.
import os, re, ssl, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
txt = open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md')).read()
LINK = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)')
def words(t): return set(w for w in re.findall(r'[a-z0-9]+', t.lower()) if len(w) > 3)
items = []
for line in txt.split('\n'):
    m = re.match(r'- \*\*(R\d+)\*\*', line)
    if not m: continue
    ls = list(LINK.finditer(line))
    for lm in ls:  # a generic link text ("preprint", "HTML") is compared with the entry's main title
        t = lm.group(1) if len(words(lm.group(1))) >= 2 else ls[0].group(1)
        items.append((m.group(1), t, lm.group(2)))
CTX = ssl.create_default_context()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

def words(t): return set(w for w in re.findall(r'[a-z0-9]+', t.lower()) if len(w) > 3)

def check(item):
    rid, title, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'text/html,application/pdf,*/*'})
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            body = r.read(200000).decode('utf-8', 'ignore') if 'arxiv.org/abs' in url else ''
        if body:
            pm = re.search(r'<title>\s*\[[^\]]+\]\s*(.*?)</title>', body, re.S)
            if pm:
                got = re.sub(r'\s+', ' ', pm.group(1)).strip()
                cw = words(re.sub(r'\(.*?\)', '', title))
                if cw and len(cw & words(got)) / len(cw) < 0.5:
                    return f'ARXIV TITLE    | {rid} | {title[:70]} | {url} | arXiv page title is "{got[:90]}"'
        return None
    except urllib.error.HTTPError as e:
        kind = 'LINK DEAD     ' if e.code in (404, 410) else 'LINK ERROR    '
        return f'{kind} | {rid} | {title[:70]} | {url} | HTTP {e.code}'
    except Exception as e:
        kind = 'LINK DEAD     ' if 'Name or service' in str(e) or 'nodename' in str(e) else 'LINK ERROR    '
        return f'{kind} | {rid} | {title[:70]} | {url} | {type(e).__name__}: {str(e)[:60]}'

with ThreadPoolExecutor(16) as ex:
    res = [r for r in ex.map(check, items) if r]
res.sort()
with open(os.path.join(HERE, 'review.txt'), 'a') as fh:
    fh.write(f'# Link check: {len(items)} URLs fetched; {len(res)} flagged. LINK ERROR is often bot blocking (403/429), check by hand.\n')
    for r in res: fh.write(r + '\n')
print(len(items), 'URLs;', len(res), 'flagged')
for r in res: print(r)
