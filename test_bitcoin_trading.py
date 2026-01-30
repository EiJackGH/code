import pytest
import pandas as pd
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals, simulate_trading

def test_simulation_runs():
    # Run with small number of days for speed
    prices = simulate_bitcoin_prices(days=20, initial_price=100)
    assert isinstance(prices, pd.Series)
    assert len(prices) == 20

    signals = calculate_moving_averages(prices, short_window=5, long_window=10)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns

    signals = generate_trading_signals(signals)
    assert 'signal' in signals.columns
    assert 'positions' in signals.columns

    # We can't easily test simulate_trading output without capturing stdout,
    # but we can check if it returns a portfolio DataFrame
    portfolio = simulate_trading(signals, initial_cash=1000)
    assert isinstance(portfolio, pd.DataFrame)
    assert 'total_value' in portfolio.columns
    # Basic sanity check that value isn't NaN or something weird
    assert not portfolio['total_value'].isnull().any()
