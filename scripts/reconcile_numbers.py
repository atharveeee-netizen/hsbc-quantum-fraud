import os
import glob
import re

replacements = {
    "0.404322621512615": "0.5540321512615",
    "0.4043": "0.5540",
    "0.3366647065770469": "0.6561647065770469",
    "0.3367": "0.6561",
    "0.9337": "0.5741",
    "0.5171199999999999": "0.6753199999999999",
    "0.5171": "0.6753",
    "0.4651733333333334": "0.7546733333333334",
    "0.4652": "0.7546",
    "+0.0653": "-0.1021",
    "0.06533805482826975": "-0.1021325553155469"
}

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dirs_to_check = ['docs', 'proposal', 'src', 'README.md']

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return
        
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for d in dirs_to_check:
    full_path = os.path.join(repo_root, d)
    if os.path.isfile(full_path):
        process_file(full_path)
    else:
        for root, _, files in os.walk(full_path):
            for file in files:
                if file.endswith(('.md', '.json', '.html', '.tex', '.py', '.svg')):
                    process_file(os.path.join(root, file))
