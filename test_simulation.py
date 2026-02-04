import subprocess
import sys
import pandas as pd
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals


def test_simulate_bitcoin_prices():
    days = 10
    prices = simulate_bitcoin_prices(days=days, initial_price=100, volatility=0.01)
    assert len(prices) == days
    assert isinstance(prices, pd.Series)
    assert prices.iloc[0] == 100


def test_calculate_moving_averages():
    prices = pd.Series([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
    signals = calculate_moving_averages(prices, short_window=3, long_window=5)
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns
    assert not signals['short_mavg'].isnull().all()


def test_generate_trading_signals():
    # Create a dummy signal dataframe
    data = {
        'price': [100, 110, 100, 90, 100],
        'short_mavg': [100, 110, 100, 90, 100],
        'long_mavg': [100, 100, 100, 100, 100]
    }
    signals = pd.DataFrame(data)
    signals = generate_trading_signals(signals)
    assert 'positions' in signals.columns
    # Check if signals are generated (1.0 or -1.0 or 0.0)
    assert signals['signal'].isin([1.0, -1.0, 0.0]).all()


def test_cli_execution():
    # Test running the script via subprocess to ensure it doesn't crash
    result = subprocess.run([sys.executable, 'bitcoin_trading_simulation.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Daily Trading Ledger" in result.stdout
    assert "Final Portfolio Performance" in result.stdout
