"""
Day 19 - Docker Container Misconfiguration Scanner
Static-analyzes a Dockerfile for common security misconfigurations.
"""


def analyze_dockerfile(path: str):
    print(f"[*] Parsing Container Directives: {path}\n")
    has_explicit_user = False
    findings = []
    try:
        with open(path, 'r') as file:
            for idx, line in enumerate(file, 1):
                cleaned = line.strip().upper()
                if cleaned.startswith("USER"):
                    has_explicit_user = True
                if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                    msg = f"[RISK DETECTED] Line {idx}: Base image uses unpinned 'latest' tag."
                    print(msg)
                    findings.append(msg)
                if "EXPOSE 22" in cleaned:
                    msg = f"[CRITICAL] Line {idx}: Container exposes SSH (port 22)."
                    print(msg)
                    findings.append(msg)
        if not has_explicit_user:
            msg = "[RISK DETECTED] No explicit USER instruction — container runs as root by default."
            print(msg)
            findings.append(msg)
        if not findings:
            print("[+] No misconfigurations detected.")
    except FileNotFoundError:
        print(f"[!] File not found: {path}")
    return findings


if __name__ == "__main__":
    analyze_dockerfile("sample_dockerfile.txt")
