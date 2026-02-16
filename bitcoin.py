import requests


def calculate_value(amount, price):
    """Calculates the USD value of a given amount of BTC."""
    return amount * price


def get_bitcoin_price():
    """Fetches the current BTC price from an API."""
    # Simplified implementation for testing purposes
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    else:
        raise ConnectionError("Failed to fetch price")
