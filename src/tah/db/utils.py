import pandas as pd

def read_data():
    df = pd.read_parquet('./data/parquet')
    return df

def top(cnt, dt):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(10)
    ddf = sdf.drop(columns=['dt'])
    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['dt'].str.contains(query)]
    cnt = fdf['cnt'].sum
