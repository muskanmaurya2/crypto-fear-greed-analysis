import pandas as pd

# Load the datasets with your filenames
print("Loading data...")
sentiment_file = 'bitcoin_sentiment.csv'
trader_file = 'trader_data.csv'

fg_df = pd.read_csv(sentiment_file)
hist_df = pd.read_csv(trader_file)

# 1. Date Preparation
fg_df['date'] = pd.to_datetime(fg_df['date'])
hist_df['date_dt'] = pd.to_datetime(hist_df['Timestamp IST'], format='%d-%m-%Y %H:%M')
hist_df['date'] = hist_df['date_dt'].dt.normalize()

# 2. Merge Data for Row-Level Analysis
# This allows us to see the sentiment for every single trade
print("Analyzing trade-level patterns...")
df = pd.merge(hist_df, fg_df[['date', 'value', 'classification']], on='date')
df.rename(columns={'classification': 'Sentiment'}, inplace=True)

# 3. Strategy 1 Logic: Margin Analysis
# Compare 'Crossed' (True) vs 'Isolated' (False) performance
margin_stats = df.groupby(['Sentiment', 'Crossed']).agg(
    Trade_Count=('Trade ID', 'count'),
    Avg_PnL=('Closed PnL', 'mean')
).reset_index()

# 4. Strategy 2 Logic: Volume vs Profitability
daily_perf = df.groupby(['date', 'Sentiment']).agg(
    Daily_Total_PnL=('Closed PnL', 'sum'),
    Daily_Trade_Count=('Trade ID', 'count')
).reset_index()

summary_stats = daily_perf.groupby('Sentiment').agg(
    Total_PnL=('Daily_Total_PnL', 'sum'),
    Avg_Trades_Per_Day=('Daily_Trade_Count', 'mean')
).reset_index()

# Sort for display
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
summary_stats['Sentiment'] = pd.Categorical(summary_stats['Sentiment'], categories=sentiment_order, ordered=True)
summary_stats = summary_stats.sort_values('Sentiment')

# --- PRINTING THE ACTIONABLE FINDINGS ---
print("\n" + "="*50)
print("PART C: ACTIONABLE STRATEGY OUTPUT")
print("="*50)

print("\n[FINDING 1] MARGIN USAGE VS PROFITABILITY")
print(margin_stats.pivot(index='Sentiment', columns='Crossed', values='Avg_PnL'))
print("-> Insight: Isolated Margin (Crossed=False) consistently outperforms Cross Margin in Greed.")

print("\n[FINDING 2] VOLUME OPPORTUNITY BY REGIME")
print(summary_stats)
print("-> Insight: Fear periods provide the highest Total PnL with higher trade frequency.")

print("\n" + "="*50)
print("PROPOSED RULES OF THUMB:")
print("1. GREED RULE: If Index > 60, use ISOLATED MARGIN only (Prevents liquidation).")
print("2. FEAR RULE: If Index < 40, INCREASE TRADE FREQUENCY (Captures volatility).")
print("="*50)