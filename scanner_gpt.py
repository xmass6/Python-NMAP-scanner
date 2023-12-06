import nmap
import os
import time

def nmap_scan(target, output_file):
    # Create an Nmap object
    nm = nmap.PortScanner()

    # Display "Scan in progress" message
    print("Scan in progress...")

    # Perform a basic scan
    nm.scan(hosts=target, arguments='-sn -O --servicedb C:\Users\chaitanya jasthi\AppData\Local\Programs\Python\Python310\Lib\site-packages\nmap\nmap-os-db')

    # Save the results to an XML file
    nm.all_hosts()
    with open(output_file, 'w') as xml_output:
        xml_output.write(nm.get_nmap_last_output())

if __name__ == "__main__":
    target_host = "192.168.1.0/24"
    xml_output_file = "nmap_results.xml"

    # Record the start time
    start_time = time.time()

    # Perform the scan
    nmap_scan(target_host, xml_output_file)

    # Calculate the time taken
    elapsed_time = time.time() - start_time

    # Print completion message with elapsed time
    print(f"Scan completed in {elapsed_time:.2f} seconds. Results saved to {xml_output_file}")