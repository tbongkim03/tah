import pandas as pd
from tabulate import tabulate

def read_data():
    df = pd.read_parquet('~/data/parquet')
    return df

def top(n, dt):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    return ddf

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
