"""
Day 13 - SIEM Log Analysis for SE Attack Detection
Parses a sample log for social-engineering-related anomalies:
brute-force patterns and suspicious mailbox rule creation.
"""
import re
from collections import Counter

LOG_SAMPLE = """
2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:16 SUCCESS_LOGIN user=admin ip=45.33.32.156
2024-01-15 08:00:01 SUCCESS_LOGIN user=riya ip=192.168.1.10
2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
2024-01-15 03:10:02 FAILED_LOGIN user=jsmith ip=88.12.4.9
2024-01-15 03:10:05 FAILED_LOGIN user=jsmith ip=88.12.4.9
2024-01-15 03:10:08 FAILED_LOGIN user=jsmith ip=88.12.4.9
2024-01-15 03:10:11 FAILED_LOGIN user=jsmith ip=88.12.4.9
2024-01-15 09:15:00 EMAIL_RULE_CREATED user=jsmith rule=delete_and_forward
2024-01-15 23:58:03 SUCCESS_LOGIN user=admin ip=45.33.32.156
"""


def analyze_logs(logs: str):
    fails = re.findall(r'FAILED_LOGIN user=(\w+) ip=([\d.]+)', logs)
    rules = re.findall(r'EMAIL_RULE_CREATED user=(\w+) rule=(\w+)', logs)
    off_hours_success = re.findall(
        r'(\d{2}):\d{2}:\d{2} SUCCESS_LOGIN user=(\w+) ip=([\d.]+)', logs)

    alerts = []

    fail_counts = Counter(u for u, _ in fails)
    for user, count in fail_counts.items():
        if count >= 3:
            alerts.append(f"[ALERT] Brute force detected: {user} ({count} failures)")

    for user, rule in rules:
        if rule in ("forward_all", "delete_and_forward"):
            alerts.append(f"[ALERT] Suspicious mail-forwarding rule created by: {user} ({rule})")
        else:
            alerts.append(f"[INFO] Mail rule created by: {user} ({rule})")

    for hour, user, ip in off_hours_success:
        if int(hour) < 6 or int(hour) >= 22:
            alerts.append(f"[ALERT] Off-hours login success: {user} at {hour}:00 from {ip}")

    for a in alerts:
        print(a)
    return alerts


if __name__ == "__main__":
    analyze_logs(LOG_SAMPLE)
