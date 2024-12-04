import pandas as pd

from guru import (
    guru_1,  # structure
    guru_2,  # ma
    guru_3,  # shape
    guru_4,  # vol
    guru_5,  # statistic
    guru_6,  # yesterday min max
    guru_7,  # price
    guru_8,  # sr level min/max
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



