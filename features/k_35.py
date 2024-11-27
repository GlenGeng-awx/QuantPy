import pandas as pd
from technical.sr_level import SR_LEVEL_MAX, SIZE

KEY = 'up away sr level max'
COLOR = 'red'


def get_below_sr_level_max(stock_df: pd.DataFrame, idx):
    close = stock_df['close']

    # sr level max below idx
    condition = (stock_df[SR_LEVEL_MAX]) & (close < close[idx])
    df1 = stock_df[condition]

    # sr level max before idx - SIZE
    df2 = df1.loc[idx - 180:idx - SIZE]

    if df2.size == 0:
        return None

    # the closest one to idx
    df3 = df2.sort_values(by='close').iloc[-1]
    # print(f'date {stock_df.loc[idx]["Date"]} aims down to {df3["close"]} at {df3["Date"]}')
    return df3['close']


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        below_sr_level_max = get_below_sr_level_max(stock_df, idx)
        if below_sr_level_max is None:
            continue

        if close[idx - 1] < close[idx] < below_sr_level_max * 1.03:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
