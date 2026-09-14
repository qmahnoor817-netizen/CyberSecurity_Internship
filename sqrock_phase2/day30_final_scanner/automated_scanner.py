"""
Day 30 - Final Project: Automated Web Vulnerability Scanner
Integrates reconnaissance, vulnerability checks, and report generation
into one CLI pipeline, reusing logic patterns from across Phase 2.
Lab/authorized-target use only.
"""
import json
import re
import socket
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    requests = None


class AutomatedScanner:
    def __init__(self, target: str):
        self.target = target
        self.findings = []

    # ---- Recon: integrates Day 16 (headers) + Day 17 (ports) + Day 20 (dirs) ----
    def run_recon(self):
        print(f"[*] Running Reconnaissance on {self.target}...")
        parsed = urlparse(self.target)
        host = parsed.hostname or self.target

        # Port sweep (Day 17)
        for port in [80, 443, 8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((host, port)) == 0:
                self.findings.append({"category": "recon", "detail": f"Open port {port} on {host}"})
            sock.close()

        # HTTP header + directory checks (Day 16, 20) — only if requests + live target
        if requests:
            try:
                res = requests.get(self.target, timeout=3)
                for header in ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options"]:
                    if header not in res.headers:
                        self.findings.append({"category": "recon", "detail": f"Missing header: {header}"})
                for path in ["admin", ".env", ".git"]:
                    r = requests.get(f"{self.target}/{path}", timeout=3)
                    if r.status_code == 200:
                        self.findings.append({"category": "recon", "detail": f"Exposed path: /{path} (200 OK)"})
            except requests.RequestException as e:
                self.findings.append({"category": "recon", "detail": f"Target unreachable: {e}"})

    # ---- Vulnerability checks: integrates Day 18 (SQLi) + Day 21 (XSS) ----
    def run_vuln_checks(self):
        print("[*] Executing Vulnerability Audits...")
        sqli_regex = re.compile(r"(?i)('|--|union\s+select|or\s+\d+=\d+)")
        sample_inputs = ["id=5", "id=5' OR '1'='1", "<script>alert(1)</script>"]
        for payload in sample_inputs:
            if sqli_regex.search(payload):
                self.findings.append({"category": "vuln", "detail": f"SQLi-pattern payload flagged: {payload}"})
            if "<script" in payload.lower():
                self.findings.append({"category": "vuln", "detail": f"XSS-pattern payload flagged: {payload}"})

    # ---- Report: integrates Day 27 aggregation pattern ----
    def generate_report(self):
        print(f"[*] Compiling Final Security Report for {self.target}...")
        report = {
            "target": self.target,
            "total_findings": len(self.findings),
            "findings": self.findings,
        }
        with open("final_scan_report.json", "w") as f:
            json.dump(report, f, indent=2)
        print(f"[+] Report saved: final_scan_report.json ({len(self.findings)} findings)")
        return report


if __name__ == "__main__":
    print("=== SQROCK INTERNSHIP FINAL PROJECT ===")
    scanner = AutomatedScanner("http://localhost:8000")  # point at your own lab target
    scanner.run_recon()
    scanner.run_vuln_checks()
    scanner.generate_report()
    print("[-] Scan Complete.")
