import requests

def get_bitcoin_price():
    """
    Fetches the current Bitcoin price in USD from the CoinDesk API.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["bpi"]["USD"]["rate_float"]
        else:
            raise ConnectionError(f"API returned status code {response.status_code}")
    except requests.RequestException:
        raise ConnectionError("Failed to fetch Bitcoin price")


def calculate_value(amount, price):
    """
    Calculates the total value of Bitcoin based on the amount and current price.
    """
    return amount * price
