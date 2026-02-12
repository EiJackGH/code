import unittest
from unittest.mock import patch
import pandas as pd
from bitcoin_trading_simulation import Colors, simulate_trading, main, simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals

class TestBitcoinSimulation(unittest.TestCase):

    def tearDown(self):
        # Reset Colors to default just in case
        Colors.HEADER = '\033[95m'
        Colors.BLUE = '\033[94m'
        Colors.GREEN = '\033[92m'
        Colors.RED = '\033[91m'
        Colors.ENDC = '\033[0m'
        Colors.BOLD = '\033[1m'

    def test_colors_disable(self):
        # Disable colors
        Colors.disable()

        # Verify empty strings
        self.assertEqual(Colors.HEADER, '')
        self.assertEqual(Colors.BLUE, '')
        self.assertEqual(Colors.GREEN, '')
        self.assertEqual(Colors.RED, '')
        self.assertEqual(Colors.ENDC, '')
        self.assertEqual(Colors.BOLD, '')

    @patch('builtins.print')
    def test_simulate_trading_quiet(self, mock_print):
        # Create dummy signals
        prices = pd.Series([100, 101, 102], name='Price')
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['positions'] = 0.0

        simulate_trading(signals, quiet=True)

        # Verify print was not called
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_simulate_trading_verbose(self, mock_print):
        # Create dummy signals
        prices = pd.Series([100, 101, 102], name='Price')
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['positions'] = 0.0

        simulate_trading(signals, quiet=False)

        # Verify print was called (at least for the header)
        self.assertTrue(mock_print.called)

    def test_main_runs(self):
        # Run main with small number of days to ensure no errors
        # We can suppress output with quiet=True
        try:
            main(days=5, initial_price=100, volatility=0.01, initial_cash=1000, quiet=True, no_color=True)
        except Exception as e:
            self.fail(f"main() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
