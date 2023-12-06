import nmap
import os

nm = nmap.PortScanner()
nm.scan( "192.168.1.0/24", arguments='-sn -O')
with open("nmap_results.xml", 'w') as xml_output: xml_output.write(nm.get_nmap_last_output())