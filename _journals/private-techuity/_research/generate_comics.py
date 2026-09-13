#!/usr/bin/env python3
"""Generate this journal's comic-panel artwork with its shared fictional cast.

Run from any directory:
  GEMINI_API_KEY=... python3 _journals/private-techuity/_research/generate_comics.py --dry-run
  GEMINI_API_KEY=... python3 _journals/private-techuity/_research/generate_comics.py --workers 6

Existing images are preserved unless --overwrite is supplied. The six existing
panel captions and dialogue remain the authoring contract. API schema reference:
https://ai.google.dev/api/generate-content#method:-models.generatecontent
"""
from __future__ import annotations
import argparse
import base64
import concurrent.futures
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.dont_write_bytecode=True
J=Path(__file__).resolve().parent.parent
if not (J/'config.yaml').exists():
    J=Path('/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/private-techuity')
ROOT=J.parent.parent
HELPER=ROOT/'.codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'
sys.path.insert(0,str(HELPER.parent))
spec=importlib.util.spec_from_file_location('owned_comic_image_helpers',HELPER)
helper=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=helper
spec.loader.exec_module(helper)
MODEL='gemini-3-pro-image-preview'
CAST=J/'_research/comic-cast-20260913.jpeg'
PANEL_RE=re.compile(r'<!-- comic-panel\s+(\{.*?\})\s*-->',re.S)
STYLE_RE=re.compile(r'<!-- comic-style\s+(\{.*?\})\s*-->',re.S)
EXTRA=(
    'Create exactly ONE finished comic panel, landscape 16:9, not a multi-panel page. '
    'The attached image is a character-design reference only. Reuse the matching named characters, '
    'their faces, hair, skin tone and clothing colors in the new scene; do not reproduce the reference-sheet layout. '
    'Use clean navy ink and restrained flat colors on warm ivory, with generous space, expressive people and simple physical props. '
    'Only draw characters required by this panel. Keep the dialogue in ONE large, high-contrast speech bubble, '
    'with the exact supplied words, correct spelling and punctuation. '
    'No panel number, title, caption, character-name labels, book name, dense chart or extra dialogue. '
    'The Convey text explains the intended meaning; do not print it in the image. '
    'Where a historical case is discussed, show fictional colleagues examining documents; do not reenact real events or impersonate actual executives. '
    'Do not invent amounts, dates, percentages or research claims on the props. '
)
IDENTITIES=(
    'Final character-identity requirements, matching the attached reference: '
    'MORGAN is a light-skinned WOMAN with a short straight black bob and green jacket. '
    'ALEX is a medium-brown-skinned MAN with short dark curly hair and a blue rolled-sleeve shirt; fill his face and hands with the same brown skin color. '
    'SAM is a light-skinned MAN with short brown hair, round glasses and an amber cardigan. '
    'PRIYA is a brown-skinned WOMAN with straight shoulder-length dark hair and a plum blouse. '
    'INES is a light-skinned older WOMAN with a short grey bob and a navy jacket. '
    'Draw only the named people called for in the scene. Any other explicitly requested owners, employees or customers are unnamed supporting people in grey clothing, distinct from this cast. '
    'Keep the entire speech bubble and its tail inside the canvas with a visible margin. '
    'Do not write numerical balances, amounts or dates on any prop. '
)
PEOPLE={
    'Morgan':'Morgan: the woman with a black bob and green jacket, first person in the reference.',
    'Alex':'Alex: the brown-skinned man with short curly hair and a blue shirt, second person in the reference.',
    'Sam':'Sam: the man with short brown hair, round spectacles and an amber cardigan, third person in the reference. He has close-cropped hair above his ears, a masculine face and no bob haircut.',
    'Priya':'Priya: the brown-skinned woman with straight dark hair and a plum blouse, fourth person in the reference.',
    'Ines':'Ines: the older woman with a grey bob and navy jacket, fifth person in the reference.'
}

def sha(data):return hashlib.sha256(data).hexdigest()

