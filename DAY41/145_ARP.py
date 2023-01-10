#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # scapy.arping(ip) # we are writing our own functin that acts like this..
    ArpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / ArpRequest
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose = False)[0]

    print("________________________________________________")
    print("IP\t\t\tMAC Address ")
    print("________________________________________________")

    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)



scan("192.168.1.254/24")
