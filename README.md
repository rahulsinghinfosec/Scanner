# Scanner
These are basic scanners.

They can check the number of devices connected to your network and print their local IP addresses along with their MAC addresses.

1. Sniff_Tool.py
_________________

I have used argparse and scapy to make this basic network scanner.

[Syntax : python &lt;file_name&gt; -ip ip_address/subnet]

[NOTE : Use it with root/administrative priviledges]

One needs to have argparse and scapy installed.

They can be installed with :

   pip install argparse

   pip install scapy

2. Sniff_Tool2.py
__________________

I have used sys and scapy to build this basic network scanner.

Call it from the command line using root/admin privileges

[Syntax : python file_name ip_address/subnet]

[Note : Put Your IP address, so that all the responses will be sent to you.]
Scapy can be installed with : 
  
   pip install scapy
