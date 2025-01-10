import pandas as pd
import os
from tqdm import tqdm

data = pd.read_csv(r"C:\Users\srile\Downloads\archive\FullDataCsv\master.csv")
print(data.head())

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each file in the directory
for file in os.listdir(r"C:\Users\srile\Downloads\archive\FullDataCsv"):
    if file.endswith('.csv'):
        df = pd.read_csv(os.path.join(r"C:\Users\srile\Downloads\archive\FullDataCsv", file))
        df['Stock'] = file.split('.')[0]  # Adding a column to identify the stock (based on the filename)
        dfs.append(df)

# Concatenate all DataFrames
merged_df = pd.concat(dfs, ignore_index=True)

print(merged_df.head()) # added comment

# Example categorization (if you have a 'volume' column)
volume = merged_df['volume'].unique()  # Get unique volumes

# Initialize tqdm with the number of unique volumes for the progress bar
for vol in tqdm(volume, desc='Processing Volumes'):
    volume_df = merged_df[merged_df['volume'] == vol]  # Filter the DataFrame by volume
    print(f'volume: {vol}, Data:\n', volume_df.head())

# Save the merged data to a new CSV file
merged_df.to_csv('merged_stock_data.csv', index=False)