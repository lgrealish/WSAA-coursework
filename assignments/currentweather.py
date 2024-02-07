# Program that returns the current temperature data
# Author: Linda Grealish

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

response = requests.get(url).json()

temperature = response['current']['temperature_2m']

print ("It is currently", temperature, "degrees celsius.")


url2 = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m,wind_direction_10m"

response2 = requests.get(url2).json()

winddir = response['current']['wind_direction_10m']

print ("The wind direction is", winddir)