def collect(post_filter):
    jobs=[]
    sources={}
    corrections_path=J/'_research/comic-visual-corrections-20260913.json'
    corrections=json.loads(corrections_path.read_text()) if corrections_path.exists() else []
    scene_overrides={v['post']+'/'+f"{v['panel']:02d}-scene":v['scene'] for v in corrections}
    for path in sorted((J/'posts').glob('*/comics.md')):
        slug=path.parent.name
        if post_filter and slug not in post_filter:continue
        text=path.read_text()
        style_match=STYLE_RE.search(text)
        assert style_match, path
        style=json.loads(style_match.group(1))
        panels=PANEL_RE.findall(text)
        assert len(panels)==6, path
        sources[slug]={'text':text,'sha256':sha(path.read_bytes()),'path':path}
        for number,raw in enumerate(panels,1):
            item=json.loads(raw)
            assert item['asset'].startswith(f'assets/images/{slug}/comic-'),item
            assert item['caption'] in item['prompt'],(slug,number)
            assert f"**Panel {number}:** {item['caption']}" in text,(slug,number)
            dialogue=re.search(r'Use one speech bubble with the exact words: "(.*?)"',item['prompt'])
            assert dialogue,(slug,number)
            asset=path.parent/'assets/images'/slug/Path(item['asset']).name
            scene=item['prompt'].split('Use one speech bubble')[0]
            scene=re.sub(r'^Panel \d+ of an explainer comic\.\s*','',scene).strip()
            scene=scene_overrides.get(slug+'/'+item['id'],scene)
            people=[description for name,description in PEOPLE.items() if re.search(r'\b'+name+r'\b',scene)]
            prompt='Draw one finished 16:9 editorial comic panel using the attached character reference. Clean navy ink, flat warm colors, ivory background.\n'
            prompt+='Scene: '+scene+'\nCharacters in this scene: '+' '.join(people)+'\n'
            prompt+='Additional unnamed people, if the scene requires them, wear plain grey clothes and do not resemble the recurring cast. Do not draw other cast members.\n'
            prompt+='Place one large WHITE speech bubble in clear empty space ABOVE all heads, fully inside the canvas, with these exact words: "'+dialogue.group(1)+'". Never overlap the bubble or its words with a person.\n'
            prompt+='Meaning to convey, not text to print: '+item['caption']+'\n'
            prompt+='No character-name labels, title, panel number, extra dialogue or caption. Props may use a few short scene labels but no amounts, percentages, dates or invented claims. Historical cases are discussed by fictional people examining documents.'
            jobs.append({'post':slug,'number':number,'id':item['id'],'item':item,
                         'prompt':prompt,'dialogue':dialogue.group(1),'asset':asset})
    return jobs,sources

def call_image(prompt,reference,key):
    endpoint='https://generativelanguage.googleapis.com/v1beta/models/'+urllib.parse.quote(MODEL,safe='')+':generateContent'
    payload={'contents':[{'role':'user','parts':[
        {'text':prompt},
        {'inline_data':{'mime_type':'image/jpeg','data':reference}}
    ]}],'generationConfig':{'responseModalities':['IMAGE'],'imageConfig':{'aspectRatio':'16:9'}}}
    body=json.dumps(payload).encode()
    for attempt in range(4):
        request=urllib.request.Request(endpoint,data=body,
            headers={'Content-Type':'application/json','x-goog-api-key':key},method='POST')
        try:
            with urllib.request.urlopen(request,timeout=300) as response:
                return helper.extract_image_bytes(json.loads(response.read().decode()))
        except urllib.error.HTTPError as exc:
            detail=exc.read().decode(errors='replace')
            if exc.code not in (429,500,502,503,504) or attempt==3:
                raise RuntimeError(f'Gemini HTTP {exc.code}: {detail[:700]}') from None
        except (urllib.error.URLError,TimeoutError) as exc:
            if attempt==3:raise RuntimeError(f'Gemini connection failed: {exc}') from None
        time.sleep(5*(2**attempt))
    raise RuntimeError('Image request exhausted retries')

