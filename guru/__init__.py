import pandas as pd

from guru import (
    guru_1,  # structure
    guru_2,  # sr level min/max
    guru_3,  # ma
    guru_4,  # shape
    guru_5,  # vol
    guru_6,  # statistic
    guru_7,  # yesterday min max
    guru_8,  # price
    guru_9,  # post
)

total_ops = guru_1.operators \
            + guru_2.operators \
            + guru_3.operators \
            + guru_4.operators \
            + guru_5.operators \
            + guru_6.operators \
            + guru_7.operators \
            + guru_8.operators \
            + guru_9.operators


def get_index(stock_df: pd.DataFrame, from_idx, to_idx) -> pd.Series:
    if from_idx is not None and to_idx is not None:
        return stock_df.index[from_idx:to_idx]

    if from_idx is not None and to_idx is None:
        return stock_df.index[from_idx:]

    if from_idx is None and to_idx is not None:
        return stock_df.index[:to_idx]

    if from_idx is None and to_idx is None:
        return stock_df.index



