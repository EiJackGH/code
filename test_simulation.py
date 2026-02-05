import pandas as pd
import pytest
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals

def test_simulate_bitcoin_prices():
    days = 100
    prices = simulate_bitcoin_prices(days=days)
    assert len(prices) == days
    assert isinstance(prices, pd.Series)
    assert prices.name == 'Price'

def test_calculate_moving_averages():
    prices = pd.Series([100] * 50, name='Price')
    signals = calculate_moving_averages(prices, short_window=5, long_window=10)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns
    assert 'price' in signals.columns

def test_generate_trading_signals():
    # Create a scenario where short crosses long
    # signal: 0, 0, 1, 1
    # positions: NaN, 0, 1, 0 (shifted by 1)

    data = {
        'price': [100, 100, 100, 100],
        'short_mavg': [90, 95, 105, 110],
        'long_mavg': [100, 100, 100, 100]
    }
    signals = pd.DataFrame(data)
    signals = generate_trading_signals(signals)

    assert 'positions' in signals.columns
    assert 'signal' in signals.columns
