import requests
import os
import argparse
from dotenv import load_dotenv

def make_auth_header(token):
  authoriz_template = "Bearer {}"
  request_header = {"Authorization":
    authoriz_template.format(token)}
  return request_header


def shorten_link(token, long_url):

  request_headers = make_auth_header(token)
  long_link_params = {
  "long_url": long_url
  }
  request_url = 'https://api-ssl.bitly.com/v4/bitlinks'
  
  try:
    response = requests.post(request_url, headers = request_headers,
      json = long_link_params)
    response.raise_for_status()
    bitlink_structure = response.json()
    return 'Битлинк = {}'.format(bitlink_structure['id'])
  
  except requests.exceptions.HTTPError as err:
    return 'Wrong link or so: {}'.format(err)


def count_clicks(token, bitlink):

  request_headers = make_auth_header(token)
  request_params = {
  "units": -1
  }
  request_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

  try:
    response = requests.get(request_url.format(bitlink=bitlink),
      headers = request_headers,
      params = request_params)
    response.raise_for_status()
    bitlink_structure = response.json()
    return 'Total clicks = {}'.format(bitlink_structure['total_clicks'])
    
  except requests.exceptions.HTTPError as err:
    return 'Wrong link or so: {}'.format(err)
    

def process_bitlink(incoming_link, token):

  if incoming_link.lower().startswith('bit.ly'):
    printing_info = count_clicks(token, incoming_link)
  else:
    printing_info = shorten_link(token, incoming_link)

  return printing_info


if __name__ == '__main__':

  load_dotenv()

  parser = argparse.ArgumentParser(description='Работа с короткими ссылками')
  parser.add_argument('--url',
         default = "https://www.marinetraffic.com/en/ais/home/centerx:103/centery:-37.2/zoom:6",
         help='Исходная ссылка')
  args = parser.parse_args()
  incoming_link = args.url

  token = os.getenv("BITLINK_TOKEN")

  print(process_bitlink(incoming_link, token))
