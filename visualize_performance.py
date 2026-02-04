import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets with your filenames
print("Loading data...")
fg_df = pd.read_csv('bitcoin_sentiment.csv')
hist_df = pd.read_csv('trader_data.csv')

# 1. Data Preparation (Aligning dates)
print("Aligning datasets...")
fg_df['date'] = pd.to_datetime(fg_df['date'])
hist_df['date_dt'] = pd.to_datetime(hist_df['Timestamp IST'], format='%d-%m-%Y %H:%M')
hist_df['date'] = hist_df['date_dt'].dt.normalize()

# 2. Aggregate Daily Metrics
daily_summary = hist_df.groupby('date').agg(
    Daily_PnL=('Closed PnL', 'sum'),
    Trade_Count=('Trade ID', 'count')
).reset_index()

# Merge metrics with sentiment
merged_df = pd.merge(daily_summary, fg_df[['date', 'value', 'classification']], on='date', how='inner')
merged_df.rename(columns={'value': 'FG_Value', 'classification': 'Sentiment'}, inplace=True)

# 3. Statistical Correlation
# (How much does the market mood affect PnL and activity?)
correlation = merged_df[['FG_Value', 'Daily_PnL', 'Trade_Count']].corr()
print("\n--- Correlation Results ---")
print(correlation)

# 4. Generate Visualizations
print("\nGenerating charts...")

# Sort sentiment for logical plotting
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
merged_df['Sentiment'] = pd.Categorical(merged_df['Sentiment'], categories=sentiment_order, ordered=True)

# Chart 1: Total PnL per Sentiment Category
plt.figure(figsize=(10, 6))
sns.barplot(data=merged_df, x='Sentiment', y='Daily_PnL', estimator=sum, palette='viridis', ci=None)
plt.title('Total Profit/Loss (PnL) by Market Sentiment')
plt.ylabel('Total Realized PnL ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('pnl_vs_sentiment.png')
print("- Saved: pnl_vs_sentiment.png")

# Chart 2: Sentiment vs. Trading Activity (Trade Volume)
plt.figure(figsize=(10, 6))
sns.barplot(data=merged_df, x='Sentiment', y='Trade_Count', palette='magma')
plt.title('Average Daily Trade Activity by Market Sentiment')
plt.ylabel('Average Number of Trades')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('trade_activity_vs_sentiment.png')
print("- Saved: trade_activity_vs_sentiment.png")

# Chart 3: Correlation Scatter Plot
plt.figure(figsize=(10, 6))
sns.regplot(data=merged_df, x='FG_Value', y='Daily_PnL', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Fear & Greed Index Value vs Daily PnL')
plt.xlabel('Fear & Greed Value (0 = Panic, 100 = Euphoria)')
plt.ylabel('Daily PnL ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('pnl_correlation.png')
print("- Saved: pnl_correlation.png")

print("\nAnalysis Complete! Check your folder for the .png image files.")