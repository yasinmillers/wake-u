#print a ip addresses from 192.168.1.0 to 192.168.1.255
ports = [80, 443, 8080, 3000, 5000, 8000, 8100]



for i in range(0, 256):
    for port in ports:
        print(f"192.168.1.{i}:{port}")  