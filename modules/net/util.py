#!/bin/python3

import netifaces
import ipaddress

def getIPRange() -> str:
    """Gets the IP Range of the machine. Used in the Ping Scan/Network Discovery.
    Example: print(getIPRange())  # Output: 192.168.0.0/24"""
    
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        if interface != 'lo':
            addresses = netifaces.ifaddresses(interface)

            if netifaces.AF_INET in addresses:
                ip_info = addresses[netifaces.AF_INET][0]
                ip_address = ip_info['addr']
                netmask = ip_info['netmask']
                break

    ip_network = ipaddress.ip_network(f"{ip_address}/{netmask}", strict=False)
    ip_range = f"{ip_network.network_address}/{ip_network.prefixlen}"

    return ip_range