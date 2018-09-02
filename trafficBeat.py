#!/usr/bin/python3
#
# NAME - trafficBeat.py
# Version 1.0
#
# SYNOPSIS
# python3 ./trafficBeat.py 8.8.8.8
#
# DESCRIPTION
# Forwards all system network traffic to IP address using the "TEE" method
#
# AUTHOR
# Juan Ortega
#
# HISTORY:
#
# Date(YYYY/MM/DD):     Version:        Modified By:    Description of Change:

import sys
from scapy.all import *

def main():

    #Ask user for Monitor IP
    monip = sys.argv[1]

    #Get Monitor IP MAC Address
    global media
    media = get_mac(str(monip))

    #Replay Packet
    while 1:
        sniff(prn=chg_mac())


def get_mac(monip):
    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=monip)
    resp, unans = srp(arp_frame)

    for s, r in resp:
        mac = r[Ether].src
        return mac


def chg_mac(x):
# Edit Packet and Replace DST MAC with Monitor MAC
    x[Ether].dst = media
    send(x)



if __name__ == "__main__": main()