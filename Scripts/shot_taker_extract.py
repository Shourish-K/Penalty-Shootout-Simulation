import pandas as pd


input_file = "D:\\USCB CSCI\\SEM 7\\Systems Modeling & Simulation\\Final Project\\Data\\shot_takers.csv"
df = pd.read_csv(input_file)

# Remove rows where the 'Position' column is 'GK'
df_filtered = df[df['Position'] != 'GK']

# Save the modified DataFrame back to the CSV
df_filtered.to_csv(input_file, index=False)