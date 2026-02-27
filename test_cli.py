import subprocess
import pytest
import sys

def run_cli(args):
    """Runs the CLI script with given arguments."""
    cmd = [sys.executable, "bitcoin_trading_simulation.py"] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    return result

def test_cli_negative_days():
    result = run_cli(["--days", "-5"])
    assert result.returncode == 1
    assert "Error: --days must be a positive integer." in result.stdout

def test_cli_zero_days():
    result = run_cli(["--days", "0"])
    assert result.returncode == 1
    assert "Error: --days must be a positive integer." in result.stdout

def test_cli_negative_cash():
    result = run_cli(["--initial-cash", "-100"])
    assert result.returncode == 1
    assert "Error: --initial-cash must be positive." in result.stdout

def test_cli_zero_cash():
    result = run_cli(["--initial-cash", "0"])
    assert result.returncode == 1
    assert "Error: --initial-cash must be positive." in result.stdout

def test_cli_negative_price():
    result = run_cli(["--initial-price", "-500"])
    assert result.returncode == 1
    assert "Error: --initial-price must be positive." in result.stdout

def test_cli_negative_volatility():
    result = run_cli(["--volatility", "-0.5"])
    assert result.returncode == 1
    assert "Error: --volatility must be non-negative." in result.stdout

def test_cli_valid_run():
    # Run with a short duration and quiet mode for speed
    result = run_cli(["--days", "5", "--quiet", "--no-color"])
    assert result.returncode == 0
    assert "Final Portfolio Performance" in result.stdout
