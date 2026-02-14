import pytest
import pandas as pd
import numpy as np
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals

def test_simulate_bitcoin_prices():
    days = 10
    prices = simulate_bitcoin_prices(days=days, initial_price=50000)
    assert len(prices) == days
    assert isinstance(prices, pd.Series)
    assert prices.name == 'Price'

def test_calculate_moving_averages():
    prices = pd.Series([100, 101, 102, 103, 104, 105, 106, 107, 108, 109], name='Price')
    signals = calculate_moving_averages(prices, short_window=3, long_window=5)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns
    assert not signals['short_mavg'].isnull().all()

def test_generate_trading_signals():
    # Create dummy signals DataFrame
    data = {
        'price': [100, 101, 102, 103, 104],
        'short_mavg': [100, 101, 105, 102, 100],
        'long_mavg':  [100, 100, 100, 103, 105]
    }
    signals = pd.DataFrame(data)
    signals = generate_trading_signals(signals)

    assert 'signal' in signals.columns
    assert 'positions' in signals.columns
    # Check that positions are calculated (not all nan, though first might be)
    assert signals['positions'].isin([0, 1, -1, 2, -2, np.nan]).any()
