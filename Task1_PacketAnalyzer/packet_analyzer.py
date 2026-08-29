"""
CodSoft Cybersecurity Internship - Task 1
Network Packet Analyzer
Author: [Your Name]
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv

# Create/open CSV file to store captured packet data
csv_file = open("captured_packets.csv", mode="a", newline="")
writer = csv.writer(csv_file)
writer.writerow(["Timestamp", "Source IP", "Destination IP", "Protocol", "Src Port", "Dst Port", "Length"])

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            proto_name = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            proto_name = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif ICMP in packet:
            proto_name = "ICMP"
            sport = dport = "-"
        else:
            proto_name = f"Other({packet[IP].proto})"
            sport = dport = "-"

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {src_ip}:{sport} -> {dst_ip}:{dport} | {proto_name} | Len: {len(packet)}")
        writer.writerow([timestamp, src_ip, dst_ip, proto_name, sport, dport, len(packet)])

print("Starting packet capture... Press Ctrl+C to stop.")
try:
    sniff(prn=process_packet, store=False, count=50)
except KeyboardInterrupt:
    print("Capture stopped by user.")
finally:
    csv_file.close()
    print("Data saved to captured_packets.csv")
