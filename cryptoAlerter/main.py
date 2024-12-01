from crypto_data import get_coins, Coin

def alert(symbol: str, top: float, bottom: float, coin_list: list[Coin]):
    for coin in coin_list:
        if symbol == coin.symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!!Trigger!!!')
            else:
                print(coin)


if __name__ == '__main__':
    coin_list = get_coins()
    alert('btc', top= 90000, bottom = 80000, coin_list = coin_list)
    alert('eth', top=2000, bottom=1000, coin_list=coin_list)
    alert('sol', top=90000, bottom=80000, coin_list=coin_list)
    alert('xrp', top=90000, bottom=80000, coin_list=coin_list)
    alert('ada', top=90000, bottom=80000, coin_list=coin_list)