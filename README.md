
# Notsafe Consulting
Notsafe Consulting is honored to bring you a coordinated and comprehensive solution to your security needs.

## Installation and Guide
### Setup
#### Install requirements:
`pip install -r requirements.txt`
#### Locations
`vuln_scan.py`, `log_analysis.py`, `AlertGeneration.py`, and `system_performance.py` should all be installed on end user devices. `traffic_monitor.py` should be installed on a router where it has access to network traffic.


### Log file analysis
log_analysis.py reads the log files from alertGeneration.py and creates a summary of any suspicious activity found within.
### System performance analysis
system_performance.py logs performance information about cpu, memory, and disc use and can be configured to send email warnings when abnormal usage is detected.
### Alert generation

#### Log file monitoring
log_analysis.py reads logs and creates a summary of suspicious information. This includes failed logins, unathorized access requests, high cpu percentage, and high ram use percentage.
#### Automatic alerts
alertGeneration.py updates AlertLogs.txt whenever system_performance.py logs suspicious behavior.
### Automated security checks

#### Traffic monitoring
traffic_monitor.py uses Python library scapy to monitor network traffic. Detects unknown IP addresses, high volume traffic, and suspicious traffic spikes. Should be run on a router.

#### Vulnerability Scans
vuln_scan.py uses nmap to scan open ports on the host and logs the states of the ports. Should be run on company servers, desktops, and laptops. This program logs files but produces no alert messages.