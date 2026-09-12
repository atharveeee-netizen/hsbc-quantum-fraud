import os
import re
import json

repo_root = '.'
search_terms = [
    '0.8845',
    '0.9412',
    '0.641',
    '13 seeds',
    '5 temporal windows',
    '14.8%',
    '€1.2M',
    '$1.2M',
    '0.40',
    '0.60',
    '185 ms hardware',
    '185ms hardware',
    'hardware 185',
    'quantum advantage demonstrated',
    'causal driver',
    'dimension collapse',
    '100% reproducible',
    'verified secure'
]

results = {term: [] for term in search_terms}

for root, dirs, files in os.walk(repo_root):
    if any(p in root for p in ['.git', '.pytest_cache', '__pycache__', 'models', 'data', 'renders']):
        continue
    for f in files:
        if f.endswith(('.csv', '.parquet', '.zip', '.png', '.pdf', '.docx', '.svg')):
            continue
        if f in ['stale_claim_audit.json', 'claim_firewall_audit.json']:
            continue
        fpath = os.path.join(root, f)
        relpath = os.path.relpath(fpath, repo_root)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                for line_no, line in enumerate(fp, 1):
                    for term in search_terms:
                        if term.lower() in line.lower():
                            results[term].append({
                                'file': relpath,
                                'line': line_no,
                                'text': line.strip()
                            })
        except Exception:
            pass

for term, occurrences in results.items():
    print(f'=== Term: "{term}" ({len(occurrences)} occurrences) ===')
    for occ in occurrences[:10]:
        print(f'  {occ["file"]}:{occ["line"]}: {occ["text"][:120]}')
    if len(occurrences) > 10:
        print(f'  ... and {len(occurrences)-10} more')

with open('docs/evidence/stale_claim_audit.json', 'w', encoding='utf-8') as fp:
    json.dump(results, fp, indent=2)
