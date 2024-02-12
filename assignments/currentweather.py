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

wind_direction_degrees = response2['current']['wind_direction_10m']

# Take the wind direction in degrees and convert it to text.
# https://stackoverflow.com/questions/7490660/converting-wind-direction-in-angles-to-text-words
def degrees_to_text(wind_direction_degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

    index = round(wind_direction_degrees / 22.5) % 16
    return directions[index]


wind_direction_text = degrees_to_text(wind_direction_degrees)
print("The wind is coming from a", wind_direction_text, "direction.")

