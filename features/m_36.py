import pandas as pd

KEY = 'down gap'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    high = stock_df['high']
    low = stock_df['low']

    indices = []

    for idx in high.index[1:]:
        if low[idx - 1] > high[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
