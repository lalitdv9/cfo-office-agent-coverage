"""
build_matrix.py -- rebuilds coverage_matrix.csv from its inputs.

NOTE ON REPRODUCIBILITY: this script's second input, matrix_rows_agent.csv,
was a working-directory scratch file (per-paper long-form scoring rationale)
that was never included in the released artifact set. Without it, this script
cannot run end-to-end from this repo alone -- coverage_matrix.csv is the
released, authoritative output, and recount.py verifies every count in the
paper against it directly. Use recount.py to check the paper; use this file
only to see how the matrix was assembled.
"""

#!/usr/bin/env python3
"""Consolidate coverage matrix from scaffold + agent rows + direct-read rows.
Provenance build: run from the repository root. 2026-07-16."""
import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

LEAVES = ['1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','2.1','2.2','2.3','2.4','2.5','2.6','2.7',
          '3.1','3.2','3.3','3.4','4.1','4.2','4.3','4.4','5.1','5.2','5.3','6.1','6.2','6.3',
          '7.1','7.2','7.3','9.1','9.2']
HDR = ['bibkey','band','eval_method','data_realism','agent_scope','headline'] + LEAVES + ['evidence_note']

def parse_cells(s):
    out = {}
    for part in (s or '').replace('◐',':P').replace('●',':F').split(';'):
        part = part.strip()
        if not part: continue
        if ':' in part:
            leaf, lvl = part.split(':',1)
            leaf, lvl = leaf.strip(), lvl.strip().upper()[:1]
            if leaf in LEAVES and lvl in 'FP': out[leaf] = lvl
    return out

rows = {}
with open('coverage_matrix.csv') as f:          # scaffold (18)
    for r in csv.DictReader(f): rows[r['bibkey']] = r

with open('matrix_rows_agent.csv') as f:        # agent + direct reads
    for r in csv.DictReader(f):
        cells = parse_cells(r['leaf_cells'])
        rec = {'bibkey':r['bibkey'],'band':r['band'],'eval_method':r['eval_method'],
               'data_realism':r['data_realism'],'agent_scope':r['agent_scope'],
               'headline':r['headline'],'evidence_note':r['note_file']}
        for l in LEAVES: rec[l] = cells.get(l,'')
        rows[r['bibkey']] = rec                        # later rows overwrite (finch dedupe)

# v1.2 completeness-audit cells (APQC PCF check, 2026-07-16): leaf 1.8 evidence
if 'cfagentbench2026' in rows: rows['cfagentbench2026']['1.8'] = 'P'   # Project Accounting domain, 157 specs [spec-vs-exec]
if 'finbalance2026' in rows: rows['finbalance2026']['1.8'] = 'P'       # asset-disposal/rollforward concept flags

def add(bibkey, band, ev, dr, sc, hl, cells, note):
    rec = {'bibkey':bibkey,'band':band,'eval_method':ev,'data_realism':dr,
           'agent_scope':sc,'headline':hl,'evidence_note':note}
    c = parse_cells(cells)
    for l in LEAVES: rec[l] = c.get(l,'')
    rows[bibkey] = rec

# direct main-assistant reads (2026-07-16)
add('fintagging2025','core','zero-shot deterministic extraction+alignment metrics',
    'real XBRL/US-GAAP reporting content (text+tables)','single-turn structured extraction (non-agentic)',
    'full-scope table-aware XBRL tagging vs 10k+ US-GAAP taxonomy (FinNI+FinCL); results tables not parsed',
    '1.7:P','notes/fintagging2025.md')
add('finsheetbench2026','adjacent','deterministic QA/numeric-reasoning accuracy',
    'synthetic, modeled on real PE fund structures','single-turn QA over serialized spreadsheets',
    "best Gemini 3.1 Pro 82.4% over 24 files; largest file (152 companies, 8 funds) avg 48.6% vs 86.2% easiest (Abstract)",
    '2.5:P; 6.2:P','notes/finsheetbench2026.md')
