def ip_to_binary(ip_address):
    """Converts a standard IP address into a 32-bit binary string."""
    octets = ip_address.split('.')
    binary_octets = [format(int(octet), '08b') for octet in octets]
    return "".join(binary_octets)

def binary_to_ip(binary_string):
    """Converts a 32-bit binary string back to a standard IP address."""
    octets = [str(int(binary_string[i:i+8], 2)) for i in range(0, 32, 8)]
    return ".".join(octets)

def get_subnet_mask_binary(cidr):
    """Generates the binary representation of the subnet mask."""
    ones = '1' * cidr
    zeros = '0' * (32 - cidr)
    return ones + zeros

def calculate_network_data(ip, cidr):
    """Calculates all subnet details using bitwise logic."""
    ip_bin = ip_to_binary(ip)
    mask_bin = get_subnet_mask_binary(cidr)
    
    # Calculate Network Address (Bitwise AND)
    network_bin = ""
    for i in range(32):
        if ip_bin[i] == '1' and mask_bin[i] == '1':
            network_bin += '1'
        else:
            network_bin += '0'
            
    # Calculate Broadcast Address (Bitwise OR)
    broadcast_bin = ""
    for i in range(32):
        if network_bin[i] == '1' or mask_bin[i] == '0':
            broadcast_bin += '1'
        else:
            broadcast_bin += '0'
    
    return {
        "ip_address": ip,
        "cidr": cidr,
        "subnet_mask": binary_to_ip(mask_bin),
        "network_address": binary_to_ip(network_bin),
        "broadcast_address": binary_to_ip(broadcast_bin),
        "total_hosts": (2 ** (32 - cidr)) - 2
    }
