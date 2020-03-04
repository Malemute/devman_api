import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

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
  response = requests.post(request_url, headers = request_headers,
    json = long_link_params)
  response.raise_for_status()
  bitlink_structure = response.json()

  return bitlink_structure['id']

def count_clicks(token, bitlink):

  request_headers = make_auth_header(token)
  request_params = {
  "units": -1
  }
  request_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
  response = requests.get(request_url.format(bitlink=bitlink),
    headers = request_headers,
    params = request_params)
  response.raise_for_status()
  bitlink_structure = response.json()

  return bitlink_structure['total_clicks']

def process_bitlink(incoming_link, token):

  if (incoming_link == None) or (incoming_link == ""):
    incoming_link = "https://www.marinetraffic.com/en/ais/home/centerx:101.5/centery:-39.0/zoom:5"

  if incoming_link.lower().startswith('bit.ly'):
    try:
      total_clicks = count_clicks(token, incoming_link)
      printing_info = 'Total clicks', total_clicks
    except requests.exceptions.HTTPError as err:
      printing_info = 'Wrong link or so: ', err
  else:
    try:
      bitlink = shorten_link(token, incoming_link)
      printing_info = 'Битлинк', bitlink
    except requests.exceptions.HTTPError as err:
      printing_info = 'Wrong link or so: ', err

  return printing_info


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Работа с короткими ссылками')
  parser.add_argument('--url', help='Исходная ссылка')
  args = parser.parse_args()
  incoming_link = args.url

  if incoming_link == None:
    incoming_link = input("Your link: ")

  token = os.getenv("BITLINK_TOKEN")

  print(process_bitlink(incoming_link, token))
