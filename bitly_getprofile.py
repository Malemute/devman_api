import requests

request_headers = {"Authorization":"Bearer <your token here>"}
url = 'https://api-ssl.bitly.com/v4/user'
response = requests.get(url, headers = request_headers)
response.raise_for_status()
print(response.json())

