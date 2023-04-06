import pandas as pd
df = pd.read_csv('gm.csv')
grouped = df.groupby('Strain').sum()
grouped.columns = grouped.columns.str.replace('\.\d+', '')
grouped = grouped.astype(int)
grouped.to_csv('pm.csv')
