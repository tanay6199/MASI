import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv("m3m.csv")

# Calculate the sum of each column and append the totals as a new row at the bottom of the dataframe
df.loc['Total'] = df.sum()

# Write the dataframe to a new CSV file with the 'Total' sum row
df.to_csv("new_csv_file.csv", index=False)

