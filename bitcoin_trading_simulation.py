import numpy as np
import pandas as pd

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

def simulate_trading(signals, initial_cash=10000):
    """
    Simulates trading based on signals and prints a daily ledger.
    Optimized to use numpy arrays instead of pandas iteration for speed.
    """
    # Pre-allocate arrays for performance
    n = len(signals)
    index = signals.index
    prices = signals['price'].values
    positions = signals['positions'].values

    cash = np.zeros(n, dtype=np.float64)
    btc = np.zeros(n, dtype=np.float64)
    total_value = np.zeros(n, dtype=np.float64)

    current_cash = float(initial_cash)
    current_btc = 0.0

    print("------ Daily Trading Ledger ------")

    for i in range(n):
        price = prices[i]
        pos = positions[i]
        idx_label = index[i]

        # Buy signal
        if pos == 2.0:
            btc_to_buy = current_cash / price
            current_btc += btc_to_buy
            current_cash -= btc_to_buy * price
            print(f"Day {idx_label}: Buy {btc_to_buy:.4f} BTC at ${price:.2f}")

        # Sell signal
        elif pos == -2.0:
            if current_btc > 0:
                cash_received = current_btc * price
                current_cash += cash_received
                print(f"Day {idx_label}: Sell {current_btc:.4f} BTC at ${price:.2f}")
                current_btc = 0.0

        cash[i] = current_cash
        btc[i] = current_btc
        total_value[i] = current_cash + current_btc * price

        print(f"Day {idx_label}: Portfolio Value: ${total_value[i]:.2f}, Cash: ${current_cash:.2f}, BTC: {current_btc:.4f}")

    portfolio = pd.DataFrame({
        'price': prices,
        'cash': cash,
        'btc': btc,
        'total_value': total_value
    }, index=index)
    
    return portfolio

if __name__ == "__main__":
    # Simulate prices
    prices = simulate_bitcoin_prices()
    
    # Calculate moving averages
    signals = calculate_moving_averages(prices)
    
    # Generate trading signals
    signals = generate_trading_signals(signals)
    
    # Simulate trading
    portfolio = simulate_trading(signals)
    
    # Final portfolio performance
    final_value = portfolio['total_value'].iloc[-1]
    initial_cash = 10000
    profit = final_value - initial_cash
    
    # Compare with buy and hold strategy
    buy_and_hold_btc = initial_cash / prices.iloc[0]
    buy_and_hold_value = buy_and_hold_btc * prices.iloc[-1]
    
    print("\n------ Final Portfolio Performance ------")
    print(f"Initial Cash: ${initial_cash:.2f}")
    print(f"Final Portfolio Value: ${final_value:.2f}")
    print(f"Profit/Loss: ${profit:.2f}")
    print(f"Buy and Hold Strategy Value: ${buy_and_hold_value:.2f}")
    print("-----------------------------------------")
