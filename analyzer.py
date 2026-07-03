from scapy.all import IP, TCP, UDP

def analyze_packet(packet):
    """Parses a captured packet and extracts key network layer details."""
    # Check if the packet has an IP (Network) Layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol_num = ip_layer.proto
        
        # Determine the Transport Layer protocol
        protocol_name = "Other"
        if packet.haslayer(TCP):
            protocol_name = "TCP"
            payload_info = f"Src Port: {packet[TCP].sport} -> Dst Port: {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
            payload_info = f"Src Port: {packet[UDP].sport} -> Dst Port: {packet[UDP].dport}"
        else:
            payload_info = f"Protocol Number: {protocol_num}"
            
        return {
            "src": src_ip,
            "dst": dst_ip,
            "proto": protocol_name,
            "info": payload_info,
            "size": len(packet)
        }
    return None
