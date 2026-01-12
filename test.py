import unittest
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals, simulate_trading

class TestSimulation(unittest.TestCase):
    def test_simulation_pipeline(self):
        # Run the full pipeline with a smaller dataset to ensure no crashes
        try:
            prices = simulate_bitcoin_prices(days=20)
            signals = calculate_moving_averages(prices, short_window=3, long_window=10)
            signals = generate_trading_signals(signals)
            portfolio = simulate_trading(signals)

            self.assertFalse(portfolio.empty)
            self.assertTrue('total_value' in portfolio.columns)
        except Exception as e:
            self.fail(f"Simulation failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
