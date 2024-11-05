import nmap
import socket

import schedule
import time
import logging


 

def vuln_scan():
    scanner = nmap.PortScanner()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    # Run a basic scan on the target
    host = 'IPAddr'
    logging.info("Scanning the Following Address:" + IPAddr)
    scanner.scan(IPAddr)

    # Print the scan results
    for host in scanner.all_hosts():
        logging.info("Host: ", host)
        logging.info("State: ", scanner[host].state())
        for proto in scanner[host].all_protocols():
            logging.info("Protocol: ", proto)
            ports = scanner[host][proto].keys()
            for port in ports:
                logging.info("Port: ", port, "State: ", scanner[host][proto][port]['state'])
    
def main():
    logname = "vuln_scan.log"
    logging.basicConfig(
        filename=logname,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - {levelname} - %(message)s",
    )
    schedule.every().hour.do(vuln_scan)