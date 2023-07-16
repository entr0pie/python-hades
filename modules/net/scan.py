#!/bin/python3

from nmap import PortScanner

def pingScan(ip_range: str) -> list:
    """
    Scans for available hosts in the network, return a list of actives.
    Usage: print(pingScan("192.168.0.1/24")) # Output: ["192.168.0.1", ...]
    """

    nm = PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')
    return nm.all_hosts()

def synScan(target: str) -> dict:
    """
    Do a SYN scan (-sS) in a target. Returns a dict with the open ports.
    Basic Usage:
        result = synScan("192.168.0.1")
        print(nm['192.168.0.1']['tcp'])
        # Output: {631: {'state': 'open', 'reason': 'syn-ack', 'name': 'ipp', ... } ...}
    """

    nm = PortScanner()
    nm.scan(hosts=target, arguments="-sS")
    return nm[target]['tcp']
