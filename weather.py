from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

#API KEY
owm = OWM('6535993f334cf4e9fe8a3fb96d3f98cf')
mgr = owm.weather_manager()

#search for current weather condition in a region
region = input('Name of region: ')

reg = owm.city_id_registry()
list_of_tuples = london = reg.ids_for(region, matching='like')
print(list_of_tuples)

choose = input('From the list provded above, enter the correct region: ')

observation = mgr.weather_at_place(choose)
w = observation.weather
print('Weather Details: ', w.detailed_status)
print('Wind Detail: ', w.wind())
print('Humidity Details: ', w.humidity)
print('Temperature Details: ', w.temperature('celsius'))
print('Rain: ', w.rain)
print('Heat_Index: ', w.heat_index)
print('Cloudy: ', w.clouds)