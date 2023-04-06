import pandas as pd
df = pd.read_csv('m2m.csv')

grouped = df.groupby('S').sum()
grouped = grouped.astype(int)
grouped.to_csv('m3m.csv')
