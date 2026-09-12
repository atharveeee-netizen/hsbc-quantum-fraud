import os
import re
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

REPO_ROOT = Path(__file__).resolve().parent.parent

# Phrases that are strictly prohibited anywhere in documentation or code (Phases 81, 96)
STRICTLY_PROHIBITED = [
    r"quantum supremacy",
    r"quantum superiority",
    r"proven quantum advantage",
    r"demonstrated quantum advantage",
    r"production-ready quantum",
    r"production quantum expert",
    r"quantum computing solves",
    r"quantum model is superior",
    r"amount causes fraud",
    r"amount is a causal",
    r"transaction amount is the dominant causal driver",
    r"100% secure",
    r"100% reproducible",
    r"hardware validation proves"
]

# Phrases that require explicit negative/inconclusive qualification
QUALIFIED_PHRASES = [
    (r"quantum advantage", [
        r"no .*quantum advantage", r"no quantum advantage", r"outcome b",
        r"not yet established", r"inconclusive", r"advantage taxonomy",
        r"does not demonstrate", r"failed to demonstrate", r"cannot assume",
        r"not demonstrated", r"lack of", r"testing for", r"potential",
        r"claim"
    ]),
    (r"hardware validated", [r"not hardware validated", r"hardware pending", r"blocked", r"not justified"])
]

def audit_claim_firewall():
    """
    [IMPLEMENTED] Phase 76: Enforces scientific claim firewall rules across documentation and code.
    Prevents unsupported marketing claims or ungrounded assertions.
    """
    logging.info("Starting Phase 76 Claim Firewall Audit...")
    violations = []
    
    scanned_extensions = ['.md', '.py', '.json']
    ignore_dirs = {'.git', '.pytest_cache', '__pycache__', '.venv', 'venv'}

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            path = Path(root) / file
            if path.suffix not in scanned_extensions:
                continue
            if path.name in ['audit_claim_firewall.py', 'claim_firewall_audit.json', 'audit_stale_claims.py', 'stale_claim_audit.json']:
                continue

            try:
                content = path.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue

            rel_path = path.relative_to(REPO_ROOT).as_posix()

            # 1. Check strictly prohibited phrases
            for pattern in STRICTLY_PROHIBITED:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    violations.append({
                        "file": rel_path,
                        "type": "STRICTLY_PROHIBITED_CLAIM",
                        "pattern": pattern,
                        "count": len(matches)
                    })

            # 2. Check qualified phrases in markdown docs
            if path.suffix == '.md':
                for target, allowed_contexts in QUALIFIED_PHRASES:
                    for line_no, line in enumerate(content.splitlines(), start=1):
                        if re.search(target, line, re.IGNORECASE):
                            # Ensure line or surrounding context contains at least one allowed qualifying keyword
                            is_qualified = any(re.search(ac, line, re.IGNORECASE) for ac in allowed_contexts)
                            if not is_qualified:
                                # Also check if line is simply a question (e.g. "Does quantum have an advantage?")
                                if "?" in line or "Question" in line or "Q2" in line:
                                    continue
                                violations.append({
                                    "file": f"{rel_path}:{line_no}",
                                    "type": "UNQUALIFIED_ADVANTAGE_ASSERTION",
                                    "content": line.strip()
                                })

    status = "[VERIFIED: FIREWALL CLEAN]" if len(violations) == 0 else "[FAILED: FIREWALL VIOLATIONS]"
    
    result = {
        "status": status,
        "violation_count": len(violations),
        "violations": violations
    }

    evidence_dir = REPO_ROOT / "docs" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    
    with open(evidence_dir / "claim_firewall_audit.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    logging.info(f"Claim firewall audit: status={status}, violations={len(violations)}")
    return result

if __name__ == "__main__":
    res = audit_claim_firewall()
    if res["violation_count"] > 0:
        for v in res["violations"]:
            logging.error(f"Firewall Violation: {v}")
        exit(1)
    exit(0)
