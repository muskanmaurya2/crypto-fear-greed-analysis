import pandas as pd

# 1. Load the datasets
print("Loading data...")
fg_df = pd.read_csv('bitcoin_sentiment.csv')  # Changed from fear_greed_index.csv
hist_df = pd.read_csv('trader_data.csv')
# 2. Convert dates and align
print("Processing dates...")
fg_df['date'] = pd.to_datetime(fg_df['date'])
# Adjusting format to match: 02-12-2024 22:50
hist_df['date_dt'] = pd.to_datetime(hist_df['Timestamp IST'], format='%d-%m-%Y %H:%M')
hist_df['date'] = hist_df['date_dt'].dt.normalize()

# 3. Create Daily Metrics
print("Calculating metrics...")
# Aggregate PnL and trade counts by date
daily_summary = hist_df.groupby('date').agg({
    'Closed PnL': 'sum',
    'Trade ID': 'count',
    'Size USD': 'mean'
}).rename(columns={'Trade ID': 'Trade_Count', 'Size USD': 'Avg_Trade_Size'})

# Calculate Long/Short Ratio
hist_df['Side_Type'] = hist_df['Direction'].apply(
    lambda x: 'Long' if 'Long' in str(x) or 'Buy' in str(x) else 'Short'
)
ls_counts = hist_df.groupby(['date', 'Side_Type']).size().unstack(fill_value=0)
if 'Short' in ls_counts.columns and 'Long' in ls_counts.columns:
    daily_summary['LS_Ratio'] = ls_counts['Long'] / ls_counts['Short'].replace(0, 1)

# 4. Merge with Fear & Greed Index
print("Merging datasets...")
final_data = pd.merge(daily_summary, fg_df[['date', 'value', 'classification']], on='date', how='inner')

# 5. Save the output
final_data.to_csv('processed_daily_data.csv', index=False)
print("Success! File saved as 'processed_daily_data.csv'")
print(final_data.head())