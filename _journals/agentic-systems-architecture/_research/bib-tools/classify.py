# Step 2 of 4: assign each harvested source a topic and an evidence type.
# Reads srcs2.json, writes srcs3.json, prints the classification for review (run.sh sends it to classify-review.txt).
#
# Evidence type = the style guide's five source groups. The group heading under which the chapters cited a source
# wins: the most frequent heading across its citations, the first-cited heading on a tie. Only a source cited
# under no recognized heading falls back to URL rules. A source cited under two different headings is printed as
# "TYPE CONFLICT" so a human can decide (override it in fix.py's FIX).
#
# Topic: a few content rules first (interview designs, legal texts, benchmarks, sandbox mechanisms, protocol
# specifications, prompt injection), then the topic whose chapters cite the source most; a tie goes to the topic
# of the first page in reading order that cites it.
import json, re, os
from collections import Counter
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))
TOPICS = ['Foundations, justification and autonomy',                                   # Part I (and the Preface)
          'Reference architecture, models, runtimes and interaction',                  # Part II
          'Planning, orchestration and multi-agent coordination',                      # Part III
          'Context, retrieval, memory and state',                                      # Part IV
          'Tool contracts, protocols and external actions',                            # Part V, ch. 19, 20, 22
          'Sandboxes and execution environments',                                      # Part V, ch. 21
          'Reliability and durable execution',                                         # Part VI
          'Security, prompt injection and agent identity',                             # Part VII, ch. 26-28
          'Human oversight, policy enforcement and regulation',                        # Part VII, ch. 29-30 + legal texts
          'Evaluation and benchmarks',                                                 # Part VIII, ch. 31, 32, 34
          'Observability',                                                             # Part VIII, ch. 33
          'Performance, cost and caching',                                             # Part IX
          'Evolution, versioning and ownership',                                       # Part X
          'Domains: coding, customer operations, back office and high-stakes decisions',  # Part XI
          "Design examples from the author's interview project"]                       # by evidence type
FOUND, ARCH, ORCH, CTX, TOOLS, SBX, REL, SEC, OVS, EVAL, OBS, PERF, EVOL, DOM, IVW = range(len(TOPICS))
CH_TOPIC = {}
for pm, t in [('introduction', FOUND), ('where-agentic-systems-go-wrong', FOUND), ('meet-ostrell', FOUND),
              ('what-makes-a-system-agentic', FOUND), ('when-agents-are-justified', FOUND),
              ('autonomy-and-consequence', FOUND), ('workflows-loops-and-autonomous-agents', FOUND),
              ('agentic-reference-architecture', ARCH), ('models-and-the-model-gateway', ARCH), ('agent-runtime', ARCH),
              ('agents-in-the-enterprise', ARCH), ('agent-interaction-design', ARCH),
              ('planning-and-decomposition', ORCH), ('routing-and-delegation', ORCH),
              ('single-and-multi-agent-designs', ORCH), ('coordination-and-handoffs', ORCH),
              ('context-engineering', CTX), ('retrieval-and-grounding', CTX), ('agent-memory', CTX),
              ('task-state-and-checkpoints', CTX), ('provenance-and-freshness', CTX),
              ('tool-contracts', TOOLS), ('tool-ecosystems-and-mcp', TOOLS), ('sandboxes-and-execution-environments', SBX),
              ('side-effects-and-external-actions', TOOLS),
              ('durable-agent-execution', REL), ('retries-idempotency-and-concurrency', REL),
              ('partial-failure-and-compensation', REL),
              ('agent-threat-model', SEC), ('prompt-injection-defense', SEC), ('agent-identity-and-least-privilege', SEC),
              ('human-oversight-and-bounded-autonomy', OVS), ('policy-enforcement-and-audit', OVS),
              ('evaluating-agentic-systems', EVAL), ('building-agent-eval-suites', EVAL), ('agent-observability', OBS),
              ('evidence-for-autonomy', EVAL),
              ('agent-latency-and-throughput', PERF), ('agent-cost-and-model-routing', PERF),
              ('caching-and-context-budgets', PERF),
              ('versioning-agent-systems', EVOL), ('staged-rollout-and-rollback', EVOL), ('owning-agentic-systems', EVOL),
              ('domain-coding-agents', DOM), ('domain-customer-operations', DOM), ('domain-back-office', DOM),
              ('domain-high-stakes-decisions', DOM),
              ('source-coverage', IVW), ('toolkit', FOUND), ('glossary', FOUND)]:
    CH_TOPIC[pm] = t
