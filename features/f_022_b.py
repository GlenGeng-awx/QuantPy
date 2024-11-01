import pandas as pd
from technical.sr_level import SR_LEVEL, SIZE
from features.common import STEP

KEY = 'up to sr level'
VAL = 22 * STEP
RECALL_DAYS = 2


def get_above_sr_level(stock_df: pd.DataFrame, idx):
    close = stock_df['close']

    # sr level above idx
    condition = (stock_df[SR_LEVEL]) & (close > close[idx])
    df1 = stock_df[condition]

    # sr level before idx - SIZE
    df2 = df1.loc[:idx - SIZE]

    if df2.size == 0:
        return None

    # the closest one to idx
    df3 = df2.sort_values(by='close').iloc[0]
    # print(f'date {stock_df.loc[idx]["Date"]} aims up to {df3["close"]} at {df3["Date"]}')
    return df3['close']


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        above_sr_level = get_above_sr_level(stock_df, idx)
        if above_sr_level is None:
            continue

        if close[idx] > close[idx - 1] and close[idx] * 1.03 > above_sr_level:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
