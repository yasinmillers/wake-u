import http.client
conn = http.client.HTTPSConnection("jasonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
response = conn.getresponse()
print("Status:", response.status)
print("Reason:", response.reason)
data = response.read()
print("Data:", data.decode("utf-8"))    