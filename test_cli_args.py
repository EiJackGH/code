import sys
import subprocess
import pytest

def run_simulation(args):
    """
    Helper function to run the simulation script as a subprocess.
    """
    cmd = [sys.executable, "bitcoin_trading_simulation.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def test_cli_invalid_days():
    """Test that non-positive days results in error."""
    result = run_simulation(["--days", "-5"])
    assert result.returncode == 1
    assert "Error: Days must be a positive integer." in result.stderr

    result = run_simulation(["--days", "0"])
    assert result.returncode == 1
    assert "Error: Days must be a positive integer." in result.stderr

def test_cli_invalid_initial_cash():
    """Test that non-positive initial cash results in error."""
    result = run_simulation(["--initial-cash", "-1000"])
    assert result.returncode == 1
    assert "Error: Initial cash must be greater than 0." in result.stderr

    result = run_simulation(["--initial-cash", "0"])
    assert result.returncode == 1
    assert "Error: Initial cash must be greater than 0." in result.stderr

def test_cli_invalid_initial_price():
    """Test that non-positive initial price results in error."""
    result = run_simulation(["--initial-price", "-500"])
    assert result.returncode == 1
    assert "Error: Initial price must be greater than 0." in result.stderr

def test_cli_invalid_volatility():
    """Test that negative volatility results in error."""
    result = run_simulation(["--volatility", "-0.1"])
    assert result.returncode == 1
    assert "Error: Volatility must be non-negative." in result.stderr

def test_cli_valid_args():
    """Test that valid arguments run successfully."""
    # Run with small days to keep test fast
    result = run_simulation(["--days", "5", "--quiet"])
    assert result.returncode == 0
    assert "Final Portfolio Performance" in result.stdout

def test_cli_no_color_error():
    """Test that error messages respect --no-color flag (no ANSI codes)."""
    result = run_simulation(["--days", "-5", "--no-color"])
    assert result.returncode == 1
    # Check that the ANSI fail code is NOT in the output
    assert "\033[91m" not in result.stderr
    assert "Error: Days must be a positive integer." in result.stderr
