import pandas as pd
from technical.min_max import LOCAL_MAX_PRICE_3RD
from technical.sr_level import SR_LEVEL_MAX

FROM = 35  # 27, 30, 35
TO = 20


def get_baseline(stock_df: pd.DataFrame, idx: int):
    df = stock_df.loc[idx - FROM:idx - TO]

    hits = df[df[SR_LEVEL_MAX]].index.tolist()
    if len(hits) != 1:
        return None

    return stock_df.loc[hits[0]]['close']


def check_short(stock_df: pd.DataFrame, idx: int, conditions) -> bool:
    if not all(stock_df.loc[idx][condition] for condition in conditions):
        return False

    if stock_df.loc[idx + 2]['close'] > stock_df.loc[idx]['close']:
        return False

    # stock_df = stock_df.loc[idx - FROM:idx - TO]
    # return stock_df[SR_LEVEL_MAX].any() and stock_df[LOCAL_MAX_PRICE_3RD].any()
    # return stock_df[SR_LEVEL_MAX].any()

    baseline = get_baseline(stock_df, idx)
    if baseline is None:
        return False

    return stock_df.loc[idx]['close'] <= baseline
