from scapy.all import sniff, conf # Added 'conf' here
import analyzer

# This line forces Scapy to use Layer 3 sockets so it works on Windows without Npcap/WinPcap
conf.L3socket = conf.L3socket6

def packet_callback(packet):
    """This function runs automatically every time a packet is captured."""
    data = analyzer.analyze_packet(packet)
    
    # If it's a valid IP packet, print out its network routing path
    if data:
        print(f"[{data['proto']}] {data['src']} -> {data['dst']} | {data['info']} ({data['size']} bytes)")

def main():
    print("=== Live Network Packet Sniffer ===")
    print("Sniffing network traffic... Press Ctrl+C to stop.\n")
    
    try:
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")

if __name__ == "__main__":
    main()
