import requests
import json

API_KEY = ''
LAT = ''
LON = ''

endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}'
response = requests.get(endpoint)

if response.status_code == 200:

    weather = json.loads(response.text)['weather'] # get all weather conditions data

    for i in weather:
        description = i['description'] # get weather conditions

    temperature = json.loads(response.text)['main']['temp'] # get kelvin temperature
    temperature = int(temperature) - 273.15 # convert kelvin to celcius
    max_temperature = json.loads(response.text)['main']['temp_max']
    max_temperature = int(max_temperature) - 273.15 
    city = json.loads(response.text)['name'] # get city name

    print(f'The current weather in {city}: {description}!')
    print(f'The current temperature in {city} is: {int(temperature)} Celsius!')
    print(f'The max temperature today in {city} is: {int(max_temperature)} Celsius!')
else:
    print(f'Erorr: {response.status_code}')