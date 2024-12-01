from typing import Final
import requests
from model import Weather, dt
import json

API_KEY: Final[str] = '1a2b4bb73c4fca415f1b229d77c99b84'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city: str, mock:bool = False) -> dict:

    if mock:
        with open('dummy_data.json', 'r') as file:
            return json.load(file)

    payload: dict = {'q':city, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data



def get_weather_details(weather:dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with json: {weather}')

    list_of_weather: list[Weather] = []

    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description')
                             )



        list_of_weather.append(w)

    return list_of_weather
