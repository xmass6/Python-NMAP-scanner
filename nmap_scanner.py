import nmap
import os

try:
     nm = nmap.PortScanner()
     print("scan in progress...")
     output = nm.scan("192.168.2.0/24", arguments='-Pn -O -v')
     with open("nmap_results.txt", 'w', encoding='utf-8') as xml_output:
        xml_output.write(nm.get_nmap_last_output().decode('utf-8'))
     print('Scan complete, please check the output file nmap_results.txt')
    
except KeyboardInterrupt:
    sys.exit()
