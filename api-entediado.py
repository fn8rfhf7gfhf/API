import requests
url = "https://www.boredapi.com/api/activity/"
response = requests.get(url)
print(response.json() )