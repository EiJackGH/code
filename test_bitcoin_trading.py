# Filename: test_bitcoin_trading.py
from bitcoin_trading_simulation import (
    simulate_bitcoin_prices,
    calculate_moving_averages,
    generate_trading_signals,
    simulate_trading
)
import pandas as pd


def test_simulate_bitcoin_prices():
    prices = simulate_bitcoin_prices(days=10, initial_price=100)
    assert len(prices) == 10
    assert prices.iloc[0] == 100


def test_calculate_moving_averages():
    prices = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], name='Price')
    signals = calculate_moving_averages(prices, short_window=2, long_window=5)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns


def test_generate_trading_signals():
    # Create a dummy signals DataFrame
    data = {
        'price': [100, 105, 110, 100, 90],
        'short_mavg': [100, 105, 110, 100, 90],
        'long_mavg': [100, 100, 100, 105, 110]
    }
    signals = pd.DataFrame(data)
    signals = generate_trading_signals(signals)
    assert 'signal' in signals.columns
    assert 'positions' in signals.columns
    # Check if signals are generated (1.0 for buy, -1.0 for sell)
    assert signals['signal'].iloc[2] == 1.0  # Buy signal
    assert signals['signal'].iloc[4] == -1.0  # Sell signal


def test_simulate_trading():
    # Create a dummy signals DataFrame with a buy signal
    data = {
        'price': [100, 105, 110],
        'short_mavg': [100, 105, 110],
        'long_mavg': [100, 100, 100],
        'positions': [0.0, 2.0, 0.0]  # Buy at index 1
    }
    signals = pd.DataFrame(data)
    portfolio = simulate_trading(signals, initial_cash=10000, quiet=True)
    assert not portfolio.empty
    assert portfolio['btc'].iloc[1] > 0
    assert portfolio['cash'].iloc[1] < 10000
