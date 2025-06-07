import pandas as pd

KEY = 'long down shadow'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']

    down_shadows = []
    for idx in stock_df.index:
        down_shadow = min(_open[idx], close[idx]) - low[idx]
        down_shadows.append((down_shadow, idx))

    down_shadows.sort(key=lambda x: x[0], reverse=True)
    reserved = int(len(down_shadows) * 0.1)

    hits = []
    for i in range(reserved):
        idx = down_shadows[i][1]
        hits.append(stock_df['Date'][idx])
    return hits
