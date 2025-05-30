import math
import pandas as pd
import plotly.graph_objects as go

from util import get_idx_by_date, get_next_n_workday
from technical.line import _Line


def _calculate_k(stock_df: pd.DataFrame, date1, date2) -> float:
    x1 = get_idx_by_date(stock_df, date1)
    y1 = stock_df.loc[x1]['close']

    x2 = get_idx_by_date(stock_df, date2)
    y2 = stock_df.loc[x2]['close']

    ratio = y2 / y1
    delta = x2 - x1
    k = math.pow(ratio, 1 / delta)
    return k


def _calculate_point(stock_df: pd.DataFrame, date, delta, k) -> tuple:
    x = get_idx_by_date(stock_df, date)
    y = stock_df.loc[x]['close']

    target_x = x + delta
    target_y = y * math.pow(k, delta)

    if target_x > stock_df.index[-1] + 10 or target_x < stock_df.index[0]:
        return ()

    if target_x in stock_df.index:
        target_date = stock_df.loc[target_x]['Date']
    else:
        diff = target_x - stock_df.index[-1]
        last_date = stock_df['Date'].iloc[-1]

        target_date = get_next_n_workday(last_date, diff)

    return target_date, target_y


class LineExpo:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.line = _Line(
            stock_df, stock_name,
            'lines_expo',
            _calculate_k,
            _calculate_point,
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self.line.build_graph(fig, enable)
