import sys
from scapy.all import scapy
print("Scapy, IP and MAC address Sniffer ",scapy.__version__)
# Call it from the command line using root/admin privileges
# Syntax : python <file_name> <ip_address>/<subnet>
# Note : Put Your IP address, so that all the responses will be sent to you.
print("IP address Entered", sys.argv[1])
# pdst stands for destination IP address
arp_req = scapy.layers.l2.ARP(pdst=sys.argv[1])
# Making a broadcast frame
broadcast_frame = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff:ff")
broadcast_frame_with_arp =broadcast_frame / arp_req
results = scapy.layers.l2.srp(broadcast_frame_with_arp, timeout=1,verbose=True)[0]
output = []
for i in range(0, len(results)):
    # psrc stands for Source IP
    # hwsrc stands for Destination MAC Address
    temp = {"ip":results[i][1].psrc,"mac":results[i][1].hwsrc}
    output.append(temp)
for i in range(len(output)):
    print(output[i])

