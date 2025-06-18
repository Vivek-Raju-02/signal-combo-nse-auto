import pandas as pd
import numpy as np

# Load signal data
signals = pd.read_csv('outputs/signal_dataset.csv', parse_dates=['Date'], index_col='Date')
signals['Signal'] = (signals['Composite_Signal'] - signals['Composite_Signal'].mean()) / signals['Composite_Signal'].std()

# Simulate price series
np.random.seed(1)
signals['Price'] = 500 + np.cumsum(np.random.normal(0, 5, len(signals)))

# Strategy
signals['Position'] = np.sign(signals['Signal'])
signals['Returns'] = signals['Price'].pct_change()
signals['Strategy_Returns'] = signals['Position'].shift(1) * signals['Returns']
signals['Cumulative_Strategy'] = (1 + signals['Strategy_Returns']).cumprod()

# Metrics
sharpe = np.sqrt(252) * signals['Strategy_Returns'].mean() / signals['Strategy_Returns'].std()
mdd = ((signals['Cumulative_Strategy'] - signals['Cumulative_Strategy'].cummax()) / signals['Cumulative_Strategy'].cummax()).min()
turnover = signals['Position'].diff().abs().mean()

print(f"Sharpe: {sharpe:.2f}, Max DD: {mdd:.2%}, Avg Turnover: {turnover:.2%}")
