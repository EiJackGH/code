# Bitcoin Trading Simulation

A Python-based CLI tool that simulates Bitcoin trading using a 'Golden Cross' moving average strategy. It generates synthetic price data using Geometric Brownian Motion, executes trades based on technical indicators, and provides a daily ledger with a final performance summary.

## Features

- **Price Simulation:** Uses Geometric Brownian Motion to simulate 60 days of Bitcoin prices.
- **Trading Strategy:** Implements a Golden Cross strategy (Short MA > Long MA = Buy, Short MA < Long MA = Sell).
- **Rich CLI Output:** features color-coded logs (Green for Buy/Profit, Red for Sell/Loss) and emojis for better readability.
- **Performance metrics:** Compares the strategy's performance against a "Buy and Hold" approach.

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the simulation script with default settings:

```bash
python bitcoin_trading_simulation.py
```

### CLI Options

You can customize the simulation using the following arguments:

- `--days`: Number of days to simulate (default: 60)
- `--initial-cash`: Initial cash in USD (default: 10000)
- `--initial-price`: Initial Bitcoin price in USD (default: 50000)
- `--volatility`: Volatility factor (default: 0.02)
- `--quiet`, `-q`: Suppress daily portfolio logs (only show buy/sell events and final summary)
- `--no-color`: Disable colored output (useful for logs or non-ANSI terminals)

Example:
```bash
python bitcoin_trading_simulation.py --days 100 --initial-cash 5000 --quiet
```

## Tests

Run the test suite:

```bash
python test.py
```
