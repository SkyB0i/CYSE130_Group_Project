import scapy #pip install scapy
from scapy.all import IP, Ether
from collections import defaultdict #pip install collections

white_list_IPS = [
    "127.0.0.1",
    "123.45.67.89"
]
traffic_threshold = 1000


def mock_packets():
    packets = []


    for i in range(10):
        packet = Ether() / IP(src="127.0.0.1", dst="123.45.67.89")
        packet.time = i
        packets.append(packet)
    
    spike_timestamp = 15
    for _ in range(10):
        packet = Ether() / IP(src="192.168.1.1", dst="98.76.54.32")
        packet.time = spike_timestamp
        packets.append(packet)
    
    for i in range (20, 1020):
        packet = Ether() / IP(src="10.10.10.10", dst="98.76.54.32")
        packet.time = i
        packets.append(packet)

    return packets

def main():
    packet_capture = mock_packets()

    # Packet counts
    packet_counts = len(packet_capture)

    # Source IPS
    source_ips = defaultdict(int)
    for packet in packet_capture:
        if IP in packet:
            source_ips[packet[IP].src] = source_ips[packet[IP].src] + 1 if packet[IP].src in source_ips else 1

    # Destination IPS
    destination_ips = defaultdict(int)
    for packet in packet_capture:
        if IP in packet:
            destination_ips[packet[IP].dst] = destination_ips[packet[IP].dst] + 1 if packet[IP].dst in destination_ips else 1

    # Timestamps
    timestamps = []
    traffic_per_second = defaultdict(int)
    for packet in packet_capture:
        if IP in packet:
            timestamps.append(packet.time)
            traffic_per_second[packet.time] = traffic_per_second[packet.time] + 1 if packet.time in traffic_per_second else 1
    
    sorted_traffic = sorted(traffic_per_second.items(), key=lambda x: x[1], reverse=True)
 
    # Find spikes
    spikes = find_spikes(sorted_traffic)
    if spikes:
        print("Spikes detected at the following timestamps:")
        for spike in spikes:
            print(spike)

    for ip in source_ips:
        if source_ips[ip] > traffic_threshold and ip not in white_list_IPS:
            print(f"High traffic volume detected from {ip}")
    for ip in destination_ips:
        if destination_ips[ip] > traffic_threshold and ip not in white_list_IPS:
            print(f"High traffic volume detected to {ip}")


def find_spikes(sorted_traffic):
    if not sorted_traffic:
        return []
    timestamps = [x[0] for x in sorted_traffic]
    counts = [x[1] for x in sorted_traffic]
    spike_threshold = 5 # Arbitrary value
    spikes = []

    for i in range(1, len(counts)):
        if counts[i] - counts[i-1] > spike_threshold:
            spikes.append((timestamps[i], counts[i]))
    
    avg_traffic = sum(counts) / len(counts)
    for timestamp, count in sorted_traffic:
        if count > avg_traffic + spike_threshold:
            spikes.append((timestamp, count))
    
    return spikes
        
    


if __name__ == "__main__":
    main()