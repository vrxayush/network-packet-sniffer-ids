from collections import defaultdict

scan_tracker = defaultdict(set)

def detect_port_scan(packet):
    src = packet["src"]
    port = packet["port"]

    if port:
        scan_tracker[src].add(port)

    # 🔥 LOWER threshold for demo
    if len(scan_tracker[src]) == 3:
        return f"Port Scan Detected: {src}"

    return None
