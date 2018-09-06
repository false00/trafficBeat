#!/usr/bin/python3
#
# NAME - trafficBeat.py
# Version 1.3
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
# 2018-09-03            1.2             Juan Ortega     Bug Fix: Fixed Endless Loop of Duplicate Packet Bug
# 2018-09-04            1.3             Juan Ortega     Bug Fix: Added code to continue loop when program crashes

import sys
from scapy.all import *


def main():
    while 1:
        try:
            sniff(prn=chg_mac, filter='ip', store=0)
        except:
            continue


def get_mac(monip):
    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=monip)
    resp, unans = srp(arp_frame)

    for s, r in resp:
        mac = r[Ether].src
    return mac


def chg_mac(pkt):
    # Get Monitor IP MAC Address
    global mac
    global monip

    # Edit Packet and Replace DST MAC with Monitor MAC
    #MON 20 xx
    #Client 22 aa
    #Remote 21 bb

    #10.0.0.22 > 10.0.0.21
    #aa bb

    #MOD
    # 10.0.0.22 > 10.0.0.21
    # 00  xx

    #valid Traffic
    # 10.0.0.22 > 10.0.0.20
    # aa  xx

    if pkt[Ether].dst != mac:
        pkt[Ether].dst = mac
        sendp(pkt)
    else:
        pass


if __name__ == "__main__":
    try:
        monip = sys.argv[1]
    except:
        print("===============trafficBeat=============== \n"
              "Pass the IP you wish to mirror traffic to.\n"
              "This application will edit every packet and modify the DST MAC\n"
              "with the MAC address associated with the IP entered. Modified packet\n"
              "will be sent over layer 2\n"
              "\n"
              "Usage: trafficBeat.exe 10.0.0.1")
        sys.exit(1)
    mac = get_mac(monip)
    print(mac)
    main()
