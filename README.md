# Live Network Packet Sniffer

A lightweight, real-time command-line network packet sniffer and protocol analyzer built in Python using Scapy. This tool hooks directly into Layer 3 network sockets to intercept, decode, and analyze live IP, TCP, and UDP traffic passing through the host's network interface.

## Features
* **Real-Time Analysis:** Dynamically tracks inbound and outbound IP traffic.
* **Protocol Identification:** Distinguishes between TCP, UDP, and other core network protocols.
* **Port Layer Parsing:** Extracts source and destination transport ports to track application traffic.
* **Cross-Platform Compatibility:** Configured with Layer 3 fallback options to ensure smooth execution on Windows architectures without requiring secondary Npcap/WinPcap installations.

## Prerequisites
* Python 3.x
* Scapy Library
  ```bash
  pip install scapy
  
