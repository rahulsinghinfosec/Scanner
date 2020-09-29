import sys
# If using Jupyter Notebook jupyter_argparse.core is another option for you
import argparse
from scapy.all import scapy

parser = argparse.ArgumentParser()
# call it from the command line using root/admin privileges
# Syntax : python <filename> -ip <IP>/<Subnet>
# e.g. sudo Sniff_Tool.py -ip 172.16.24.1/24
# Note : Put the ip address of your default gateway(router).
parser.add_argument("-ip", "--ipadd", help="IP Address/Subnet Mask")
args = parser.parse_args()

if not args.ipadd:
    print("Invalid Syntax")
    print("Use --help or -h for options.")
    sys.exit(1)
else:
    # pdst stands for destination IP address
    arp_request = scapy.layers.l2.ARP(pdst= args.ipadd)
    broadcast_frame = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_request = broadcast_frame/arp_request
    results_ans = scapy.layers.l2.srp(final_request, timeout=2, verbose=False)[0]
    # results_unaswered = scapy.layers.l2.srp(final_request, timeout=2, verbose=False)[1]
    results = []
    for i in range(0,len(results_ans)):
        # psrc stands for source IP Address
        # hwsrc stands for destination MAC Address
        clients = {"ip":results_ans[i][1].psrc," mac":results_ans[i][1].hwsrc}
        results.append(clients)
    for i in range(len(results)):
        print(results[i])
