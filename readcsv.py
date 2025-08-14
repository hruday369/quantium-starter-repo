import pandas as pd
import glob

# Get a list of all CSV files in a directory
csv_files = glob.glob('data/*.csv')
dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)
combined_df = pd.concat(dataframes, ignore_index=True)
pink_morsel_df = combined_df[combined_df['product']=='pink morsel']

price = pink_morsel_df['price'].str.replace('$', '', regex=False).astype(float)
quantity = pink_morsel_df['quantity']

pink_morsel_df['sales'] = price * quantity
pink_morsel_df=pink_morsel_df[['sales','date','region']]

pink_morsel_df.to_csv('pink_morsel_sales.csv', index=False)