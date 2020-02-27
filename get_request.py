import requests

request_params = {"nTqm":"", "lang":"ru"}
url_template = 'http://wttr.in/{}'
for location in ['London', 'svo', 'Череповец']:
    url = url_template.format(location)
    response = requests.get(url, params = request_params)
    response.raise_for_status()
    print(response.text)
