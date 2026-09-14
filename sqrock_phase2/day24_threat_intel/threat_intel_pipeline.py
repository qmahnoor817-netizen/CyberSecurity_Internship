"""
Day 24 - Automated Threat Intel IP Blocking Pipeline
Ingests a (mock) threat intel feed and simulates firewall rule updates
based on risk score. No real firewall is modified by this script.
"""
import json

MOCK_INTEL_FEED = [
    {"ip": "103.45.67.89", "indicator": "malware_c2", "risk_score": 98},
    {"ip": "185.10.11.12", "indicator": "botnet_node", "risk_score": 85},
    {"ip": "198.51.100.33", "indicator": "brute_forcer", "risk_score": 92},
    {"ip": "192.0.2.44", "indicator": "port_scanner", "risk_score": 60},
]


def update_firewall_rules(feed_data: list, risk_threshold: int = 90):
    print("[*] Ingesting Threat Intelligence Feed...")
    blocked = []
    for entry in feed_data:
        score = entry.get("risk_score", 0)
        if score > risk_threshold:
            print(f"[ACTION] HIGH RISK - Deploying block rule for IP: {entry['ip']} (Reason: {entry['indicator']}, score={score})")
            blocked.append(entry)
        else:
            print(f"[*] LOGGING - Suspicious activity monitored for IP: {entry['ip']} (score={score})")

    with open("blocklist.json", "w") as f:
        json.dump(blocked, f, indent=2)
    print(f"\n[+] {len(blocked)} IP(s) written to blocklist.json")
    return blocked


if __name__ == "__main__":
    update_firewall_rules(MOCK_INTEL_FEED)
