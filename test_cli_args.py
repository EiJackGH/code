import subprocess
import sys
import pytest

def run_simulation(args):
    """Runs the simulation script with the given arguments."""
    cmd = [sys.executable, "bitcoin_trading_simulation.py"] + args
    return subprocess.run(cmd, capture_output=True, text=True)

def test_invalid_days():
    result = run_simulation(["--days", "-5"])
    assert result.returncode != 0, "Simulation should fail with negative days"
    assert "days must be a positive integer" in result.stderr.lower() or "days must be a positive integer" in result.stdout.lower()

def test_invalid_initial_cash():
    result = run_simulation(["--initial-cash", "-1000"])
    assert result.returncode != 0, "Simulation should fail with negative cash"
    assert "initial cash must be positive" in result.stderr.lower() or "initial cash must be positive" in result.stdout.lower()

def test_invalid_initial_price():
    result = run_simulation(["--initial-price", "-500"])
    assert result.returncode != 0, "Simulation should fail with negative price"
    assert "initial price must be positive" in result.stderr.lower() or "initial price must be positive" in result.stdout.lower()

def test_invalid_volatility():
    result = run_simulation(["--volatility", "-0.1"])
    assert result.returncode != 0, "Simulation should fail with negative volatility"
    assert "volatility must be non-negative" in result.stderr.lower() or "volatility must be non-negative" in result.stdout.lower()

def test_valid_run():
    # Run with quiet mode to speed up test
    result = run_simulation(["--days", "10", "--quiet"])
    assert result.returncode == 0, "Valid simulation should succeed"
