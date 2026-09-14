"""
Day 28 - SIEM Alert Trigger Automation via Webhooks
Formats and (optionally) dispatches a security alert payload to a
chat-ops webhook (Slack/Teams-style). Network call is commented out
by default so this is safe to run without a real webhook configured -
uncomment the requests.post line and supply your own webhook URL to
actually send it.
"""
import json

try:
    import requests
except ImportError:
    requests = None


def send_alert_webhook(webhook_url: str, alert_data: dict):
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": (
            f"**CRITICAL SECURITY ALERT**\n"
            f"**Type:** {alert_data['type']}\n"
            f"**Source:** {alert_data['ip']}\n"
            f"**Time:** {alert_data.get('time', 'n/a')}"
        )
    }

    print(f"[*] Dispatching webhook to {webhook_url[:30]}...")
    print(f"[*] Payload: {json.dumps(payload, indent=2)}")

    # Uncomment to actually send, once you have a real webhook URL configured:
    # if requests:
    #     response = requests.post(webhook_url, headers=headers, data=json.dumps(payload), timeout=5)
    #     print(f"[+] Webhook responded with status: {response.status_code}")
    # else:
    #     print("[!] requests library not installed - run: pip install requests")

    print("[+] Webhook dispatch simulated successfully (network call disabled by default).")


if __name__ == "__main__":
    send_alert_webhook(
        "https://hooks.slack.com/services/T000/B000/XXX",
        {"type": "Multiple Failed Logins", "ip": "10.0.0.5", "time": "2026-09-14 03:12:00"},
    )
