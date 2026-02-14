import argparse
import numpy as np
import pandas as pd


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
    Simulates Bitcoin prices for a given number of days using GBM.
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
    signals['short_mavg'] = prices.rolling(
        window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = prices.rolling(
        window=long_window, min_periods=1, center=False).mean()
    return signals


def generate_trading_signals(signals):
    """
    Generates trading signals based on the Golden Cross strategy.
    """
    signals['signal'] = 0.0
    # A Golden Cross (buy signal)
    signals.loc[signals['short_mavg'] > signals['long_mavg'], 'signal'] = 1.0
    # A Death Cross (sell signal)
    signals.loc[signals['short_mavg'] < signals['long_mavg'], 'signal'] = -1.0

    # Create 'positions': 1 for buy, -1 for sell, 0 for hold
    signals['positions'] = signals['signal'].diff().shift(1)
    return signals


def simulate_trading(signals, initial_cash=10000, quiet=False):
    """
    Simulates trading based on signals and prints a daily ledger.
    """
    # Use lists to store history for performance optimization
    # Iterating over numpy arrays is faster than DataFrame.loc access
    cash_history = []
    btc_history = []
    total_value_history = []

    current_cash = float(initial_cash)
    current_btc = 0.0

    # Extract data to numpy arrays for faster iteration
    prices = signals['price'].values
    positions = signals['positions'].fillna(0.0).values

    if not quiet:
        print(f"{Colors.HEADER}{Colors.BOLD}"
              f"------ Daily Trading Ledger ------{Colors.ENDC}")

    for i in range(len(signals)):
        price = prices[i]
        position = positions[i]

        # Buy signal
        if position == 2.0:
            btc_to_buy = current_cash / price
            current_btc += btc_to_buy
            current_cash -= btc_to_buy * price
            if not quiet:
                print(f"{Colors.GREEN}Day {i}: 💰 Buy {btc_to_buy:.4f} "
                      f"BTC at ${price:.2f}{Colors.ENDC}")

        # Sell signal
        elif position == -2.0:
            if current_btc > 0:
                cash_received = current_btc * price
                current_cash += cash_received
                if not quiet:
                    print(f"{Colors.RED}Day {i}: 📉 Sell {current_btc:.4f} "
                          f"BTC at ${price:.2f}{Colors.ENDC}")
                current_btc = 0.0

        # Calculate total value
        total_value = current_cash + current_btc * price

        # Store history
        cash_history.append(current_cash)
        btc_history.append(current_btc)
        total_value_history.append(total_value)

        if not quiet:
            print(f"Day {i}: Portfolio Value: ${total_value:.2f}, "
                  f"Cash: ${current_cash:.2f}, BTC: {current_btc:.4f}")

    # Create portfolio DataFrame from lists
    portfolio = pd.DataFrame(index=signals.index)
    portfolio['price'] = signals['price']
    portfolio['cash'] = cash_history
    portfolio['btc'] = btc_history
    portfolio['total_value'] = total_value_history

    return portfolio


def main(days, initial_cash, initial_price, volatility, quiet, no_color):
    if no_color:
        Colors.disable()

    # Simulate prices
    prices = simulate_bitcoin_prices(
        days=days, initial_price=initial_price, volatility=volatility)

    # Calculate moving averages
    signals = calculate_moving_averages(prices)

    # Generate trading signals
    signals = generate_trading_signals(signals)

    # Simulate trading
    portfolio = simulate_trading(
        signals, initial_cash=initial_cash, quiet=quiet)

    # Final portfolio performance
    final_value = portfolio['total_value'].iloc[-1]
    profit = final_value - initial_cash

    # Compare with buy and hold strategy
    buy_and_hold_btc = initial_cash / prices.iloc[0]
    buy_and_hold_value = buy_and_hold_btc * prices.iloc[-1]

    print(f"\n{Colors.HEADER}{Colors.BOLD}"
          f"------ Final Portfolio Performance ------{Colors.ENDC}")
    print(f"Initial Cash: ${initial_cash:.2f}")
    print(f"Final Portfolio Value: ${final_value:.2f}")

    if profit >= 0:
        print(f"Profit/Loss: {Colors.GREEN}📈 ${profit:.2f}{Colors.ENDC}")
    else:
        print(f"Profit/Loss: {Colors.RED}📉 ${profit:.2f}{Colors.ENDC}")

    print(f"Buy and Hold Strategy Value: ${buy_and_hold_value:.2f}")
    print(f"{Colors.HEADER}-----------------------------------------"
          f"{Colors.ENDC}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitcoin Trading Simulation")
    parser.add_argument("--days", type=int, default=60,
                        help="Number of days to simulate")
    parser.add_argument("--initial-cash", type=float, default=10000,
                        help="Initial cash amount")
    parser.add_argument("--initial-price", type=float, default=50000,
                        help="Initial Bitcoin price")
    parser.add_argument("--volatility", type=float, default=0.02,
                        help="Price volatility")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress daily portfolio log")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable colored output")

    args = parser.parse_args()

    main(
        days=args.days,
        initial_cash=args.initial_cash,
        initial_price=args.initial_price,
        volatility=args.volatility,
        quiet=args.quiet,
        no_color=args.no_color
    )
