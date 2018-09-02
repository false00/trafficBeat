#!/usr/bin/python3
#
# NAME - trafficBeat.py
# Version 1.0
#
# SYNOPSIS
# python3 ./trafficBeat.py
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
    get_mac()
    # #Ask user for Monitor IP
    # IP = sys.argv[1]
    #
    # #Get Monitor IP MAC Address
    # get_mac()
    #
    # #SNIFF PACKET
    # sniff_packet()
    #
    # #Edit Packet and Replace DST MAC with Monitor MAC
    # edit_packet()
    #
    # #Replay Packet
    # replay_packet()




def get_mac():
    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="172.16.20.151")
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