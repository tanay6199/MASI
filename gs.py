import pandas as pd
# Read the input CSV file into a DataFrame, selecting only the NAME and score columns
df = pd.read_csv('masi1.csv', usecols=['Microbe-Name', 'Substance-Name'])

# Group the DataFrame by desired columns, then count the occurrences
grouped = df.groupby(['Microbe-Name', 'Substance-Name']).size().reset_index(name='count')

# Create a new column with the row indices
grouped['row'] = grouped.groupby('Microbe-Name').ngroup()

# Pivot the DataFrame to create the desired matrix
matrix = grouped.pivot(index='row', columns='Substance-Name', values='count')
matrix = matrix.fillna(0).astype(int)

# Write the output CSV file
matrix.index = grouped['Microbe-Name'].unique()
matrix.columns.name = 'Substance-Name'
matrix.to_csv('output.csv')