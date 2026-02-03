# Crypto Trading & Sentiment Analysis Project

This project explores the correlation between market sentiment (Bitcoin Fear & Greed Index) and real-world trading performance. By merging historical trade logs with daily sentiment data, we identify high-probability trading regimes and risk management strategies.

## 📂 Project Structure
* `trader_data.csv`: Raw historical trading data (PnL, Side, Margin type).
* `bitcoin_sentiment.csv`: Daily Fear & Greed Index records.
* `analysis.py`: Cleans, aligns, and merges datasets into daily metrics.
* `visualize_performance.py`: Generates visual charts for PnL and activity analysis.
* `strategy_insights.py`: Provides statistical proof for "Actionable Output" rules.
* `processed_daily_data.csv`: (Generated) The final merged dataset for analysis.

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.9 or higher installed.

### 2. Install Dependencies
Run the following command in your terminal to install the necessary data science libraries:
```bash
pip install pandas matplotlib seaborn