def sync_post(slug,source,jobs):
    path=source['path']
    assert sha(path.read_bytes())==source['sha256'],f'Concurrent comic edit: {path}'
    original=source['text']
    available=[j for j in jobs if j['asset'].exists()]
    if not available:return
    style_match=STYLE_RE.search(original)
    intro=original[style_match.end():PANEL_RE.search(original).start()].strip()
    status='**Comic.**' if len(available)==6 else '**Comic — artwork partially generated.**'
    intro=re.sub(r'^\*\*Comic(?: storyboard)?[^\n]*?\*\*',status,intro,count=1)
    text=style_match.group(0)+'\n\n'+intro+'\n\n'
    for job in jobs:
        item=dict(job['item'])
        exists=job['asset'].exists()
        item['status']='generated' if exists else 'pending'
        if exists:
            item['generation']={'model':MODEL,'reference_id':'owned-cast-20260913','sha256':sha(job['asset'].read_bytes())}
        text+='<!-- comic-panel\n'+json.dumps(item,ensure_ascii=False,indent=2)+'\n-->\n\n'
        if exists:
            text+=f"![{item['alt']}]({item['asset']})\n\n"
        text+=f"**Panel {job['number']}:** {item['caption']}\n\n"
        # The transcript remains readable independently of image text.
        text+=f"*Dialogue:* “{job['dialogue']}”\n\n"
    path.write_text(text.rstrip()+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--post',action='append',default=[])
    parser.add_argument('--only',action='append',default=[],help='Panel id, e.g. 01-scene; combine with --post.')
    parser.add_argument('--only-key',action='append',default=[],help='Exact post/panel-id, e.g. 00-how-companies-get-money/01-scene.')
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--limit',type=int,default=0)
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--overwrite',action='store_true')
    args=parser.parse_args()
    jobs,sources=collect(set(args.post))
    assert jobs,'No comic panels found'
    selected=[j for j in jobs if not args.only or j['id'] in args.only]
    selected=[j for j in selected if not args.only_key or j['post']+'/'+j['id'] in args.only_key]
    pending=[j for j in selected if args.overwrite or not j['asset'].exists()]
    if args.limit:pending=pending[:args.limit]
    print(json.dumps({'posts':len(sources),'panels':len(jobs),'to_generate':len(pending),'dry_run':args.dry_run}),flush=True)
    if args.dry_run:
        assert len({str(j['asset']) for j in jobs})==len(jobs)
        for job in pending:print(f"would generate: {job['post']} / panel {job['number']} -> {job['asset'].name}")
        return 0
    key=os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key,'Set GEMINI_API_KEY locally before generating comic artwork.'
    assert CAST.exists(),'Generate and inspect the shared cast reference first.'
    reference=base64.b64encode(CAST.read_bytes()).decode()
    archive_path=J/'_research/comic-generation-prompts-20260913.json'
    archive=json.loads(archive_path.read_text()) if archive_path.exists() else {'date':'2026-09-13','model':MODEL,'reference':'comic-cast-20260913.jpeg','panels':{}}
    pending_keys={job['post']+'/'+job['id'] for job in pending}
    for job in jobs:
        archive_key=job['post']+'/'+job['id']
        if archive_key not in pending_keys and archive_key in archive['panels']:continue
        previous=archive['panels'].get(archive_key)
        entry={'post':job['post'],'panel':job['number'],
            'asset':job['item']['asset'],'prompt':job['prompt'],'dialogue':job['dialogue'],
            'alt':job['item']['alt'],'caption':job['item']['caption']}
        if previous and previous['prompt']!=job['prompt']:
            entry['previous_prompt']=previous['prompt']
        archive['panels'][archive_key]=entry
    archive_path.write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
    def generate(job):
        try:
            data,mime=call_image(job['prompt'],reference,key)
            data,_,_=helper.normalize_image_bytes_for_target(data,mime,job['asset'])
            assert helper.detect_image_mime(data)=='image/jpeg'
            job['asset'].parent.mkdir(parents=True,exist_ok=True)
            if job['asset'].exists():
                previous=job['asset'].read_bytes()
                backups=J/'_research/discarded-comic-variants'
                backups.mkdir(exist_ok=True)
                (backups/(job['post']+'-'+job['asset'].stem+'-'+sha(previous)[:12]+'.jpeg')).write_bytes(previous)
            job['asset'].write_bytes(data)
            return {'post':job['post'],'panel':job['number'],'status':'generated','sha256':sha(data)}
        except Exception as exc:
            return {'post':job['post'],'panel':job['number'],'status':'error','error':str(exc)}
    results=[]
    report_path=J/'_research/comic-generation-progress-20260913.json'
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,8))) as pool:
        futures=[pool.submit(generate,job) for job in pending]
        for future in concurrent.futures.as_completed(futures):
            result=future.result()
            results.append(result)
            print(json.dumps(result),flush=True)
            report_path.write_text(json.dumps(results,indent=2)+'\n')
    for slug,source in sources.items():
        sync_post(slug,source,[j for j in jobs if j['post']==slug])
    for job in jobs:
        if job['asset'].exists():
            archive['panels'][job['post']+'/'+job['id']].update(status='generated',sha256=sha(job['asset'].read_bytes()))
    archive_path.write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
    failures=[r for r in results if r['status']=='error']
    ready=sum(j['asset'].exists() for j in jobs)
    print(json.dumps({'ready_panels':ready,'total_panels':len(jobs),'failures':len(failures)}),flush=True)
    return 1 if failures else 0

if __name__=='__main__':raise SystemExit(main())
