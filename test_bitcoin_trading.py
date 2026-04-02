import pytest
import pandas as pd
from bitcoin_trading_simulation import (
    simulate_trading, Colors, calculate_moving_averages,
    generate_trading_signals, simulate_bitcoin_prices
)


@pytest.fixture
def reset_colors():
    # Save original colors
    original_colors = {
        'HEADER': Colors.HEADER,
        'BLUE': Colors.BLUE,
        'GREEN': Colors.GREEN,
        'FAIL': Colors.FAIL,
        'ENDC': Colors.ENDC,
        'BOLD': Colors.BOLD,
    }
    yield
    # Restore colors
    Colors.HEADER = original_colors['HEADER']
    Colors.BLUE = original_colors['BLUE']
    Colors.GREEN = original_colors['GREEN']
    Colors.FAIL = original_colors['FAIL']
    Colors.ENDC = original_colors['ENDC']
    Colors.BOLD = original_colors['BOLD']


def test_simulate_trading_quiet_mode(capsys):
    """Test that quiet mode suppresses output."""
    signals = pd.DataFrame(index=range(5))
    signals['price'] = [100.0, 101.0, 102.0, 103.0, 104.0]
    signals['signal'] = [0.0] * 5
    signals['positions'] = [0.0] * 5

    simulate_trading(signals, initial_cash=1000, quiet=True)

    captured = capsys.readouterr()
    assert captured.out == ""


def test_simulate_trading_verbose_mode(capsys):
    """Test that verbose mode prints daily ledger."""
    signals = pd.DataFrame(index=range(2))
    signals['price'] = [100.0, 101.0]
    signals['signal'] = [0.0, 0.0]
    signals['positions'] = [0.0, 0.0]

    simulate_trading(signals, initial_cash=1000, quiet=False)

    captured = capsys.readouterr()
    assert "Daily Trading Ledger" in captured.out
    assert "Portfolio Value" in captured.out


def test_colors_disable(reset_colors):
    """Test that Colors.disable() clears color codes."""
    assert Colors.HEADER != ""
    Colors.disable()
    assert Colors.HEADER == ""
    assert Colors.GREEN == ""
    assert Colors.FAIL == ""


def test_simulation_integration():
    """Test full simulation pipeline with small parameters."""
    prices = simulate_bitcoin_prices(days=10, initial_price=100)
    signals = calculate_moving_averages(prices, short_window=2, long_window=5)
    signals = generate_trading_signals(signals)
    portfolio = simulate_trading(signals, quiet=True)

    assert len(portfolio) == 10
    assert 'total_value' in portfolio.columns
    assert 'btc' in portfolio.columns
    assert 'cash' in portfolio.columns
