import pandas as pd
from features.util import STEP

KEY = 'low incr 1d'
VAL = 42 * STEP
RECALL_DAYS = 1


def price_incr_n_days(stock_df: pd.DataFrame, n: int, price_key: str, output_key: str):
    price = stock_df[price_key]

    indices = []

    for idx in price.index[n:]:
        if all(price[idx - i] > price[idx - i - 1] for i in range(n)):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 1, 'low', KEY)
