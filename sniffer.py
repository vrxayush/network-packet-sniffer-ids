from scapy.all import sniff, IP, TCP, UDP, ICMP
from database import save_packet
from analyzer import detect_port_scan
