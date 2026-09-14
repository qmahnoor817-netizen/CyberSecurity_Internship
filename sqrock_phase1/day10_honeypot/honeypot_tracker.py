"""
Day 10 - Baiting & Watering Hole: Honeypot link tracker.
Logs visits to a 'bait' link on localhost - for awareness demos only.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

LOG = []


class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?"),
        }
        LOG.append(entry)
        print(json.dumps(entry))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting!")

    def log_message(self, *args):
        pass  # suppress default console noise


def dump_log(path="honeypot_log.json"):
    with open(path, "w") as f:
        json.dump(LOG, f, indent=2)


if __name__ == "__main__":
    print("Honeypot running on http://localhost:8080  (Ctrl+C to stop and save log)")
    try:
        HTTPServer(("", 8080), HoneyHandler).serve_forever()
    except KeyboardInterrupt:
        dump_log()
        print("\nLog saved to honeypot_log.json")