add('finauditing2025','core','zero-shot unified retrieval/classification/reasoning metrics',
    'real US-GAAP XBRL filings','single-turn multi-document reasoning (non-agentic)',
    "13 LLMs: 'accuracy drops of up to 60-90% when reasoning over hierarchical multi-document structures' (Abstract)",
    '1.7:P','notes/finauditing2025.md')
# from the internal ft_decisions_D/E full-text-screening worksheets
# (working-directory scratch CSVs, not part of this release; cells transcribed into notes/)
add('coffeebench2026','cross-domain','execution-based simulation (net-income KPI)',
    'synthetic multi-agent coffee-economy sim (Sakana AI + KPMG AZSA)','long-horizon multi-agent (ReAct, 90 days)',
    'GPT-5.5 best +3109 net income vs passive -2765; agent state incl. AR/AP+cash, net-30 invoices, bad-debt writeoffs',
    '3.1:P; 7.1:P; 7.2:P','notes/2606_16613.md')
add('auditcopilot2025','audit','F1 vs pseudo-labels (circularity flagged) + synthetic labels',
    'synthetic ledgers (5000 IDs, 1% anomalies) + real anonymized ledger','single-turn anomaly detection (prompt-tuned open-weight LLMs)',
    'Mistral-8B F1 0.94 vs IsolationForest 0.68 (synthetic); Gemma-7B 0.83 (real)',
    '1.1:P','notes/2512_02726.md')
add('sheetagent2024','cross-domain','SheetRM benchmark (317 exam-sourced tasks); execution checks',
    'real exam-sourced workbooks incl. finance assets (PayrollSummary, Deposit journal, BudgetForecast, TaxFilingSummary)',
    'multi-step spreadsheet agent (Planner/Informer/Retriever)',
    'general spreadsheet agent; analysis restricted to finance-workbook subset per E6 rule',
    '2.5:P; 7.3:P','notes/2403_03636.md')
add('spreadsheetarena2026','cross-domain','live pairwise human preference (4,357 votes) + 52-battle expert rubric study',
    'live arena prompts incl. dedicated Corporate Finance & FP&A category','single-shot end-to-end workbook generation (16 models)',
    'finance expert-rubric study: mean expert rating 2.87/5 on DCF/LBO/waterfall prompts; models fail professional modeling conventions',
    '2.5:F','notes/2603_10002.md')
add('theagentcompany2024','cross-domain','checkpoint-based deterministic graders',
    'simulated software company (GitLab/ownCloud/Plane/Rocket.Chat + LLM NPCs)','long-horizon multi-app single agent (175 tasks)',
    'expert-curated 12-task Finance subset (e.g., IRS Form 6765 from company financials); Finance among WORST categories; top agent 30% overall',
    '4.2:P; 2.5:P','notes/2412_14161.md')
# pending rows (no cells; listed for completeness)
for bk, band in [('xbrltagrec2026','core'),('acctreasoning2025','core'),('finrulebench2026','core'),
                 ('finverbench2026','core'),('lava2025','audit'),('xbrlagent2024','core')]:
    add(bk, band+' (PENDING-FULLTEXT — no cells scored)','—','—','—','full-text read pending; excluded from v1 analysis','','')

order_band = {'core':0,'benchmark+system':0,'cross-domain':1,'adjacent':2,'audit':3}
out = sorted(rows.values(), key=lambda r:(order_band.get(r['band'].split(' ')[0],4), r['bibkey']))
with open('coverage_matrix.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=HDR); w.writeheader()
    for r in out: w.writerow({k:r.get(k,'') for k in HDR})

# census
from collections import Counter
cnt = Counter(); scored = [r for r in out if 'PENDING' not in r['band']]
for r in scored:
    for l in LEAVES:
        if r.get(l): cnt[l] += 1
empty = [l for l in LEAVES if cnt[l]==0]
print(f"matrix rows: {len(out)} ({len(scored)} scored, {len(out)-len(scored)} pending)")
print("cells filled:", sum(cnt.values()))
print("EMPTY columns:", empty)
print("near-empty (1 paper):", [l for l in LEAVES if cnt[l]==1])
