import json,re
TOPICS=["Enterprise architecture practice","Integration, data and ledger engineering","Accounting, controls and regulation","SAP","Workday","Oracle","BlackLine and close automation","OneStream and EPM","Payments","Satellite platforms","AI and automation","Modernization, governance and strategy","Public case studies"]
EA,INT,ACC,SAP,WD,ORA,BL,OS,PAY,SAT,AI,MOD,CASE=range(13)
VD,SR,RO,PR,BK,RS,NW='Vendor documentation','Standard or regulation','Regulator or official','Practitioner','Book','Research','News'
FIX={ # title substring -> (topic or None, type or None)
 'Viertes Bürokratie':(ACC,PR),'GDPR Article 17':(ACC,SR),'Keeping business records':(ACC,RO),
 'Gartner TIME Framework':(None,PR),"Gartner's PACE":(None,PR),'Systems of Engagement':(None,PR),
 'AS 2201':(ACC,SR),"Management's Report on Internal Control Over Financial Reporting":(ACC,RO),
 'Regulation (EU) 2022/2554':(ACC,SR),'Regulation (EU) 2023/2854':(ACC,SR),'EU Data Act':(ACC,PR),
 '2024/1773':(ACC,SR),'2025/301':(ACC,SR),'Digital Operational Resilience Act':(ACC,RO),
 'Patterns for Accounting':(None,PR),'Accounting Patterns':(None,PR),'Money':(INT,BK),
 'Schema evolution':(None,VD),'Schema Registry':(None,VD),
 'ASU 2024-03':(None,PR),'Heads Up: COSO 2013':(None,PR),'Heads Up: COSO internal':(None,PR),
 'Form 10-Q':(None,RO),'ISO 20022 and Swift':(None,PR),'ING Format':(None,VD),'camt.053 and camt.052':(None,VD),
 'Oracle Fusion Cloud implementation architecture':(ORA,VD),'Workday Rising 2026 recap':(WD,PR),
 'Identifying SAP Joule':(None,VD),'Workday Unveils Workday Build':(None,VD),'Introducing Adyen Uplift':(None,VD),
 'Microsoft 365':(None,VD),'Donating the Model Context':(None,VD),"The IIA's":(None,SR),
 'Group Reporting in S/4HANA':(SAP,PR),'Workday, Inc.':(WD,PR),'IFRS 10':(ACC,SR),
 "Ledger: Stripe's system":(INT,PR),'Designing robust and predictable APIs':(INT,PR),
 'iDEAL':(None,VD),'UPI product':(None,VD),'Spreedly':(None,VD),'Hyperswitch':(None,VD),'More PSPs':(None,VD),
 'Workiva overview':(None,PR),'Explore Phase':(SAP,VD),'Fit-to-Standard':(SAP,VD),'Methodology Structure':(SAP,VD),
 'Launch Flex':(WD,VD),'E-Business Suite end of life':(ORA,PR),'Two-Tier ERP':(SAP,VD),
 'Change coupling':(None,VD),'Disaster Recovery of Workloads':(None,VD),
 'Planning and Roadmapping':(None,PR),'Transition Architecture':(None,PR),'MADR':(None,PR),
 'Hypothesis documentation':(None,VD),'Pact documentation':(None,VD),
 'Thoma Bravo completes acquisition of Anaplan':(None,VD),'Revlon':(None,RO),
 'Pix':(PAY,NW),
}
D=json.load(open('srcs3.json'))
VDOM=('docs.adyen.com','adyen.com','investors.adyen.com','learning.sap.com','docs.oracle.com','doc.workday.com','docs.stripe.com')
for s in D['srcs']:
    for k,(tp,ty) in FIX.items():
        if k in s['title'] or (k=='Money' and s['title']=='Money'):
            if k=='Money' and s['title']!='Money': continue
            if tp is not None: s['topic']=tp
            if ty: s['type']=ty
            break
    if s['url'] and any(d in s['url'] for d in VDOM) and 'wikipedia' not in s['url']: s['type']=VD
json.dump(D,open('srcs4.json','w'),indent=1)
from collections import Counter
print(Counter(TOPICS[s['topic']] for s in D['srcs']))
print(Counter(s['type'] for s in D['srcs']))
