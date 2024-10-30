import scapy #pip install scapy
from collections import defaultdict #pip install collections

white_list_IPS = [
    "127.0.0.1",
    "123.45.67.89"
]
traffic_threshold = 1000


def main():
    packet_capture = scapy.sniff()

    # Packet counts
    packet_counts = len(packet_capture)

    # Source IPS
    source_ips = defaultdict(int)
    for packet in packet_capture:
        if scapy.IP in packet:
            source_ips[packet[scapy.IP].src] = source_ips[packet[scapy.IP].src] + 1 if packet[scapy.IP].src in source_ips else 1

    # Destination IPS
    destination_ips = defaultdict(int)
    for packet in packet_capture:
        if scapy.IP in packet:
            destination_ips[packet[scapy.IP].dst] = destination_ips[packet[scapy.IP].dst] + 1 if packet[scapy.IP].dst in destination_ips else 1

    # Timestamps
    timestamps = []
    traffic_per_second = defaultdict(int)
    for packet in packet_capture:
        if scapy.IP in packet:
            timestamps.append(packet.time)
            traffic_per_second[packet.time] = traffic_per_second[packet.time] + 1 if packet.time in traffic_per_second else 1
    
    sorted_traffic = sorted(traffic_per_second.items(), key=lambda x: x[1], reverse=True)
 
    # Find spikes
    spikes = find_spikes(sorted_traffic)
    if spikes:
        print("Spikes detected at the following timestamps:")
        for spike in spikes:
            print(spike)

    if packet_counts > traffic_threshold:
        print("High traffic volume detected")

    for ip in source_ips:
        if source_ips[ip] > traffic_threshold and ip not in white_list_IPS:
            print(f"High traffic volume detected from {ip}")
    for ip in destination_ips:
        if destination_ips[ip] > traffic_threshold and ip not in white_list_IPS:
            print(f"High traffic volume detected to {ip}")


def find_spikes(sorted_traffic):
    timestamps = [x[0] for x in sorted_traffic]
    counts = [x[1] for x in sorted_traffic]
    spike_threshold = 5 # Arbitrary value
    spikes = []

    for i in range(1, len(counts)):
        if counts[i] - counts[i-1] > spike_threshold:
            spikes.append((timestamps[i], counts[i]))
    
    return spikes
        
    


if __name__ == "__main__":
    main()