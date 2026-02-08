import numpy as np
import pandas as pd
import argparse


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    @classmethod
    def disable(cls):
        cls.HEADER = ''
        cls.BLUE = ''
        cls.GREEN = ''
        cls.RED = ''
        cls.ENDC = ''
        cls.BOLD = ''


def simulate_bitcoin_prices(days=60, initial_price=50000, volatility=0.02):
    """
    Simulates Bitcoin prices for a given number of days using Geometric Brownian Motion.
    """
    dt = 1
    prices = [initial_price]
    for _ in range(days - 1):
        # Using a simplified model for daily price changes
        drift = 0  # Assuming no long-term drift for simplicity
        shock = np.random.normal(0, volatility)
        price_change = prices[-1] * (drift * dt + shock * np.sqrt(dt))
        prices.append(prices[-1] + price_change)
    return pd.Series(prices, name='Price')


def calculate_moving_averages(prices, short_window=7, long_window=30):
    """
    Calculates short and long moving averages for a given price series.
    """
    signals = pd.DataFrame(index=prices.index)
    signals['price'] = prices
    signals['short_mavg'] = prices.rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = prices.rolling(window=long_window, min_periods=1, center=False).mean()
    return signals


def generate_trading_signals(signals):
    """
    Generates trading signals based on the Golden Cross strategy.
    A buy signal (1.0) is generated when the short moving average crosses above the long moving average.
    A sell signal (-1.0) is generated when the short moving average crosses below the long moving average.
    """
    signals['signal'] = 0.0
    # A Golden Cross (buy signal)
    signals.loc[signals['short_mavg'] > signals['long_mavg'], 'signal'] = 1.0
    # A Death Cross (sell signal)
    signals.loc[signals['short_mavg'] < signals['long_mavg'], 'signal'] = -1.0

    # We create 'positions' to represent the trading action: 1 for buy, -1 for sell, 0 for hold
    signals['positions'] = signals['signal'].diff().shift(1)
    return signals


def simulate_trading(signals, initial_cash=10000, quiet=False):
    """
    Simulates trading based on signals and prints a daily ledger.
    """
    portfolio = pd.DataFrame(index=signals.index).fillna(0.0)
    portfolio['price'] = signals['price']
    portfolio['cash'] = float(initial_cash)
    portfolio['btc'] = 0.0
    portfolio['total_value'] = float(initial_cash)

    if not quiet:
        print(f"{Colors.HEADER}{Colors.BOLD}------ Daily Trading Ledger ------{Colors.ENDC}")

    for i, row in signals.iterrows():
        if i > 0:
            portfolio.loc[i, 'cash'] = portfolio.loc[i - 1, 'cash']
            portfolio.loc[i, 'btc'] = portfolio.loc[i - 1, 'btc']

        # Buy signal
        if row['positions'] == 2.0:
            btc_to_buy = portfolio.loc[i, 'cash'] / row['price']
            portfolio.loc[i, 'btc'] += btc_to_buy
            portfolio.loc[i, 'cash'] -= btc_to_buy * row['price']
            print(f"{Colors.GREEN}Day {i}: 💰 Buy {btc_to_buy:.4f} BTC at ${row['price']:.2f}{Colors.ENDC}")

        # Sell signal
        elif row['positions'] == -2.0:
            if portfolio.loc[i, 'btc'] > 0:
                cash_received = portfolio.loc[i, 'btc'] * row['price']
                portfolio.loc[i, 'cash'] += cash_received
                print(f"{Colors.RED}Day {i}: 📉 Sell {portfolio.loc[i, 'btc']:.4f} BTC at ${row['price']:.2f}{Colors.ENDC}")
                portfolio.loc[i, 'btc'] = 0

        portfolio.loc[i, 'total_value'] = portfolio.loc[i, 'cash'] + portfolio.loc[i, 'btc'] * row['price']

        if not quiet:
            print(f"Day {i}: Portfolio Value: ${portfolio.loc[i, 'total_value']:.2f}, "
                  f"Cash: ${portfolio.loc[i, 'cash']:.2f}, BTC: {portfolio.loc[i, 'btc']:.4f}")

    return portfolio


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitcoin Trading Simulation")
    parser.add_argument("--days", type=int, default=60, help="Number of days to simulate")
    parser.add_argument("--initial-cash", type=float, default=10000, help="Initial cash amount")
    parser.add_argument("--initial-price", type=float, default=50000, help="Initial Bitcoin price")
    parser.add_argument("--volatility", type=float, default=0.02, help="Price volatility")
    parser.add_argument("--quiet", action="store_true", help="Suppress daily ledger output")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")

    args = parser.parse_args()

    if args.no_color:
        Colors.disable()

    # Simulate prices
    prices = simulate_bitcoin_prices(days=args.days, initial_price=args.initial_price, volatility=args.volatility)

    # Calculate moving averages
    signals = calculate_moving_averages(prices)

    # Generate trading signals
    signals = generate_trading_signals(signals)

    # Simulate trading
    portfolio = simulate_trading(signals, initial_cash=args.initial_cash, quiet=args.quiet)

    # Final portfolio performance
    final_value = portfolio['total_value'].iloc[-1]
    initial_cash = args.initial_cash
    profit = final_value - initial_cash

    # Compare with buy and hold strategy
    buy_and_hold_btc = initial_cash / prices.iloc[0]
    buy_and_hold_value = buy_and_hold_btc * prices.iloc[-1]

    print(f"\n{Colors.HEADER}{Colors.BOLD}------ Final Portfolio Performance ------{Colors.ENDC}")
    print(f"Initial Cash: ${initial_cash:.2f}")
    print(f"Final Portfolio Value: ${final_value:.2f}")

    if profit >= 0:
        print(f"Profit/Loss: {Colors.GREEN}📈 ${profit:.2f}{Colors.ENDC}")
    else:
        print(f"Profit/Loss: {Colors.RED}📉 ${profit:.2f}{Colors.ENDC}")

    print(f"Buy and Hold Strategy Value: ${buy_and_hold_value:.2f}")
    print(f"{Colors.HEADER}-----------------------------------------{Colors.ENDC}")
