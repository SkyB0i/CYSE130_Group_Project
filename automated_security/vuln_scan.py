import nmap
import socket 
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
scanner = nmap.PortScanner()
host = 'IPAddr'
print("Scanning the Following Address:" + IPAddr)
# Define target IP address or hostname


# Run a basic scan on the target
scanner.scan(IPAddr)

# Print the scan results
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])
    
