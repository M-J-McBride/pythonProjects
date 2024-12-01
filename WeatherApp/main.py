from weather_api import get_weather, get_weather_details, Weather

def main():
    user_city: str = input('What city do need the weather for?: ')
    current_weather: dict = get_weather(city=user_city)
    weather_list: list[Weather] = get_weather_details(current_weather)

    dfmt: str = '%Y/%m/%d'
    days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_list})
    print(days)

    for day in days:
        print(day)
        print('----')

        grouped: list[Weather] = [current for current in weather_list if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)

if __name__ == '__main__':
    main()