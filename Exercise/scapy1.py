from scapy.all import sniff

def mycallback(packet):
    if packet.haslayer('IP'):
        print(f"Source: {packet['IP'].src} -> Destination: {packet['IP'].dst}")
        print(f"Protocol: {packet['IP'].proto}")
        print("......")
  
sniff(prn=mycallback, count=10)


