import requests
from typing import Final
from dataclasses import dataclass

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'

@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24: float
    low_24: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): €{self.current_price:,}'

def get_coins() -> list[Coin]:
    payload: dict = {'vs_currency': 'eur','order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    jsondata: dict = data.json()

    coin_list: list[Coin] = []
    for item in jsondata:
        current_coin: Coin = Coin(name=item.get('name'),
                              symbol=item.get('symbol'),
                              current_price=item.get('current_price'),
                              high_24=item.get('high_24'),
                              low_24=item.get('low_24'),
                              price_change_24h=item.get('price_change_24h'),
                              price_change_percentage_24h=item.get('price_change_percentage_24h')
                              )
        coin_list.append(current_coin)
    return coin_list

if __name__ == '__main__':
    coins = get_coins()
    for coin in coins:
        print(coin)