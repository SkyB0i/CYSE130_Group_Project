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
    logging.info("Scanning the Following Address:" + IPAddr)
    scanner.scan(IPAddr)

    # Print the scan results
    for host in scanner.all_hosts():
        logging.info("Host:\t%s", host)
        logging.info("State:\t%s", scanner[host].state())
        for proto in scanner[host].all_protocols():
            logging.info("Protocol:\t%s", proto)
            ports = scanner[host][proto].keys()
            for port in ports:
                logging.info("Port:\t%s", port)
                logging.info("State:\t%s", scanner[host][proto][port]["state"])
    
def main():
    logname = "logs/vuln_scan.log"
    logging.basicConfig(
        filename=logname,
        filemode="a",
        level=logging.DEBUG,
        format="%(asctime)s - {levelname} - %(message)s",
    )
    schedule.every().hour.do(vuln_scan)

if __name__ == "__main__":
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)