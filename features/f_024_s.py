import pandas as pd
from technical.sr_level import SR_LEVEL, SIZE
from features.util import STEP, DELTA

KEY = 'down thru sr level'
VAL = 24 * STEP + DELTA
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        condition = (stock_df[SR_LEVEL]) & (close[idx - 1] > close) & (close > close[idx])
        df1 = stock_df[condition]
        df2 = df1.loc[:idx - SIZE]

        if df2.size != 0:
            # print(f'{stock_df.loc[idx]["Date"]} down thru sr level at {df2["close"].iloc[0]}')
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
