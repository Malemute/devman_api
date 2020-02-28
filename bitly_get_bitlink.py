import requests

def shorten_link(token, long_url):
  authoriz_template = "Bearer {}"
  request_headers = {"Authorization":
    authoriz_template.format(token)}
  long_link_params = {
  "long_url": long_url
  }
  request_url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(request_url, headers = request_headers,
    json = long_link_params)
  response.raise_for_status()
  bitlink_json = response.json()
  return bitlink_json['link']

token = "c65b488a8ca81706b68d41030fd118461b056012"
long_link = "https://www.marinetraffic.com/en/ais/home/centerx:89.6/centery:-40.9/zoom:5"

print('Битлинк', shorten_link(token, long_link))

