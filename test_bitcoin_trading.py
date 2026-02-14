import unittest
import sys
import io
import pandas as pd
import subprocess
from bitcoin_trading_simulation import Colors, simulate_trading, simulate_bitcoin_prices

class TestBitcoinTradingSimulation(unittest.TestCase):

    def setUp(self):
        # Reset Colors to default before each test to prevent side effects
        Colors.HEADER = '\033[95m'
        Colors.BLUE = '\033[94m'
        Colors.GREEN = '\033[92m'
        Colors.RED = '\033[91m'
        Colors.ENDC = '\033[0m'
        Colors.BOLD = '\033[1m'

    def test_simulate_bitcoin_prices(self):
        prices = simulate_bitcoin_prices(days=10, initial_price=100)
        self.assertEqual(len(prices), 10)
        self.assertEqual(prices.iloc[0], 100)

    def test_colors_disable(self):
        Colors.disable()
        self.assertEqual(Colors.HEADER, '')
        self.assertEqual(Colors.GREEN, '')
        self.assertEqual(Colors.RED, '')

    def test_quiet_mode_function(self):
        # Create dummy signals
        prices = pd.Series([100, 101, 102], name='Price')
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['positions'] = 0.0

        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        simulate_trading(signals, quiet=True)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Expect no output in quiet mode (since no trades and quiet=True)
        self.assertEqual(output, "")

    def test_verbose_mode_function(self):
        # Create dummy signals
        prices = pd.Series([100, 101, 102], name='Price')
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['positions'] = 0.0

        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        simulate_trading(signals, quiet=False)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Daily Trading Ledger", output)

    def test_integration_no_color(self):
        # Run the script via subprocess to verify --no-color
        result = subprocess.run(
            [sys.executable, 'bitcoin_trading_simulation.py', '--days', '5', '--no-color'],
            capture_output=True,
            text=True
        )
        # Check that ANSI codes are NOT present
        self.assertNotIn('\033[', result.stdout)
        # Check that the output is still meaningful
        self.assertIn('Final Portfolio Performance', result.stdout)

    def test_integration_quiet(self):
        # Run the script via subprocess to verify --quiet
        result = subprocess.run(
            [sys.executable, 'bitcoin_trading_simulation.py', '--days', '5', '--quiet'],
            capture_output=True,
            text=True
        )
        # Check that Daily Ledger is NOT present
        self.assertNotIn('Daily Trading Ledger', result.stdout)
        # Check that Final Performance IS present
        self.assertIn('Final Portfolio Performance', result.stdout)

    def test_integration_args(self):
        # Verify custom arguments work
        result = subprocess.run(
            [sys.executable, 'bitcoin_trading_simulation.py', '--days', '5', '--initial-cash', '500'],
            capture_output=True,
            text=True
        )
        self.assertIn('Initial Cash: $500.00', result.stdout)

if __name__ == '__main__':
    unittest.main()
