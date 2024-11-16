import pandas as pd
from technical.min_max import LOCAL_MIN_PRICE_3RD
from technical.sr_level import SR_LEVEL_MIN

FROM = 50  # 27, 30, 35
TO = 20


# local min price 3rd
def cond_0(stock_df: pd.DataFrame, idx: int) -> bool:
    stock_df = stock_df.loc[idx - FROM:idx - TO]
    return stock_df[SR_LEVEL_MIN].any()


# positive 2 days later
def cond_1(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df.loc[idx + 2]['close'] >= stock_df.loc[idx]['close']


# above baseline
def cond_2(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - FROM:idx - TO]

    hits = df[df[SR_LEVEL_MIN]].index.tolist()
    if len(hits) != 1:
        return False

    return stock_df.loc[idx]['close'] >= stock_df.loc[hits[0]]['close']


def check_long(stock_df: pd.DataFrame, idx: int, conditions: list) -> bool:
    if not all(stock_df.loc[idx][condition] for condition in conditions):
        return False

    # stock_df = stock_df.loc[idx - FROM:idx - TO]
    # return stock_df[SR_LEVEL_MIN].any() and stock_df[LOCAL_MIN_PRICE_3RD].any()
    # return stock_df[SR_LEVEL_MIN].any()

    return cond_0(stock_df, idx)  \
        and cond_1(stock_df, idx) \
        and cond_2(stock_df, idx)
