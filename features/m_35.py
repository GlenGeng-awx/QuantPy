import pandas as pd

KEY = 'up gap'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    high = stock_df['high']
    low = stock_df['low']

    indices = []

    for idx in high.index[1:]:
        if high[idx - 1] < low[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
