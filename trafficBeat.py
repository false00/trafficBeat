#!/usr/bin/python3
#
# NAME - trafficBeat.py
# Version 1.0
#
# SYNOPSIS
# python3 ./trafficBeat.py 10.0.0.1
#
# DESCRIPTION
# Forwards all system network traffic to IP address using the iptables "TEE" method
#
# AUTHOR
# Juan Ortega
#
# HISTORY:
#
# Date(YYYY/MM/DD):     Version:        Modified By:    Description of Change:
# 2018-09-02            1.0             Juan Ortega     First Working Version of Script
# 2018-09-02            1.1             Juan Ortega     Windows x86-64 Binary Support

import sys
from scapy.all import *

arp_count = 0

def main():

    sniff(prn=chg_mac)


def get_mac(monip):

    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=monip)
    resp, unans = srp(arp_frame)

    for s, r in resp:
        mac = r[Ether].src
    return mac


def chg_mac(pkt):
    # Get Monitor IP MAC Address
    global arp_count

    try:
        monip = sys.argv[1]
    except:
        print("===============Error=============== \n"
              "Pass the IP you wish to mirror traffic to.\n"
              "This application will edit every packet and modify the DST MAC\n"
              "with the MAC address associated with the IP entered. Modified packet\n"
              "will be sent over layer 2\n"
              "\n"
              "Usage: trafficBeat.exe 10.0.0.1")
        sys.exit(1)

    if arp_count == 0 :
        arp_count +=1
        print (str(arp_count))
        get_mac(str(monip))

    # Edit Packet and Replace DST MAC with Monitor MAC
    try:
        pkt[Ether].dst = mac
        sendp(pkt)
    except:
        pass


if __name__ == "__main__": main()