import pandas as pd
from features.util import STEP

KEY = 'Monday'
VAL = 40 * STEP + 0
RECALL_DAYS = 1


# 0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 4: Friday, 5: Saturday, 6: Sunday
def weekday_is_n(stock_df: pd.DataFrame, n: int, key: str):
    indices = []

    for idx in stock_df.index:
        date_str = stock_df.loc[idx]['Date']
        date = pd.to_datetime(date_str)

        if date.weekday() == n:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    weekday_is_n(stock_df, 0, KEY)
