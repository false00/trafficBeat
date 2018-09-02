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
    get_mac(str(monip))

    # #SNIFF PACKET
    # sniff_packet()
    #
    # #Edit Packet and Replace DST MAC with Monitor MAC
    # edit_packet()
    #
    # #Replay Packet
    # replay_packet()




def get_mac(monip):
    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=monip)
    resp, unans = srp(arp_frame)

    for s, r in resp:
        print(r[Ether].src)


def sniff_packet():
    pass


def edit_packet():
    pass

def replay_packet():
    pass


if __name__ == "__main__": main()