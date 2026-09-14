"""
Day 7 - Defensive rate limiter for the lab Flask server.
Blocks an IP after N failed attempts within a time window.
"""
import time
from collections import defaultdict
from flask import Flask, request, jsonify

app = Flask(__name__)
REAL_PASSWORD = "S3cur3P@ss!"

MAX_ATTEMPTS = 3
WINDOW_SECONDS = 60
failures = defaultdict(list)  # ip -> [timestamps]


def is_locked_out(ip: str) -> bool:
    now = time.time()
    failures[ip] = [t for t in failures[ip] if now - t < WINDOW_SECONDS]
    return len(failures[ip]) >= MAX_ATTEMPTS


@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    if is_locked_out(ip):
        return jsonify({"error": "Too many attempts. Try again later."}), 429

    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == REAL_PASSWORD:
        failures[ip] = []  # reset on success
        return "Welcome admin!", 200

    failures[ip].append(time.time())
    return "Invalid credentials", 401


if __name__ == "__main__":
    app.run(port=5000)
