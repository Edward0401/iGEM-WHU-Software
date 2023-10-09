import pandas as pd
import numpy as np
import random

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('D:/Sourcefiles/igem/Result5bp.csv')

# Normalize the values in the fourth column
max_value = df['column4'].max()
min_value = df['column4'].min()
df['column4_normalized'] = (df['column4'] - min_value) / (max_value - min_value)

# Combine the DNA sequences randomly
combined_sequences = []
for i in range(len(df)):
    combined_sequence = df.sample(n=1, weights=df['column4_normalized']).iloc[0]['column2'] + df.sample(n=1, weights=df['column4_normalized']).iloc[0]['column2']
    combined_sequences.append(combined_sequence)

# Write the combined sequences to a new CSV file
new_df = pd.DataFrame({'combined_sequences': combined_sequences})
new_df.to_csv('D:/Filesgenerated/igem/combinedsequence111001.csv', index=False)