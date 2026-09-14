"""
Day 20 - Web Directory Brute-Force Simulation
Audits which paths respond on your OWN local lab server.
Run only against http://localhost or a lab target you control.
"""
import requests

WORDLIST = ["admin", "dashboard", "api/v1", ".env", "backup.sql", ".git", "config.php"]


def audit_directory_paths(base_url: str, wordlist: list):
    print(f"[*] Discovering endpoints for: {base_url}")
    found = []
    for directory in wordlist:
        target_path = f"{base_url}/{directory}"
        try:
            response = requests.get(target_path, timeout=3)
            if response.status_code == 200:
                print(f"[MATCH DETECTED] Route accessible: {target_path} (Status: 200)")
                found.append((target_path, 200))
            elif response.status_code == 403:
                print(f"[RESTRICTED ROUTE] Forbidden resource mapped: {target_path} (Status: 403)")
                found.append((target_path, 403))
        except requests.RequestException:
            pass
    if not found:
        print("[*] No matching or restricted routes found.")
    return found


if __name__ == "__main__":
    audit_directory_paths("http://localhost:5000", WORDLIST)
