import json,re
from urllib.parse import urlparse
D=json.load(open('srcs2.json'))
TOPICS=['Enterprise architecture practice','Integration, data and ledger engineering','Accounting, controls and regulation','SAP','Workday','Oracle','BlackLine and close automation','OneStream and EPM','Payments','Satellite platforms','AI and automation','Modernization, governance and strategy','Public case studies']
EA,INT,ACC,SAP,WD,ORA,BL,OS,PAY,SAT,AI,MOD,CASE=range(13)
def dom(s): return urlparse(s['url']).netloc.replace('www.','').split(':')[0] if s['url'] else ''
# keyword overrides on title/url (first match wins)
OV=[ # (regex on title|url, topic, type or None)
 (r'birmingham|revlon|erp disasters',CASE,None),
 (r'leanix|togaf|architect elevator|selling options|conversationally|facilitating software|documenting architecture|business architecture key|archimate|pace layered|time framework|madr|architecture decision record|lightweight architecture decision|golden paths|transition architecture|planning and roadmapping|committees invent|team topologies|talk about platforms|products over projects|communities of practice|software architecture guide|systems of engagement|conway',EA,None),
 (r'strangler|legacy displacement|transitional architecture|branchbyabstraction|migration strategies|technical debt|wycash|nobody ever gets credit|fitness function|evolutionary architectures|residu|wardley|embracing risk|chaos|disaster recovery|composable erp|data act|switching|two-tier|netsuite unveils|owned|e-business suite end of life|change coupling|data tests to your dag|launch flex|methodology structure|explore phase|fit-to-standard',MOD,None),
 (r'agent|joule|illuminate|copilot|uplift|model context protocol|foundation model|generative|artificial intelligence|\bai\b|gartner|cfo optimism|ai in finance|omnibus|integration of generative|business ai|autonomous|claude|sensibleai|verity',AI,None),
 (r'stripe|adyen|psd|e-money|2015/2366|2018/389|2015/751|2024/886|interchange|pci dss|ideal|upi|pix|spreedly|hyperswitch|psps|camt|iso 20022|cass 15|verification of payee|safeguard|payment services',PAY,None),
 (r'blackline|trintech|floqast|account reconciliation|transaction matching|advanced financial closing|account substantiation|solution exchange',BL,None),
 (r'onestream|anaplan|consolidation and close|group reporting|extensible dimensionality|consolidation dimension|dimensions$|hg\b|loading sap data into cloud epm',OS,None),
 (r'vertex|kyriba|zuora|coupa|workiva|avalara|avatax|fis treasury|ariba|orbitax|ecosio|in-house banking|peppol|e-invoicing|einvoic|e-reporting',SAT,None),
]
DOMTOP={'help.sap.com':SAP,'news.sap.com':SAP,'learning.sap.com':SAP,'blog.sap-press.com':SAP,'sapinsider.org':SAP,'eursap.eu':SAP,'userapps.support.sap.com':SAP,'api.sap.com':SAP,'blogs.sap.com':SAP,'sapusers.org':SAP,'timetoact-group.com':SAP,'enterprisedna.co':SAP,'sap.com':SAP,'assets.cdn.sap.com':SAP,'pages.community.sap.com':SAP,
 'workday.com':WD,'doc.workday.com':WD,'community-content.workday.com':WD,'blog.workday.com':WD,'newsroom.workday.com':WD,'s21.q4cdn.com':WD,
 'docs.oracle.com':ORA,'blogs.oracle.com':ORA,'oracle.com':ORA,'ateam-oracle.com':ORA,'erp.today':ORA,'cfotech.co.uk':ORA,'doyensys.com':ORA,
 'docs.adyen.com':PAY,'adyen.com':PAY,'investors.adyen.com':PAY,'trust.adyen.com':PAY,'docs.stripe.com':PAY,'stripe.com':PAY,'support.stripe.com':PAY,'stripe.dev':INT,
 'documentation.onestream.com':OS,'onestream.com':OS,'blackline.com':BL,'investors.blackline.com':BL}
