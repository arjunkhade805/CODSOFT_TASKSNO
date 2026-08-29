# Task 1 - Network Packet Analyzer

## Objective
- Develop a Python application to capture packets transmitted over a network.
- Inspect captured packets to understand network communication and protocol behavior.
- Extract important details such as source IP, destination IP, protocol type, and packet data.
- Use Python libraries such as Scapy or Socket to perform packet capturing.
- Present the captured information in a clear and organized format.

## Tools & Libraries Used
- Python 3
- Scapy

## How It Works
The script uses Scapy's `sniff()` function to capture live packets on the network interface. For each captured packet, it checks the protocol (TCP, UDP, or ICMP), then extracts:
- Source IP address
- Destination IP address
- Source port / Destination port (if applicable)
- Protocol type
- Packet length

The extracted details are printed to the console in real time and also saved to a CSV file (`captured_packets.csv`) for organized record-keeping.

## How to Run
```bash
pip install scapy
sudo python3 packet_analyzer.py
```
(Run as Administrator on Windows, with Npcap installed)

## Sample Output
