import requests

# URL to send request to
url = "https://google.com"

# send GET request
response = requests.get(url)

# print status code
print("Status Code:", response.status_code)

# print response headers
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")