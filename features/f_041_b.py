import pandas as pd
from features.util import STEP

KEY = 'close incr'
VAL = 41 * STEP
RECALL_DAYS = 1


def price_incr(stock_df: pd.DataFrame, price_key: str, output_key: str):
    price = stock_df[price_key]

    indices = []

    for idx in price.index[1:]:
        if price[idx] > price[idx - 1]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr(stock_df, 'close', KEY)
