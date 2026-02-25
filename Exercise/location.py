import requests
ip="154.72.210.168"
response = requests.get(f"http://ipinfo.io/{ip}/json")
data = response.json()
print("IP Address:", data.get("ip"))
print("City:", data.get("city"))
print("Region:", data.get("region"))
print("Country:", data.get("country")) 
print("Location:", data.get("loc"))
print("Organization:", data.get("org"))
print("Postal Code:", data.get("postal"))
print("Timezone:", data.get("timezone"))
print("Hostname:", data.get("hostname"))
print("Readme:", data.get("readme")) 