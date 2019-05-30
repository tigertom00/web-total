from requests import get
from decouple import config

# Get Weather for Oslo/Norway
api_key = config('W_APIKEY')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'
city = 'Oslo'
units = 'Metric'

response = get(url.format(city, units, api_key)).json()

# Make dictionary
city_weather = {
    'city': city,
    'temp': response['main']['temp'],
    'description': response['weather'][0]['description'],
    'icon': response['weather'][0]['icon']
}

# Write dictionary to file
with open('city_weather.py', 'w') as file:
    file.write("city_weather = { \n")
    for k in sorted(city_weather.keys()):
        file.write("'%s':'%s', \n" % (k, city_weather[k]))
    file.write("}")
