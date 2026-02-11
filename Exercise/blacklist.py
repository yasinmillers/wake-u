import os
blacklist={"45.33.32.156","123.24.67.89"}
whitelist={"8.8.8.8 ","1.1.1.1"}
incoming_ip={"45.33.32.156"}

if incoming_ip in blacklist:
    print("Blocked: ", incoming_ip)
elif incoming_ip in whitelist:
    print("Allowed: ", incoming_ip)  
else:
    print("Unknown IP: ", incoming_ip)