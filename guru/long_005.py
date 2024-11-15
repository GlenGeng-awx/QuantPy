import pandas as pd
from technical.min_max import LOCAL_MIN_PRICE_3RD
from technical.sr_level import SR_LEVEL_MIN

NAME = 'up thru ma20'
COLOR = 'orange'
TYPE = 'long'

FROM = 27  # 27, 30, 35
TO = 20


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['up thru ma20']
    if not all(stock_df.loc[idx][condition] for condition in conditions):
        return False

    stock_df = stock_df.loc[idx - FROM:idx - TO]
    return stock_df[SR_LEVEL_MIN].any() and stock_df[LOCAL_MIN_PRICE_3RD].any()
