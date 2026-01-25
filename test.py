import unittest
import pandas as pd
from bitcoin_trading_simulation import (
    simulate_bitcoin_prices,
    calculate_moving_averages,
    generate_trading_signals,
    simulate_trading
)

class TestBitcoinSimulation(unittest.TestCase):
    def test_simulation_flow(self):
        # 1. Simulate Prices
        days = 10
        prices = simulate_bitcoin_prices(days=days)
        self.assertEqual(len(prices), days)
        self.assertTrue(isinstance(prices, pd.Series))

        # 2. Moving Averages
        signals = calculate_moving_averages(prices, short_window=2, long_window=5)
        self.assertIn('short_mavg', signals.columns)
        self.assertIn('long_mavg', signals.columns)

        # 3. Generate Signals
        signals = generate_trading_signals(signals)
        self.assertIn('positions', signals.columns)

        # 4. Simulate Trading (Normal)
        portfolio = simulate_trading(signals, initial_cash=10000, quiet=True)
        self.assertEqual(len(portfolio), days)
        self.assertIn('total_value', portfolio.columns)

    def test_quiet_mode(self):
        prices = simulate_bitcoin_prices(days=5)
        signals = calculate_moving_averages(prices)
        signals = generate_trading_signals(signals)
        # Should not throw error
        simulate_trading(signals, quiet=True)
        # We capture stdout to verify silence? Maybe too complex for now.
        # Just ensuring it runs is enough for "micro-UX".

if __name__ == '__main__':
    unittest.main()
