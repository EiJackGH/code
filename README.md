# Bitcoin Trading Simulation

A Python-based simulation of Bitcoin trading using a "Golden Cross" strategy (Moving Average Crossover).

## Features

- **Simulated Data**: Generates synthetic Bitcoin price data using Geometric Brownian Motion.
- **Trading Strategy**: Implements a Golden Cross strategy (Short MA > Long MA = Buy).
- **Performance Analysis**: Calculates final portfolio value and compares it against a "Buy and Hold" strategy.
- **Visual CLI**: Color-coded output for easy reading of trade actions and performance.

## Requirements

- Python 3.x
- pandas
- numpy

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the simulation:
   ```bash
   python bitcoin_trading_simulation.py
   ```
