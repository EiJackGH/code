import unittest
import pandas as pd
from bitcoin_trading_simulation import (
    simulate_bitcoin_prices,
    calculate_moving_averages,
    generate_trading_signals,
    simulate_trading
)


class TestBitcoinSimulation(unittest.TestCase):
    def test_simulate_bitcoin_prices(self):
        days = 10
        prices = simulate_bitcoin_prices(days=days)
        self.assertIsInstance(prices, pd.Series)
        self.assertEqual(len(prices), days)

    def test_calculate_moving_averages(self):
        prices = simulate_bitcoin_prices(days=20)
        signals = calculate_moving_averages(prices, short_window=5, long_window=10)
        self.assertIsInstance(signals, pd.DataFrame)
        self.assertIn('short_mavg', signals.columns)
        self.assertIn('long_mavg', signals.columns)

    def test_generate_trading_signals(self):
        prices = simulate_bitcoin_prices(days=20)
        signals = calculate_moving_averages(prices, short_window=5, long_window=10)
        signals = generate_trading_signals(signals)
        self.assertIn('signal', signals.columns)
        self.assertIn('positions', signals.columns)

    def test_simulate_trading(self):
        prices = simulate_bitcoin_prices(days=20)
        signals = calculate_moving_averages(prices, short_window=5, long_window=10)
        signals = generate_trading_signals(signals)
        portfolio = simulate_trading(signals, initial_cash=10000, quiet=True)
        self.assertIsInstance(portfolio, pd.DataFrame)
        self.assertIn('total_value', portfolio.columns)
        self.assertIn('cash', portfolio.columns)
        self.assertIn('btc', portfolio.columns)
        self.assertEqual(len(portfolio), 20)


if __name__ == '__main__':
    unittest.main()
