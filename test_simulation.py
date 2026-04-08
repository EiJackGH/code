import pandas as pd
import numpy as np
from bitcoin_trading_simulation import (
    simulate_bitcoin_prices, calculate_moving_averages,
    generate_trading_signals, simulate_trading
)


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


def test_initial_buy_signal():
    """Verify that a buy signal on the very first day is executed."""
    data = {
        'price': [100, 105, 110],
        'signal': [1.0, 1.0, 1.0]  # Constant buy signal from day 0
    }
    signals = pd.DataFrame(data)
    portfolio = simulate_trading(signals, initial_cash=1000, quiet=True)

    # On day 0, it should have bought BTC
    assert portfolio.loc[0, 'btc'] == 1000 / 100
    assert portfolio.loc[0, 'cash'] == 0


def test_initial_sell_signal():
    """Verify that a sell signal on the first day is handled (though usually we start with cash)."""
    # Start with some BTC and a sell signal
    data = {
        'price': [100, 90, 80],
        'signal': [-1.0, -1.0, -1.0]
    }
    signals = pd.DataFrame(data)
    # Manually inject BTC into the simulation for testing if possible,
    # but simulate_trading initializes btc to 0.
    # So we test if it stays at 0 and doesn't crash.
    portfolio = simulate_trading(signals, initial_cash=1000, quiet=True)
    assert portfolio.loc[0, 'btc'] == 0
    assert portfolio.loc[0, 'cash'] == 1000
