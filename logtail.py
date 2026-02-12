from collections import Counter

#Sample log data

log_data = ["192.168.1.10", "192.168.1.15","192.168.1.25","1.1.1.1","192.168.1.10", "192.168.1.10", "192.168.1.25","8.8.8.8","8.8.8.8","10.0.0.1", "172.16.0.1"]

freq=Counter(log_data)
print(freq)

for ip, count in freq.items():
    print(f"IP Address: {ip} - Count: {count}")
  
print("Most common IP address:", freq.most_common(1))

print("\n short tail")
for ip, count in freq.items():
    if count >1:
        print(ip)
        
print("\n long tail")
for ip, count in freq.items():
    if count ==1:
        print(ip)