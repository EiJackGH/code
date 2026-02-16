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

Run the simulation script:

```bash
python bitcoin_trading_simulation.py
```

## Tests

Run the test suite:

```bash
python test.py
```
