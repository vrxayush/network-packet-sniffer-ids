from scapy.all import sniff, IP, TCP, UDP, ICMP
from database import save_packet
from analyzer import detect_port_scan
def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]

        protocol = "OTHER"
        port = None

        if TCP in packet:
            protocol = "TCP"
            port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            port = packet[UDP].dport

        data = {
            "src": ip_layer.src,
            "dst": ip_layer.dst,
            "protocol": protocol,
            "port": port
        }

        alert = detect_port_scan(data)
        print(f"[+] Packet: {data['src']} → {data['dst']} ({data['protocol']})")

        if alert:
            print(alert)

        save_packet(data, alert)   # 🔥 THIS IS THE FIX

def start_sniffing():
    sniff(prn=process_packet, store=False)
