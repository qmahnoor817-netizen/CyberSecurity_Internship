"""
Day 8 - USB Drop Attack Simulation (BENIGN)
Logs local system info to a text file to demonstrate what a malicious
autorun payload could collect - performs no exfiltration, no network
calls, no persistence, and no destructive action.
"""
import platform
import socket
import datetime
import os


def usb_payload_sim(output_file="recon_log.txt"):
    info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd(),
    }
    with open(output_file, "w") as f:
        for k, v in info.items():
            f.write(f"{k}: {v}\n")
    print(f"[SIM] Recon data saved to {output_file}")
    return info

if __name__ == "__main__":
    usb_payload_sim()
    
