import unittest
import pandas as pd
from bitcoin_trading_simulation import simulate_bitcoin_prices


class TestBitcoinSimulation(unittest.TestCase):
    def test_simulate_bitcoin_prices_length(self):
        days = 100
        prices = simulate_bitcoin_prices(days=days)
        self.assertEqual(len(prices), days)

    def test_simulate_bitcoin_prices_start_value(self):
        initial_price = 50000
        prices = simulate_bitcoin_prices(initial_price=initial_price)
        self.assertEqual(prices.iloc[0], initial_price)

    def test_simulate_bitcoin_prices_type(self):
        prices = simulate_bitcoin_prices()
        self.assertIsInstance(prices, pd.Series)
        self.assertEqual(prices.name, 'Price')

    def test_simulate_bitcoin_prices_values(self):
        # Check that prices are not all the same (volatility implies change)
        prices = simulate_bitcoin_prices(days=100, volatility=0.02)
        self.assertGreater(prices.std(), 0)


if __name__ == '__main__':
    unittest.main()
