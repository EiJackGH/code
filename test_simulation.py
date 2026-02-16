import pytest
import pandas as pd
import numpy as np
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals

def test_simulate_bitcoin_prices():
    prices = simulate_bitcoin_prices(days=10, initial_price=100, volatility=0.01)
    assert len(prices) == 10
    assert isinstance(prices, pd.Series)
    assert prices.iloc[0] == 100

def test_calculate_moving_averages():
    prices = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], name='Price')
    signals = calculate_moving_averages(prices, short_window=3, long_window=5)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns
    assert len(signals) == 10

def test_generate_trading_signals():
    # create dummy signals dataframe
    signals = pd.DataFrame({
        'price': [100, 101, 102, 103, 104],
        'short_mavg': [100, 101, 102, 103, 104],
        'long_mavg': [99, 100, 101, 102, 103]
    })
    # Here short > long, so signal should be 1.0 (buy)

    signals_with_logic = generate_trading_signals(signals)
    assert 'signal' in signals_with_logic.columns
    assert 'positions' in signals_with_logic.columns
    # Check if logic is applied (dummy check)
    assert (signals_with_logic['signal'] == 1.0).all()
