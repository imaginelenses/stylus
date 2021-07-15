import requests

response = requests.get("https://randomuser.me/api").json()
result = response["results"]

print(result)
