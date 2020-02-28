import requests

request_headers = {"Authorization":"Bearer c65b488a8ca81706b68d41030fd118461b056012"}
url = 'https://api-ssl.bitly.com/v4/user'
response = requests.get(url, headers = request_headers)
response.raise_for_status()
print(response.json())

