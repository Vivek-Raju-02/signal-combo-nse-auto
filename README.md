# 🚗 NSE Auto Sector: Signal Combination & Backtest Strategy

This repo implements a signal combination strategy for stocks like Tata Motors using both price-volume and macroeconomic signals.

---

## Structure

- `notebooks/` – Contains signal engineering and backtesting workflows.
- `outputs/` – Auto-saved intermediate signal datasets and performance plots.
- `CandidateName_SignalCombination.py` – Summarized runnable script for quick strategy testing.
- `requirements.txt` – Python dependencies.


## Signal Construction

We combine 3 predictive features:
- **Momentum Signal** – Price-based momentum from stock price trends.
- **Auto Sales YoY** – Derived from macro auto sales data.
- **Repo Rate Change** – RBI repo rate trends as proxy for monetary policy.

Signals are standardized and aggregated using a simple linear combination.


## Backtesting

Backtest period: **2018–2024**

- Positioning: Long if composite signal > 0, short if < 0
- Daily turnover controlled under 40%
- Metrics:
  - **Annualized Return**: X%
  - **Sharpe Ratio**: Y
  - **Max Drawdown**: Z%
  - **Avg Daily Turnover**: < 40%


## To Run

1. Clone repo and install:
```bash
pip install -r requirements.txt
