from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=6535993f334cf4e9fe8a3fb96d3f98cf')
pprint(r.json)