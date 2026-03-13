import sys
from bitcoin_trading_simulation import simulate_bitcoin_prices, calculate_moving_averages, generate_trading_signals, simulate_trading

prices = simulate_bitcoin_prices(days=60, initial_price=50000, volatility=0.02)
signals = calculate_moving_averages(prices)
signals = generate_trading_signals(signals)
simulate_trading(signals, quiet=True)
