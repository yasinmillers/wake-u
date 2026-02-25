ip="154.72.210.168"
response = requests.get(f"http://ipinfo.io/{ip}/json")
data = response.json()
print("IP Address:", data.get("ip"))
print("City:", data.get("city"))
print("Region:", data.get("region"))
print("Country:", data.get("country"))  