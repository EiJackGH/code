import unittest
from unittest.mock import patch
from io import StringIO
import sys
from bitcoin_trading_simulation import main

class TestSecurity(unittest.TestCase):

    def test_negative_days(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stderr', new=StringIO()) as fake_err:
                main(['--days', '-5'])
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: --days must be positive.", fake_err.getvalue())

    def test_excessive_days_dos(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stderr', new=StringIO()) as fake_err:
                main(['--days', '100000'])
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: --days must be <= 36500", fake_err.getvalue())

    def test_negative_cash(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stderr', new=StringIO()) as fake_err:
                main(['--initial-cash', '-100'])
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: --initial-cash must be non-negative.", fake_err.getvalue())

    def test_negative_price(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stderr', new=StringIO()) as fake_err:
                main(['--initial-price', '-500'])
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: --initial-price must be positive.", fake_err.getvalue())

    def test_negative_volatility(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stderr', new=StringIO()) as fake_err:
                main(['--volatility', '-0.1'])
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: --volatility must be non-negative.", fake_err.getvalue())

if __name__ == '__main__':
    unittest.main()
