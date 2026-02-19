import requests


def calculate_value(amount, price):
    """
    Calculates the value of the Bitcoin amount at the given price.
    """
    return float(amount * price)


def get_bitcoin_price():
    """
    Fetches the current Bitcoin price from CoinDesk API.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    if response.status_code != 200:
        raise ConnectionError("Failed to fetch Bitcoin price")

    data = response.json()
    return data["bpi"]["USD"]["rate_float"]
