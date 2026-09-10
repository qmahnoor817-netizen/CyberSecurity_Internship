"""
Day 7 - Local Flask test server (the ATTACK TARGET for this lab).
Run this first, in a separate terminal, before running brute_force_sim.py.
This is a toy server for YOUR OWN localhost lab only.
"""
from flask import Flask, request

app = Flask(__name__)
REAL_PASSWORD = "S3cur3P@ss!"  # intentionally NOT in the wordlist, for demo


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == REAL_PASSWORD:
        return "Welcome admin!", 200
    return "Invalid credentials", 401


if __name__ == "__main__":
    app.run(port=5000)
