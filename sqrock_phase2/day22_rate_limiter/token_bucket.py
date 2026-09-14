"""
Day 22 - API Rate Limiting: Token Bucket Logic
Per-client token bucket rate limiter with linear refill.
"""
import time


class RateLimiter:
    def __init__(self, token_capacity: int, refill_rate_per_sec: float):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}

    def allow_request(self, client_ip: str) -> bool:
        now = time.time()
        if client_ip not in self.ledger:
            self.ledger[client_ip] = {"tokens": self.capacity, "last_updated": now}

        state = self.ledger[client_ip]
        elapsed = now - state["last_updated"]
        state["tokens"] = min(self.capacity, state["tokens"] + (elapsed * self.refill_rate))
        state["last_updated"] = now

        if state["tokens"] >= 1:
            state["tokens"] -= 1
            return True
        return False


if __name__ == "__main__":
    limiter = RateLimiter(token_capacity=3, refill_rate_per_sec=0.5)
    client = "203.0.113.9"

    print("[*] Simulating 6 rapid requests from one client (bucket capacity=3):")
    for i in range(1, 7):
        allowed = limiter.allow_request(client)
        print(f"  Request {i}: {'ALLOWED' if allowed else 'BLOCKED (429)'}")

    print("\n[*] Waiting 4 seconds for tokens to refill (rate=0.5/sec -> 2 tokens)...")
    time.sleep(4)
    for i in range(7, 10):
        allowed = limiter.allow_request(client)
        print(f"  Request {i}: {'ALLOWED' if allowed else 'BLOCKED (429)'}")
