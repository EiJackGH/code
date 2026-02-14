import pytest
from unittest.mock import patch
from bitcoin import get_bitcoin_price, calculate_value

# Test 1: Verify the calculation logic
def test_calculate_value():
    """Ensure BTC to USD conversion math is correct."""
    price = 50000.0
    amount = 2.5
    expected = 125000.0
    assert calculate_value(amount, price) == expected

# Test 2: Verify handling of zero amount
def test_calculate_value_zero():
    assert calculate_value(0, 50000.0) == 0.0

# Test 3: Mocking an API response
@patch('bitcoin.requests.get')
def test_get_bitcoin_price(mock_get):
    """Simulate a successful API response from CoinDesk or similar."""
    # Mock the JSON return value
    mock_get.return_value.json.return_value = {
        "bpi": {"USD": {"rate_float": 62000.50}}
    }
    mock_get.return_value.status_code = 200
    
    price = get_bitcoin_price()
    assert price == 62000.50

# Test 4: Handling API failure
@patch('bitcoin.requests.get')
def test_get_price_api_error(mock_get):
    mock_get.return_value.status_code = 404
    with pytest.raises(ConnectionError):
        get_bitcoin_price()
