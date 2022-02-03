import requests

from constants import COIN_LIST_URL, COIN_DATA_URL


def get_coin_id(coin_code):
    coin_list = requests.get(COIN_LIST_URL).json()

    coin_ifo = next(filter(lambda coin: coin["symbol"] == coin_code, coin_list), None)

    return -1 if coin_ifo is None else coin_ifo["id"]


def get_coin_data(coin_code):
    coin_id = get_coin_id(coin_code)

    if coin_id == -1:
        return -1

    return requests.get(COIN_DATA_URL.format(coin_id)).json()


def get_coin_price(coin_code, currency_code):
    coin_data = get_coin_data(coin_code)

    if coin_data == -1:
        return f"There is no data for coin with the '{coin_code}' code"

    coins_current_price = coin_data["market_data"]["current_price"]

    if currency_code not in coins_current_price:
        return f"There is no price data for currency with the '{currency_code}' code"

    return coins_current_price[currency_code]
