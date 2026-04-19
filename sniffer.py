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
