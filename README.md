# 📊 Crypto Trading & Sentiment Analysis Project

This project analyzes the relationship between **crypto market sentiment** (Bitcoin Fear & Greed Index) and **real trading performance**. By merging historical trade logs with daily sentiment data, it uncovers **high‑probability trading regimes**, **risk patterns**, and **actionable strategy insights** backed by statistics.
---

## 🎯 Project Objectives
* Understand how **market sentiment impacts PnL and trade behavior**
* Identify **profitable vs risky sentiment zones**
* Validate **data‑driven trading rules** using statistical analysis
* Provide **clear visualizations** for performance evaluation
---

## 📂 Project Structure
```
├── trader_data.csv              # Raw historical trade data (PnL, side, margin type, timestamps)
├── bitcoin_sentiment.csv        # Daily Bitcoin Fear & Greed Index data
├── analysis.py                  # Data cleaning, alignment, and daily aggregation
├── visualize_performance.py     # Visual analysis (PnL, volume, sentiment impact)
├── strategy_insights.py         # Statistical validation of actionable trading rules
├── processed_daily_data.csv     # (Auto‑generated) Final merged dataset
└── README.md
```
---

## 🛠️ Setup & Installation

### 1️⃣ Prerequisites
* Python **3.9+**
* pip (Python package manager)
### 2️⃣ Install Dependencies
Run the following command in your terminal:
```bash
pip install pandas matplotlib seaborn numpy scipy
```
---

## ▶️ How to Run the Project
Execute the scripts in the order below:
```bash
python analysis.py
python visualize_performance.py
python strategy_insights.py
```
---

## 🔄 Script Workflow

### `analysis.py`
* Cleans raw trade data
* Aligns trades with daily sentiment values
* Aggregates metrics such as:
  * Daily PnL
  * Trade count
  * Buy vs Sell dominance
* Outputs `processed_daily_data.csv`

### `visualize_performance.py`
* Generates charts including:
  * PnL vs Fear & Greed Index
  * Trade activity across sentiment zones
  * Volatility and exposure trends

### `strategy_insights.py`
* Performs statistical analysis to validate:

  * High‑probability sentiment regimes
  * Risk‑off vs risk‑on zones
  * Drawdown patterns
* Outputs **actionable trading rules** with data support
---

## 📈 Sample Insights (Example)
* Extreme **Fear (0–25)** often correlates with **higher long‑term returns**
* **Greed (>70)** shows increased volatility and drawdown risk
* Reduced leverage improves outcomes during high‑greed phases
*(Actual results depend on your dataset)*
---

## 🧠 Actionable Use Cases
* Improve **risk management** using sentiment filters
* Build **sentiment‑aware trading strategies**
* Enhance **backtesting frameworks**
* Academic or portfolio research projects
---

## 🚀 Future Improvements
* Add live sentiment API integration
* Include more assets (ETH, SOL, etc.)
* Machine learning‑based regime detection
* Interactive dashboards (Plotly / Streamlit)
---

## 📜 License
This project is open‑source and available for educational and research purposes.
---

## 🤝 Contributions
Pull requests and suggestions are welcome! If you find this useful, consider ⭐ starring the repo.
