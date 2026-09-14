"""
Day 27 - Automated Vulnerability Report Aggregator
Merges findings from multiple (mocked) security tool outputs into one
unified, prioritized summary.
"""
import json

# Mocked outputs standing in for real tool exports (Bandit, Trivy, npm audit, etc.)
MOCK_TOOL_OUTPUTS = [
    {"tool": "Bandit", "vuln": "Hardcoded Password", "severity": "HIGH", "location": "app/config.py:12"},
    {"tool": "Trivy", "vuln": "CVE-2024-XXXX in libcurl", "severity": "CRITICAL", "location": "base-image"},
    {"tool": "Bandit", "vuln": "Use of eval()", "severity": "MEDIUM", "location": "app/utils.py:44"},
    {"tool": "Trivy", "vuln": "Outdated OpenSSL package", "severity": "LOW", "location": "base-image"},
    {"tool": "npm-audit", "vuln": "Prototype Pollution in lodash", "severity": "HIGH", "location": "package.json"},
]

SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


def aggregate_reports(tool_outputs: list, min_severity: str = "HIGH") -> list:
    print("[*] Aggregating Vulnerability Scans...")
    threshold = SEVERITY_ORDER[min_severity]
    unified = []
    for issue in tool_outputs:
        if SEVERITY_ORDER.get(issue["severity"], 99) <= threshold:
            unified.append(issue)
            print(f"[+] Aggregated: {issue['vuln']} (Source: {issue['tool']}, Severity: {issue['severity']}, Location: {issue['location']})")

    unified.sort(key=lambda i: SEVERITY_ORDER[i["severity"]])
    with open("unified_findings.json", "w") as f:
        json.dump(unified, f, indent=2)
    print(f"\n[+] {len(unified)} finding(s) at {min_severity}+ severity written to unified_findings.json")
    return unified


if __name__ == "__main__":
    aggregate_reports(MOCK_TOOL_OUTPUTS, min_severity="HIGH")
