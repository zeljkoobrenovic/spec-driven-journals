import re,sys,glob
files=sorted(glob.glob('*/index.md'))
texts={f:open(f).read().split('## Sources and Evidence')[0] for f in files}
for t in sys.argv[1:]:
    print('##',t)
    n=0
    for f,x in texts.items():
        for m in re.finditer(r'[^.\n]{0,140}'+re.escape(t)+r'[^.\n]{0,240}',x):
            print('   ',f.split('/')[0][:14],'|',m.group(0)[:380]); n+=1
            if n>=2: break
        if n>=2: break
