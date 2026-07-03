import calculator # Now Python will successfully find your calculator.py file!

def main():
    print("=== IPv4 Subnet Calculator ===")
    print("Enter an IP address and CIDR prefix (e.g., 192.168.1.50/24)")
    
    user_input = input("Network> ")
    
    try:
        ip, cidr_str = user_input.split('/')
        cidr = int(cidr_str)
        
        results = calculator.calculate_network_data(ip, cidr)
        
        print("\n--- Results ---")
        print(f"IP Address:         {results['ip_address']}")
        print(f"Subnet Mask:        {results['subnet_mask']}")
        print(f"Network Address:    {results['network_address']}")
        print(f"Broadcast Address:  {results['broadcast_address']}") # <-- Make sure this line is here!
        print(f"Total Usable Hosts: {results['total_hosts']}")
        
    except ValueError:
        print("Error: Invalid format. Please use standard format like 192.168.1.0/24")

if __name__ == "__main__":
    main()
