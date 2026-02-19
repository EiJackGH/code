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
            # The API returns price as a float in data['bpi']['USD']['rate_float']
            return data["bpi"]["USD"]["rate_float"]
        else:
            raise ConnectionError(f"Failed to fetch Bitcoin price. Status code: {response.status_code}")
    except Exception as e:
        if isinstance(e, ConnectionError):
            raise
        raise ConnectionError(f"An error occurred while fetching Bitcoin price: {e}")

def calculate_value(amount, price):
    """
    Calculates the total value of Bitcoin based on the amount and current price.
    """
    return amount * price
