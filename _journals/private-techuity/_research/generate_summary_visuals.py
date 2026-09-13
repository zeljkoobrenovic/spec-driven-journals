#!/usr/bin/env python3
"""Generate TL;DR visuals using the repository's Nano Banana article illustrator.

Run --dry-run before generating. Select --post SLUG to regenerate one visual;
existing images are preserved unless --overwrite is explicitly supplied.
"""
from pathlib import Path
import argparse, concurrent.futures, hashlib, importlib.util, json, os, re, sys, time

sys.dont_write_bytecode=True
J=Path(__file__).resolve().parent.parent
if not (J/'config.yaml').exists():
    J=Path('/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/private-techuity')
ROOT=J.parent.parent
GENERATOR=ROOT/'.codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'
sys.path.insert(0,str(GENERATOR.parent))
spec=importlib.util.spec_from_file_location('owned_summary_illustrator',GENERATOR)
helper=importlib.util.module_from_spec(spec);sys.modules[spec.name]=helper;spec.loader.exec_module(helper)
original_path_resolver=helper.source_image_path
# Modalities share the folder-layout post's unique asset namespace.
helper.source_image_path=lambda path,asset:original_path_resolver(path.with_name('index.md') if path.name=='summary.md' else path,asset)
ARCHIVE=J/'_research/summary-visual-prompts-20260913.json'
def sha(data):return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--post',action='append',default=[])
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--overwrite',action='store_true')
    args=parser.parse_args()
    archive=json.loads(ARCHIVE.read_text())
    selected=[v for v in archive['figures'] if not args.post or v['post'] in args.post]
    assert selected,'No summary visuals selected'
    jobs=[]
    for item in selected:
        source=J/'posts'/item['post']/'summary.md'
        asset=helper.source_image_path(source,item['asset'])
        assert asset.is_relative_to(source.parent/'assets')
        text=source.read_text();targets=helper.load_targets(source)
        if targets:
            assert len(targets)==1 and targets[0].id==item['id'],source
            target=targets[0]
            # The archived prompt can be revised for a selected retry.
            target.item=dict(item)
        else:
            assert f"![{item['alt']}]({item['asset']})" in text,source
            assert f"**Figure 1:** *{item['caption']}*" in text,source
            target=helper.IllustrationTarget(source,1,-1,-1,dict(item),asset)
        jobs.append({'item':item,'source':source,'text':text,'source_sha':sha(source.read_bytes()),'target':target,'pending':args.overwrite or not asset.exists()})
    pending=[v for v in jobs if v['pending']]
    print(json.dumps({'summary_visuals':len(jobs),'to_generate':len(pending),'dry_run':args.dry_run}),flush=True)
    if args.dry_run:
        if all(v['target'].start>=0 for v in jobs):
            return helper.main([str(v['source']) for v in jobs]+['--dry-run','--replace','--print-prompts']+(['--overwrite'] if args.overwrite else []))
        for job in pending:print('would generate: '+str(job['target'].image_path))
        return 0
    key=os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key,'Set GEMINI_API_KEY locally before generating summary visuals.'
    native_args=helper.parse_args([str(jobs[0]['source']),'--replace'])
    native_args.timeout=300
    def generate(job):
        target=job['target'];item=job['item'];source=job['source']
        for attempt in range(4):
            try:
                raw,mime=helper.call_gemini(key,archive['model'],target,native_args)
                raw,_,_=helper.normalize_image_bytes_for_target(raw,mime,target.image_path)
                assert raw.startswith(b'\xff\xd8\xff')
                assert sha(source.read_bytes())==job['source_sha'],f'Concurrent summary edit: {source}'
                if target.image_path.exists():
                    old=target.image_path.read_bytes();backup=J/'_research/discarded-summary-variants'
                    backup.mkdir(exist_ok=True)
                    (backup/(item['post']+'-'+sha(old)[:12]+'.jpeg')).write_bytes(old)
                target.image_path.parent.mkdir(parents=True,exist_ok=True)
                target.image_path.write_bytes(raw)
                if target.start>=0:
                    text=job['text'][:target.start]+helper.replacement_text(item,1)+job['text'][target.end:]
                    source.write_text(text)
                return {'post':item['post'],'status':'generated','sha256':sha(raw)}
            except Exception as exc:
                error=str(exc).replace(key,'[redacted]')
                if attempt==3:return {'post':item['post'],'status':'error','error':error}
                time.sleep(4*(attempt+1))
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,6))) as pool:
        for result in pool.map(generate,pending):
            results.append(result)
            item=next(v for v in archive['figures'] if v['post']==result['post'])
            if result['status']=='generated':
                item.update(result)
                item.pop('visual_review',None)
            ARCHIVE.write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
            print(json.dumps(result),flush=True)
    failures=[v for v in results if v['status']=='error']
    print(json.dumps({'generated':len(results)-len(failures),'failures':len(failures)}),flush=True)
    return int(bool(failures))

if __name__=='__main__':raise SystemExit(main())
