import json
from typing import Final
import requests

BASE_URL: Final[str]= 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str]= '31cf9319d51a6415cc63b370586c9bf2'


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open ('rates.json','r') as file:
            return json.load(file)
    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data

def get_currency(currency:str, rates:dict) -> float:
    currency:str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'"{currency}" is not a valid currency.')


def convert_currency(amount: float, base: str, vs: str, rates:dict) -> float:
    base_rate = get_currency(base, rates)
    vs_rate = get_currency(vs, rates)

    conversion: float = round((vs_rate/base_rate) * amount, 2)
    print(f'{amount:,.2f} {base} is {conversion:,.2f} {vs}.')
    return conversion

def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    convert_currency(amount=10, base='EUR', vs='GBP', rates=rates)
    convert_currency(amount=100, base='USD', vs='GBP', rates=rates)

if __name__ == '__main__':
    main()
