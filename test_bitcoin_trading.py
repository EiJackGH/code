import unittest
import pandas as pd
import numpy as np
from bitcoin_trading_simulation import (
    simulate_bitcoin_prices,
    calculate_moving_averages,
    generate_trading_signals,
    Colors
)

class TestBitcoinTrading(unittest.TestCase):
    def test_simulate_bitcoin_prices(self):
        days = 10
        initial_price = 100
        prices = simulate_bitcoin_prices(days=days, initial_price=initial_price)
        self.assertIsInstance(prices, pd.Series)
        self.assertEqual(len(prices), days)
        self.assertEqual(prices.iloc[0], initial_price)

    def test_calculate_moving_averages(self):
        prices = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], name='Price')
        signals = calculate_moving_averages(prices, short_window=2, long_window=5)
        self.assertIn('short_mavg', signals.columns)
        self.assertIn('long_mavg', signals.columns)
        # Check values: window=2, min_periods=1
        # Day 0: 10
        # Day 1: (10+11)/2 = 10.5
        self.assertEqual(signals['short_mavg'].iloc[1], 10.5)

    def test_generate_trading_signals(self):
        # Create a dummy signals DataFrame
        data = {
            'price': [100, 101, 102, 103],
            'short_mavg': [100, 105, 90, 95],
            'long_mavg':  [100, 100, 100, 100]
        }
        signals = pd.DataFrame(data)
        signals = generate_trading_signals(signals)

        self.assertIn('signal', signals.columns)
        self.assertIn('positions', signals.columns)

        # Day 1: short (105) > long (100) -> signal 1.0 (Buy)
        self.assertEqual(signals['signal'].iloc[1], 1.0)

        # Day 2: short (90) < long (100) -> signal -1.0 (Sell)
        self.assertEqual(signals['signal'].iloc[2], -1.0)

        # Positions are shifted diff
        # signal: 0, 1, -1, -1
        # diff: NaN, 1, -2, 0
        # shifted: NaN, NaN, 1, -2
        self.assertTrue(np.isnan(signals['positions'].iloc[0]))
        self.assertTrue(np.isnan(signals['positions'].iloc[1]))
        self.assertEqual(signals['positions'].iloc[2], 1.0)
        self.assertEqual(signals['positions'].iloc[3], -2.0)

    def test_colors_disable(self):
        # Save original values just in case
        original_header = Colors.HEADER

        Colors.disable()
        self.assertEqual(Colors.HEADER, '')
        self.assertEqual(Colors.GREEN, '')
        self.assertEqual(Colors.RED, '')
        self.assertEqual(Colors.ENDC, '')

if __name__ == '__main__':
    unittest.main()
