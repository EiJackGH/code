import sys
import pandas as pd
from bitcoin_trading_simulation import simulate_trading, Colors

# mock isatty
sys.stdout.isatty = lambda: True

signals = pd.DataFrame(index=range(10))
signals['price'] = [100.0] * 10
signals['positions'] = [0.0] * 10

simulate_trading(signals, quiet=True)
