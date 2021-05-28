import requests
import json
import os
from dotenv import load_dotenv
from requests import api
import json
import pprint as p

load_dotenv()
API_key = os.getenv('WEATHER_API')
print(API_key)

API_URL = "https://api.openweathermap.org/data/2.5/"

#Helper function
def kelvin_to_celsius(number):
    kelvin = 273.15
    number = float(number)
    return int(number-kelvin)

#main functions
def weather_5day(city="athens"):
    url = f"{API_URL}?q={city}&appid={API_key}"
    print(url)
    r = requests.get(f"{API_URL}forecast?q={city}&appid={API_key}")
    p.pprint(json.loads(r.content))
    
def currentWeather(city="athens"):
    url = f"weather?q={city}&appid={API_key}"
    r= requests.get(f"{API_URL}{url}")
    data = json.loads(r.content)
    data_main = data.get("main")
    temp = kelvin_to_celsius(data_main.get("temp"))
    temp_max = kelvin_to_celsius(data_main.get("temp_max"))
    temp_min = kelvin_to_celsius(data_main.get("temp_min"))
    p.pprint(data_main)
    if(temp > 20):
        weather = f"The Current Weather is quite warm with tempatures ranging from {temp_min} to {temp_max} degrees celsius"
    elif(temp < 20 and temp >10):
        weather = f"The Current Weather is ok with tempatures ranging from {temp_min} to {temp_max} degrees celsius, i suggest a jasket sir"
    elif(temp < 10):
        weather = f"The Current Weather is quite cold with tempatures ranging from {temp_min} to {temp_max} degrees celsius, i suggest a heavy jasket sir"
    else:
        weather = f"Tempatures are ranging from {temp_min} to {temp_max} degrees celsius sir"
    
    
    return weather