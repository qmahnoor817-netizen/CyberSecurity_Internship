"""
Day 17 - Local Network Port & Service Scanning
Sweeps a short list of common ports on a host. Run against 127.0.0.1 or a
host you own/control (e.g., your own lab VM/container) only.
"""
import socket

COMMON_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    5432: "PostgreSQL",
    8080: "HTTP-Alt / Admin console",
}


def scan_local_ports(host: str, ports: list) -> list:
    print(f"[*] Initiating Socket Sweep on: {host}")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        state = sock.connect_ex((host, port))
        if state == 0:
            label = COMMON_PORTS.get(port, "Unknown service")
            print(f"[!] OPEN SERVICE DETECTED: Port {port} ({label})")
            open_ports.append(port)
        sock.close()
    if not open_ports:
        print("[*] No open ports found in the scanned list.")
    return open_ports


if __name__ == "__main__":
    scan_local_ports("127.0.0.1", list(COMMON_PORTS.keys()))