corder = {pm: i for i, (f, pm, t) in enumerate(D['chapters'])}

GROUPS = ['Research papers', 'Specifications, standards and regulation', 'Vendor documentation and engineering reports',
          'Incidents, cases and decisions', "Design examples from the author's interview project"]
RES, SPEC, VEND, INC, DES = GROUPS

def dom(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''

LAW_RX = (r'eur-lex\.europa|artificialintelligenceact\.eu|publications\.europa|law\.cornell\.edu|ecfr\.gov|'
          r'legislation\.gov\.uk|federalregister\.gov|gdpr-info|edpb\.europa|ico\.org\.uk|digital-strategy\.ec\.europa|'
          r'hhs\.gov/hipaa|eeoc\.gov|consumerfinance\.gov|regulation \(eu\)|\bgdpr\b|ai act')
TYPE_URL = [  # fallback only, for sources cited under no recognized heading
    (r'arxiv\.org|doi\.org|dl\.acm\.org|aclanthology|openreview|proceedings\.|papers\.nips|pubmed|usenix\.org', RES),
    (r'rfc-editor|datatracker\.ietf|w3\.org|nist\.gov|owasp\.org|modelcontextprotocol\.io|' + LAW_RX, SPEC),
    (r'decisions\.|courtlistener|incident|postmortem', INC),
]

def evidence_type(s):
    cats = [c for c in s['cats'] if c in GROUPS]
    if s['key'].startswith('interview:'): return DES, False
    if cats:
        c = Counter(cats)
        best = max(c, key=lambda g: (c[g], -cats.index(g)))
        return best, len(c) > 1
    u = (s['url'] or '').lower() + ' ' + s['title'].lower()
    return next((t for rx, t in TYPE_URL if re.search(rx, u)), VEND), False

def topic_of(s, ty):
    tu = (s['title'] + ' ' + (s['url'] or '')).lower()
    if ty == DES: return IVW
    if re.search(LAW_RX, tu) and ty in (SPEC, INC): return OVS
    if re.search(r'prompt injection|prompt-injection|jailbreak|indirect injection', tu): return SEC
    if re.search(r'gvisor|firecracker|seccomp|landlock|bubblewrap|nsjail|microvm|sandbox', tu): return SBX
    if re.search(r'(?<![a-z])[a-z0-9τ-]*-?bench\b|benchmark|leaderboard', tu) and ty == RES: return EVAL
    if re.search(r'modelcontextprotocol\.io|a2a-protocol|agent2agent', tu): return TOOLS
    ts = [CH_TOPIC[p] for p in s['chapters'] if p in CH_TOPIC]
    if not ts: return FOUND
    c = Counter(ts)
    first = min(s['chapters'], key=lambda p: corder.get(p, 999))
    return max(c, key=lambda t: (c[t], t == CH_TOPIC.get(first), -t))

unknown = Counter(c for s in D['srcs'] for c in s['cats'] if c not in GROUPS)
for s in D['srcs']:
    s['type'], conflict = evidence_type(s)
    s['type_conflict'] = conflict
    s['topic'] = topic_of(s, s['type'])
for i, T in enumerate(TOPICS):
    print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
    for s in D['srcs']:
        if s['topic'] == i: print('  ', s['type'][:12].ljust(12), '|', s['title'][:60], '|', dom(s), '|', ','.join(p[:14] for p in s['chapters'][:3]))
print('===== evidence types', dict(Counter(s['type'] for s in D['srcs'])))
for c, n in unknown.items(): print('UNKNOWN HEADING', repr(c), n)
for s in D['srcs']:
    if s['type_conflict']:
        print('TYPE CONFLICT', s['title'][:60], '|', dict(Counter(c for c in s['cats'] if c in GROUPS)), '->', s['type'])
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
