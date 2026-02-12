from collections import Counter

#Sample log data

log_data = ["192.168.1.10", "192.168.1.15", "192.168.1.10", "192.168.1.10", "192.168.1.25","8.8.8.8", "10.0.0.1", "172.16.0.1"]

freq=Counter(log_data)
print(freq)