CHTOP={'chief-architect-role':EA,'capability-mapping':EA,'application-portfolio':EA,'architecture-governance':EA,'organizing-for-architecture':EA,'principles-standards-reference':EA,
 'integration-architecture':INT,'finance-data-architecture':INT,'designing-financial-ledgers':INT,'custom-finance-platforms':INT,'finance-data-flows':INT,'loosely-coupled-domains':INT,'redundancy-and-coupling':INT,'traceability-and-reconciliation':INT,'systems-of-record':INT,
 'accounting-for-architects':ACC,'controls-and-auditability':ACC,'global-scale':ACC,'finance-processes':ACC,'transaction-to-report':ACC,'brands-entities-markets':ACC,
 'sap-s4hana':SAP,'workday':WD,'oracle-fusion':ORA,'blackline':BL,'onestream':OS,'payments-fundamentals':PAY,'adyen':PAY,'stripe':PAY,'payments-to-ledger':PAY,'satellite-platforms':SAT,'ai-in-finance':AI}
NEWS={'theregister.com','computing.co.uk','techcrunch.com','cio.com','eweek.com','techzine.eu','cpapracticeadvisor.com','erp.today','cfotech.co.uk','accountingtoday.com','globalgovernmentforum.com','cfo.com','journalofaccountancy.com'}
STD=r'ifrs|ias |fasb|as 2201|soc 1|coso|corporate governance code|iso 4217|pci dss|archimate|togaf|open data contract|openlineage|opentelemetry|cloudevents|model context protocol specification|madr|directive|regulation \(eu\)|delegated regulation|17 cfr|gdpr|bürokratie|vat directive|peppol: about|camt|iso 20022|data act|dora'
REG=r'sec\.gov|pcaobus|europa\.eu|federalreserve|revenue\.ie|canada\.ca|supremecourt|business\.gov\.nl|ecb\.europa|law\.cornell|frc\.org'
BOOK=r'architect elevator|facilitating software|team topologies, 2nd|enterprise integration patterns\*?$|balancing coupling|evolutionary architectures|managing technical debt|site reliability|residues|communities of practice|dama-dmbok|^money$|owned|domain-driven design reference'
RES=r'sagas|wycash|nobody ever gets|residuality theory: an|committees invent|two-phase commit|gartner|forrester|barc|ai in finance|patterns for accounting|accounting patterns'
def classify(s):
    t=(s['title']+' '+(s['url'] or '')).lower(); d=dom(s)
    topic=None
    for rx,tp,_ in OV:
        if re.search(rx,t): topic=tp; break
    if s['chapters'][0]=='ai-in-finance' and topic not in (AI,): topic=AI
    if topic is None: topic=DOMTOP.get(d)
    if topic is None: topic=CHTOP.get(s['chapters'][0],MOD)
    # type
    tl=s['title'].lower()
    if re.search(BOOK,tl): ty='Book'
    elif re.search(RES,tl+' '+d): ty='Research'
    elif d in NEWS or 'wikipedia' in d: ty='News' if 'wikipedia' not in d else 'Practitioner'
    elif re.search(REG,(s['url'] or '')) and not re.search(r'10-k|10-q|8-k|results release|form 10',tl): ty='Regulator or official'
    elif re.search(STD,tl): ty='Standard or regulation'
    elif any('Vendor' in c or 'filings' in c.lower() for c in s['cats']): ty='Vendor documentation'
    elif any('Standards' in c for c in s['cats']): ty='Practitioner'  # commentaries filed under standards
    else: ty='Practitioner'
    if re.search(r'10-k|10-q|8-k|results release|form 10|results$',tl): ty='Vendor documentation'
    if re.search(r'eur-lex',s['url'] or ''): ty='Standard or regulation'
    return topic,ty
out=[]
for s in D['srcs']:
    tp,ty=classify(s); s['topic']=tp; s['type']=ty
for i,T in enumerate(TOPICS):
    print('=====',T)
    for s in D['srcs']:
        if s['topic']==i: print('  ',s['type'][:10].ljust(10),'|',s['title'][:60],'|',dom(s),'|',s['chapters'][0][:16])
json.dump(D,open('srcs3.json','w'),indent=1)
