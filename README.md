# Bitcoin Trading Simulation

A Python-based CLI tool that simulates Bitcoin trading using a 'Golden Cross' moving average strategy. It generates synthetic price data using Geometric Brownian Motion, executes trades based on technical indicators, and provides a daily ledger with a final performance summary.

## Features

- **Price Simulation:** Uses Geometric Brownian Motion to simulate Bitcoin prices.
- **Trading Strategy:** Implements a Golden Cross strategy (Short MA > Long MA = Buy, Short MA < Long MA = Sell).
- **Rich CLI Output:** Features color-coded logs (Green for Buy/Profit, Red for Sell/Loss) and emojis for better readability.
- **Performance metrics:** Compares the strategy's performance against a "Buy and Hold" approach.
- **Customizable:** Configure simulation parameters via command-line arguments.

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the simulation script with default settings (60 days, $10k initial cash):

```bash
python bitcoin_trading_simulation.py
```

### Options

Customize the simulation with the following arguments:

```bash
python bitcoin_trading_simulation.py --days 100 --initial-cash 5000 --initial-price 60000 --volatility 0.03
```

- `--days`: Number of days to simulate (default: 60)
- `--initial-cash`: Initial cash amount (default: 10000)
- `--initial-price`: Initial Bitcoin price (default: 50000)
- `--volatility`: Price volatility (default: 0.02)
- `--quiet`: Suppress daily portfolio log (only show final result)
- `--no-color`: Disable colored output (for accessibility or logging)

Example:
```bash
python bitcoin_trading_simulation.py --days 30 --quiet --no-color
```

## Tests

Run the test suite using `pytest`:

```bash
pytest
```
