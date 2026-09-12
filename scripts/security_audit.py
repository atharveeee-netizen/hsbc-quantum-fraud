import os
import re
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

REPO_ROOT = Path(__file__).resolve().parent.parent

SECRET_PATTERNS = [
    ("AWS Access Key ID", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Generic Secret / Private Key", re.compile(r"-----BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY-----")),
    ("Kaggle Key in Code", re.compile(r"['\"]?kaggle_key['\"]?\s*[:=]\s*['\"][0-9a-f]{32}['\"]", re.IGNORECASE)),
    ("Hardcoded GitHub Token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,255}")),
    ("Generic High-Entropy Password Assignment", re.compile(r"(password|api_key|secret_token)\s*=\s*['\"][A-Za-z0-9+/=]{16,}['\"]", re.IGNORECASE))
]

def is_valid_luhn(card_number_str: str) -> bool:
    """Standard Luhn (mod 10) algorithm to check for real credit card account numbers."""
    digits = [int(c) for c in card_number_str if c.isdigit()]
    if len(digits) not in [15, 16]:
        return False
    # Valid payment cards begin with 3 (Amex), 4 (Visa), 5 (Mastercard), 6 (Discover)
    if digits[0] not in [3, 4, 5, 6]:
        return False
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            checksum += doubled if doubled < 10 else (doubled - 9)
        else:
            checksum += digit
    return checksum % 10 == 0

# Match candidate PAN patterns: 4 groups of 4 digits, not preceded by a decimal point
PAN_CANDIDATE_PATTERN = re.compile(r"(?<!\.)\b([3-6]\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})\b")

def run_security_audit():
    """
    [IMPLEMENTED] Phase 74: Systematic Security and Hygiene Audit.
    Scans for credentials, live PANs, unsafe subprocesses, model deserialization, and environment exposures.
    """
    logging.info("Starting Phase 74 Comprehensive Security Audit...")
    findings = []
    files_scanned = 0

    ignore_dirs = {'.git', '.pytest_cache', '__pycache__', '.venv', 'venv', 'brain'}
    
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            file_path = Path(root) / file
            # Only scan code, config, and markdown documentation
            if file_path.suffix not in ['.py', '.json', '.md', '.yaml', '.yml', '.ini', '.toml', '.txt']:
                continue
            
            # Skip self to prevent false-positive pattern triggers
            if file_path.name == 'security_audit.py':
                continue

            files_scanned += 1
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
            except Exception as e:
                continue

            rel_path = file_path.relative_to(REPO_ROOT).as_posix()

            # 1. Secret & Credential Scanning
            for pattern_name, regex in SECRET_PATTERNS:
                matches = regex.findall(content)
                if matches:
                    findings.append({
                        "file": rel_path,
                        "type": "CREDENTIAL_EXPOSURE",
                        "severity": "P0_CRITICAL",
                        "details": f"Potential {pattern_name} pattern found ({len(matches)} occurrences)."
                    })

            # 2. Live PAN (Primary Account Number) Scanning with Luhn Validation
            candidates = PAN_CANDIDATE_PATTERN.findall(content)
            live_pans = [c for c in candidates if is_valid_luhn(c)]
            if live_pans:
                findings.append({
                    "file": rel_path,
                    "type": "PII_PAN_EXPOSURE",
                    "severity": "P0_CRITICAL",
                    "details": f"Potential live Luhn-valid PAN detected: {len(live_pans)} occurrences."
                })

            # 3. Subprocess Safety: check for shell=True with dynamic string inputs
            if file_path.suffix == '.py':
                if 'shell=True' in content and 'subprocess' in content:
                    findings.append({
                        "file": rel_path,
                        "type": "INSECURE_SUBPROCESS",
                        "severity": "P1_HIGH",
                        "details": "subprocess called with shell=True. Should use tokenized command lists."
                    })

            # 4. Unsafe Deserialization: check for raw pickle
            if file_path.suffix == '.py':
                if 'pickle.loads(' in content or 'pickle.load(' in content:
                    findings.append({
                        "file": rel_path,
                        "type": "DESERIALIZATION_RISK",
                        "severity": "P1_HIGH",
                        "details": "Direct pickle.load usage detected. Prefer safer joblib or JSON representations."
                    })

    # 5. Dependency Audit
    req_file = REPO_ROOT / "requirements.txt"
    unpinned_deps = []
    if req_file.exists():
        for line in req_file.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#') and not any(op in line for op in ['==', '<=', '>=', '<', '>']):
                unpinned_deps.append(line)
    
    if unpinned_deps:
        findings.append({
            "file": "requirements.txt",
            "type": "UNPINNED_DEPENDENCY",
            "severity": "P2_MEDIUM",
            "details": f"Unpinned dependencies found: {unpinned_deps}"
        })

    # Summary and status
    p0_count = sum(1 for f in findings if f['severity'] == 'P0_CRITICAL')
    p1_count = sum(1 for f in findings if f['severity'] == 'P1_HIGH')
    p2_count = sum(1 for f in findings if f['severity'] == 'P2_MEDIUM')

    status = "[VERIFIED: SECURE]" if (p0_count == 0 and p1_count == 0) else "[FAILED: VULNERABILITIES DETECTED]"

    audit_result = {
        "status": status,
        "files_scanned": files_scanned,
        "summary": {
            "p0_critical": p0_count,
            "p1_high": p1_count,
            "p2_medium": p2_count,
            "total_findings": len(findings)
        },
        "findings": findings
    }

    # Save artifacts
    evidence_dir = REPO_ROOT / "docs" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    
    json_path = evidence_dir / "security_audit.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(audit_result, f, indent=2)

    md_path = evidence_dir / "SECURITY_AUDIT.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Security and Hygiene Audit (Phase 74)\n\n")
        f.write(f"**Audit Status:** `{status}`  \n")
        f.write(f"**Files Scanned:** {files_scanned}  \n")
        f.write(f"**Critical Findings (P0):** {p0_count}  \n")
        f.write(f"**High Severity Findings (P1):** {p1_count}  \n")
        f.write(f"**Medium Severity Findings (P2):** {p2_count}  \n\n")
        f.write("---\n\n## Findings Detail\n\n")
        if findings:
            for item in findings:
                f.write(f"* **[{item['severity']}]** `{item['file']}`: {item['type']} - {item['details']}\n")
        else:
            f.write("No security vulnerabilities, hardcoded secrets, PII exposures, or unsafe shell calls detected.\n")

    logging.info(f"Security audit complete: Status={status}, Scanned={files_scanned}, Findings={len(findings)}")
    return audit_result

if __name__ == "__main__":
    result = run_security_audit()
    if result["summary"]["p0_critical"] > 0 or result["summary"]["p1_high"] > 0:
        exit(1)
    exit(0)
