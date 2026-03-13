import pandas as pd
from bitcoin_trading_simulation import simulate_trading

def test_quiet_suppresses_buys_sells():
    signals = pd.DataFrame(index=range(3))
    signals['price'] = [100.0, 101.0, 102.0]
    signals['positions'] = [2.0, -2.0, 0.0]

    import io
    import sys

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    simulate_trading(signals, initial_cash=1000, quiet=True)
    out = sys.stdout.getvalue()
    sys.stdout = old_stdout

    assert out == ""

test_quiet_suppresses_buys_sells()
print("Passed")
