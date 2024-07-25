import pandas as pd

def read_data():
    df = pd.read_parquet('~/data/parquet')
    return df

def top(n, dt):
    df = read_data()
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    
    return ddf.to_string(index=False)

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
