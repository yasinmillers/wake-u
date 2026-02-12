from collections import Counter

#Sample log data

log_data = ["192.168.1.10", "192.168.1.15", "192.168.1.10", "192.168.1.10", "192.168.1.25","8.8.8.8", "10.0.0.1", "172.16.0.1"]

def count_ip_addresses(logs):
    """
    Count occurrences of each IP address in the log data.

    Args:
        logs (list): List of IP addresses as strings.

    Returns:
        dict: A dictionary with IP addresses as keys and their counts as values.
    """
    ip_counter = Counter(logs)
    return dict(ip_counter) 

if __name__ == "__main__":
    

    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")
    # Example usage
    # log_file_path = "path_to_log_file.log"
    # ip_counts = count_ip_addresses_from_file(log_file_path)
    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")

    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")
    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")
    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")
    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")
    ip_counts = count_ip_addresses(log_data)
    for ip, count in ip_counts.items():
        print(f"IP Address: {ip}, Count: {count}")