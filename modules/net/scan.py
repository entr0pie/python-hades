#!/bin/python3

from nmap import PortScanner

def pingScan(ip_range: str) -> PortScanner:
    """
    Scans for available hosts in the network, return the PortScanner object.
    Usage: print(pingScan("192.168.0.1/24").all_hosts()) # Output: ["192.168.0.1", ...]
    """

    nm = PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')
    return nm