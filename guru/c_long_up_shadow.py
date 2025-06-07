import pandas as pd

KEY = 'long up shadow'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close, high = stock_df['open'], stock_df['close'], stock_df['high']

    up_shadows = []
    for idx in stock_df.index:
        up_shadow = high[idx] - max(_open[idx], close[idx])
        up_shadows.append((up_shadow, idx))

    up_shadows.sort(key=lambda x: x[0], reverse=True)
    reserved = int(len(up_shadows) * 0.1)

    hits = []
    for i in range(reserved):
        idx = up_shadows[i][1]
        hits.append(stock_df['Date'][idx])
    return hits
