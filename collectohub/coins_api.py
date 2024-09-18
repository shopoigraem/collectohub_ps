import requests
import pprint

url = 'http://127.0.0.1:8000/api/coin/recent/'

data = requests.get(url).json()
pprint.pprint(data)