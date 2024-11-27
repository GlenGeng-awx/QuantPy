import pandas as pd

from d2_margins import MARGINS
from .holding_long import eval_long
from .holding_short import eval_short


def get_index(stock_df: pd.DataFrame, from_idx, to_idx) -> pd.Series:
    if from_idx is not None and to_idx is not None:
        return stock_df.index[from_idx:to_idx]

    if from_idx is not None and to_idx is None:
        return stock_df.index[from_idx:]

    if from_idx is None and to_idx is not None:
        return stock_df.index[:to_idx]

    if from_idx is None and to_idx is None:
        return stock_df.index


# return (pnl_tag, color)
def eval_ops(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    long_profit = min(MARGINS[stock_name]['15']['incr'], 0.20)
    short_profit = min(MARGINS[stock_name]['15']['decr'], 0.20)

    if indices[-1] - indices[0] < 10:
        return None, None

    # eval long
    long_results = eval_long(stock_df, indices)

    if all(hit_num >= 2 and total_pnl / hit_num >= long_profit for (_, hit_num, total_pnl) in long_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in long_results)
        color = 'orange'
        return pnl_tag, color

    # eval short
    short_results = eval_short(stock_df, indices)

    if all(hit_num >= 2 and total_pnl / hit_num >= short_profit for (_, hit_num, total_pnl) in short_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in short_results)
        color = 'black'
        return pnl_tag, color

    return None, None
