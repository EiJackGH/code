import subprocess
import sys


def run_cli(args):
    return subprocess.run(
        [sys.executable, "bitcoin_trading_simulation.py"] + args,
        capture_output=True,
        text=True
    )


def test_negative_days_error():
    """Negative days should fail with a helpful error message."""
    result = run_cli(["--days", "-5", "--quiet"])
    assert result.returncode == 1
    assert "Error: --days must be a positive integer" in result.stdout


def test_negative_cash_error():
    """Negative cash should fail with a helpful error message."""
    result = run_cli(["--initial-cash", "-100", "--quiet"])
    assert result.returncode == 1
    assert "Error: --initial-cash must be a positive amount" in result.stdout


def test_negative_volatility_error():
    """Negative volatility should fail with a helpful error message."""
    result = run_cli(["--volatility", "-0.1", "--quiet"])
    assert result.returncode == 1
    assert "Error: --volatility must be non-negative" in result.stdout
