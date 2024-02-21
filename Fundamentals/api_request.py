import requests

response = requests.get('http://api.open-notify.org/astros.json')
json1 = response.json()

print(json1)
